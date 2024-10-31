import sys
import numpy as np

import mindspore as ms

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()
    data = torch.zeros(1).to(f'cuda:{rank}')

    if rank == 0:
        data += 1
        def _func(data):
            out = dist.send(data, 1)
            return out
    else:
        def _func(data):
            dist.recv(data, 0)
            return data.sum()

    grad_fn = ms.ops.value_and_grad(_func)
    value, grad = grad_fn(data)

    if rank == 0:
        assert np.allclose(grad.numpy(), np.array([1.]))
        assert grad.shape == (1,)
    if rank == 1:
        assert np.allclose(value.numpy(), np.array(1.))
        assert value.shape == ()

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)
