import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    if rank == 2:
        data = torch.tensor([1, 2.]).to(f'cuda:{rank}')
    else:
        data = torch.zeros(2).to(f'cuda:{rank}')

    ng = dist.new_group([0, 2])
    dist.broadcast(data, 2, ng)
    if rank in (0, 2):
        assert np.allclose(data.cpu().numpy(), np.array([1, 2.]))
    else:
        assert np.allclose(data.cpu().numpy(), np.array([0, 0.]))

    assert data.shape == (2,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)