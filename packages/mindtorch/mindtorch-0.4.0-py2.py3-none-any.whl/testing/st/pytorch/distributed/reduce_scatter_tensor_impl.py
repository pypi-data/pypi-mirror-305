import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    # mindspore reduce_scatter not support int64
    tensor = torch.arange(2, dtype=torch.float32).to(f'cuda:{rank}') + 2 * rank
    output = torch.empty(1, dtype=torch.float32).to(f'cuda:{rank}')

    dist.reduce_scatter_tensor(output, tensor)

    if rank == 0:
        assert np.allclose(output.cpu().numpy(), np.array([2]).astype(np.float32))
        assert output.shape == (1,)
    else:
        assert np.allclose(output.cpu().numpy(), np.array([4]).astype(np.float32))
        assert output.shape == (1,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)