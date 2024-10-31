import pickle
import numpy as np
import torch
import mindspore as ms
from mindspore import context
import mindtorch.torch as ms_torch
from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, param_compare, \
    SKIP_ENV_CPU, SKIP_ENV_ASCEND, enable_backward

set_mode_by_env_config()

@SKIP_ENV_CPU(reason="torch only support GradScaler on GPU.")
@SKIP_ENV_ASCEND(reason="torch only support GradScaler on GPU.")
@SKIP_ENV_GRAPH_MODE(reason="unscale_() not support in GraphMode")
def test_grad_scalar():
    _inputs = np.random.randn(3, 3).astype(np.float32)
    _target = 2.0

    def torch_scaler():
        class Model(torch.nn.Module):
            def __init__(self, *args, **kwargs):
                super().__init__()
                self.a = torch.nn.Parameter(torch.tensor(2.0).to(torch.float32))

            def forward(self, inputs):
                return (inputs * self.a).sum()

        class Cri(torch.nn.Module):
            def forward(self, out, target):
                return out - target

        model = Model().cuda()
        # model = Pt_Model()
        critirion = Cri()

        inputs = torch.tensor(_inputs).to("cuda")
        target = torch.tensor(_target).to(torch.float32).to("cuda")
        # inputs = torch.tensor(_inputs)
        # target = torch.tensor(_target).to(torch.float32)
        optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

        scaler = torch.cuda.amp.GradScaler(init_scale=2.**8, growth_factor=1.6, growth_interval=1)
        # with torch.autocast(device_type="cpu", dtype=torch.bfloat16):
        with torch.autocast(device_type="cuda", dtype=torch.float16):
            out = model(inputs)
            loss = critirion(out, target)

        scaler.scale(loss).backward()
        scaler.unscale_(optimizer)  # unscale the gradients
        scaler.step(optimizer)      # optimizer.step()
        scaler.update()             # 更新scaler
        pt_result = model.a.cpu().detach()
        pt_scale = scaler.get_scale()
        return pt_result, pt_scale
    
    # adapter
    def ms_scaler():
        class Model(ms_torch.nn.Module):
            def __init__(self, *args, **kwargs):
                super().__init__()
                self.a = ms_torch.nn.Parameter(ms_torch.tensor(2.0).to(ms_torch.float32))

            def forward(self, inputs):
                return (inputs * self.a).sum()

        class Cri(ms_torch.nn.Module):
            def forward(self, out, target):
                return out - target
        
        model = Model()
        critirion = Cri()

        inputs = ms_torch.tensor(_inputs)
        target = ms_torch.tensor(_target).to(ms_torch.float32)
        optimizer = ms_torch.optim.SGD(model.parameters(), lr=0.1)

        scaler = ms_torch.cuda.amp.GradScaler(init_scale=2.**8, growth_factor=1.6, growth_interval=1)
        class Net(ms_torch.nn.Module):
            def __init__(self, model, critirion):
                super().__init__()
                self.model = model
                self.critirion = critirion

            def forward(self, inputs, target):
                out = self.model(inputs)
                loss = self.critirion(out, target)
                return loss
        net = Net(model, critirion)
        net = ms.amp.auto_mixed_precision(net)

        def func(inputs, target):
            loss = net(inputs, target)
            out = scaler.scale(loss)
            return out

        grad_fn = ms.ops.grad(func, None, net.trainable_params())
        grads = grad_fn(inputs, target)

        scaler.unscale_(optimizer, grads)
        scaler.step(optimizer, grads)
        scaler.update()
        ms_result = model.a.detach()
        ms_scale = scaler.get_scale()
        return ms_result, ms_scale


    pt_result, pt_scale = torch_scaler()
    ms_result, ms_scale = ms_scaler()

    param_compare(pt_result, ms_result)
    assert pt_scale == ms_scale

@SKIP_ENV_CPU(reason="torch only support GradScaler on GPU.")
@SKIP_ENV_ASCEND(reason="torch only support GradScaler on GPU.")
def test_get_scale():
    pt_scaler = torch.cuda.amp.GradScaler()
    ms_scaler = ms_torch.cuda.amp.GradScaler()

    assert pt_scaler.get_scale() == ms_scaler.get_scale()
    assert pt_scaler.get_growth_factor() == ms_scaler.get_growth_factor()
    assert pt_scaler.get_backoff_factor() == ms_scaler.get_backoff_factor()
    assert pt_scaler.get_growth_interval() == ms_scaler.get_growth_interval()

    pt_scaler.set_growth_factor(4.)
    pt_scaler.set_backoff_factor(0.25)
    pt_scaler.set_growth_interval(1000)
    ms_scaler.set_growth_factor(4.)
    ms_scaler.set_backoff_factor(0.25)
    ms_scaler.set_growth_interval(1000)

    assert pt_scaler.get_growth_factor() == ms_scaler.get_growth_factor()
    assert pt_scaler.get_backoff_factor() == ms_scaler.get_backoff_factor()
    assert pt_scaler.get_growth_interval() == ms_scaler.get_growth_interval()

@SKIP_ENV_CPU(reason="torch only support GradScaler on GPU.")
@SKIP_ENV_ASCEND(reason="torch only support GradScaler on GPU.")
def test_state_dict():
    pt_scaler = torch.cuda.amp.GradScaler(init_scale=2.**3,
                                          growth_factor=5.0,
                                          backoff_factor=0.1,
                                          growth_interval=100,)
    ms_scaler = ms_torch.cuda.amp.GradScaler()

    pt_state = pt_scaler.state_dict()
    pt_state['_growth_tracker'] = 2
    ms_scaler.load_state_dict(pt_state)

    assert pt_scaler.get_scale() == ms_scaler.get_scale()
    assert pt_scaler.get_growth_factor() == ms_scaler.get_growth_factor()
    assert pt_scaler.get_backoff_factor() == ms_scaler.get_backoff_factor()
    assert pt_scaler.get_growth_interval() == ms_scaler.get_growth_interval()
    assert ms_scaler._get_growth_tracker() == 2

def test_get_state_set_state():
    a = ms_torch.cuda.amp.GradScaler(3, 1.4, 0.2, 6)
    data = pickle.dumps(a)
    b = pickle.loads(data)
    assert b.is_enabled() == a.is_enabled()
    assert b.get_scale() == 3
    assert b.get_growth_factor() == 1.4
    assert b.get_backoff_factor() == 0.2
    assert b.get_growth_interval() == 6

def test_grad_scaling_scale():
    scaler = ms_torch.cuda.amp.GradScaler(init_scale=2.)
    t0 = ms_torch.full((1,), 4.0, dtype=ms_torch.float32)
    t1 = ms_torch.full((1,), 4.0, dtype=ms_torch.float32)
    # Create some nested iterables of tensors on different devices.
    outputs = (t1.clone(), (t0.clone(), t1.clone()), [t0.clone(), (t1.clone(), t0.clone())])
    outputs = scaler.scale(outputs)
    assert (outputs[0] == 8.0 and outputs[1][0] == 8.0 and outputs[1][1] == 8.0 and
            outputs[2][0] == 8.0 and outputs[2][1][0] == 8.0 and outputs[2][1][1] == 8.0)

@SKIP_ENV_ASCEND(reason='torch.cuda.amp.GradScaler only support on GPU')
@SKIP_ENV_CPU(reason='torch.cuda.amp.GradScaler only support on GPU')
@SKIP_ENV_GRAPH_MODE(reason='scaler.unscale_ not support GRAPH_MODE')
def test_grad_inf_not_step():
    scaler = torch.cuda.amp.GradScaler(init_scale=2**5.)
    _param1 = torch.nn.Parameter(torch.tensor(2.).to(torch.float32).to('cuda'))
    _param2 = torch.nn.Parameter(torch.tensor(3.).to(torch.float32).to('cuda'))
    _param = (_param1, _param2)
    optimizer = torch.optim.SGD(_param, lr=0.3)
    y = _param1 + _param2
    scaler.scale(y)
    _param1.grad = torch.tensor(3333.).to(torch.float32).to('cuda')
    _param2.grad = torch.tensor(np.inf).to(torch.float32).to('cuda')
    scaler.unscale_(optimizer)
    scaler.step(optimizer)
    scaler.update()
    pt_result1 = _param1.cpu().detach()
    pt_result2 = _param2.cpu().detach()
    pt_result_scale = scaler.get_scale()

    scaler = ms_torch.cuda.amp.GradScaler(init_scale=2**5.)
    _param1 = ms_torch.nn.Parameter(ms_torch.tensor(2.).to(ms_torch.float32).to('cuda'))
    _param2 = ms_torch.nn.Parameter(ms_torch.tensor(3.).to(ms_torch.float32).to('cuda'))
    _param = (_param1, _param2)
    optimizer = ms_torch.optim.SGD(_param, lr=0.3)
    y = _param1 + _param2
    scaler.scale(y)
    grads = [ms_torch.tensor(3333.).to(ms_torch.float32).to('cuda'),
             ms_torch.tensor(np.inf).to(ms_torch.float32).to('cuda')]
    scaler.unscale_(optimizer, grads)
    scaler.step(optimizer, grads)
    scaler.update()
    ms_result1 = _param1.cpu().detach()
    ms_result2 = _param2.cpu().detach()
    ms_result_scale = scaler.get_scale()

    param_compare(pt_result1, ms_result1) # pt_result1 = 2
    param_compare(pt_result2, ms_result2) # pt_result2 = 3
    assert pt_result_scale == ms_result_scale # pt_result_scale = 16

@SKIP_ENV_ASCEND(reason='torch.cuda.amp.GradScaler only support on GPU')
@SKIP_ENV_CPU(reason='torch.cuda.amp.GradScaler only support on GPU')
@SKIP_ENV_GRAPH_MODE(reason='scaler.unscale_ not support GRAPH_MODE')
def test_one_gradscaler_two_optimizer():
    scaler = torch.cuda.amp.GradScaler(init_scale=2**5.)
    _param1 = torch.nn.Parameter(torch.tensor(2.).to(torch.float32).to('cuda'))
    _param2 = torch.nn.Parameter(torch.tensor(3.).to(torch.float32).to('cuda'))
    param1 = (_param1, _param2)
    _param3 = torch.nn.Parameter(torch.tensor(2.).to(torch.float32).to('cuda'))
    _param4 = torch.nn.Parameter(torch.tensor(3.).to(torch.float32).to('cuda'))
    param2 = (_param3, _param4)
    optimizer1 = torch.optim.SGD(param1, lr=0.3)
    optimizer2 = torch.optim.Adam(param2, lr=0.1)
    y1 = _param1 + _param2
    y2 = _param3 + _param4
    scaler.scale(y1)
    scaler.scale(y2)
    _param1.grad = torch.tensor(3333.).to(torch.float32).to('cuda')
    _param2.grad = torch.tensor(np.inf).to(torch.float32).to('cuda')
    _param3.grad = torch.tensor(3333.).to(torch.float32).to('cuda')
    _param4.grad = torch.tensor(2222.).to(torch.float32).to('cuda')
    scaler.unscale_(optimizer1)
    scaler.unscale_(optimizer2)
    scaler.step(optimizer1)
    scaler.step(optimizer2)
    scaler.update()
    pt_result1 = _param1.cpu().detach()
    pt_result2 = _param2.cpu().detach()
    pt_result3 = _param3.cpu().detach()
    pt_result4 = _param4.cpu().detach()
    pt_result_scale = scaler.get_scale()

    scaler = ms_torch.cuda.amp.GradScaler(init_scale=2**5.)
    _param1 = ms_torch.nn.Parameter(ms_torch.tensor(2.).to(ms_torch.float32).to('cuda'))
    _param2 = ms_torch.nn.Parameter(ms_torch.tensor(3.).to(ms_torch.float32).to('cuda'))
    param1 = (_param1, _param2)
    _param3 = ms_torch.nn.Parameter(ms_torch.tensor(2.).to(ms_torch.float32).to('cuda'))
    _param4 = ms_torch.nn.Parameter(ms_torch.tensor(3.).to(ms_torch.float32).to('cuda'))
    param2 = (_param3, _param4)
    optimizer1 = ms_torch.optim.SGD(param1, lr=0.3)
    optimizer2 = ms_torch.optim.Adam(param2, lr=0.1)
    y1 = _param1 + _param2
    y2 = _param3 + _param4
    scaler.scale(y1)
    scaler.scale(y2)
    grads1 = [ms_torch.tensor(3333.).to(ms_torch.float32).to('cuda'),
              ms_torch.tensor(np.inf).to(ms_torch.float32).to('cuda')]
    grads2 = [ms_torch.tensor(3333.).to(ms_torch.float32).to('cuda'),
              ms_torch.tensor(2222.).to(ms_torch.float32).to('cuda')]
    scaler.unscale_(optimizer1, grads1)
    scaler.unscale_(optimizer2, grads2)
    scaler.step(optimizer1, grads1)
    scaler.step(optimizer2, grads2)
    scaler.update()
    ms_result1 = _param1.cpu().detach()
    ms_result2 = _param2.cpu().detach()
    ms_result3 = _param3.cpu().detach()
    ms_result4 = _param4.cpu().detach()
    ms_result_scale = scaler.get_scale()

    param_compare(pt_result1, ms_result1) # pt_result1 = 2
    param_compare(pt_result2, ms_result2) # pt_result2 = 3
    param_compare(pt_result3, ms_result3) # pt_result1 = 1.9
    param_compare(pt_result4, ms_result4) # pt_result2 = 2.9
    assert pt_result_scale == ms_result_scale # pt_result_scale = 16


def test_gradscaler_disable():
    pt_scaler = torch.cuda.amp.GradScaler(enabled=False)
    ms_scaler = ms_torch.cuda.amp.GradScaler(enabled=False)

    pt_a = torch.tensor(2.)
    ms_a = ms_torch.tensor(2.)
    param_compare(pt_scaler.scale(pt_a), ms_scaler.scale(ms_a))

    assert pt_scaler.state_dict() == ms_scaler.state_dict()

    pt_scaler.update()
    ms_scaler.update()
    assert pt_scaler.get_scale() == ms_scaler.get_scale()

if __name__ == '__main__':
    test_grad_scalar()
    test_get_scale()
    test_state_dict()
    test_get_state_set_state()
    test_grad_scaling_scale()
    test_grad_inf_not_step()
    test_grad_scalar()
    test_one_gradscaler_two_optimizer()
    test_gradscaler_disable()