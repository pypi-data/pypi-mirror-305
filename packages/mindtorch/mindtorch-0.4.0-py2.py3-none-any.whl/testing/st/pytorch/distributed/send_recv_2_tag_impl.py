import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()
    data1 = torch.zeros(1).to(f'cuda:{rank}')
    data2 = torch.ones(1).to(f'cuda:{rank}')

    if rank == 0:
        data1 += 1
        data2 += 1
        dist.send(data1, 1, tag=1)
        dist.send(data2, 1, tag=2)
    else:
        dist.recv(data1, 0, tag=1)
        dist.recv(data2, 0, tag=2)

    if rank == 1:
        assert data1.cpu().numpy() == np.array([1.])
        assert data2.cpu().numpy() == np.array([2.])
        assert data1.shape == (1,)
        assert data2.shape == (1,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)
