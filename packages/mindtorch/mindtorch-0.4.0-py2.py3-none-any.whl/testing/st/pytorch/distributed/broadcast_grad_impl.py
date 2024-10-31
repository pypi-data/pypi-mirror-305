import sys
import numpy as np

import mindspore as ms

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    if rank == 0:
        data = torch.tensor([1, 2.]).to(f'cuda:{rank}')
    else:
        data = torch.zeros(2).to(f'cuda:{rank}')

    def _func(x):
        dist.broadcast(x, 0)
        return x.sum()

    grad_fn = ms.ops.value_and_grad(_func)
    value, grad = grad_fn(data)

    expected_value = np.array(3).astype(np.float32)
    expected_grad = np.array([2, 2]).astype(np.float32)

    assert np.allclose(value.numpy(), expected_value)
    assert np.allclose(grad.numpy(), expected_grad)
    assert value.shape == expected_value.shape
    assert grad.shape == expected_grad.shape

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)