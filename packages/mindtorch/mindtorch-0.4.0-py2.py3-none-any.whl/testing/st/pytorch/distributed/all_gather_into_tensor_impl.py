import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    world_size = 2
    dist.init_process_group(backend)

    rank = dist.get_rank()

    # all_gather not support int64 input on Ascend
    tensor_in = torch.arange(2, dtype=torch.float32).to(f'cuda:{rank}') + 1 + 2 * rank
    tensor_out = torch.zeros(world_size * 2, dtype=torch.float32).to(f'cuda:{rank}')
    dist.all_gather_into_tensor(tensor_out, tensor_in)

    tensor_out_stack = torch.zeros(world_size, 2, dtype=torch.float32).to(f'cuda:{rank}')
    dist.all_gather_into_tensor(tensor_out_stack, tensor_in)

    assert np.allclose(tensor_out.cpu().numpy(), np.array([1, 2, 3, 4]).astype(np.float32))
    assert np.allclose(tensor_out_stack.cpu().numpy(), np.array([[1, 2],
                                                                 [3, 4]]).astype(np.float32))
    assert tensor_out.shape == (4,)
    assert tensor_out_stack.shape == (2, 2)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)