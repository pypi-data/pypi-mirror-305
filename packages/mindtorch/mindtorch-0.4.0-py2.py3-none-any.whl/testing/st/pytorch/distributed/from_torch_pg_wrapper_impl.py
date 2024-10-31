import os
from datetime import timedelta

import mindtorch.torch as torch
import mindtorch.torch.distributed as c10d

class AbstractProcessGroupWrapperTest():
    # TODO: need 'timeout' feature for process_group to accomplish the test.
    # timeout can escape from hang, and raise a error. 
    # but now mindspore not support timeout option, will hang here without raise error. 
    def _test_collective_hang(self, wrapper_pg, use_cuda=False):
        # All ranks besides 1 call allreduce and wrapper_pg should detect a hang
        # and report an issue with rank 1.
        faulty_rank = 1
        if self.rank != faulty_rank:
            tensor = torch.randn(20, 10)
            if use_cuda:
                tensor = tensor.to(self.rank)

            if self.rank == 0:
                # Rank 0 reports faulty ranks
                err = f"Ranks {faulty_rank} failed to pass monitoredBarrier"
            else:
                err = "Please check rank 0 logs for faulty rank"

            # Gloo can sometimes throw the following error if a rank exits early
            # before rank 0 calls into the allreduce.
            err += "|Connection closed by peer|Connection reset by peer"
            wrapper_pg.allreduce([tensor])

    def _test_collectives_op_mismatch(self, wrapper_pg, use_cuda=False):
        tensor = torch.randn(20, 10)
        if use_cuda:
            tensor = tensor.to(self.rank)
        works = []
        # Run a few successful collectives
        for _ in range(10):
            work = wrapper_pg.allreduce([tensor])
            works.append(work)

        for w in works:
            w.wait()

        # Simulate mismatch: allreduce vs reduce.
        # Error including info about inconsistent collective, rank, tensor
        # shape, device, and dtype should be raised.
        # TODO: reduce not support
        # if self.rank == 0:
        #     wrapper_pg.allreduce([tensor])
        # else:
        #     wrapper_pg.reduce([tensor], self.rank)

        # if self.rank == 0:
        #     wrapper_pg.reduce([tensor], 0)
        # else:
        #     wrapper_pg.barrier()

        # TODO: wrapper_pg.scatter not support yet.
        # scatter_result = [torch.ones(4) * i for i in range(self.world_size)]
        # scattered_tensor = torch.empty(4)
        # if self.rank == 0:
        #     wrapper_pg.scatter(scattered_tensor, scatter_result, 0)
        # else:
        #     wrapper_pg.reduce_scatter(scattered_tensor, scatter_result)

        if self.rank == 0:
            wrapper_pg.broadcast(tensor, 0)
        else:
            output_tensors = [
                torch.zeros_like(tensor) for _ in range(self.world_size)
            ]
            wrapper_pg.allgather([output_tensors], [tensor])

    def _test_collective_shape_mismatch(self, wrapper_pg, use_cuda=False):
        wrapper_pg.barrier()
        dim = 2 if self.rank == 0 else 10
        tensor = torch.randn(20, dim)
        if use_cuda:
            tensor = tensor.to(self.rank)
        with self.assertRaisesRegex(RuntimeError, ".*") as cm:
            wrapper_pg.allreduce([tensor])
        self._validate_error(
            exception=cm.exception,
            op_type="ALLREDUCE",
            rank=self.rank,
            tensor=tensor,
        )

        # Check errors are raised when dimensionality of shapes is different
        tensor = torch.randn(20, 10, 2) if self.rank == 0 else torch.randn(20, 10)
        if use_cuda:
            tensor = tensor.to(self.rank)
        with self.assertRaisesRegex(RuntimeError, ".*") as cm:
            wrapper_pg.allreduce([tensor])
        self._validate_error(
            exception=cm.exception,
            op_type="ALLREDUCE",
            rank=self.rank,
            tensor=tensor,
        )

        # Check shape errors with scatter
        input = [
            torch.tensor(
                [self.rank] if self.rank == 0 else [self.rank, self.rank],
                device=self.rank if use_cuda else "cpu",
            )
            for _ in range(self.world_size)
        ]
        outputs = [
            torch.tensor(
                [-1] if self.rank == 0 else [-1, -1],
                device=self.rank if use_cuda else "cpu",
            )
            for _ in range(self.world_size)
        ]
        root_rank = 0
        opts = c10d.ScatterOptions()
        opts.rootRank = root_rank
        with self.assertRaisesRegex(RuntimeError, ".*") as cm:
            if self.rank == root_rank:
                wrapper_pg.scatter([outputs[self.rank]], [input], opts).wait()
            else:
                wrapper_pg.scatter([outputs[self.rank]], [], opts).wait()
        self._validate_error(
            exception=cm.exception,
            op_type="SCATTER",
            rank=self.rank,
            tensor=outputs[self.rank],
        )

class ProcessGroupNCCLWrapperTest(AbstractProcessGroupWrapperTest):
    # TODO: not support spawn processes
    # def setUp(self):
    #     super(AbstractProcessGroupWrapperTest, self).setUp()
    #     self._spawn_processes()
    #     # NCCL_BLOCKING_WAIT overrides NCCL_ASYNC_ERROR_HANDLING hence tests
    #     # that use NCCL_BLOCKING_WAIT will test it as expected.
    #     os.environ["NCCL_ASYNC_ERROR_HANDLING"] = "1"

    @property
    def world_size(self) -> int:
        return 2

    def _create_wrapper_pg(self, with_new_group=False, timeout=10.0):
        # store = c10d.FileStore(self.file_name, self.world_size) # store not support yet.
        store = None
        self.rank = -1
        if not c10d.is_initialized():
            c10d.init_process_group(
                backend="nccl",
                rank=self.rank,
                world_size=self.world_size,
                store=store, 
                timeout=timedelta(seconds=timeout),
            )

        self.rank = c10d.get_rank()

        if with_new_group:
            pg = c10d.new_group(backend="nccl", timeout=timedelta(seconds=timeout))
        # TODO: not support create process Group from create Object.
        # else:
        #     _pg = c10d.ProcessGroupNCCL(
        #         store, self.rank, self.world_size, timeout=timedelta(seconds=timeout)
        #     )
        #     pg = c10d._create_process_group_wrapper(
        #         _pg,
        #         "unused",
        #         store,
        #         self.rank,
        #         self.world_size,
        #         timeout=timeout,
        #     )
        return pg

    def test_collective_hang(self):
        pg = self._create_wrapper_pg(with_new_group=True, timeout=2.0)
        self._test_collective_hang(pg)
        c10d.destroy_process_group()

    # NOTE: these tests are separated by debug level instead of combined into
    # one due to https://github.com/pytorch/pytorch/issues/55967, they can be
    # combined after that is resolved.
    def test_collectives_op_mismatch_debug_mode(self):
        pg = self._create_wrapper_pg(with_new_group=True)
        self._test_collectives_op_mismatch(pg, use_cuda=True)
        self._test_nccl_only_op_mismatch(pg)

    def test_collectives_op_mismatch(self):
        # pg = self._create_wrapper_pg(with_new_group=False)
        pg = self._create_wrapper_pg(with_new_group=True)
        self._test_collectives_op_mismatch(pg, use_cuda=True)
        # self._test_nccl_only_op_mismatch(pg)
        c10d.destroy_process_group()

    def test_collective_shape_mismatch_debug_mode(self):
        pg = self._create_wrapper_pg(with_new_group=True)
        self._test_collective_shape_mismatch(pg, use_cuda=True)
        self._test_nccl_only_shape_mismatch(pg)

    def test_collective_shape_mismatch(self):
        # pg = self._create_wrapper_pg(with_new_group=False)
        pg = self._create_wrapper_pg(with_new_group=True)
        self._test_collective_shape_mismatch(pg, use_cuda=True)
        self._test_nccl_only_shape_mismatch(pg)

    def _test_nccl_only_op_mismatch(self, wrapper_pg):
        device = f"cuda:{self.rank}"
        with self.assertRaisesRegex(RuntimeError, ".*") as cm:
            output = torch.zeros(4 + self.rank, device=device)
            input = torch.ones(4 * self.world_size, device=device)
            if self.rank == 0:
                wrapper_pg._allgather_base(output, input).wait()
            else:
                wrapper_pg._reduce_scatter_base(output, input).wait()
        self._validate_error(
            exception=cm.exception,
            op_type="ALLGATHER_BASE" if self.rank == 0 else "REDUCE_SCATTER_BASE",
            rank=self.rank,
            tensor=input,
        )

    def _test_nccl_only_shape_mismatch(self, wrapper_pg):
        device = f"cuda:{self.rank}"
        with self.assertRaisesRegex(RuntimeError, ".*") as cm:
            output = torch.zeros(4 + self.rank, device=device)
            input = torch.ones(4 * self.world_size, device=device)

            wrapper_pg._reduce_scatter_base(output, input).wait()
        self._validate_error(
            exception=cm.exception,
            op_type="REDUCE_SCATTER_BASE",
            rank=self.rank,
            tensor=input,
        )
        with self.assertRaisesRegex(RuntimeError, ".*") as cm:
            output = torch.zeros(4, device=device)
            input = torch.ones((4 + self.rank) * self.world_size, device=device)

            wrapper_pg._reduce_scatter_base(output, input).wait()
        self._validate_error(
            exception=cm.exception,
            op_type="REDUCE_SCATTER_BASE",
            rank=self.rank,
            tensor=input,
        )

if __name__ == '__main__':
    PgNCCLTest = ProcessGroupNCCLWrapperTest()
    PgNCCLTest.test_collectives_op_mismatch()
    PgNCCLTest.test_collective_hang()

