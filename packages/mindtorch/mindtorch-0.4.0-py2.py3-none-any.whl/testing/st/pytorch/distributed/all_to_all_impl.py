import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    tensor = torch.arange(2, dtype=torch.int64).to(f'cuda:{rank}') + 2 * rank
    tensor = list(tensor.chunk(2))
    output = list(torch.empty(2, dtype=torch.int64).to(f'cuda:{rank}').chunk(2))

    dist.all_to_all(output, tensor)

    if rank == 0:
        assert np.allclose(output[0].cpu().numpy(), np.array([0]))
        assert np.allclose(output[1].cpu().numpy(), np.array([2]))
    else:
        assert np.allclose(output[0].cpu().numpy(), np.array([1]))
        assert np.allclose(output[1].cpu().numpy(), np.array([3]))

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)