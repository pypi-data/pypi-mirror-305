import numpy as np

import mindspore as ms
from mindspore import nn

import mindtorch.torch as torch
from mindtorch.torch.nn.parallel import DistributedDataParallel as DDP
from mindtorch.torch import distributed as dist


class NetWork(torch.nn.Module):
    def __init__(self):
        super(NetWork, self).__init__()
        self.dense = torch.nn.Linear(3, 3)

    def forward(self, x):
        return self.dense(x).sum()


def ddp_basic():
    # you can use the following bash command to see the print log
    # mpirun --allow-run-as-root -n 3 python ddp_impl.py
    dist.init_process_group(backend='nccl', rank=-1, world_size=3)

    network = NetWork()
    opt = torch.optim.Adam(network.parameters())
    grad_fn = ms.value_and_grad(network, None, opt.parameters, has_aux=False)

    rank = dist.get_rank()
    network = DDP(network, device_ids=[rank], find_unused_parameters=False)
    ranks = [0, 2]
    if rank in ranks:
        pg = dist.new_group(ranks)
        network_p = DDP(network, device_ids=[rank], process_group=pg)
    else:
        network_p = None

    inputs = torch.tensor(np.random.random((2, 3)).astype(np.float32))
    for _ in range(1):
        loss, grads = grad_fn(inputs)
        grads = network.all_reduce(grads)
        opt(grads)
        if network_p is not None:
            grads = network_p.all_reduce(grads)
            opt(grads)
        print('rank:', rank, ', loss:', loss)


if __name__ == '__main__':
    ddp_basic()
