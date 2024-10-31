import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    _total_device = 2

    dist.init_process_group(backend, world_size=_total_device)

    rank = dist.get_rank()

    w = torch.tensor([[1, 2., 3, 4.], [5, 6, 7, 8]])
    x = torch.tensor([2., 2, 2, 2])

    w_device = w[:, w.size(1) // _total_device * rank : w.size(1) // _total_device * (rank + 1)].to(rank)
    x_device = x[x.size(0) // _total_device * rank : x.size(0) // _total_device * (rank + 1)].to(rank)

    result = torch.matmul(w_device, x_device)

    dist.all_reduce(result)

    expected_result = np.array([20, 52.])
    assert np.allclose(result.cpu().numpy(), expected_result)
    assert result.shape == expected_result.shape

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)
