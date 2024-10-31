import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    data = torch.zeros(2).to(torch.float32)

    scatter_list = [data + 1, data + 2]

    output = torch.zeros(2).to(torch.float32)

    if rank == 0:
        dist.scatter(output, scatter_list, src=0)
        assert np.allclose(output.cpu().numpy(), np.array([1, 1]))
        assert output.shape == (2,)
    else:
        dist.scatter(output, None, src=0)
        assert np.allclose(output.cpu().numpy(), np.array([2, 2]))
        assert output.shape == (2,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)