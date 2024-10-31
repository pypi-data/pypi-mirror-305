import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    ng = dist.new_group([0, 1])

    # all_gather not support int64 input on Ascend
    tensor_list = [torch.zeros(2, dtype=torch.float32).to(f'cuda:{rank}') for _ in range(2)]
    tensor = torch.arange(2, dtype=torch.float32).to(f'cuda:{rank}') + 1 + 2 * rank
    dist.all_gather(tensor_list, tensor, ng)

    if rank in (0, 1):
        assert np.allclose(tensor_list[0].cpu().numpy(), np.array([1, 2.]).astype(np.float32))
        assert np.allclose(tensor_list[1].cpu().numpy(), np.array([3, 4.]).astype(np.float32))
        assert tensor_list[0].shape == (2,)
        assert tensor_list[1].shape == (2,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)