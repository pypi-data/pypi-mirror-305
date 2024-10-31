import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    data = torch.zeros(2).to(torch.float32)

    gather_list = [torch.zeros(2).to(torch.float32), torch.zeros(2).to(torch.float32)]

    if rank == 0:
        dist.gather(data + 1, gather_list, dst=0)
        assert np.allclose(gather_list[0].cpu().numpy(), np.array([1, 1]))
        assert np.allclose(gather_list[1].cpu().numpy(), np.array([2, 2]))
        assert gather_list[0].shape == (2,)
        assert gather_list[1].shape == (2,)
    else:
        dist.gather(data + 2, None, dst=0)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)