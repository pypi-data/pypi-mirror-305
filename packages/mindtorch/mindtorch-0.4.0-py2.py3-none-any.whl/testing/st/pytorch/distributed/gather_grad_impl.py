import sys
import numpy as np

import mindspore as ms

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    data = torch.zeros(2).to(torch.float32)

    gather_list = [torch.zeros(2).to(torch.float32), torch.zeros(2).to(torch.float32)]

    if rank == 0:
        def _func(x):
            dist.gather(x + 1, gather_list, dst=0)
            return (gather_list[0] + gather_list[1]).sum()
    elif rank == 1:
        def _func(x):
            dist.gather(x + 1, None, dst=0)
            return x.sum()
    
    grad_fn = ms.ops.value_and_grad(_func)
    value, grad = grad_fn(data)

    if rank == 0:
        assert np.allclose(value.numpy(), np.array([3, 3.]))
        assert np.allclose(grad.numpy(), np.array([1, 1.]))
        assert value.shape == (2,)
        assert grad.shape == (2,)
    elif rank == 1:
        assert np.allclose(grad.numpy(), np.array([2, 2.]))
        assert grad.shape == (2,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)