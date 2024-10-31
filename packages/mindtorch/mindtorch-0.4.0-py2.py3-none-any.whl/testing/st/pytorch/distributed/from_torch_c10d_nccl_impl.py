import sys
import math
import numbers
import numpy as np
from mindspore import get_context
import mindtorch.torch as torch
import mindtorch.torch.distributed as c10d
import mindtorch.torch.distributed as dist


def init_multigpu_helper(world_size: int, backend: str):
    """Multigpu tests are designed to simulate the multi nodes with multi
    GPUs on each node. Nccl backend requires equal #GPUs in each process.
    On a single node, all visible GPUs are evenly
    divided to subsets, each process only uses a subset.
    """
    # TODO: torch.cuda.device_count() not support yet.
    # nGPUs = torch.cuda.device_count()
    nGPUs = world_size
    visible_devices = range(nGPUs)

    # If rank is less than or equal to number of available GPU's
    # then each rank can be mapped to corresponding GPU.
    nGPUs_per_process = 1
    # TODO: Only support nGPUs_per_process == 1
    # if world_size > nGPUs:
    #     nGPUs_per_process = nGPUs // world_size
    rank_to_GPU = {
        i: list(visible_devices[i * nGPUs_per_process : (i + 1) * nGPUs_per_process])
        for i in range(world_size)
    }
    return rank_to_GPU

class ProcessGroupNCCLTest():
    def __init__(self, backend):
        self._backend = backend

    def assertEqual(self, tensor1, tensor2):
        if isinstance(tensor1, numbers.Number):
            assert tensor1 == tensor2
            return

        if isinstance(tensor1, (list, tuple)):
            for t1, t2 in zip(tensor1, tensor2):
                assert np.allclose(t1.detach().numpy(), t2.detach().numpy())
        else:
            assert np.allclose(tensor1.detach().numpy(), tensor2.detach().numpy())

    def _create_process_group_nccl(self, store, opts):
        # create nccl processgroup with opts
        if not c10d.is_initialized():
            # c10d.init_process_group(
            #     "nccl",
            #     world_size=self.world_size,
            #     rank=self.rank,
            #     store=store,
            #     pg_options=opts)
            c10d.init_process_group(
                self._backend,
                world_size=self.world_size,
                rank=-1,
                # store=store,
                # pg_options=opts
                )
            self.rank = c10d.get_rank()
        pg = c10d.distributed_c10d._get_default_group()
        return pg

    def opts(self, high_priority_stream=False):
        opts = c10d.ProcessGroupNCCL.Options()
        opts.is_high_priority_stream = high_priority_stream
        return opts

    # TODO: not support spawn processes to launch.
    # def setUp(self):
    #     super().setUp()
    #     # NCCL_BLOCKING_WAIT overrides NCCL_ASYNC_ERROR_HANDLING hence tests
    #     # that use NCCL_BLOCKING_WAIT will test it as expected.
    #     os.environ["NCCL_ASYNC_ERROR_HANDLING"] = "1"
    #     # self.num_gpus = torch.cuda.device_count()
    #     self._spawn_processes()

    # TODO: tearDown is for file store and spawn process, which is not support yet.
    # def tearDown(self):
    #     super().tearDown()
    #     try:
    #         os.remove(self.file_name)
    #     except OSError:
    #         pass

    @property
    def world_size(self):
        return 2

    @property
    def rank_to_GPU(self):
        # return rank to GPU map
        return init_multigpu_helper(self.world_size, "nccl")

    # TODO: MindSpore's broadcast ops not support empty tensor as input.
    # def test_empty_tensors(self):
    #     # TODO: store not support yet.
    #     # store = c10d.FileStore(self.file_name, self.world_size)
    #     store = None
    #     pg = self._create_process_group_nccl(store, self.opts())
    #     local_device_idx = self.rank_to_GPU[self.rank][0]

    #     xs = [torch.FloatTensor([]).cuda(local_device_idx)]
    #     pg.broadcast(xs).wait()
    #     assert 0 == xs[0].numel()

    #     pg.allreduce(xs).wait()
    #     assert 0 == xs[0].numel()

    #     pg.reduce(xs).wait()
    #     assert 0 == xs[0].numel()

    #     ys = [[torch.FloatTensor([]).cuda(local_device_idx) for _ in range(self.world_size)]]
    #     pg.allgather(ys, xs).wait()
    #     for y in ys[0]:
    #         assert 0 == y.numel()

    #     ys = [torch.FloatTensor([]).cuda(local_device_idx)]
    #     xs = [[torch.FloatTensor([]).cuda(local_device_idx) for _ in range(self.world_size)]]
    #     pg.reduce_scatter(ys, xs).wait()
    #     assert 0, ys[0].numel()
    #     c10d.destroy_process_group()

    def test_broadcast_ops(self):
        # TODO: store not support yet.
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())

        def broadcast(xs, rootRank, rootTensor):
            opts = c10d.BroadcastOptions()
            opts.rootRank = rootRank
            opts.rootTensor = rootTensor
            work = pg.broadcast(xs, opts)
            work.wait()
            return work.result()

        # Every rank is root once
        for i in range(self.world_size):
            # Run with 1 input tensor
            x = torch.tensor([self.rank]).to(torch.int32).cuda(self.rank_to_GPU[self.rank][0])
            output = broadcast([x], i, 0)
            self.assertEqual(torch.tensor([i]), output[0])

            # TODO: MindSpore not support broadcast list of tensors yet.
            # expected_tensor = torch.empty([i + 1, i + 1]).fill_(i + 1)
            # xs = [torch.empty([i + 1, i + 1]).fill_(-1).cuda(device=device_idx) for device_idx in self.rank_to_GPU[self.rank]]

            # # test with multiple input tensors (multiple gpu in one rank)
            # for j in range(len(xs)):
            #     if self.rank == i:
            #         xs[j] = expected_tensor.cuda(device=self.rank_to_GPU[self.rank][j])

            #     broadcast(xs, i, j)

            #     for tensor in xs:
            #         self.assertEqual(tensor, expected_tensor)
        c10d.destroy_process_group()

    def test_allreduce_ops(self):
        # TODO: store not support yet.
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        # device_count = torch.cuda.device_count()
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_id = self.rank_to_GPU[self.rank][0]

        def allreduce(tensors, op):
            opts = c10d.AllreduceOptions()
            opts.reduceOp = op
            work = pg.allreduce(tensors, opts)
            work.wait()

        # Sum
        tensors = [torch.tensor([self.rank + 1]).to(torch.int32).cuda(local_device_id)]

        allreduce(tensors, c10d.ReduceOp.SUM)

        ndev = self.world_size

        self.assertEqual(
            torch.tensor([ndev * (ndev + 1) // 2]),
            tensors[0],
        )

        # TODO: AVG not support yet.
        # # Avg (only available for NCCL 2.10+)
        # tensors = [torch.tensor([self.rank + 1.]).cuda(local_device_id)]

        # allreduce(tensors, c10d.ReduceOp.AVG)
        # ndev = self.world_size
        # self.assertEqual(
        #     torch.tensor([ndev * (ndev + 1.) / (2. * ndev)]),
        #     tensors[0],
        # )

        # TODO: Premul Sum not support.
        # Premul Sum
        # if torch.cuda.nccl.version() >= (2, 11, 1):
        #     for dtype in torch.half, torch.float, torch.double:
        #         for factor in (3.0, torch.tensor([5.0], device=local_device_id, dtype=dtype)):
        #             tensors = [torch.tensor([self.rank + 1]).cuda(local_device_id).to(dtype=dtype)]

        #             allreduce(tensors, c10d._make_nccl_premul_sum(factor))

        #             self.assertEqual(
        #                 factor * torch.tensor([self.world_size * (self.world_size + 1) / 2],
        #                                       dtype=dtype, device=local_device_id),
        #                 tensors[0],
        #             )

        # Product
        tensors = [torch.tensor([self.rank + 1]).to(torch.int32).cuda(local_device_id)]

        allreduce(tensors, c10d.ReduceOp.PRODUCT)
        self.assertEqual(
            torch.tensor([math.factorial(self.world_size)]), tensors[0]
        )

        # Min
        tensors = [torch.tensor([self.rank + 1]).to(torch.int32).cuda(local_device_id)]

        allreduce(tensors, c10d.ReduceOp.MIN)
        self.assertEqual(torch.tensor([1]), tensors[0])

        # Max
        tensors = [torch.tensor([self.rank + 1]).to(torch.int32).cuda(local_device_id)]

        allreduce(tensors, c10d.ReduceOp.MAX)
        self.assertEqual(torch.tensor([self.world_size]), tensors[0])

        # TODO: not support ReduceOp: BAND, BOR, BXOR
        # for op, err in zip((c10d.ReduceOp.BAND, c10d.ReduceOp.BOR, c10d.ReduceOp.BXOR),
        #                    ("ReduceOp.BAND", "ReduceOp.BOR", "ReduceOp.BXOR")):
        #     with self.assertRaisesRegex(
        #             RuntimeError, "Cannot use " + err + " with NCCL"
        #     ):
        #         allreduce(tensors, op)
        c10d.destroy_process_group()

    def test_reduce_ops(self):
        # TODO: store not support yet.
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_id = self.rank_to_GPU[self.rank][0]

        def reduce(xs, rootRank, rootTensor, op=None):
            opts = c10d.ReduceOptions()
            opts.rootRank = rootRank
            opts.rootTensor = rootTensor
            if op:
                opts.reduceOp = op
            work = pg.reduce(xs, opts)
            work.wait()

        # for every root tensor
        for rt in range(self.world_size):
            tensors = [torch.tensor([self.rank + 1]).cuda(local_device_id)]

            reduce(tensors, rt, 0)

            if self.rank == rt:
                self.assertEqual(
                    torch.tensor([self.world_size * (self.world_size + 1) // 2]),
                    tensors[0],
                )
            else:
                self.assertEqual(
                    torch.tensor([self.rank + 1]),
                    tensors[0],
                )

            for op, err in zip(
                (c10d.ReduceOp.BAND, c10d.ReduceOp.BOR, c10d.ReduceOp.BXOR),
                ("ReduceOp.BAND", "ReduceOp.BOR", "ReduceOp.BXOR"),
            ):
                with self.assertRaisesRegex(
                        RuntimeError, "Cannot use " + err + " with NCCL"
                ):
                    reduce(tensors, self.rank, rt, op)

            # Premul sum
            if torch.cuda.nccl.version() >= (2, 11, 1):
                for factor in (3.0, torch.tensor([5.0], device=local_device_id)):
                    if isinstance(factor, torch.Tensor):
                        factor_ref = factor.cpu().item()
                    else:
                        factor_ref = factor
                    float_tensors = [
                        torch.tensor(
                            [self.rank + 1.0], device=f"cuda:{local_device_id}")
                    ]
                    float_tensors_ref = [
                        torch.tensor(
                            [(self.rank + 1.0) * factor_ref], device=f"cuda:{local_device_id}")
                    ]

                    reduce(float_tensors_ref, rt, 0)
                    reduce(float_tensors, rt, 0, c10d._make_nccl_premul_sum(factor))
                    if self.rank == rt:
                        self.assertEqual(float_tensors_ref[0], float_tensors[0])

    def test_allgather_ops(self):
        # TODO: store not support yet.
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_ids = self.rank_to_GPU[self.rank]

        def allgather(output_ts, input_ts):
            work = pg.allgather(output_ts, input_ts)
            return work.wait()

        tensors = [torch.empty(2, 2).fill_(2).to(torch.int32).cuda(device=i) for i in local_device_ids]
        output_tensors = []
        expected_output = []

        output_per_gpu = ([torch.empty(2, 2).fill_(-1)] * len(local_device_ids) * self.world_size)
        expected_per_gpu = ([torch.empty(2, 2).fill_(2)] * len(local_device_ids) * self.world_size)

        # TODO: MindSpore not support nGPUS per-process allgather
        # for gpu in local_device_ids:
        #     output_tensors.append([t.cuda(device=gpu) for t in output_per_gpu])
        #     expected_output.append([t.cuda(device=gpu) for t in expected_per_gpu])
        gpu = local_device_ids[0]
        output_tensors = [t.cuda(device=gpu) for t in output_per_gpu]
        expected_output = [t.cuda(device=gpu) for t in expected_per_gpu]

        result = allgather(output_tensors, tensors)

        # Verification
        self.assertEqual(output_tensors, expected_output)
        c10d.destroy_process_group()

    def test_allgather_base_ops(self):
        # TODO: store not support yet.
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_id = self.rank_to_GPU[self.rank][0]

        def allgather_base(output_t, input_t):
            work = pg._allgather_base(output_t, input_t)
            work.wait()

        # allgather_base is GPU number agnostic.
        # Each rank contribute one tensor regardless of GPU counts
        tensor = torch.tensor([self.rank]).to(torch.int32).cuda(local_device_id)
        output_t = torch.empty((self.world_size), dtype=tensor.dtype).cuda(local_device_id)

        allgather_base(output_t, tensor)

        # Verification
        self.assertEqual(torch.arange(self.world_size), output_t)
        c10d.destroy_process_group()

    def test_allgather_base_basics(self):
        # TODO: store not support yet.
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_id = self.rank_to_GPU[self.rank][0]

        def allgather_base(output_t, input_t):
            work = pg._allgather_base(output_t, input_t)
            work.wait()

        # anticipate an error
        # RuntimeError, "output tensor must have the same type as input tensor"
        try:
            tensor = torch.tensor([self.rank]).to(torch.int32).cuda(local_device_id)
            output_t = torch.empty((self.world_size + 1), dtype=tensor.dtype).cuda(
                local_device_id
            )
            # fails the check because output_t is not correctly sized
            allgather_base(output_t, tensor)
        except:
            assert True

        # anticipate an error
        # RuntimeError, "output tensor must have the same type as input tensor"
        try:
            tensor = torch.tensor([self.rank], dtype=torch.float).cuda(local_device_id)
            output_t = torch.empty((self.world_size + 1), dtype=torch.long).cuda(
                local_device_id
            )
            # fails the check because the dtype is different
            allgather_base(output_t, tensor)
        except:
            assert True
        c10d.destroy_process_group()

    def test_gather_ops(self):
        if self._backend == 'nccl':
            # TODO: gather not support on gpu yet.
            return
        # TODO: store not support yet.
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_ids = self.rank_to_GPU[self.rank]
        num_gpus = len(local_device_ids)

        def gather(output_t, input_t, rootRank):
            opts = c10d.GatherOptions()
            opts.rootRank = rootRank
            if rootRank == self.rank:
                work = pg.gather(output_t, input_t, opts)
            else:
                work = pg.gather([], input_t, opts)
            work.wait()

        tensors = torch.tensor([self.rank], dtype=torch.float) # mindspore gather can only support int
        output_ts = []
        for rank in range(self.world_size):
            output_ts.append(torch.tensor([-1],dtype=torch.float))
        gather(output_ts, tensors, 0)
        if self.rank == 0:
            expected = []
            for rank in range(self.world_size):
                expected.append(torch.tensor([rank], dtype=torch.float))
            self.assertEqual(expected, output_ts)

    #   # TODO: not support create tensor on other device, like "cuda(device_id)"
    #   # so the testcase below can not be run
    #     # init input
    #     tensors = []
    #     for device_id in local_device_ids:
    #         tensors.append(torch.tensor([self.rank]).cuda(device_id))

    #     # init output
    #     output_ts = []
    #     for idx in range(num_gpus):
    #         gpu_idx = local_device_ids[idx]
    #         output_ts.append([])
    #         for rank in range(self.world_size):
    #             output_ts[idx].append(torch.tensor([-1]).cuda(gpu_idx))

    #     expected = [[torch.tensor([rank]) for rank in range(self.world_size)]]
    #     for rank in range(self.world_size):
    #         gather(output_ts, tensors, rank)
    #         if rank == self.rank:
    #             self.assertEqual(expected, output_ts)

    # def test_gather_stress(self):
    #     store = c10d.FileStore(self.file_name, self.world_size)
    #     pg = self._create_process_group_nccl(store, self.opts())
    #     local_device_ids = self.rank_to_GPU[self.rank]
    #     num_gpus = len(local_device_ids)

    #     def gather(output_t, input_t, rootRank):
    #         opts = c10d.GatherOptions()
    #         opts.rootRank = rootRank
    #         if rootRank == self.rank:
    #             work = pg.gather(output_t, input_t, opts)
    #         else:
    #             work = pg.gather([], input_t, opts)
    #         work.wait()

    #     stress_length = 1000

    #     # init input
    #     tensors = []
    #     for i in range(stress_length):
    #         tensors.append([])
    #         for device_id in local_device_ids:
    #             tensors[i].append(torch.tensor([self.rank]).cuda(device_id))

    #     # init output
    #     output_ts = []
    #     for i in range(stress_length):
    #         output_ts.append([[] for _ in range(num_gpus)])
    #         for idx, ls in enumerate(output_ts[i]):
    #             gpu_idx = local_device_ids[idx]
    #             for _ in range(self.world_size):
    #                 ls.append(torch.tensor([-1]).cuda(gpu_idx))

    #     expected = [[torch.tensor([rank]) for rank in range(self.world_size)]]
    #     for i in range(stress_length):
    #         for rank in range(self.world_size):
    #             gather(output_ts[i], tensors[i], rank)
    #             # Verification
    #             if rank == self.rank:
    #                 self.assertEqual(output_ts[i], expected)

    # def test_gather_checks(self):
    #     store = c10d.FileStore(self.file_name, self.world_size)
    #     pg = self._create_process_group_nccl(store, self.opts())
    #     local_device_ids = self.rank_to_GPU[self.rank]
    #     num_gpus = len(local_device_ids)

    #     # init input
    #     tensors = []
    #     for device_id in local_device_ids:
    #         tensors.append(torch.tensor([self.rank]).cuda(device_id))

    #     # init output
    #     output_ts = []
    #     for idx in range(num_gpus):
    #         gpu_idx = local_device_ids[idx]
    #         output_ts.append([])
    #         for rank in range(self.world_size):
    #             output_ts[idx].append(torch.tensor([-1]).cuda(gpu_idx))

    #     with self.assertRaisesRegex(RuntimeError, "invalid root rank"):
    #         opts = c10d.GatherOptions()
    #         opts.rootRank = -1
    #         pg.gather(output_ts, tensors, opts)

    #     with self.assertRaisesRegex(TypeError, "incompatible function arguments"):
    #         pg.gather(output_ts, tensors, 0)

    #     with self.assertRaisesRegex(RuntimeError, "invalid root rank"):
    #         opts = c10d.GatherOptions()
    #         opts.rootRank = self.world_size
    #         pg.gather(output_ts, tensors, opts)

    #     with self.assertRaisesRegex(
    #         # throws error message from dispatcher
    #         RuntimeError, "There were no tensor arguments to this function"
    #     ):
    #         opts = c10d.GatherOptions()
    #         opts.rootRank = 0
    #         pg.gather(output_ts, [], opts)

    #     with self.assertRaisesRegex(
    #         RuntimeError, "Tensors must be on distinct GPU devices"
    #     ):
    #         # init input
    #         tensors2 = []
    #         for device_id in local_device_ids:
    #             tensors2.append(torch.tensor([self.rank]).cuda(device_id))
    #             tensors2.append(torch.tensor([self.rank]).cuda(device_id))

    #         opts = c10d.GatherOptions()
    #         opts.rootRank = 0
    #         pg.gather(output_ts, tensors2, opts)

    def test_scatter_ops(self):
        if self._backend == 'nccl':
            # TODO: scatter not support on gpu yet.
            return
        # TODO: store not support yet.
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_ids = self.rank_to_GPU[self.rank]
        num_gpus = len(local_device_ids)

        def scatter(output_t, input_t, rootRank):
            opts = c10d.ScatterOptions()
            opts.rootRank = rootRank
            if rootRank == self.rank:
                work = pg.scatter(output_t, input_t, opts)
            else:
                work = pg.scatter(output_t, [], opts)
            work.wait()

        tensors = torch.tensor([-1], dtype=torch.float)
        scatter_list = []
        for rank in range(self.world_size):
            scatter_list.append(torch.tensor([rank], dtype=torch.float))
        expected = torch.tensor([self.rank], dtype=torch.float)
        scatter(tensors, scatter_list, 0)
        self.assertEqual(expected, tensors)

    #     # init output
    #     tensors = []
    #     for device_id in local_device_ids:
    #         tensors.append(torch.tensor([-1]).cuda(device_id))

    #     # init input
    #     scatter_list = []
    #     for idx in range(num_gpus):
    #         gpu_idx = local_device_ids[idx]
    #         scatter_list.append([])
    #         for rank in range(self.world_size):
    #             scatter_list[idx].append(torch.tensor([rank]).cuda(gpu_idx))

    #     # test each rank to scatter
    #     expected = [torch.tensor([self.rank])]
    #     for rank in range(self.world_size):
    #         scatter(tensors, scatter_list, rank)
    #         self.assertEqual(expected, tensors)

    # def test_scatter_stress(self):
    #     store = c10d.FileStore(self.file_name, self.world_size)
    #     pg = self._create_process_group_nccl(store, self.opts())
    #     local_device_ids = self.rank_to_GPU[self.rank]
    #     num_gpus = len(local_device_ids)

    #     def scatter(output_t, input_t, rootRank):
    #         opts = c10d.ScatterOptions()
    #         opts.rootRank = rootRank
    #         if rootRank == self.rank:
    #             work = pg.scatter(output_t, input_t, opts)
    #         else:
    #             work = pg.scatter(output_t, [], opts)
    #         work.wait()

    #     stress_length = 1000

    #     # init output
    #     tensors = []
    #     for i in range(stress_length):
    #         tensors.append([])
    #         for device_id in local_device_ids:
    #             tensors[i].append(torch.tensor([-1]).cuda(device_id))

    #     # init input
    #     scatter_list = []
    #     for i in range(stress_length):
    #         scatter_list.append([[] for _ in range(num_gpus)])
    #         for idx, ls in enumerate(scatter_list[i]):
    #             gpu_idx = local_device_ids[idx]
    #             for rank in range(self.world_size):
    #                 ls.append(torch.tensor([rank]).cuda(gpu_idx))


    #     # test each rank to scatter
    #     expected = [torch.tensor([self.rank])]
    #     for i in range(stress_length):
    #         for rank in range(self.world_size):
    #             scatter(tensors[i], scatter_list[i], rank)
    #             # Verification
    #             self.assertEqual(tensors[i], expected)

    # def test_scatter_checks(self):
    #     store = c10d.FileStore(self.file_name, self.world_size)
    #     pg = self._create_process_group_nccl(store, self.opts())
    #     local_device_ids = self.rank_to_GPU[self.rank]
    #     num_gpus = len(local_device_ids)

    #     # init output
    #     tensors = []
    #     for device_id in local_device_ids:
    #         tensors.append(torch.tensor([-1]).cuda(device_id))

    #     # init input
    #     scatter_list = []
    #     for idx in range(num_gpus):
    #         gpu_idx = local_device_ids[idx]
    #         scatter_list.append([])
    #         for rank in range(self.world_size):
    #             scatter_list[idx].append(torch.tensor([rank]).cuda(gpu_idx))

    #     with self.assertRaisesRegex(RuntimeError, "invalid root rank"):
    #         opts = c10d.ScatterOptions()
    #         opts.rootRank = -1
    #         pg.scatter(tensors, scatter_list, opts)

    #     with self.assertRaisesRegex(TypeError, "incompatible function arguments"):
    #         pg.scatter(tensors, scatter_list, 0)

    #     with self.assertRaisesRegex(RuntimeError, "invalid root rank"):
    #         opts = c10d.ScatterOptions()
    #         opts.rootRank = self.world_size
    #         pg.scatter(tensors, scatter_list, opts)

    #     with self.assertRaisesRegex(
    #         # throws error message from dispatcher
    #         RuntimeError, "There were no tensor arguments to this function"
    #     ):
    #         opts = c10d.ScatterOptions()
    #         opts.rootRank = 0
    #         pg.scatter([], scatter_list, opts)

    def test_reduce_scatter_ops(self):
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_ids = self.rank_to_GPU[self.rank]
        num_gpus = len(local_device_ids)

        # def reduce_scatter(outputs, input_lists, op):
        #     opts = c10d.ReduceScatterOptions()
        #     opts.reduceOp = op
        #     work = pg.reduce_scatter(outputs, input_lists, opts)
        #     work.wait()

        # TODO: reduce scatter not support mutil-gpu per-process
        # output = [torch.tensor([0]).cuda(i) for i in local_device_ids]

        #  GPU/rank
        #   0         [1], [2], [3], [4]
        #   1         [2], [3], [4], [5]
        #   2         [3], [4], [5], [6]
        #   3         [4], [5], [6], [7]

        # Sum
        tensor_lists = []
        input_per_gpu = []

        for i in range(self.world_size):
            input_per_gpu.append(torch.tensor([self.rank + i + 1]).to(torch.int32))

        for gpu in local_device_ids:
            tensor_lists.append([t.cuda(device=gpu) for t in input_per_gpu])

        # reduce_scatter(output, tensor_lists, c10d.ReduceOp.SUM)

        # for i in range(num_gpus):
        #     expected = torch.tensor(
        #         [
        #             (1 + self.world_size) * self.world_size // 2
        #             + self.world_size * self.rank
        #         ])
        #     self.assertEqual(expected, output[i])

        # Min
        # reduce_scatter(output, tensor_lists, c10d.ReduceOp.MIN)

        # for i in range(num_gpus):
        #     expected = torch.tensor([self.rank + 1 + i])
        #     self.assertEqual(expected, output[i])

        # Max
        # reduce_scatter(output, tensor_lists, c10d.ReduceOp.MAX)

        # for i in range(num_gpus):
        #     expected = torch.tensor(
        #         [self.rank + self.world_size + i]
        #     )
        #     self.assertEqual(expected, output[i])

        # Product
        # reduce_scatter(output, tensor_lists, c10d.ReduceOp.PRODUCT)

        # math package don't have math.perm until python 3.8, so
        # we implement a naive version here.
        # def perm(n, k):
        #     prod_val = n
        #     for val in range(n - k + 1, n):
        #         prod_val *= val
        #     return prod_val

        # for i in range(num_gpus):
        #     prod_val = perm(self.rank + self.world_size, self.world_size)

        #     expected = torch.tensor([prod_val])
        #     self.assertEqual(expected, output[i])

        # Test the input params overridden scenarios, aka, when the input is
        # a list and output is just one tensor.
        # Sum
        output_tensor = torch.empty_like(input_per_gpu[0][0]).cuda(self.rank)
        input_list = [tensor[0].cuda(self.rank) for tensor in input_per_gpu]
        pg.reduce_scatter(output_tensor, input_list, c10d.ReduceOp.SUM).wait()
        expected = torch.tensor(
            (1 + self.world_size) * self.world_size // 2 + self.world_size * self.rank
        )
        self.assertEqual(expected, output_tensor)

        # TODO: MindSpore not support Min
        # # Min
        # pg.reduce_scatter(output_tensor, input_list, c10d.ReduceOp.MIN).wait()
        # expected = torch.tensor(self.rank + 1)
        # self.assertEqual(expected, output_tensor)

        # Max
        pg.reduce_scatter(output_tensor, input_list, c10d.ReduceOp.MAX).wait()
        expected = torch.tensor(self.rank + self.world_size)
        self.assertEqual(expected, output_tensor)

        # TODO: MindSpore not support Product
        # # Product
        # pg.reduce_scatter(output_tensor, input_list, c10d.ReduceOp.PRODUCT).wait()
        # prod_val = self.rank + 1
        # for k in range(1, self.world_size):
        #     prod_val = prod_val * (self.rank + 1 + k)
        # expected = torch.tensor(prod_val)
        # self.assertEqual(expected, output_tensor)

        # TODO: MindSpore not support premul sum yet.
        # if torch.cuda.nccl.version() >= (2, 11, 1):
        #     for factor in (3.0, torch.tensor([5.0], device=self.rank)):
        #         if isinstance(factor, torch.Tensor):
        #             factor_ref = factor.cpu().item()
        #         else:
        #             factor_ref = factor
        #         output = [t.float() for t in output]
        #         tensor_lists = [[t.float() for t in tl] for tl in tensor_lists]
        #         output_ref = [t.float() for t in output]
        #         tensor_lists_ref = [[t.float() * factor_ref for t in tl] for tl in tensor_lists]
        #         reduce_scatter(output, tensor_lists, c10d._make_nccl_premul_sum(factor))
        #         reduce_scatter(output_ref, tensor_lists_ref, c10d.ReduceOp.SUM)
        #         self.assertEqual(output_ref, output)

    def test_reduce_scatter_base_ops(self):
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_id = self.rank_to_GPU[self.rank][0]

        def reduce_scatter_base(output_t, input_t):
            work = pg._reduce_scatter_base(output_t, input_t)
            work.wait()

        # reduce_scatter_base is GPU number agnostic.
        # Each rank contribute one tensor regardless of GPU counts
        output_t = torch.empty([1]).cuda(local_device_id)
        tensor = torch.arange(self.world_size, dtype=output_t.dtype).cuda(local_device_id)

        reduce_scatter_base(output_t, tensor)

        # Verification
        self.assertEqual(output_t[0].item(), self.rank * self.world_size)

    def test_barrier(self):
        # TODO: MindSpore only support barrier on Ascend.
        if get_context("device_target") != "Ascend":
            return
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        pg = self._create_process_group_nccl(store, self.opts())
        local_device_ids = self.rank_to_GPU[self.rank]

        def allreduce(tensors):
            opts = c10d.AllreduceOptions()
            work = pg.allreduce(tensors, opts)
            return work

        # Making the collective to operate on
        # 1, 2, 3, 4, .... len(local_device_ids) GPUs
        tensors_list = [[] for _ in range(len(local_device_ids))]

        for i in range(1, len(local_device_ids) + 1):
            for j in range(i):
                tensors_list[i - 1].append(torch.tensor([j + 1]).to(torch.int32).cuda(local_device_ids[j]))

        works = []
        for tensors in tensors_list:
            work = allreduce(tensors)
            works.append(work)

        # Barrier will ensure that all previous work is completed
        pg.barrier().wait()

        for i in range(1, len(local_device_ids) + 1):
            for j in range(i):
                self.assertEqual(
                    torch.tensor([(j + 1) * self.world_size]), tensors_list[i - 1][j]
                )

    def test_send_recv(self):
        # store = c10d.FileStore(self.file_name, self.world_size)
        store = None
        self._create_process_group_nccl(store, self.opts())
        device = self.rank_to_GPU[self.rank][0]

        # Generate the same random tensor
        torch.manual_seed(0)
        send_tensor = torch.rand(10, 10, device=device).to(torch.float32)
        if self.rank == 0:
            dist.send(send_tensor, 1)
        if self.rank == 1:
            recv_tensor = torch.rand(10, 10, device=device).to(torch.float32)
            dist.recv(recv_tensor, 0)
            self.assertEqual(send_tensor, recv_tensor)

        # TODO: don't have problem when send view tensor.
        # # Test with non-contiguous tensors.
        # send_tensor_view = send_tensor.t()
        # if self.rank == 0:
        #     # with self.assertRaisesRegex(RuntimeError, 'Tensors must be contiguous'):
        #     try:
        #         dist.send(send_tensor_view, 1)
        #     except:
        #         assert True

    # TODO: MindSpore not support to(device), so this testcase will not raise error.
    # def test_nccl_dist_backend_error(self):
    #     store = c10d.FileStore(self.file_name, self.world_size)
    #     self._create_process_group_nccl(store, self.opts())

    #     # Both rank 0 and 1 will use the same CUDA device resulting in ncclInvalidUsage
    #     with self.assertRaises(dist.DistBackendError) as cm:
    #         dist.broadcast(torch.tensor([1, 2, 3]).cuda(), 0)

    #     self.assertIsInstance(cm.exception, RuntimeError)

if __name__ == '__main__':
    backend = sys.argv[1]
    NCCLTest = ProcessGroupNCCLTest(backend)
    # NCCLTest.test_empty_tensors()
    NCCLTest.test_broadcast_ops()
    NCCLTest.test_allreduce_ops()
    # NCCLTest.test_reduce_ops() # MindSpore's Reduce not support yet
    NCCLTest.test_allgather_ops()
    NCCLTest.test_allgather_base_ops()
    NCCLTest.test_allgather_base_basics()
    NCCLTest.test_gather_ops()
    # NCCLTest.test_gather_stress() # MindSpore's Gather not support yet
    # NCCLTest.test_gather_checks() # MindSpore's Gather not support yet
    NCCLTest.test_scatter_ops()
    NCCLTest.test_reduce_scatter_ops()
    NCCLTest.test_reduce_scatter_base_ops()
    NCCLTest.test_barrier()
    NCCLTest.test_send_recv()
