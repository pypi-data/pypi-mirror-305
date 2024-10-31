import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    ng1 = dist.new_group([0])
    ng2 = dist.new_group([1])

    dist.destroy_process_group(ng1)
    dist.destroy_process_group(ng2)
    dist.destroy_process_group()

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)