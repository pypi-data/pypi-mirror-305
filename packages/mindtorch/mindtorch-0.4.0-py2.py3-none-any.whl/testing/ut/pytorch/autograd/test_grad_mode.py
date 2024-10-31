#!/usr/bin/env python
# -*- coding: utf-8 -*-
import torch
import mindspore as ms
import mindtorch.torch as ms_torch
from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE

set_mode_by_env_config()

'''
# requires_grad is currently not effective.

def test_no_grad1():
    x = torch.tensor([1.], requires_grad=True)
    with torch.no_grad():
        y = x * 2
    assert y.requires_grad == False

    @torch.no_grad()
    def doubler(x):
        return x * 2
    z = doubler(x)
    assert z.requires_grad == False
'''


def adapter_no_grad():
    @ms_torch.no_grad()
    def doubler(x):
        return x * 2

    class Net(ms_torch.nn.Module):
        def __init__(self):
            super(Net, self).__init__()

        def forward(self, x, y, z):
            y = doubler(y)
            with ms_torch.no_grad():
                z = z * 2
            out = ms_torch.matmul(x, y) + z
            return out

    x = ms_torch.tensor([[0.5, 0.6, 0.4]], dtype=ms_torch.float32)
    y = ms_torch.tensor([[0.01], [0.2], [3.3]], dtype=ms_torch.float32)
    z = ms_torch.tensor([[0.01]], dtype=ms_torch.float32, requires_grad=True)
    net = Net()
    out = net(x, y, z)
    grad_out = ms.grad(net, grad_position=(0, 1, 2))(x, y, z)
    return out, grad_out


def torch_no_grad():
    @torch.no_grad()
    def doubler(x):
        return x * 2

    class Net(torch.nn.Module):
        def __init__(self):
            super(Net, self).__init__()

        def forward(self, x, y, z):
            y = doubler(y)
            with torch.no_grad():
                z = z * 2
            result = torch.matmul(x, y) + z
            return result

    x = torch.tensor([[0.5, 0.6, 0.4]], dtype=torch.float32, requires_grad=True)
    y = torch.tensor([[0.01], [0.2], [3.3]], dtype=torch.float32, requires_grad=True)
    z = torch.tensor([[0.01]], dtype=torch.float32, requires_grad=True)
    out = Net()(x, y, z)
    out.backward()
    grad_out = x.grad, y.grad, z.grad
    return out, grad_out

@SKIP_ENV_GRAPH_MODE(reason="no_grad only support on pynative mode.")
def test_no_grad():
    ms_out, ms_grad_out = adapter_no_grad()
    pt_out, pt_grad_out = torch_no_grad()

    param_compare(ms_out, pt_out.detach(), atol=1e-3)  # atol is for Ascend
    param_compare(ms_grad_out[0], pt_grad_out[0].detach(), atol=1e-2)  # atol is for Ascend
    param_compare(ms_grad_out[1], ms_torch.zeros_like(ms_grad_out[1]))
    param_compare(ms_grad_out[2], ms_torch.zeros_like(ms_grad_out[2]))

@SKIP_ENV_GRAPH_MODE(reason="enable_grad grad only support on pynative mode.")
def test_enbale_grad_func():
    @torch.enable_grad()
    def torch_doubler(input):
        return input * 2

    def torch_func(input1):
        with torch.no_grad():
            with torch.enable_grad():
                a = input1 ** 2
            a = torch_doubler(a)
            with torch.enable_grad():
                a = torch.mean(a)
        return a

    input1 = torch.tensor([2, 3.], requires_grad=True).to(torch.float32)
    pt_out = torch_func(input1)
    pt_out.backward()
    pt_grads = input1.grad

    @ms_torch.enable_grad()
    def ms_doubler(input):
        return input * 2

    def ms_func(input1):
        with ms_torch.no_grad():
            with ms_torch.enable_grad():
                a = input1 ** 2
            a = ms_doubler(a)
            with ms_torch.enable_grad():
                a = ms_torch.mean(a)
        return a

    input1 = ms_torch.tensor([2, 3.], requires_grad=True).to(ms_torch.float32)

    # Automatic differentiation method 1
    ms_out, ms_grads = ms.ops.value_and_grad(ms_func, grad_position=0)(input1)
    param_compare(ms_out, pt_out.detach())
    param_compare(ms_grads, pt_grads.detach())


@SKIP_ENV_GRAPH_MODE(reason="set_grad_enable grad only support on pynative mode.")
def test_set_grad_enable_func():
    def torch_func(input1, input2, input3):
        input1 = input1 ** 2
        with torch.set_grad_enabled(False):
            input2 = input2 * 2
        _ = torch.set_grad_enabled(False)
        input3 = input3 * 2
        _ = torch.set_grad_enabled(True)

        result = input1 + input2 + input3
        result = torch.mean(result)
        return result

    input1 = torch.tensor([1, 2.], requires_grad=True).to(torch.float32)
    input2 = torch.tensor([3, 4.], requires_grad=True).to(torch.float32)
    input3 = torch.tensor([5, 6.], requires_grad=True).to(torch.float32)

    pt_out = torch_func(input1, input2, input3)
    pt_out.backward()
    pt_grad_out = input1.grad

    def ms_torch_func(input1, input2, input3):
        input1 = input1 ** 2
        with ms_torch.set_grad_enabled(False):
            input2 = input2 * 2
        _ = ms_torch.set_grad_enabled(False)
        input3 = input3 * 2
        _ = ms_torch.set_grad_enabled(True)

        result = input1 + input2 + input3
        result = ms_torch.mean(result)
        return result

    input1 = ms_torch.tensor([1, 2.], requires_grad=True).to(ms_torch.float32)
    input2 = ms_torch.tensor([3, 4.], requires_grad=True).to(ms_torch.float32)
    input3 = ms_torch.tensor([5, 6.], requires_grad=True).to(ms_torch.float32)

    # Automatic differentiation method 1
    ms_out, ms_grad_out = ms.ops.value_and_grad(ms_torch_func, (0, 1, 2))(input1, input2, input3)

    param_compare(ms_out, pt_out.detach())
    param_compare(ms_grad_out[0], pt_grad_out.detach())
    param_compare(ms_grad_out[1], ms_torch.zeros_like(ms_grad_out[1]))
    param_compare(ms_grad_out[2], ms_torch.zeros_like(ms_grad_out[2]))


@SKIP_ENV_GRAPH_MODE(reason="tensor.require_grad not actually support yet")
@SKIP_ENV_PYNATIVE_MODE(reason="tensor.require_grad not actually support yet")
def test_require_grad():
    a = torch.tensor(2.).to(torch.float32)
    b = torch.tensor(3.).to(torch.float32)
    d = torch.tensor(4.).to(torch.float32)
    d.requires_grad = True

    c = a * b
    pt_ret_1 = c.requires_grad   # pt_ret_1 = False
    c = c * b
    pt_ret_2 = c.requires_grad   # pt_ret_2 = False
    c = c + d
    pt_ret_3 = c.requires_grad   # pt_ret_3 = True

    a = ms_torch.tensor(2.).to(ms_torch.float32)
    b = ms_torch.tensor(3.).to(ms_torch.float32)
    d = ms_torch.tensor(4.).to(ms_torch.float32)
    d.requires_grad = True

    c = a * b
    ms_ret_1 = c.requires_grad
    c = c * b
    ms_ret_2 = c.requires_grad
    c = c + d
    ms_ret_3 = c.requires_grad

    assert pt_ret_1 == ms_ret_1
    assert pt_ret_2 == ms_ret_2
    assert pt_ret_3 == ms_ret_3

@SKIP_ENV_GRAPH_MODE(reason="tensor.detach_() not support under graph-mode")
def test_detach_():
    a = torch.tensor(1.).to(torch.float32)
    a.requires_grad = True
    b = torch.tensor(2.).to(torch.float32)
    b.requires_grad = True

    c = a ** 2
    c = c * b
    c.detach_()
    d = c + a
    d.backward()
    pt_grad_0 = a.grad.detach()

    a = ms_torch.tensor(1.).to(ms_torch.float32)
    a.requires_grad = True
    b = ms_torch.tensor(2.).to(ms_torch.float32)
    b.requires_grad = True

    def func(a, b):
        c = a ** 2
        c = c * b
        c.detach_()
        d = c + a
        return d

    ms_grads = ms.ops.grad(func, (0, 1))(a, b)

    param_compare(pt_grad_0, ms_grads[0])
    param_compare(ms_grads[1], ms_torch.zeros_like(ms_grads[1]))

@SKIP_ENV_GRAPH_MODE(reason="tensor.fill_ not support graph mode")
def test_parameter_data_grad():
    a = torch.nn.Parameter(torch.tensor(1.))
    a.data.fill_(2.)
    c = a * 3
    c.backward()
    pt_grad = a.grad.detach()

    a = ms_torch.nn.Parameter(ms_torch.tensor(1.))
    a.data.fill_(2.)
    def func(x):
        return x * 3
    ms_grads = ms.ops.grad(func)(a)
    param_compare(pt_grad, ms_grads)

@SKIP_ENV_GRAPH_MODE(reason="is_grad_enabled not support graph mode")
def test_is_grad_enable():
    @ms_torch.no_grad()
    class Foo():
        def __init__(self):
            assert not ms_torch.is_grad_enabled()

        def foo(self):
            # Not applied to methods
            assert ms_torch.is_grad_enabled()

    # Show that we can actually construct the class
    foo = Foo()
    foo.foo()

@SKIP_ENV_GRAPH_MODE(reason="is_grad_enabled not support graph mode")
def test_is_grad_enable_nested():
    x = ms_torch.randn([3, 4])
    before = ms_torch.is_grad_enabled()
    with ms_torch.set_grad_enabled(False):
        with ms_torch.set_grad_enabled(True):
            x = ms_torch.mul(x, 5)
            x = ms_torch.sqrt(x)
            assert ms_torch.is_grad_enabled()
        assert not ms_torch.is_grad_enabled()
    assert ms_torch.is_grad_enabled() == before
    return x

@SKIP_ENV_GRAPH_MODE(reason="inference_mode not support graph mode")
def test_inference_mode_context_manager():
    with ms_torch.inference_mode():
        assert ms_torch.is_inference_mode_enabled()
        with ms_torch.inference_mode(False):
            assert not ms_torch.is_inference_mode_enabled()
        assert ms_torch.is_inference_mode_enabled()
    assert not ms_torch.is_inference_mode_enabled()

@SKIP_ENV_GRAPH_MODE(reason="inference_mode not support graph mode")
def test_inference_mode_decorator():
    for mode in (True, False):
        @ms_torch.inference_mode(mode)
        def ms_func(x):
            assert ms_torch.is_inference_mode_enabled() == mode
            return x * x

        x = ms_torch.tensor(2., requires_grad=True).to(ms_torch.float32)
        ms_result = ms.ops.grad(ms_func)(x)

        @torch.inference_mode(mode)
        def torch_func(x):
            assert torch.is_inference_mode_enabled() == mode
            return x * x

        x = torch.tensor(2., requires_grad=True).to(torch.float32)
        y = torch_func(x)

        if not mode:
            y.backward()
            pt_result = x.grad
            param_compare(ms_result, pt_result)
        else:
            param_compare(ms_result, ms.ops.zeros_like(ms_result))

if __name__ == '__main__':
    set_mode_by_env_config()
    test_no_grad()
    test_enbale_grad_func()
    test_set_grad_enable_func()
    test_detach_()
    test_parameter_data_grad()
    test_is_grad_enable()
    test_is_grad_enable_nested()
    test_inference_mode_context_manager()
    test_inference_mode_decorator()
