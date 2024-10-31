import sys
import numpy as np

import mindspore as ms

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

    def mat(x, y):
        result = torch.matmul(x, y)
        dist.all_reduce(result)
        return result.sum()

    grad_fn = ms.value_and_grad(mat, (0, 1))
    value, grad = grad_fn(w_device, x_device)

    expected_result = np.array(72.)
    assert np.allclose(value.cpu().numpy(), expected_result)

    grad_w = grad[0]
    grad_x = grad[1]

    if rank == 0:
        expected_w_grad = np.array([[4, 4.], [4, 4]])
        expected_x_grad = np.array([12, 16.])
    else:
        expected_w_grad = np.array([[4, 4.], [4, 4]])
        expected_x_grad = np.array([20, 24.])

    assert np.allclose(grad_w.numpy(), expected_w_grad)
    assert np.allclose(grad_x.numpy(), expected_x_grad)
    assert grad_w.shape == expected_w_grad.shape
    assert grad_x.shape == expected_x_grad.shape


if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)