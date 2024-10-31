import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()
    world_size = dist.get_world_size()

    send_tensor = torch.arange(2, dtype=torch.float32) + 2 * rank
    recv_tensor = torch.randn(2, dtype=torch.float32)
    send_op = dist.P2POp(dist.isend, send_tensor, (rank + 1)%world_size)
    recv_op = dist.P2POp(dist.irecv, recv_tensor, (rank - 1 + world_size)%world_size)
    reqs = dist.batch_isend_irecv([send_op, recv_op])
    for req in reqs:
        req.wait()
    if rank == 0:
        assert np.allclose(recv_tensor.numpy(), np.array([2, 3]).astype(np.float32))
    elif rank == 1:
        assert np.allclose(recv_tensor.numpy(), np.array([0, 1]).astype(np.float32))


if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)
