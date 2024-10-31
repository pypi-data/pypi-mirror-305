import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()
    data = torch.zeros(1).to(f'cuda:{rank}')

    ng = dist.new_group([2, 3])

    if rank == 2:
        data += 1
        dist.send(data, 3, ng)
    else:
        dist.recv(data, 2, ng)

    if rank == 3:
        assert data.cpu().numpy() == np.array([1.])
        assert data.shape == (1,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)
