import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    # mindspore reduce_scatter not support int64
    tensor = torch.arange(2, dtype=torch.float32).to(f'cuda:{rank}') + 2 * rank
    tensor = list(tensor.chunk(2))
    output = torch.empty(1, dtype=torch.float32).to(f'cuda:{rank}')

    ng = dist.new_group([0, 1])

    dist.reduce_scatter(output, tensor, group=ng)

    if rank == 0:
        assert np.allclose(output.cpu().numpy(), np.array([2]).astype(np.float32))
        assert output.shape == (1,)
    elif rank == 1:
        assert np.allclose(output.cpu().numpy(), np.array([4]).astype(np.float32))
        assert output.shape == (1,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)