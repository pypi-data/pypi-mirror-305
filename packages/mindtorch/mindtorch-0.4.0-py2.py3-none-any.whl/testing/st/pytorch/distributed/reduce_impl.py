import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    tensor = torch.arange(2, dtype=torch.int32).to(f'cuda:{rank}') + 1 + 2 * rank
    dist.reduce(tensor, 0)

    if rank == 0:
        assert np.allclose(tensor.cpu().numpy(), np.array([4, 6]))
        assert tensor.shape == (2,)
    else:
        assert np.allclose(tensor.cpu().numpy(), np.array([3, 4]))
        assert tensor.shape == (2,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)