import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    _total_device = 4

    dist.init_process_group(backend, world_size=_total_device)

    rank = dist.get_rank()

    w = torch.tensor([[1, 2., 3, 4.,4, 3, 2, 1], [5, 6, 7, 8, 8, 7, 6, 5]])
    x = torch.tensor([2., 2, 2, 2, 2, 2, 2, 2])

    w_device = w[:, w.size(1) // _total_device * rank : w.size(1) // _total_device * (rank + 1)].to(rank)
    x_device = x[x.size(0) // _total_device * rank : x.size(0) // _total_device * (rank + 1)].to(rank)

    result = torch.matmul(w_device, x_device)

    new_gp = dist.new_group([0, 1])

    if new_gp is not None:
        dist.all_reduce(result, group=new_gp)

    if rank in (0, 1):
        assert np.allclose(result.cpu().numpy(), np.array([20, 52.]))
    elif rank == 2:
        assert np.allclose(result.cpu().numpy(), np.array([14., 30.]))
    elif rank == 3:
        assert np.allclose(result.cpu().numpy(), np.array([6., 22.]))

    assert result.shape == (2,)

    dist.all_reduce(result)

    expected_result = np.array([60, 156.])
    assert np.allclose(result.cpu().numpy(), expected_result)
    assert result.shape == (2,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)
