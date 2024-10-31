import numpy as np
import torch

import mindtorch.torch as ms_torch
from mindtorch.torch.nn import AdaptiveLogSoftmaxWithLoss
from mindtorch.torch.nn import Parameter

from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason="Unsupport Graph mode now.")
def test_adaptive_logsoftmax_withloss():
    n = 50
    in_fea = 200
    n_class = 100
    cutoffs = [10, 30, 60]
    seed = 1000
    np.random.seed(seed)
    data = np.random.rand(n, in_fea).astype(np.float32)*10
    target = np.random.rand(n)*n_class
    target = target.astype(np.int32)

    headweight = np.random.rand(13, 200)
    weight00 = np.random.rand(50, 200)
    weight01 = np.random.rand(20, 50)
    weight10 = np.random.rand(12, 200)
    weight11 = np.random.rand(30, 12)
    weight20 = np.random.rand(3, 200)
    weight21 = np.random.rand(40, 3)

    torch_net = torch.nn.AdaptiveLogSoftmaxWithLoss(in_fea, n_class, cutoffs)
    ms_net = AdaptiveLogSoftmaxWithLoss(in_fea, n_class, cutoffs)
    torch_net.head.weight = torch.nn.Parameter(torch.tensor(headweight, dtype=torch.float32))
    torch_net.tail[0][0].weight = torch.nn.Parameter(torch.tensor(weight00, dtype=torch.float32))
    torch_net.tail[0][1].weight = torch.nn.Parameter(torch.tensor(weight01, dtype=torch.float32))
    torch_net.tail[1][0].weight = torch.nn.Parameter(torch.tensor(weight10, dtype=torch.float32))
    torch_net.tail[1][1].weight = torch.nn.Parameter(torch.tensor(weight11, dtype=torch.float32))
    torch_net.tail[2][0].weight = torch.nn.Parameter(torch.tensor(weight20, dtype=torch.float32))
    torch_net.tail[2][1].weight = torch.nn.Parameter(torch.tensor(weight21, dtype=torch.float32))
    ms_net.head.weight = Parameter(ms_torch.tensor(headweight, dtype=torch.float32))
    ms_net.tail[0][0].weight = Parameter(ms_torch.tensor(weight00, dtype=torch.float32))
    ms_net.tail[0][1].weight = Parameter(ms_torch.tensor(weight01, dtype=torch.float32))
    ms_net.tail[1][0].weight = Parameter(ms_torch.tensor(weight10, dtype=torch.float32))
    ms_net.tail[1][1].weight = Parameter(ms_torch.tensor(weight11, dtype=torch.float32))
    ms_net.tail[2][0].weight = Parameter(ms_torch.tensor(weight20, dtype=torch.float32))
    ms_net.tail[2][1].weight = Parameter(ms_torch.tensor(weight21, dtype=torch.float32))

    torch_input = torch.tensor(data)
    torch_target = torch.tensor(target).long()
    ms_input = ms_torch.tensor(data)
    ms_target = ms_torch.tensor(target).long()

    torch_out, torch_loss = torch_net(torch_input, torch_target)
    ms_out, ms_loss = ms_net(ms_input, ms_target)

    # Implemented by concatenation of small operators, there is some error accumulation.
    param_compare(torch_out.detach(), ms_out, atol=1e-3)
    param_compare(torch_loss.detach(), ms_loss, atol=1e-3)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_adaptive_logsoftmax_withloss()
