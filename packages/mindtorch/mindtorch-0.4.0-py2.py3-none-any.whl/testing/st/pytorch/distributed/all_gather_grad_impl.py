import sys
import numpy as np

import mindspore as ms

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    # all_gather not support int64 input on Ascend
    tensor_list = [torch.zeros(2, dtype=torch.float32).to(f'cuda:{rank}') for _ in range(2)]
    tensor = torch.arange(2, dtype=torch.float32).to(f'cuda:{rank}') + 1 + 2 * rank

    def _func(x):
        dist.all_gather(tensor_list, x)
        a = torch.stack(tensor_list)
        return a.sum()
    
    grad_fn = ms.value_and_grad(_func)
    value, grad = grad_fn(tensor)

    expected_value = np.array(10).astype(np.float32)
    expected_grad = np.array([2, 2]).astype(np.float32)

    assert np.allclose(value.numpy(), expected_value)
    assert np.allclose(grad.numpy(), expected_grad)
    assert expected_value.shape == expected_value.shape
    assert expected_grad.shape == expected_grad.shape

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)