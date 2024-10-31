import math
import os
import mindtorch.torch as ms_torch
import mindspore as ms
import numpy as np
import torch
from mindtorch.torch.optim.lr_scheduler import _LRScheduler

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, param_compare, \
                    SKIP_ENV_PYNATIVE_MODE
set_mode_by_env_config()

def _number_compare(a1, b1, rtol=1e-5, atol=1e-8):
    assert math.isclose(a1, b1, rel_tol=rtol, abs_tol=atol)

def number_compare(a1, b1, rtol=1e-5, atol=1e-8, equal_nan=False):
    if isinstance(a1, (tuple, list)) or isinstance(b1, (tuple, list)):
        assert len(a1) == len(b1)
        for i in range(len(a1)):
            if isinstance(a1[i], ms.Tensor):
                _ms_i = a1[i].item()
            else:
                _ms_i = a1[i]
            _number_compare(_ms_i, b1[i], rtol=rtol, atol=atol)
    else:
        if isinstance(a1, ms.Tensor):
            _ms_i = a1.item()
        else:
            _ms_i = a1
        _number_compare(_ms_i, b1, rtol=rtol, atol=atol)

class SchedulerTest:
    def __init__(self, ms_optim, ms_lrsch, torch_optim, torch_lrsch):
        self.ms_optim = ms_optim
        self.ms_lrsch = ms_lrsch
        self.torch_optim = torch_optim
        self.torch_lrsch = torch_lrsch
        self.max_iter = 6

    def test(self, ms_a, ms_grads, pt_a, pt_grads, ms_step_args=(), pt_step_args=()):
        ms_lr_result = []
        ms_param_result = []
        pt_lr_result = []
        pt_param_result = []

        pt_a.grad = pt_grads[0]

        for i in range(self.max_iter):
            if i != 0:
                self.ms_optim.step(ms_grads)
                self.ms_lrsch.step(*ms_step_args)
                self.torch_optim.step()
                self.torch_lrsch.step(*pt_step_args)
                ms_param_result.append(ms_a.item())
                pt_param_result.append(pt_a.item())
            if hasattr(self.torch_lrsch, 'get_last_lr'):
                ms_lr_result.extend(self.ms_lrsch.get_last_lr())
                pt_lr_result.extend(self.torch_lrsch.get_last_lr())

        if hasattr(self.torch_lrsch, 'get_last_lr'):
            number_compare(ms_lr_result, pt_lr_result)

        number_compare(ms_param_result, pt_param_result, atol=1e-4)


def test_StepLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.StepLR(ms_optimizer, step_size=1, gamma=0.2)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.StepLR(pt_optimizer, step_size=1, gamma=0.2)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)


class ms_FindLR(_LRScheduler):
    """exponentially increasing learning rate    Args:
        optimizer: optimzier(e.g. SGD)
        num_iter: totoal_iters
        max_lr: maximum  learning rate
    """
    def __init__(self, optimizer, max_lr=10, num_iter=100, last_epoch=-1):
        self.total_iters = num_iter
        self.max_lr = max_lr
        super().__init__(optimizer, last_epoch)

    def get_lr(self):
        return [base_lr * (self.max_lr / base_lr) ** (self.last_epoch / (self.total_iters + 1e-32)) for base_lr in self.base_lrs]

class pt_FindLR(torch.optim.lr_scheduler._LRScheduler):
    """exponentially increasing learning rate    Args:
        optimizer: optimzier(e.g. SGD)
        num_iter: totoal_iters
        max_lr: maximum  learning rate
    """
    def __init__(self, optimizer, max_lr=10, num_iter=100, last_epoch=-1):
        self.total_iters = num_iter
        self.max_lr = max_lr
        super().__init__(optimizer, last_epoch)

    def get_lr(self):
        return [base_lr * (self.max_lr / base_lr) ** (self.last_epoch / (self.total_iters + 1e-32)) for base_lr in self.base_lrs]

def test_user_lr_scheduler():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_FindLR(ms_optimizer, max_lr=5, num_iter=1000)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = pt_FindLR(pt_optimizer, max_lr=5, num_iter=1000)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)


def test_MultiStepLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.MultiStepLR(ms_optimizer, milestones=[0,2], gamma=0.2)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.MultiStepLR(pt_optimizer, milestones=[0,2], gamma=0.2)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

def test_LambdaLR():
    lambda1 = lambda epoch: epoch // 30
    lambda2 = lambda epoch: 0.95 ** epoch
    grads = (ms.Tensor([1.]), ms.Tensor([2.]))
    a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    b = ms_torch.nn.Parameter(ms_torch.tensor([2.]).to(ms_torch.float32))
    optimizer = ms_torch.optim.SGD([{'params': a}, {'params': b}], lr=0.01, momentum=0.9, weight_decay=5e-4)
    lr_scheduler = ms_torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=[lambda1, lambda2]) #learning rate decay
    # round 1
    ms_lr1 = lr_scheduler.get_last_lr()
    # round 2
    optimizer.step(grads)
    lr_scheduler.step()
    ms_lr2 = lr_scheduler.get_last_lr()
    ms_param_1 = [a.item(), b.item()]
    # round 3
    optimizer.step(grads)
    lr_scheduler.step()
    ms_lr3 = lr_scheduler.get_last_lr()
    ms_param_2 = [a.item(), b.item()]
    # round 4
    optimizer.step(grads)
    lr_scheduler.step()
    ms_lr4 = lr_scheduler.get_last_lr()
    ms_param_3 = [a.item(), b.item()]

    grads = (torch.tensor([1.]).to(torch.float32), torch.tensor([2.]).to(torch.float32),)
    a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    b = torch.nn.Parameter(torch.tensor([2.]).to(torch.float32))
    optimizer = torch.optim.SGD([{'params': a}, {'params': b}], lr=0.01, momentum=0.9, weight_decay=5e-4)
    lr_scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=[lambda1, lambda2]) #learning rate decay
    a.grad = grads[0]
    b.grad = grads[1]
    pt_lr1 = lr_scheduler.get_last_lr()
    # round 2
    optimizer.step()
    lr_scheduler.step()
    pt_lr2 = lr_scheduler.get_last_lr()
    pt_param_1 = [a.item(), b.item()]
    # round 3
    optimizer.step()
    lr_scheduler.step()
    pt_lr3 = lr_scheduler.get_last_lr()
    pt_param_2 = [a.item(), b.item()]
    # round 4
    optimizer.step()
    lr_scheduler.step()
    pt_lr4 = lr_scheduler.get_last_lr()
    pt_param_3 = [a.item(), b.item()]

    number_compare(ms_lr1, pt_lr1)
    number_compare(ms_lr2, pt_lr2)
    number_compare(ms_lr3, pt_lr3)
    number_compare(ms_lr4, pt_lr4)

    number_compare(ms_param_1, pt_param_1)
    number_compare(ms_param_2, pt_param_2)
    number_compare(ms_param_3, pt_param_3)

def test_MultiplicativeLR():
    lmbda = lambda epoch: 0.95

    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.MultiplicativeLR(ms_optimizer, lr_lambda=lmbda)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.MultiplicativeLR(pt_optimizer, lr_lambda=lmbda)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)


def test_ConstantLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.ConstantLR(ms_optimizer, total_iters=3)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.ConstantLR(pt_optimizer, total_iters=3)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

def test_LinearLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.LinearLR(ms_optimizer, 1.0 / 5, 0.7, 10)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.LinearLR(pt_optimizer, 1.0 / 5, 0.7, 10)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

def test_ExponentialLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.ExponentialLR(ms_optimizer, 0.6)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.ExponentialLR(pt_optimizer, 0.6)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

def test_SequentialLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)

    ms_scheduler1 = ms_torch.optim.lr_scheduler.ConstantLR(ms_optimizer, factor=0.1, total_iters=2)
    ms_scheduler2 = ms_torch.optim.lr_scheduler.ExponentialLR(ms_optimizer, gamma=0.9)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.SequentialLR(ms_optimizer,
                                                               [ms_scheduler1, ms_scheduler2],
                                                               milestones=[2])

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_scheduler1 = torch.optim.lr_scheduler.ConstantLR(pt_optimizer, factor=0.1, total_iters=2)
    pt_scheduler2 = torch.optim.lr_scheduler.ExponentialLR(pt_optimizer, gamma=0.9)
    pt_lr_scheduler = torch.optim.lr_scheduler.SequentialLR(pt_optimizer,
                                                            [pt_scheduler1, pt_scheduler2],
                                                            milestones=[2])

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

@SKIP_ENV_GRAPH_MODE(reason="torch 1.12 not support PolynomialLR yet.")
@SKIP_ENV_PYNATIVE_MODE(reason="torch 1.12 not support PolynomialLR yet.")
def test_PolynomialLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.PolynomialLR(ms_optimizer, total_iters=4, power=1.0)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.PolynomialLR(pt_optimizer, total_iters=4, power=1.0)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)


def test_CosineAnnealingLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.CosineAnnealingLR(ms_optimizer, 3, 0.1)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(pt_optimizer, 3, 0.1)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)


def test_state_dict():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    # different of `T_max` and `eta_min` from pt_lr_scheduler
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.CosineAnnealingLR(ms_optimizer, 2, 0.5)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(pt_optimizer, 3, 0.1)

    s = pt_lr_scheduler.state_dict()
    torch.save(s, 'a.pth')
    s_ = ms_torch.load('a.pth')
    ms_lr_scheduler.load_state_dict(s_)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)


def test_load_from_ms():
    lmbda = lambda epoch: 0.95

    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.MultiplicativeLR(ms_optimizer, lr_lambda=lmbda)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.MultiplicativeLR(pt_optimizer, lr_lambda=lmbda)

    s = ms_lr_scheduler.state_dict()
    ms_torch.save(s, 'a.pth')
    s_ = ms_torch.load('a.pth')
    ms_lr_scheduler.load_state_dict(s_)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)
    os.remove('a.pth')

def test_load_from_ms_wrong():
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.StepLR(ms_optimizer, 2)

    s = {'base_lrs':[]}
    try:
        ms_lr_scheduler.load_state_dict(s)
    except Exception as e:
        assert "len of state_dict['base_lrs'] is not the same" in str(e)

    s = {'_last_lr':[]}
    try:
        ms_lr_scheduler.load_state_dict(s)
    except Exception as e:
        assert "len of state_dict['_last_lr'] is not the same" in str(e)

def test_jit():
    # ms.set_context(save_graphs=True, save_graphs_path='./ir')
    class ms_Net(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.w = ms_torch.nn.Parameter(ms_torch.tensor([3.]))

        def forward(self, x):
            return x * self.w

    ms_net = ms_Net()
    ms_optimizer = ms_torch.optim.SGD(ms_net.parameters(), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_scheduler = ms_torch.optim.lr_scheduler.StepLR(ms_optimizer, 2)
    grad_fn = ms.ops.value_and_grad(ms_net, None, ms_optimizer.parameters)

    @ms.jit
    def ms_fun(x):
        loss, grads = grad_fn(x)
        grads = ms.ops.depend(grads, loss)  # loss to be compute before grads, so the loss can be right
        ms_optimizer.step(grads)
        ms_scheduler.step()
        return loss

    class pt_Net(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.w = torch.nn.Parameter(torch.tensor([3.]))

        def forward(self, x):
            return x * self.w

    pt_net = pt_Net()
    pt_optimizer = torch.optim.SGD(pt_net.parameters(), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_scheduler = torch.optim.lr_scheduler.StepLR(pt_optimizer, 2)

    def pt_fun(x):
        loss = pt_net(x)
        pt_optimizer.zero_grad()
        loss.backward()
        pt_optimizer.step()
        pt_scheduler.step()
        return loss

    ms_x = ms_torch.tensor([2.])
    pt_x = torch.tensor([2.])
    for i in range(5):
        pt_loss = pt_fun(pt_x)
        ms_loss = ms_fun(ms_x)
        number_compare(ms_loss, pt_loss, atol=1e-4)
        number_compare(ms_scheduler.get_last_lr(), pt_scheduler.get_last_lr())
        param_compare(ms_net.w.detach(), pt_net.w.detach())

@SKIP_ENV_GRAPH_MODE(reason="ChainedScheduler not support on MindSpore r2.3.")
@SKIP_ENV_PYNATIVE_MODE(reason="ChainedScheduler not support on MindSpore r2.3.")
def test_ChainedScheduler():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)

    ms_scheduler1 = ms_torch.optim.lr_scheduler.ConstantLR(ms_optimizer, factor=0.1, total_iters=2)
    ms_scheduler2 = ms_torch.optim.lr_scheduler.ExponentialLR(ms_optimizer, gamma=0.9)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.ChainedScheduler([ms_scheduler1, ms_scheduler2])

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_scheduler1 = torch.optim.lr_scheduler.ConstantLR(pt_optimizer, factor=0.1, total_iters=2)
    pt_scheduler2 = torch.optim.lr_scheduler.ExponentialLR(pt_optimizer, gamma=0.9)
    pt_lr_scheduler = torch.optim.lr_scheduler.ChainedScheduler([pt_scheduler1, pt_scheduler2])

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

def test_ReduceLROnPlateau():
    ms.set_context(pynative_synchronize=True)
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.ReduceLROnPlateau(ms_optimizer, 'min')
    ms_metric = ms_torch.tensor(2.)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(pt_optimizer, 'min')
    pt_metric = torch.tensor(2.)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads, (ms_metric,), (pt_metric,))

def test_CyclicLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.CyclicLR(ms_optimizer, base_lr=0.01, max_lr=0.1, cycle_momentum=False)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.CyclicLR(pt_optimizer, base_lr=0.01, max_lr=0.1, cycle_momentum=False)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

def test_CosineAnnealingWarmRestarts():
    T_0 = 1
    T_mult = 3
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(ms_optimizer, T_0, T_mult)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(pt_optimizer, T_0, T_mult)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

@SKIP_ENV_GRAPH_MODE(reason="OneCycleLR not support graph mode now.")
def test_OneCycleLR():
    ms_grads = (ms.Tensor([1.]),)
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.OneCycleLR(ms_optimizer, max_lr=0.01, total_steps=5)

    pt_grads = (torch.tensor([1.]).to(torch.float32),)
    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.OneCycleLR(pt_optimizer, max_lr=0.01, total_steps=5)

    test_op = SchedulerTest(ms_optimizer, ms_lr_scheduler, pt_optimizer, pt_lr_scheduler)
    test_op.test(ms_a, ms_grads, pt_a, pt_grads)

def test_LambdaLR_state_dict():
    lambda1 = lambda epoch: epoch // 30
    lambda2 = lambda epoch: 0.95 ** epoch
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_b = ms_torch.nn.Parameter(ms_torch.tensor([2.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD([{'params': ms_a}, {'params': ms_b}], lr=0.01, momentum=0.9, weight_decay=5e-4)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.LambdaLR(ms_optimizer, lr_lambda=[lambda1, lambda2])

    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_b = torch.nn.Parameter(torch.tensor([2.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD([{'params': pt_a}, {'params': pt_b}], lr=0.01, momentum=0.9, weight_decay=5e-4)
    pt_lr_scheduler = torch.optim.lr_scheduler.LambdaLR(pt_optimizer, lr_lambda=[lambda1, lambda2])

    s = pt_lr_scheduler.state_dict()
    ms_lr_scheduler.load_state_dict(s)
    ms_lr_scheduler.load_state_dict(ms_lr_scheduler.state_dict())

def test_MultiplicativeLR_state_dict():
    lmbda = lambda epoch: 0.95

    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.MultiplicativeLR(ms_optimizer, lr_lambda=lmbda)

    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.MultiplicativeLR(pt_optimizer, lr_lambda=lmbda)

    s = pt_lr_scheduler.state_dict()
    ms_lr_scheduler.load_state_dict(s)
    ms_lr_scheduler.load_state_dict(ms_lr_scheduler.state_dict())

def test_SequentialLR_state_dict():
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)

    ms_scheduler1 = ms_torch.optim.lr_scheduler.ConstantLR(ms_optimizer, factor=0.1, total_iters=2)
    ms_scheduler2 = ms_torch.optim.lr_scheduler.ExponentialLR(ms_optimizer, gamma=0.9)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.SequentialLR(ms_optimizer,
                                                               [ms_scheduler1, ms_scheduler2],
                                                               milestones=[2])

    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_scheduler1 = torch.optim.lr_scheduler.ConstantLR(pt_optimizer, factor=0.1, total_iters=2)
    pt_scheduler2 = torch.optim.lr_scheduler.ExponentialLR(pt_optimizer, gamma=0.9)
    pt_lr_scheduler = torch.optim.lr_scheduler.SequentialLR(pt_optimizer,
                                                            [pt_scheduler1, pt_scheduler2],
                                                            milestones=[2])

    s = pt_lr_scheduler.state_dict()
    ms_lr_scheduler.load_state_dict(s)
    ms_lr_scheduler.load_state_dict(ms_lr_scheduler.state_dict())

@SKIP_ENV_GRAPH_MODE(reason="ChainedScheduler not support on MindSpore r2.3.")
@SKIP_ENV_PYNATIVE_MODE(reason="ChainedScheduler not support on MindSpore r2.3.")
def test_ChainedScheduler_state_dict():
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)

    ms_scheduler1 = ms_torch.optim.lr_scheduler.ConstantLR(ms_optimizer, factor=0.1, total_iters=2)
    ms_scheduler2 = ms_torch.optim.lr_scheduler.ExponentialLR(ms_optimizer, gamma=0.9)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.ChainedScheduler([ms_scheduler1, ms_scheduler2])

    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_scheduler1 = torch.optim.lr_scheduler.ConstantLR(pt_optimizer, factor=0.1, total_iters=2)
    pt_scheduler2 = torch.optim.lr_scheduler.ExponentialLR(pt_optimizer, gamma=0.9)
    pt_lr_scheduler = torch.optim.lr_scheduler.ChainedScheduler([pt_scheduler1, pt_scheduler2])

    s = pt_lr_scheduler.state_dict()
    ms_lr_scheduler.load_state_dict(s)
    ms_lr_scheduler.load_state_dict(ms_lr_scheduler.state_dict())

def test_ReduceLROnPlateau_state_dict():
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.ReduceLROnPlateau(ms_optimizer, 'min')

    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(pt_optimizer, 'min')

    s = pt_lr_scheduler.state_dict()
    ms_lr_scheduler.load_state_dict(s)
    ms_lr_scheduler.load_state_dict(ms_lr_scheduler.state_dict())

def test_CyclicLR_state_dict():
    ms_a = ms_torch.nn.Parameter(ms_torch.tensor([1.]).to(ms_torch.float32))
    ms_optimizer = ms_torch.optim.SGD((ms_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    ms_lr_scheduler = ms_torch.optim.lr_scheduler.CyclicLR(ms_optimizer, base_lr=0.01, max_lr=0.1, cycle_momentum=False)

    pt_a = torch.nn.Parameter(torch.tensor([1.]).to(torch.float32))
    pt_optimizer = torch.optim.SGD((pt_a,), lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=False)
    pt_lr_scheduler = torch.optim.lr_scheduler.CyclicLR(pt_optimizer, base_lr=0.01, max_lr=0.1, cycle_momentum=False)

    s = pt_lr_scheduler.state_dict()
    ms_lr_scheduler.load_state_dict(s)
    ms_lr_scheduler.load_state_dict(ms_lr_scheduler.state_dict())


if __name__ == '__main__':
    test_StepLR()
    test_user_lr_scheduler()
    test_MultiStepLR()
    test_LambdaLR()
    test_MultiplicativeLR()
    test_ConstantLR()
    test_LinearLR()
    test_ExponentialLR()
    test_CosineAnnealingLR()
    test_state_dict()
    test_load_from_ms()
    test_jit()
    test_ChainedScheduler()
    test_ReduceLROnPlateau()
    test_CyclicLR()
    test_CosineAnnealingWarmRestarts()
    test_OneCycleLR()
    test_SequentialLR()
    test_PolynomialLR()
    test_CyclicLR_state_dict()
    test_LambdaLR_state_dict()
    test_SequentialLR_state_dict()
    test_ChainedScheduler_state_dict()
    test_MultiplicativeLR_state_dict()
    test_ReduceLROnPlateau_state_dict()