import copy
import os
import pickle
import sys
import tempfile
import threading
import time
from contextlib import suppress
from dataclasses import dataclass
from datetime import timedelta
from itertools import product
from sys import platform
from typing import Callable, Dict, Optional

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

if not dist.is_available():
    print("distributed package not available, skipping tests", file=sys.stderr)
    sys.exit(0)

import mindtorch.torch.distributed.distributed_c10d as c10d
# import mindtorch.torch.distributed.algorithms.ddp_comm_hooks.powerSGD_hook as powerSGD
import mindtorch.torch.nn.functional as F
# import torch.testing._internal.common_utils as common
from mindtorch.torch import nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 10, bias=False)
        self.fc2 = nn.Linear(10, 50, bias=False)
        self.fc3 = nn.Linear(50, 4, bias=False)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return F.softmax(x, dim=1)


class DoubleGpuNet(nn.Module):
    def __init__(self, gpus):
        super().__init__()
        self.fc1 = nn.Linear(2, 10, bias=False).to(gpus[0])
        self.fc2 = nn.Linear(10, 50, bias=False).to(gpus[1])
        self.fc3 = nn.Linear(50, 4, bias=False).to(gpus[1])
        self.relu = nn.ReLU()
        self.no_grad_param = nn.Parameter(
            torch.tensor([2, 2]).long(), requires_grad=False
        ).to(gpus[0])

    def forward(self, x):
        dev0 = self.fc1.weight.device
        dev1 = self.fc2.weight.device
        x = self.relu(self.fc1(x.to(dev0)))
        x = self.relu(self.fc2(x.to(dev1)))
        x = self.fc3(x)
        return F.softmax(x, dim=1).to(dev0)


class QuadraGpuNet(nn.Module):
    def __init__(self, gpus):
        super().__init__()
        self.fc1 = nn.Linear(2, 10, bias=False).to(gpus[0])
        self.fc2 = nn.Linear(10, 50, bias=False).to(gpus[1])
        self.fc3 = nn.Linear(50, 4, bias=False).to(gpus[2])
        self.fc4 = nn.Linear(4, 4, bias=False).to(gpus[3])
        self.relu = nn.ReLU()
        self.no_grad_param = nn.Parameter(
            torch.tensor([2, 2]).long(), requires_grad=False
        ).to(gpus[0])

    def forward(self, x):
        dev0 = self.fc1.weight.device
        dev1 = self.fc2.weight.device
        dev2 = self.fc3.weight.device
        dev3 = self.fc4.weight.device
        x = self.relu(self.fc1(x.to(dev0)))
        x = self.relu(self.fc2(x.to(dev1)))
        x = self.relu(self.fc3(x.to(dev2)))
        x = self.fc4(x.to(dev3))
        return F.softmax(x, dim=1).to(dev0)


class ConvNet(nn.Module):
    def __init__(self, gpus, layouts, dtypes):
        super().__init__()
        self.dtypes = dtypes
        if isinstance(gpus, list):
            self.layer_gpus = gpus
        else:
            gpus = [gpus] * 4
        self.conv0 = torch.nn.Conv2d(8, 16, (2, 2)).to(
            device=gpus[0], memory_format=layouts[0], dtype=dtypes[0]
        )
        self.conv1 = torch.nn.Conv2d(16, 32, (2, 2)).to(
            device=gpus[1], memory_format=layouts[1], dtype=dtypes[1]
        )
        self.conv2 = torch.nn.Conv2d(32, 16, (2, 2)).to(
            device=gpus[2], memory_format=layouts[2], dtype=dtypes[2]
        )
        self.conv3 = torch.nn.Conv2d(16, 8, (2, 2)).to(
            device=gpus[3], memory_format=layouts[3], dtype=dtypes[3]
        )

    def forward(self, x):
        x = x.to(self.dtypes[0])
        # Could say
        # x = self.conv0(x).to(device=self.conv1.weight.device, dtype=self.dtypes[1])
        # etc.  But I don't want to appeal to the weights' devices directly, because part of this test's purpose
        # is to verify weights are where expected if the model gets replicated.
        gpus = self.layer_gpus if hasattr(self, "layer_gpus") else [x.device] * 4
        x = self.conv0(x).to(device=gpus[1], dtype=self.dtypes[1])
        x = self.conv1(x).to(device=gpus[2], dtype=self.dtypes[2])
        x = self.conv2(x).to(device=gpus[3], dtype=self.dtypes[3])
        return self.conv3(x)

class DummyProcessGroup(dist.ProcessGroup):
    def getBackendName(self):
        return "Dummy"

class AbstractCommTest:
    def __init__(self):
        # self.world_size = 2
        self.rank = -1

    @property
    def op_timeout_sec(self):
        return 1

    @property
    def world_size(self):
        return 2

    @property
    def device(self):
        self.fail("test subclass didn't override device")

    # TODO: not support dist.all_gather_object
    # def _verify_sequence_number_across_pg(self, pg, verify_pg):

    #     seq_num = pg._get_sequence_number_for_group()
    #     obj_list = [None for _ in range(dist.get_world_size(verify_pg))]
    #     # We use a separate pg to verify the sequence numbers, otherwise these
    #     # collectives will themselves increment the sequence number.
    #     dist.all_gather_object(obj_list, seq_num, group=verify_pg)
    #     self.assertEqual(len(set(obj_list)), 1)
    #     return obj_list[0]

    # TODO: not support dist.all_gather_object
    # def _test_sequence_num_incremented(self, process_group, ranks):
    #     # verify initial sequence numbers. Use a distinct process group for
    #     # verification to keep counts as expected with respect to process_group.
    #     verify_pg = dist.new_group(
    #         ranks=ranks,
    #         backend="gloo",
    #     )
    #     assert dist.get_world_size(process_group) == dist.get_world_size(verify_pg)

    #     initial_num = (
    #         self._verify_sequence_number_across_pg(
    #             pg=process_group, verify_pg=verify_pg
    #         )
    #         if not c10d._rank_not_in_group(process_group)
    #         else -1
    #     )

    #     # Verify sequence numbers are appropriately incremented
    #     for i in range(10):
    #         t = torch.ones(1, device=torch.cuda.current_device())
    #         dist.all_reduce(t, group=process_group)
    #         if not c10d._rank_not_in_group(process_group):
    #             seq_num = self._verify_sequence_number_across_pg(
    #                 pg=process_group,
    #                 verify_pg=verify_pg,
    #             )
    #             self.assertEqual(initial_num + i + 1, seq_num)

    #     if dist.get_world_size(process_group) > 2:
    #         # Test when certain ranks don't call collectives
    #         if dist.get_rank(process_group) not in [0, 2]:
    #             dist.all_reduce(t, group=process_group, async_op=True)
    #         # Now ranks 0 and 2 should be lagging by 1.
    #         if not c10d._rank_not_in_group(process_group):
    #             seq_num = process_group._get_sequence_number_for_group()
    #             rank = dist.get_rank(process_group)
    #             obj_list = [None for _ in range(dist.get_world_size(verify_pg))]
    #             dist.all_gather_object(obj_list, (rank, seq_num), group=verify_pg)
    #             rank_to_seq_num = dict(obj_list)
    #             self.assertEqual(len(set(rank_to_seq_num.values())), 2)
    #             self.assertEqual(rank_to_seq_num[0], rank_to_seq_num[2])
    #             expected_same = {
    #                 rank_to_seq_num[i]
    #                 for i in rank_to_seq_num.keys()
    #                 if i not in [0, 2]
    #             }
    #             self.assertEqual(len(expected_same), 1)
    #             self.assertEqual(rank_to_seq_num[0] + 1, rank_to_seq_num[1])

    # TODO: not support dist.all_gather_object
    # def _test_sequence_num_incremented_default_group(self, backend_name):
    #     torch.cuda.set_device(self.rank)
    #     store = dist.FileStore(self.file_name, self.world_size)
    #     dist.init_process_group(
    #         backend_name,
    #         world_size=self.world_size,
    #         rank=self.rank,
    #         store=store,
    #     )
    #     self._test_sequence_num_incremented(
    #         c10d._get_default_group(),
    #         ranks=list(range(dist.get_world_size())),
    #     )

    # TODO: not support dist.all_gather_object
    # def _test_sequence_num_incremented_subgroup(self, backend_name):
    #     torch.cuda.set_device(self.rank)
    #     store = dist.FileStore(self.file_name, self.world_size)
    #     dist.init_process_group(
    #         backend_name,
    #         world_size=self.world_size,
    #         rank=self.rank,
    #         store=store,
    #     )
    #     subgroup_ranks = [0, 1, 2]
    #     subgroup = dist.new_group(subgroup_ranks)
    #     self._test_sequence_num_incremented(subgroup, subgroup_ranks)

    # TODO: not support dist.all_gather_object
    # def _test_sequence_num_set_default_pg(self, backend):
    #     store = dist.FileStore(self.file_name, self.world_size)
    #     dist.init_process_group(
    #         backend,
    #         world_size=self.world_size,
    #         rank=self.rank,
    #         store=store,
    #     )

    #     default_pg = c10d._get_default_group()
    #     seq_num = default_pg._get_sequence_number_for_group()
    #     obj_list = [None for _ in range(dist.get_world_size())]
    #     dist.all_gather_object(obj_list, seq_num)
    #     self.assertEqual(len(set(obj_list)), 1)

    # TODO: not support dist.all_gather_object
    # def _test_sequence_num_set_new_group(self, backend):
    #     store = dist.FileStore(self.file_name, self.world_size)
    #     dist.init_process_group(
    #         backend,
    #         world_size=self.world_size,
    #         rank=self.rank,
    #         store=store,
    #     )

    #     subgroup = dist.new_group([0, 1])

    #     if not c10d._rank_not_in_group(subgroup):
    #         subgroup_seq = subgroup._get_sequence_number_for_group()
    #         obj_list = [None for _ in range(dist.get_world_size(subgroup))]
    #         dist.all_gather_object(obj_list, subgroup_seq, group=subgroup)
    #         self.assertEqual(len(set(obj_list)), 1)

    def _test_warn_not_in_group(self, backend):
        dist.init_process_group(
            backend,
            world_size=self.world_size,
        )
        in_group_ranks = list(filter(lambda x: x % 2 == 0, range(self.world_size)))
        group = dist.new_group(in_group_ranks)

        x = torch.zeros(2, 2).cuda(self.rank)
        xs = [torch.zeros(2, 2).cuda(self.rank) for _ in range(len(in_group_ranks))]
        rank = dist.get_rank()
        if rank not in in_group_ranks:
            # not hang, on error
            dist.all_gather(xs, x, group=group)
            dist.all_reduce(x, group=group)
            # TODO: mindspore.ops barrier not support GPU yet
            # dist.barrier(group=group)
            dist.broadcast(x, src=0, group=group)
        else:
            dist.all_gather(xs, x, group=group)
            dist.all_reduce(x, group=group)
            # TODO: mindspore.ops barrier not support GPU yet
            # dist.barrier(group=group)
            dist.broadcast(x, src=0, group=group)
        dist.destroy_process_group()

    def _test_rank_membership(self, backend):
        if not dist.is_initialized():
            dist.init_process_group(
                backend,
                world_size=self.world_size,
            )

        assert self.world_size > 1

        group = dist.new_group(ranks=[1])
        rank = dist.get_rank()
        if rank == 1:
            assert dist.get_group_rank(group, 1) == 0
        else:
            # TODO: mindspore not support get group rank when this process is not in group
            assert dist.get_group_rank(group, 1) is None

        try:
            dist.get_group_rank(group, 0)
            # Raise error: Group group_1 doesn't contain the global rank 0
            assert False
        except:
            ...

        try:
            dist.get_group_rank(DummyProcessGroup(self.rank, self.world_size), 0)
            # Raise error: Group is not registerd.
            assert False
        except:
            ...

        if rank == 1:
            # TODO: mindspore not support get group rank when this process is not in group
            dist.get_process_group_ranks(group), [1]
        dist.destroy_process_group()

    # TODO: not check tensor dtype for performance.
    # def _test_tensor_dtype_mismatch(self, backend):
    #     store = dist.FileStore(self.file_name, self.world_size)
    #     dist.init_process_group(
    #         backend,
    #         world_size=self.world_size,
    #         rank=self.rank,
    #         store=store,
    #     )

    #     tensor = torch.ones(2, 2, device=self.device) * 7
    #     tensor_h = tensor.half()
    #     tensor_list = [torch.zeros(2, 2, device=self.device) for _ in range(self.world_size)]
    #     tensor_list_h = list(tensor_list)
    #     tensor_list_h[1] = tensor_list_h[1].half()


    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.all_gather(tensor_list_h, tensor)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.all_gather(tensor_list, tensor_h)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.all_gather_coalesced([tensor_list_h], tensor_list)
    #         dist.all_gather_coalesced([tensor_list], tensor_list_h)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.all_reduce_coalesced(tensor_list_h)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.reduce_scatter(tensor, tensor_list_h)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.reduce_scatter(tensor_h, tensor_list)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.all_to_all_single(tensor_h, tensor)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.all_to_all(tensor_list_h, tensor_list)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.all_to_all(tensor_list, tensor_list_h)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.scatter(tensor, tensor_list_h)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.gather(tensor_h, tensor_list)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.gather(tensor, tensor_list_h)

    #     with self.assertRaisesRegex(RuntimeError, "tensors with different dtypes"):
    #         dist.scatter(tensor_h, tensor_list)

    # TODO: mindspore ops not suppport complex dtype.
    # def _test_tensor_dtype_complex(self, backend):
    #     dist.init_process_group(
    #         backend,
    #         world_size=self.world_size,
    #     )

    #     tensor = torch.rand(2, device=self.device)
    #     tensor_c = torch.view_as_complex(tensor)
    #     tensor_list = [torch.rand(2, device=self.device) for _ in range(self.world_size)]
    #     tensor_list_c = list(tensor_list)
    #     tensor_list_c[1] = torch.view_as_complex(tensor_list_c[1])

    #     dist.all_gather(tensor_list, tensor)
    #     dist.all_gather(tensor_list, tensor_c)
    #     dist.all_gather(tensor_list_c, tensor)
    #     dist.all_gather(tensor_list_c, tensor_c)


# TODO: mindspore not support spawn, register_backend and mutilple backend. The testcase below can not be run.
# class PythonProcessGroupExtensionTest(MultiProcessTestCase):
#     def setUp(self):
#         super().setUp()
#         self._spawn_processes()

#     def tearDown(self):
#         super().tearDown()
#         try:
#             os.remove(self.file_name)
#         except OSError:
#             pass

#     def test_get_backend_name(self):
#         dpg = DummyProcessGroup(0, 1)
#         self.assertEqual("Dummy", dpg.name())

#     def test_backend_class_attr(self):
#         dist.Backend.register_backend(
#             "dummy",
#             PythonProcessGroupExtensionTest.create_dummy
#         )
#         self.assertEqual(dist.Backend.DUMMY, "DUMMY")
#         self.assertEqual(
#             dist.Backend._plugins["DUMMY"].creator_fn,
#             PythonProcessGroupExtensionTest.create_dummy
#         )

#     def test_backend_config(self):
#         dist.Backend.register_backend(
#             "dummy",
#             PythonProcessGroupExtensionTest.create_dummy
#         )

#         # Ensure backend config can be created with the following arguments
#         backend_config_strings_and_expected_values = [
#             (dist.Backend.GLOO, "cpu:gloo,cuda:gloo"),
#             (dist.Backend.NCCL, "cpu:nccl,cuda:nccl"),
#             (dist.Backend.MPI, "cpu:mpi,cuda:mpi"),
#             (dist.Backend.UCC, "cpu:ucc,cuda:ucc"),
#             (dist.Backend.DUMMY, "cpu:dummy,cuda:dummy"),
#             ("DUMMY", "cpu:dummy,cuda:dummy"),
#             ("dummy", "cpu:dummy,cuda:dummy"),
#             ("cpu:dummy,cuda:dummy", "cpu:dummy,cuda:dummy"),
#             ("cpu:dummy,cuda:nccl", "cpu:dummy,cuda:nccl"),
#             ("cpu:gloo,cuda:dummy", "cpu:gloo,cuda:dummy"),
#             ("cpu:gloo,cuda:nccl", "cpu:gloo,cuda:nccl"),
#             ("cPu:gLoO,cuDa:NcCl", "cpu:gloo,cuda:nccl")
#         ]

#         for config_str, expected_value in backend_config_strings_and_expected_values:
#             with self.subTest(config_str):
#                 # ensures these configs strings are valid and no ValueError is raised
#                 config = dist.BackendConfig(config_str)
#                 self.assertEqual(str(config), expected_value)

#         # Ensure backend config will raise ValueError with the following arguments
#         invalid_backend_config_strings = [
#             "cpu:gloo,cuda:nccl,",  # trailing comma
#             "cpu:gloo,cuda:nccl,cpu:dummy",  # duplicate device
#         ]
#         for config_str in invalid_backend_config_strings:
#             with self.subTest(config_str):
#                 with self.assertRaises(ValueError):
#                     dist.BackendConfig(config_str)

#     def test_init_process_group_with_multiple_backends(self):
#         dist.Backend.register_backend("dummy", PythonProcessGroupExtensionTest.create_dummy)

#         os.environ['MASTER_ADDR'] = 'localhost'
#         os.environ['MASTER_PORT'] = '6789'
#         dist.init_process_group("cpu:dummy,cuda:dummy", rank=self.rank, world_size=self.world_size)

#         # test all_gather
#         input_tensor = torch.ones(2, 2) * 7
#         output_tensor_list = [torch.zeros(2, 2) for _ in range(self.world_size)]
#         dist.all_gather(output_tensor_list, input_tensor)

#         dist.barrier()
#         dist.destroy_process_group()

#     class Options:
#         def __init__(self):
#             pass

#         def create(self):
#             pass

#     @staticmethod
#     def create_dummy(store, group_rank, group_size, timeout):
#         return DummyProcessGroup(group_rank, group_size)

#     def test_collectives(self):
#         dist.Backend.register_backend("dummy", PythonProcessGroupExtensionTest.create_dummy)

#         os.environ['MASTER_ADDR'] = 'localhost'
#         os.environ['MASTER_PORT'] = '6789'
#         dist.init_process_group("dummy", rank=self.rank, world_size=self.world_size)

#         # test all_gather
#         input_tensor = torch.ones(2, 2) * 7
#         output_tensor_list = [torch.zeros(2, 2) for _ in range(self.world_size)]
#         dist.all_gather(output_tensor_list, input_tensor)

#         for tensor in output_tensor_list:
#             self.assertEqual(tensor, input_tensor)

#         # test all_reduce
#         input_tensor = torch.ones(2, 2) * 7
#         dist.all_reduce(input_tensor)
#         self.assertEqual(input_tensor, torch.ones(2, 2) * 7 + 2)

#         # test broadcast
#         input_tensor = torch.zeros(2, 2)
#         dist.broadcast(input_tensor, 0, async_op=True).wait()
#         self.assertEqual(torch.ones(2, 2), input_tensor)

#         # test reduce_scatter
#         output_tensor = torch.zeros(2, 2)
#         input_tensor_list = [torch.ones(2, 2) for _ in range(self.world_size)]
#         dist.reduce_scatter(output_tensor, input_tensor_list)
#         self.assertEqual(output_tensor, torch.zeros(2, 2) + 1)

#         dist.barrier()
#         dist.destroy_process_group()

#     def test_send_recv(self):
#         dist.Backend.register_backend("dummy", PythonProcessGroupExtensionTest.create_dummy)

#         os.environ['MASTER_ADDR'] = 'localhost'
#         os.environ['MASTER_PORT'] = '6789'
#         dist.init_process_group("dummy", rank=self.rank, world_size=self.world_size)

#         # test send
#         input_tensor = torch.zeros(2, 2)
#         dist.send(input_tensor, (self.rank + 1) % self.world_size)
#         self.assertEqual(input_tensor, torch.zeros(2, 2) + 1)

#         with self.assertRaises(ValueError):
#             dist.send(input_tensor, dist.get_rank())

#         # test recv
#         input_tensor = torch.zeros(2, 2)
#         dist.recv(input_tensor, (self.rank + 1) % self.world_size)
#         self.assertEqual(input_tensor, torch.zeros(2, 2) + 2)

#         dist.barrier()
#         # intentionally not calling into `destroy_process_group` as not all
#         # user applications would explicitly that.

# TODO: mindspore not support async ops and return work to do work.wait()
# class CompilerTest(MultiProcessTestCase):
#     def setUp(self):
#         super().setUp()
#         self._spawn_processes()

#     def tearDown(self):
#         super().tearDown()
#         try:
#             os.remove(self.file_name)
#         except OSError:
#             pass

#     def _get_process_group(self):
#         raise NotImplementedError("To be implemented by subclass")

#     def _test_work_wait(self, x: torch.Tensor, comm_fn: Callable):
#         pg = self._get_default_group()

#         def fn(x: torch.Tensor) -> torch.Tensor:
#             # N.B.: explicitly wrapping with CommTensor instead of updating
#             # all_reduce Python implementation, as the later will need more
#             # discussion.
#             y = CommTensor(x + x)
#             work, z = comm_fn(y, group=pg)
#             # this wait() will be ignored in tracing mode as
#             # ProxyTorchDispatchMode only supports torch.Tensor, _ProxyTensor,
#             # and torch.nn.Parameter objects
#             work.wait()
#             if isinstance(z, list):
#                 return [zz * 2 for zz in z]
#             elif isinstance(z, torch.Tensor):
#                 return z * 2
#             else:
#                 raise RuntimeError("Unexpected return type")

#         xx = x.clone()

#         # trace fn into a GraphModule
#         traced_fn = make_fx(fn)(xx)
#         traced_fn.graph.lint()
#         traced_fn.graph.eliminate_dead_code()

#         # make sure the mul op indeed waits for comm
#         for node in traced_fn.graph.nodes:
#             if node.op == "call_function" and "mul.Tensor" in node.target.__name__:
#                 prev = node.args[0]
#                 curr = None
#                 waited = False
#                 commed = False
#                 while prev is not None and not commed:
#                     curr = prev
#                     waited |= all([
#                         curr.op == "call_function",
#                         curr.target == _wait_comm,
#                     ])
#                     commed |= all([
#                         curr.op == "call_function",
#                         CommTensor._is_supported(curr.target.__name__),
#                     ])

#                     prev = curr.args[0]

#                 self.assertTrue(waited)
#                 self.assertTrue(commed)

#         # Update input to make sure we are not recording it as constant during
#         # tracing.
#         x += 1
#         xx += 1

#         y = fn(x)
#         yy = traced_fn(xx)

#         # check correctness
#         self.assertEqual(y, yy)

#         xx += 1
#         yy = traced_fn(xx)
#         self.assertNotEqual(y, yy)

#     def _test_allreduce_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             work = dist.all_reduce(tensor, group=group, async_op=True)
#             return work, tensor

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_allgather_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             out_tensors = [torch.zeros_like(tensor) for _ in range(group.size())]
#             work = dist.all_gather(out_tensors, tensor, group=group, async_op=True)
#             work.wait()

#             return work, sum(out_tensors)

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_allgather_into_tensor_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             out_tensors = [torch.zeros_like(tensor) for _ in range(group.size())]
#             output_tensor = torch.cat(out_tensors, dim=0)
#             work = dist.all_gather_into_tensor(output_tensor, tensor, group=group, async_op=True)
#             work.wait()

#             return work, output_tensor

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_reduce_scatter_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             in_tensors = [tensor.clone() + i for i in range(group.size())]
#             out_tensor = torch.zeros_like(tensor)
#             work = dist.reduce_scatter(out_tensor, in_tensors, group=group, async_op=True)
#             return work, out_tensor

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_reduce_scatter_tensor_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             out_tensor = torch.zeros_like(tensor).chunk(group.size(), dim=0)[self.rank]
#             work = dist.reduce_scatter_tensor(out_tensor, tensor, group=group, async_op=True)
#             return work, out_tensor

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_broadcast_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             work = dist.broadcast(tensor, src=0, group=group, async_op=True)
#             return work, tensor

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_scatter_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             in_tensors = [tensor + i for i in range(group.size())] if self.rank == 0 else None
#             out_tensor = torch.zeros_like(tensor)
#             work = dist.scatter(out_tensor, in_tensors, src=0, group=group, async_op=True)
#             return work, out_tensor

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_alltoall_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             out_tensors = [torch.zeros_like(tensor) for _ in range(group.size())]
#             in_tensors = [tensor for i in range(group.size())]
#             work = dist.all_to_all(out_tensors, in_tensors, group=group, async_op=True)
#             return work, out_tensors

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_nested_comm_tensor_wrapping(self, tensor):
#         def comm_fn(tensor, group=None):
#             work = dist.all_reduce(CommTensor(tensor), group=group, async_op=True)
#             return work, tensor

#         self._test_work_wait(tensor, comm_fn=comm_fn)

#     def _test_consecutive_comm_work_wait(self, tensor):
#         def comm_fn(tensor, group=None):
#             work1 = dist.all_reduce(tensor, group=group, async_op=True)
#             work1.wait()
#             work2 = dist.all_reduce(tensor, group=group, async_op=True)
#             return work2, tensor

#         self._test_work_wait(tensor, comm_fn=comm_fn)

class ReduceOpTest:
    # Ref: https://github.com/pytorch/pytorch/issues/87191
    def test_op_isinstance_of_reduceop(self):
        for reduce_op in (
            c10d.ReduceOp.SUM, c10d.ReduceOp.PRODUCT, c10d.ReduceOp.MIN, c10d.ReduceOp.MAX,
            # TODO: mindspore not support ReduceOp below.
            # c10d.ReduceOp.BAND, c10d.ReduceOp.BOR, c10d.ReduceOp.BXOR, c10d.ReduceOp.AVG, 
        ):
            assert isinstance(reduce_op, c10d.ReduceOp)
        # TODO: mindspore not support PREMUL_SUM ReduceOp yet.
        # for scale in (torch.tensor(1.0), 2.0):
        #     self.assertTrue(isinstance(dist._make_nccl_premul_sum(scale), c10d.ReduceOp))

    # Ref: https://github.com/pytorch/pytorch/pull/87303#discussion_r1002879700
    def test_reduceop_copyable(self):
        for reduce_op in (
            c10d.ReduceOp.SUM, c10d.ReduceOp.PRODUCT, c10d.ReduceOp.MIN, c10d.ReduceOp.MAX,
            # c10d.ReduceOp.BAND, c10d.ReduceOp.BOR, c10d.ReduceOp.BXOR, c10d.ReduceOp.AVG,
        ):
            assert copy.copy(reduce_op) == reduce_op
            assert copy.deepcopy(reduce_op) == reduce_op
            assert copy.copy(c10d.ReduceOp(reduce_op)) == reduce_op
            assert copy.deepcopy(c10d.ReduceOp(reduce_op)) == reduce_op

        # TODO: mindspore not support PREMUL_SUM ReduceOp yet.
        # for scale in (torch.tensor(1.0), 2.0):
        #     reduce_op = dist._make_nccl_premul_sum(scale)
        #     self.assertEqual(copy.copy(reduce_op), reduce_op)
        #     self.assertEqual(copy.deepcopy(reduce_op), reduce_op)

    def test_reduceop_pickle(self):
        for reduce_op in (
            c10d.ReduceOp.SUM, c10d.ReduceOp.PRODUCT, c10d.ReduceOp.MIN, c10d.ReduceOp.MAX,
            # c10d.ReduceOp.AVG, c10d.ReduceOp.BAND, c10d.ReduceOp.BOR, c10d.ReduceOp.BXOR,
        ):
            pickle.loads(pickle.dumps(reduce_op))
            orig = c10d.ReduceOp(reduce_op)
            assert pickle.loads(pickle.dumps(orig)) == orig
        # TODO: mindspore not support PREMUL_SUM ReduceOp yet.
        # for scale in (torch.tensor(1.0), 2.0):
        #     reduce_op = dist._make_nccl_premul_sum(scale)
        #     self.assertEqual(pickle.loads(pickle.dumps(reduce_op)), reduce_op)

    # Ref: https://github.com/pytorch/pytorch/issues/90072
    def test_reduceop_equal(self):
        not_reduceop = "abc"
        for reduce_op in (
            c10d.ReduceOp.SUM, c10d.ReduceOp.PRODUCT, c10d.ReduceOp.MIN, c10d.ReduceOp.MAX,
            # c10d.ReduceOp.AVG, c10d.ReduceOp.BAND, c10d.ReduceOp.BOR, c10d.ReduceOp.BXOR,
        ):
            reduce_op_obj = c10d.ReduceOp(reduce_op)
            # this calls `ReduceOp.__eq__(self, other)`
            assert reduce_op_obj == reduce_op_obj
            # pytorch can not pass either.
            # assert reduce_op_obj != reduce_op
            assert reduce_op_obj != not_reduceop
            assert reduce_op != not_reduceop
            # TODO(crcrpar): This needs to be `assertEqual` for the associativity even though
            # the comparison of `RedOpType` and `ReduceOp` sounds less likely to happen compared
            # to that of `ReduceOp` and `RedOptype`.
            # this calls `RedOpType.__eq__(self, other)`
            # pytorch can not pass either.
            # assert reduce_op != reduce_op_obj

            assert not (None in (reduce_op, reduce_op_obj))
            assert not (not_reduceop in (reduce_op, reduce_op_obj))


if __name__ == '__main__':
    backend = sys.argv[1]
    common_test = AbstractCommTest()
    common_test._test_warn_not_in_group(backend=backend)
    common_test._test_rank_membership(backend=backend)
    reduce_op_test = ReduceOpTest()
    reduce_op_test.test_reduceop_copyable()
    reduce_op_test.test_reduceop_pickle()
    reduce_op_test.test_reduceop_equal()
