import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    if rank == 0:
        data = torch.tensor([1, 2.]).to(f'cuda:{rank}')
    else:
        data = torch.tensor([3, 4.]).to(f'cuda:{rank}')

    dist.all_to_all_single(data, data)

    if rank == 0:
        assert np.allclose(data.cpu().numpy(), np.array([1, 3.]))
    else:
        assert np.allclose(data.cpu().numpy(), np.array([2, 4.]))

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)
