import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    world_size = 2

    assert dist.is_available() == True
    assert dist.is_mpi_available() == True

    if backend == 'nccl':
        assert dist.is_nccl_available() == True
    else:
        assert dist.is_nccl_available() == False

    assert dist.is_initialized() == False

    dist.init_process_group(backend)

    assert dist.is_initialized() == True

    assert dist.get_world_size() == world_size
    assert dist.get_rank() in [i for i in range(world_size)]

    rank = dist.get_rank()

    ng = dist.new_group([1])
    if rank == 0:
        assert dist.get_rank(ng) == -1
    else:
        assert dist.get_rank(ng) == 0

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)