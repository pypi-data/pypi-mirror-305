import os
import mindtorch.torch as ms_torch
import mindspore as ms
import numpy as np
import torch

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE, enable_backward
set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason='inplace op in step() not support graph mode')
def test_optimizer_custom():
    class Ranger(ms_torch.optim.Optimizer):
        def __init__(self, params, lr=1e-3, alpha=0.5, k=6):
            defaults = dict(lr=lr, alpha=alpha)
            super().__init__(params, defaults)
            self.k = k
        def __setstate__(self, state):
            print("set state called")
            super().__setstate__(state)
        def step(self, grads, closure=None):
            loss = None
            i = 0
            for group in self.param_groups:
                for p in group['params']:
                    i = i + 1
                    grad = grads[i]
                    p_data_fp32 = p.data.float()
                    state = self.state[p]
                    if len(state) == 0:
                        state['step'] = 0
                        state['exp_avg'] = ms_torch.tensor(0.9)
                    else:
                        state['exp_avg'] = state['exp_avg'].type_as(p_data_fp32)
                    exp_avg = state['exp_avg']
                    state['step'] += 1
                    p_data_fp32.add_(exp_avg * grad)
                    p.data.copy_(p_data_fp32)
            return loss

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    grads = ms_torch.tensor([3, 4.])
    optim_cus = Ranger([weight])
    for group in optim_cus.param_groups:
        group['lr'] = 0.2
    optim_cus.step(grads)
    assert optim_cus.state[optim_cus.param_groups[0]['params'][0]]['step'] == 1
    assert optim_cus.param_groups[0]['lr'] == 0.2
    for group in optim_cus.param_groups:
        group['lr'] = 0.3
    optim_cus.step(grads)
    assert optim_cus.state[optim_cus.param_groups[0]['params'][0]]['step'] == 2
    assert optim_cus.param_groups[0]['lr'] == 0.3

    s = optim_cus.state_dict()
    optim_cus.load_state_dict(s)

def test_sgd():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.SGD([weight], lr=0.01)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.SGD([weight], lr=0.01)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

@SKIP_ENV_GRAPH_MODE("optimizer.step without grad do not support graph mode.")
def test_sgd_step_no_grads():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.SGD([weight], lr=0.01)

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    weight.grad = ms_torch.tensor([3, 4.])
    opt.step()
    opt.zero_grad()
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = ms_torch.tensor([3, 4.])
    opt.step()
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.SGD([weight], lr=0.01)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    opt.zero_grad()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

@SKIP_ENV_GRAPH_MODE(reason='retain_graph of backward not support yet.')
@SKIP_ENV_PYNATIVE_MODE(reason='retain_graph of backward not support yet.')
def test_sgd_autograd_retain_graph():
    with enable_backward():
        weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
        opt = ms_torch.optim.SGD([weight], lr=0.01)
        def ms_torch_func(x):
            return (x * 2).sum()

        # step 1
        for group in opt.param_groups:
            group['lr'] = 0.2
        opt.zero_grad()
        loss = ms_torch_func(weight)
        loss.backward(retain_graph=True)
        loss.backward()
        opt.step()
        ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
        # step 2
        for group in opt.param_groups:
            group['lr'] = 0.5
        opt.zero_grad()
        loss = ms_torch_func(weight)
        loss.backward(retain_graph=True)
        loss.backward()
        opt.step()
        ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

        weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
        opt = torch.optim.SGD([weight], lr=0.01)
        def torch_func(x):
            return (x * 2).sum()

        for group in opt.param_groups:
            group['lr'] = 0.2
        # step 1
        opt.zero_grad()
        loss = torch_func(weight)
        loss.backward(retain_graph=True)
        loss.backward()
        opt.step()
        torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
        assert np.allclose(ms_result1, torch_result1)

        # step 2
        for group in opt.param_groups:
            group['lr'] = 0.5
        weight.grad = torch.tensor([3, 4.])
        opt.zero_grad()
        loss = torch_func(weight)
        loss.backward(retain_graph=True)
        loss.backward()
        opt.step()
        torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
        assert np.allclose(ms_result2, torch_result2)


# [CI] ms2.4 0920 still not fix.
@SKIP_ENV_GRAPH_MODE(reason="MindSpore has some bug at 'group['lr'] *= 0.2' situation.")
@SKIP_ENV_PYNATIVE_MODE(reason="MindSpore has some bug at 'group['lr'] *= 0.2' situation.")
def test_sgd_mul_lr():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.SGD([weight], lr=0.01)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] *= 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] *= 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.SGD([weight], lr=0.01)
    for group in opt.param_groups:
        group['lr'] *= 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] *= 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_sgd_jit():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.SGD([weight], lr=0.01)
    grads = ms_torch.tensor([3, 4.])

    @ms.jit
    def do_optim(opt, grads):
        opt.step((grads,))
        # In MindSpore Strict Graph-Mode on Ascend, not support return None Value, so return True.
        return True

    # step 1
    for group in opt.param_groups:
        ms.ops.assign(group['lr'], 0.2)
    do_optim(opt, grads)
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        ms.ops.assign(group['lr'], 0.5)
    do_optim(opt, grads)
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.SGD([weight], lr=0.01)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    assert np.allclose(ms_result2, torch_result2)

def test_sgd_multi_group():
    weight1 = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    weight2 = ms_torch.nn.Parameter(ms_torch.tensor([3, 4]).to(ms_torch.float))
    # opt = ms_torch.optim.SGD([weight], lr=0.01)
    opt = ms_torch.optim.SGD([{'params': weight1, 'lr':0.01},
                              {'params': weight2, 'lr':0.1}])
    grads = (ms_torch.tensor([3, 4.]), ms_torch.tensor([3, 4.]))

    # step 1
    opt.step(grads)
    ms_result1_1 = opt.param_groups[0]['params'][0].detach().numpy()
    ms_result1_2 = opt.param_groups[1]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step(grads)
    ms_result2_1 = opt.param_groups[0]['params'][0].detach().numpy()
    ms_result2_2 = opt.param_groups[1]['params'][0].detach().numpy()

    weight1 = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    weight2 = torch.nn.Parameter(torch.tensor([3, 4]).to(torch.float))
    opt = torch.optim.SGD([{'params': weight1, 'lr':0.01},
                           {'params': weight2, 'lr':0.1}])

    # step 1
    weight1.grad = torch.tensor([3, 4.])
    weight2.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1_1 = opt.param_groups[0]['params'][0].detach().numpy()
    torch_result1_2 = opt.param_groups[1]['params'][0].detach().numpy()
    assert np.allclose(ms_result1_1, torch_result1_1)
    assert np.allclose(ms_result1_2, torch_result1_2)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight1.grad = torch.tensor([3, 4.])
    weight2.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2_1 = opt.param_groups[0]['params'][0].detach().numpy()
    torch_result2_2 = opt.param_groups[1]['params'][0].detach().numpy()
    assert np.allclose(ms_result2_1, torch_result2_1)
    assert np.allclose(ms_result2_2, torch_result2_2)

def test_sgd_with_required_lr():
    weight1 = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    weight2 = torch.nn.Parameter(torch.tensor([2, 3]).to(torch.float))
    weight_groups = [{'params':weight1, 'lr': 0.1}, {'params':weight2, 'lr': 0.001}]
    _sgd = torch.optim.SGD(weight_groups)  # no lr input
    assert _sgd.param_groups[0]['lr'] == 0.1
    assert _sgd.param_groups[1]['lr'] == 0.001
    weight_groups_no_lr = [{'params':weight1, 'lr': 0.1}, {'params':weight2}]
    try:
        _sgd1 = torch.optim.SGD(weight_groups_no_lr)
        assert False
    except Exception as e:
        assert "required optimization parameter lr" in str(e)

    weight1 = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    weight2 = ms_torch.nn.Parameter(ms_torch.tensor([2, 3]).to(ms_torch.float))
    weight_groups = [{'params':weight1, 'lr': 0.1}, {'params':weight2, 'lr': 0.001}]
    _sgd = ms_torch.optim.SGD(weight_groups)  # no lr input
    assert np.allclose(_sgd.param_groups[0]['lr'].asnumpy(), np.array(0.1))  # adapter lr is a parameters
    assert np.allclose(_sgd.param_groups[1]['lr'].asnumpy(), np.array(0.001))
    weight_groups_no_lr = [{'params':weight1, 'lr': 0.1}, {'params':weight2}]
    try:
        _sgd1 = ms_torch.optim.SGD(weight_groups_no_lr)
        assert False
    except Exception as e:
        assert "required optimization parameter lr" in str(e)

def test_sgd_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.SGD([weight], lr=0.01)
    opt.accum = [ms.Parameter([1, 2])]
    s = opt.state_dict()

    ms_torch.save(s, 'sgd.pth')
    s = ms_torch.load('sgd.pth')
    os.remove('sgd.pth')

    opt2 = ms_torch.optim.SGD([weight], lr=0.05)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.accum[0].asnumpy(), opt.accum[0].asnumpy())
    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.01))

def test_sgd_state_dict_load_from_pytorch_int_args():
    pt_weight1 = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    pt_weight2 = torch.nn.Parameter(torch.tensor([3, 4]).to(torch.float))
    opt = torch.optim.SGD([{'params': pt_weight1, 'lr':0.01},
                           {'params': pt_weight2, 'lr':0.1}])
    grads1 = torch.tensor([3, 4.])
    grads2 = torch.tensor([5, 6.])
    pt_weight1.grad = grads1
    pt_weight2.grad = grads2

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    torch_result2 = opt.param_groups[1]['params'][0].detach().numpy()

    ms_weight1 = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    ms_weight2 = ms_torch.nn.Parameter(ms_torch.tensor([3, 4]).to(ms_torch.float))
    opt2 = ms_torch.optim.SGD([{'params': ms_weight1, 'lr':0.01},
                           {'params': ms_weight2, 'lr':0.1}])
    grads1 = ms_torch.tensor([3, 4.])
    grads2 = ms_torch.tensor([5, 6.])
    opt2.load_state_dict(s)
    opt2.step((grads1, grads2))

    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    ms_result2 = opt.param_groups[1]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(ms_result2, torch_result2)

def test_adam():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adam([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adam([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_adam_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adam([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'adam.pth')
    s = ms_torch.load('adam.pth')
    os.remove('adam.pth')

    opt2 = ms_torch.optim.Adam([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.exp_avg[0].asnumpy(), opt.exp_avg[0].asnumpy())
    assert np.allclose(opt2.exp_avg_sq[0].asnumpy(), opt.exp_avg_sq[0].asnumpy())
    assert np.allclose(opt2.max_exp_avg_sq[0].asnumpy(), opt.max_exp_avg_sq[0].asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.01))


def test_adamw():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.AdamW([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.AdamW([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_adamax_jit():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0.3)
    grads = ms_torch.tensor([3, 4.])

    @ms.jit
    def do_optim(opt, grads):
        opt.step((grads,))
        # In MindSpore Strict Graph-Mode on Ascend, not support return None Value, so return True.
        return True

    # step 1
    for group in opt.param_groups:
        ms.ops.assign(group['lr'], 0.2)
    do_optim(opt, grads)
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        ms.ops.assign(group['lr'], 0.5)
    do_optim(opt, grads)
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0.3)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_adamw_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.AdamW([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.AdamW([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.exp_avg[0].asnumpy(), opt.exp_avg[0].asnumpy())
    assert np.allclose(opt2.exp_avg_sq[0].asnumpy(), opt.exp_avg_sq[0].asnumpy())
    assert np.allclose(opt2.max_exp_avg_sq[0].asnumpy(), opt.max_exp_avg_sq[0].asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.01))

def test_isinstance_optimizer():
    _param = [ms_torch.nn.Parameter(1.),]
    _sgd = ms_torch.optim.SGD(_param, 1.0)
    _adam = ms_torch.optim.Adam(_param, 1.0)
    _adamw = ms_torch.optim.AdamW(_param, 1.0)

    assert isinstance(_sgd, ms_torch.optim.Optimizer)
    assert isinstance(_adam, ms_torch.optim.Optimizer)
    assert isinstance(_adamw, ms_torch.optim.Optimizer)

def test_adamw_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adam([pt_weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.Adam([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0)
    opt2.load_state_dict(s)
    ms_grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(ms_grads)
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.exp_avg[0].numpy(), opt.state[pt_weight]['exp_avg'].numpy())
    assert np.allclose(opt2.exp_avg_sq[0].numpy(), opt.state[pt_weight]['exp_avg_sq'].numpy())

def test_adamw_group_state_dict_from_pytorch_pth():
    pt_weight_1 = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    pt_weight_2 = torch.nn.Parameter(torch.tensor([3, 4]).to(torch.float))
    weight_groups = [{'params':pt_weight_1, 'lr': 0.1}, {'params':pt_weight_2, 'lr': 0.001}]
    opt = torch.optim.AdamW(weight_groups, lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    grads = torch.tensor([3, 4.])
    pt_weight_1.grad = grads
    pt_weight_2.grad = grads
    opt.step()

    s = opt.state_dict()
    torch.save(s, 'adam_pt_group.pth')
    s = ms_torch.load('adam_pt_group.pth')
    os.remove('adam_pt_group.pth')

    weight_1 = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    weight_2 = ms_torch.nn.Parameter(ms_torch.tensor([3, 4]).to(ms_torch.float))
    weight_groups = [{'params':weight_1, 'lr': 0.1}, {'params':weight_2, 'lr': 0.001}]
    opt2 = ms_torch.optim.AdamW(weight_groups, lr=0.01, betas=(0.9, 0.8), weight_decay=0.5)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.exp_avg[0].numpy(), opt.state[pt_weight_1]['exp_avg'].numpy())
    assert np.allclose(opt2.exp_avg[1].numpy(), opt.state[pt_weight_2]['exp_avg'].numpy())
    assert np.allclose(opt2.exp_avg_sq[0].numpy(), opt.state[pt_weight_1]['exp_avg_sq'].numpy())
    assert np.allclose(opt2.exp_avg_sq[1].numpy(), opt.state[pt_weight_2]['exp_avg_sq'].numpy())

def test_adadelta():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adadelta([weight], lr=0.01, rho=0.8, eps=0.2, weight_decay=0.5)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adadelta([weight], lr=0.01, rho=0.8, eps=0.2, weight_decay=0.5)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_adadelta_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adadelta([weight], lr=0.01, rho=0.8, eps=0.2, weight_decay=0.5)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.Adadelta([weight], lr=0.01, rho=0.8, eps=0.2, weight_decay=0.5)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.accum[0].asnumpy(), opt.accum[0].asnumpy())
    assert np.allclose(opt2.accum_update[0].asnumpy(), opt.accum_update[0].asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.01))

def test_adadelta_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adadelta([pt_weight], lr=0.01, rho=0.8, eps=0.2, weight_decay=0)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    opt.step()

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.Adadelta([weight], lr=0.01, rho=0.8, eps=0.2, weight_decay=0)
    opt2.load_state_dict(s)
    ms_grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(ms_grads)
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.accum[0].numpy(), opt.state[pt_weight]['square_avg'].numpy())
    assert np.allclose(opt2.accum_update[0].numpy(), opt.state[pt_weight]['acc_delta'].numpy())

def test_adagrad():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adagrad([weight], lr=0.01, lr_decay=0.1, weight_decay=0.5, initial_accumulator_value=0.1, eps=0.2)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adagrad([weight], lr=0.01, lr_decay=0.1, weight_decay=0.5, initial_accumulator_value=0.1, eps=0.2)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_adagrad_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adagrad([weight], lr=0.01, lr_decay=0.1, weight_decay=0.5, initial_accumulator_value=0.1, eps=0.2)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.Adagrad([weight], lr=0.01, lr_decay=0.1, weight_decay=0.5, initial_accumulator_value=0.1, eps=0.2)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.accum[0].asnumpy(), opt.accum[0].asnumpy())
    assert np.allclose(opt2.step_t.asnumpy(), opt.step_t.asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.01))

def test_adagrad_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adagrad([pt_weight], lr=0.01, lr_decay=0, weight_decay=0, initial_accumulator_value=0, eps=0.2)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.Adagrad([weight], lr=0.01, lr_decay=0.1, weight_decay=0.5, initial_accumulator_value=0.1, eps=0.2)
    opt2.load_state_dict(s)
    grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(grads)
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.accum[0].numpy(), opt.state[pt_weight]['sum'].numpy())
    assert np.allclose(opt2.step_t.numpy(), opt.state[pt_weight]['step'].numpy())

def test_asgd():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.ASGD([weight], lr=1e-1, lambd=1e-3, alpha=0.45, t0=1e5, weight_decay=0.1)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.ASGD([weight], lr=1e-1, lambd=1e-3, alpha=0.45, t0=1e5, weight_decay=0.1)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_asgd_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.ASGD([weight], lr=1e-1, lambd=1e-3, alpha=0.45, t0=1e5, weight_decay=0.1)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.ASGD([weight], lr=1e-1, lambd=1e-3, alpha=0.45, t0=1e5, weight_decay=0.1)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.eta[0].asnumpy(), opt.eta[0].asnumpy())
    assert np.allclose(opt2.mu[0].asnumpy(), opt.mu[0].asnumpy())
    assert np.allclose(opt2.ax[0].asnumpy(), opt.ax[0].asnumpy())
    assert np.allclose(opt2.step_t.asnumpy(), opt.step_t.asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.1))

def test_asgd_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.ASGD([pt_weight], lr=1e-1, lambd=1e-3, alpha=0.45, t0=1e5, weight_decay=0)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.ASGD([weight], lr=1e-1, lambd=1e-3, alpha=0.45, t0=1e5, weight_decay=0)
    opt2.load_state_dict(s)
    grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(grads)
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.eta[0].numpy(), opt.state[pt_weight]['eta'].numpy())
    assert np.allclose(opt2.mu[0].numpy(), opt.state[pt_weight]['mu'].numpy())
    assert np.allclose(opt2.ax[0].numpy(), opt.state[pt_weight]['ax'].numpy())
    assert np.allclose(opt2.step_t.numpy(), opt.state[pt_weight]['step'].numpy())

def test_adamax():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0.3)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0.3)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_adamax_maximize():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0.3, maximize=True)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0.3, maximize=True)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_adamax_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0.3)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0.3)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.exp_avg[0].asnumpy(), opt.exp_avg[0].asnumpy())
    assert np.allclose(opt2.exp_inf[0].asnumpy(), opt.exp_inf[0].asnumpy())
    assert np.allclose(opt2.step_t.asnumpy(), opt.step_t.asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.001))

def test_adamax_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Adamax([pt_weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.Adamax([weight], lr=1e-3, betas=(0.8, 0.88), eps=1e-7, weight_decay=0)
    opt2.load_state_dict(s)

    grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(grads)
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.exp_avg[0].numpy(), opt.state[pt_weight]['exp_avg'].numpy())
    assert np.allclose(opt2.exp_inf[0].numpy(), opt.state[pt_weight]['exp_inf'].numpy())
    assert np.allclose(opt2.step_t.numpy(), opt.state[pt_weight]['step'].numpy())

def test_rmsprop():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.RMSprop([weight], lr=1e-3, alpha=0.90, eps=1e-7, weight_decay=0.3, momentum=0)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.RMSprop([weight], lr=1e-3, alpha=0.90, eps=1e-7, weight_decay=0.3, momentum=0)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_rmsprop_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.RMSprop([weight], lr=1e-3, alpha=0.90, eps=1e-7, weight_decay=0.3, momentum=0.1, centered=True)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.RMSprop([weight], lr=1e-3, alpha=0.90, eps=1e-7, weight_decay=0.3, momentum=0.1, centered=True)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.mean_grad[0].asnumpy(), opt.mean_grad[0].asnumpy())
    assert np.allclose(opt2.mean_square[0].asnumpy(), opt.mean_square[0].asnumpy())
    assert np.allclose(opt2.moment[0].asnumpy(), opt.moment[0].asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.001))

def test_rmsprop_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.RMSprop([pt_weight], lr=1e-3, alpha=0.90, eps=1e-7, weight_decay=0, momentum=0.1, centered=True)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.RMSprop([weight], lr=1e-3, alpha=0.90, eps=1e-7, weight_decay=0, momentum=0.1, centered=True)
    opt2.load_state_dict(s)
    grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(grads)
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.mean_grad[0].numpy(), opt.state[pt_weight]['grad_avg'].numpy())
    assert np.allclose(opt2.mean_square[0].numpy(), opt.state[pt_weight]['square_avg'].numpy())
    assert np.allclose(opt2.moment[0].numpy(), opt.state[pt_weight]['momentum_buffer'].numpy())

def test_rprop():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Rprop([weight], lr=1e-1, etas=(0.3, 1.5), step_sizes=(1e-5, 2))
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Rprop([weight], lr=1e-1, etas=(0.3, 1.5), step_sizes=(1e-5, 2))
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_rprop_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.Rprop([weight], lr=1e-1, etas=(0.3, 1.5), step_sizes=(1e-5, 2))
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.Rprop([weight], lr=1e-1, etas=(0.3, 1.5), step_sizes=(1e-5, 2))
    opt2.load_state_dict(s)
    assert np.allclose(opt2.step_size[0].asnumpy(), opt.step_size[0].asnumpy())
    assert np.allclose(opt2.prev[0].asnumpy(), opt.prev[0].asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.1))

def test_rprop_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.Rprop([pt_weight], lr=1e-1, etas=(0.3, 1.5), step_sizes=(1e-5, 2))
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.Rprop([weight], lr=1e-1, etas=(0.3, 1.5), step_sizes=(1e-5, 2))
    opt2.load_state_dict(s)
    grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(grads)
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.step_size[0].numpy(), opt.state[pt_weight]['step_size'].numpy())
    assert np.allclose(opt2.prev[0].numpy(), opt.state[pt_weight]['prev'].numpy())

def test_nadam():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.NAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0.2)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.NAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0.2)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # MindSpore's NAdam is align for PyTorch 2.0 NAdam, whoes algorithum is slightly different from PyTorch 1.12.0 NAdam.
    # So here should add "atol=1e-2"
    assert np.allclose(ms_result1, torch_result1, atol=1e-2)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2, atol=1e-2)

def test_nadam_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.NAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0.2)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.NAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0.2)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.exp_avg[0].asnumpy(), opt.exp_avg[0].asnumpy())
    assert np.allclose(opt2.exp_avg_sq[0].asnumpy(), opt.exp_avg_sq[0].asnumpy())
    assert np.allclose(opt2.mu_product[0].asnumpy(), opt.mu_product[0].asnumpy())
    assert np.allclose(opt2.step_t.asnumpy(), opt.step_t.asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.001))

def test_nadam_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.NAdam([pt_weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.NAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0)
    opt2.load_state_dict(s)
    grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(grads)
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.exp_avg[0].numpy(), opt.state[pt_weight]['exp_avg'].numpy())
    assert np.allclose(opt2.exp_avg_sq[0].numpy(), opt.state[pt_weight]['exp_avg_sq'].numpy())
    assert np.allclose(opt2.mu_product[0].numpy(), opt.state[pt_weight]['mu_product'].numpy())
    assert np.allclose(opt2.step_t.numpy(), opt.state[pt_weight]['step'].numpy())

def test_radam():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.RAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0.2)
    grads = ms_torch.tensor([3, 4.])

    # step 1
    for group in opt.param_groups:
        group['lr'] = 0.2
    opt.step((grads,))
    ms_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    opt.step((grads,))
    ms_result2 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.RAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0.2)
    for group in opt.param_groups:
        group['lr'] = 0.2
    # step 1
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)

    # step 2
    for group in opt.param_groups:
        group['lr'] = 0.5
    weight.grad = torch.tensor([3, 4.])
    opt.step()
    torch_result2 = opt.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result2, torch_result2)

def test_radam_state_dict():
    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt = ms_torch.optim.RAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0.2)
    grads = ms_torch.tensor([3, 4.])
    opt.step((grads,))

    s = opt.state_dict()
    ms_torch.save(s, 'state.pth')
    s = ms_torch.load('state.pth')
    os.remove('state.pth')

    opt2 = ms_torch.optim.RAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0.2)
    opt2.load_state_dict(s)
    assert np.allclose(opt2.exp_avg[0].asnumpy(), opt.exp_avg[0].asnumpy())
    assert np.allclose(opt2.exp_avg_sq[0].asnumpy(), opt.exp_avg_sq[0].asnumpy())
    assert np.allclose(opt2.step_t.asnumpy(), opt.step_t.asnumpy())

    # 0.099999999 == 0.01
    assert np.allclose(opt2.param_groups[0]['lr'].asnumpy(), np.array(0.001))

def test_radam_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.RAdam([pt_weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim.RAdam([weight], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0)
    opt2.load_state_dict(s)
    grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(grads)
    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.exp_avg[0].numpy(), opt.state[pt_weight]['exp_avg'].numpy())
    assert np.allclose(opt2.exp_avg_sq[0].numpy(), opt.state[pt_weight]['exp_avg_sq'].numpy())
    assert np.allclose(opt2.step_t.numpy(), opt.state[pt_weight]['step'].numpy())

def test_adamw_inner():
    weight2 = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float16))
    opt2 = ms_torch.optim._adamw.Float32AdamW([weight2], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0)
    weight2_1 = ms_torch.nn.Parameter(ms_torch.tensor([5, 6]).to(ms_torch.float32))
    opt2.param_groups[0]['params'] = [weight2_1]
    weight2_1.grad = ms_torch.tensor([3, 4.]).to(ms_torch.float32)
    for _ in range(5):
        opt2.step()

    weight1 = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float16))
    opt = torch.optim.AdamW([weight1], lr=1e-3, betas=(0.8, 0.88), eps=2e-8, weight_decay=0)
    weight1_1 = torch.nn.Parameter(torch.tensor([5, 6]).to(torch.float32))
    opt.param_groups[0]['params'] = [weight1_1]
    weight1_1.grad = torch.tensor([3, 4.]).to(torch.float32)
    for _ in range(5):
        opt.step()

    assert np.allclose(weight2_1.detach().numpy(), weight1_1.detach().numpy())

def test_Float32adamw_state_dict_from_pytorch_pth():
    pt_weight = torch.nn.Parameter(torch.tensor([1, 2]).to(torch.float))
    opt = torch.optim.AdamW([pt_weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0)
    grads = torch.tensor([3, 4.])
    pt_weight.grad = grads

    s = opt.state_dict()
    torch.save(s, 'state_pt.pth')
    s = ms_torch.load('state_pt.pth')
    os.remove('state_pt.pth')

    opt.step()
    torch_result1 = opt.param_groups[0]['params'][0].detach().numpy()

    weight = ms_torch.nn.Parameter(ms_torch.tensor([1, 2]).to(ms_torch.float))
    opt2 = ms_torch.optim._adamw.Float32AdamW([weight], lr=0.01, betas=(0.9, 0.8), weight_decay=0)
    opt2.load_state_dict(s)
    ms_grads = (ms_torch.tensor([3, 4.]),)
    opt2.step(ms_grads)
    ms_result1 = opt2.param_groups[0]['params'][0].detach().numpy()
    assert np.allclose(ms_result1, torch_result1)
    assert np.allclose(opt2.exp_avg[0].numpy(), opt.state[pt_weight]['exp_avg'].numpy())
    assert np.allclose(opt2.exp_avg_sq[0].numpy(), opt.state[pt_weight]['exp_avg_sq'].numpy())


if __name__ == '__main__':
    test_optimizer_custom()
    test_sgd()
    test_adam()
    test_adamw()
    test_sgd_state_dict()
    test_adam_state_dict()
    test_adamw_state_dict()
    test_isinstance_optimizer()
    test_sgd_with_required_lr()
    test_adamw_state_dict_from_pytorch_pth()
    test_adamw_group_state_dict_from_pytorch_pth()
    test_adadelta()
    test_adadelta_state_dict()
    test_adadelta_state_dict_from_pytorch_pth()
    test_adagrad()
    test_adagrad_state_dict()
    test_adagrad_state_dict_from_pytorch_pth()
    test_asgd()
    test_asgd_state_dict()
    test_asgd_state_dict_from_pytorch_pth()
    test_adamax()
    test_adamax_maximize()
    test_adamax_state_dict()
    test_adamax_state_dict_from_pytorch_pth()
    test_rmsprop()
    test_rmsprop_state_dict()
    test_rmsprop_state_dict_from_pytorch_pth()
    test_rprop()
    test_rprop_state_dict()
    test_rprop_state_dict_from_pytorch_pth()
    test_nadam()
    test_nadam_state_dict()
    test_nadam_state_dict_from_pytorch_pth()
    test_radam()
    test_radam_state_dict()
    test_radam_state_dict_from_pytorch_pth()
    test_sgd_mul_lr()
    test_sgd_jit()
    test_sgd_multi_group()
    test_adamax_jit()
    test_sgd_state_dict_load_from_pytorch_int_args()
    test_sgd_autograd()
    test_sgd_autograd_double_backward()
