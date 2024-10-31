import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    ng1 = dist.new_group([0])
    ng2 = dist.new_group([1])

    if rank == 0:
        dist.get_global_rank(ng1, 0) == 0
    elif rank == 1:
        dist.get_global_rank(ng2, 0) == 1

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)