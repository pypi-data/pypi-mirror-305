import sys
import numpy as np

import mindspore as ms

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    # mindspore reduce_scatter not support int64
    tensor = torch.arange(2, dtype=torch.float32).to(f'cuda:{rank}') + 2 * rank
    tensor = list(tensor.chunk(2))
    output = torch.empty(1, dtype=torch.float32).to(f'cuda:{rank}')

    def _func(x, y):
        dist.reduce_scatter(output, [x, y])
        return output.sum() * (rank + 1)

    grad_fn = ms.ops.value_and_grad(_func, (0, 1))
    value, grad = grad_fn(tensor[0], tensor[1])
    if rank == 0:
        assert value.numpy() == np.array(2).astype(np.float32)
        assert grad[0].numpy() == np.array([1]).astype(np.float32)
        assert grad[1].numpy() == np.array([2]).astype(np.float32)
        assert value.shape == ()
        assert grad[0].shape == (1,)
        assert grad[1].shape == (1,)
    if rank == 1:
        assert value.numpy() == np.array(8).astype(np.float32)
        assert grad[0].numpy() == np.array([1]).astype(np.float32)
        assert grad[1].numpy() == np.array([2]).astype(np.float32)
        assert value.shape == ()
        assert grad[0].shape == (1,)
        assert grad[1].shape == (1,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)