#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import torch
import mindspore as ms
from mindspore import context
import mindtorch.torch as ms_torch
from ...utils import set_mode_by_env_config
from mindtorch.torch.autograd import Function
from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, enable_backward, param_compare

set_mode_by_env_config()

def adapter_autograd_function():
    class Net(ms_torch.nn.Module):
        def __init__(self):
            super(Net, self).__init__()

        def forward(self, x, y):
            out = ms_torch.matmul(x, y)
            return out

        # bprop: https://www.mindspore.cn/tutorials/experts/zh-CN/r1.9/network/custom_cell_reverse.html
        def bprop(self, x, y, out, dout):
            dx = x + 1
            dy = y + 1
            return dx, dy

    x = ms_torch.tensor([[0.5, 0.6, 0.4]], dtype=ms_torch.float32)
    y = ms_torch.tensor([[0.01], [0.2], [3.3]], dtype=ms_torch.float32)
    net = Net()
    out = net(x, y)
    grad_out = ms.grad(net, grad_position=(0, 1))(x, y)
    return out, grad_out


def torch_autograd_function():
    class Net(torch.autograd.Function):
        @staticmethod
        def forward(ctx, x, y):
            result = torch.matmul(x, y)
            ctx.save_for_backward(x, y)
            return result

        @staticmethod
        def backward(ctx, grad_output):
            x, y = ctx.saved_tensors
            dx = x + 1
            dy = y + 1
            return dx, dy

    x = torch.tensor([[0.5, 0.6, 0.4]], dtype=torch.float32, requires_grad=True)
    y = torch.tensor([[0.01], [0.2], [3.3]], dtype=torch.float32, requires_grad=True)
    out = Net.apply(x, y)
    out.backward()
    grad_out = x.grad, y.grad
    return out, grad_out

# TODO: backward not support custom bprop yet.
# def adapter_autograd_function_backward():
#     class Net(ms_torch.autograd.Function):
#         @staticmethod
#         def forward(ctx, x, y):
#             result = ms_torch.matmul(x, y)
#             ctx.save_for_backward(x, y)
#             return result

#         @staticmethod
#         def backward(ctx, grad_output):
#             x, y = ctx.saved_tensors
#             dx = x + 1
#             dy = y + 1
#             return dx, dy

#     x = ms_torch.tensor([[0.5, 0.6, 0.4]], dtype=ms_torch.float32, requires_grad=True)
#     y = ms_torch.tensor([[0.01], [0.2], [3.3]], dtype=ms_torch.float32, requires_grad=True)
#     with enable_backward():
#         out = Net.apply(x, y)
#         out.backward()
#     grad_out = x.grad, y.grad
#     return out, grad_out

def test_autograd_funciton():
    ms_out, ms_grad_out = adapter_autograd_function()
    pt_out, pt_grad_out = torch_autograd_function()
    assert np.allclose(ms_out.asnumpy(), pt_out.detach().numpy())
    assert np.allclose(ms_grad_out[0].asnumpy(), pt_grad_out[0].numpy())
    assert np.allclose(ms_grad_out[1].asnumpy(), pt_grad_out[1].numpy())

# TODO: backward not support custom bprop yet.
# @SKIP_ENV_GRAPH_MODE(reason="tensor.backward not support graphmode")
# def test_autograd_function_bprop_backward():
#     ms_out, ms_grad_out = adapter_autograd_function_backward()
#     pt_out, pt_grad_out = torch_autograd_function()
#     assert np.allclose(ms_out.asnumpy(), pt_out.detach().numpy())
#     assert np.allclose(ms_grad_out[0].asnumpy(), pt_grad_out[0].numpy())
#     assert np.allclose(ms_grad_out[1].asnumpy(), pt_grad_out[1].numpy())

@SKIP_ENV_GRAPH_MODE(reason="Funtion.apply not support graphmode")
def test_autograd_function_grad():
    def adapter_autograd_function_ms_grad():
        class Net(ms_torch.autograd.Function):
            @staticmethod
            def forward(ctx, x, y):
                result = ms_torch.matmul(x, y)
                ctx.save_for_backward(x, y)
                return result

            @staticmethod
            def backward(ctx, grad_output):
                x, y = ctx.saved_tensors
                dx = x + 1
                dy = y + 1
                return dx, dy

        x = ms_torch.tensor([[0.5, 0.6, 0.4]], dtype=ms_torch.float32, requires_grad=True)
        y = ms_torch.tensor([[0.01], [0.2], [3.3]], dtype=ms_torch.float32, requires_grad=True)
        def _func(a, b):
            out = Net.apply(a, b)
            return out
        out, grad_out = ms.value_and_grad(_func, grad_position=(0, 1))(x, y)
        return out, grad_out
    ms_out, ms_grad_out = adapter_autograd_function_ms_grad()
    pt_out, pt_grad_out = torch_autograd_function()
    assert np.allclose(ms_out.asnumpy(), pt_out.detach().numpy())
    assert np.allclose(ms_grad_out[0].asnumpy(), pt_grad_out[0].numpy())
    assert np.allclose(ms_grad_out[1].asnumpy(), pt_grad_out[1].numpy())

@SKIP_ENV_GRAPH_MODE(reason="Funtion.apply not support graphmode")
def test_autograd_function_grad_bias_None():
    def ms_torch_func():
        class TestFunction(ms_torch.autograd.Function):
            @staticmethod
            def forward(ctx, input1, input2, bias, has_bias):
                result = ms_torch.matmul(input1, input2)
                ctx.save_for_backward(result, bias)
                ctx.has_bias = has_bias

                if has_bias:
                    result = result + bias

                return result.sum()

            @staticmethod
            def backward(ctx, grad_outputs):
                result, bias = ctx.saved_tensors
                has_bias = ctx.has_bias
                result = grad_outputs * result
                if has_bias:
                    result = result + bias
                # TODO: not support bias gradient auto-reducesum.
                # return result + 1, result + 2, result + 3, None
                return result + 1, result + 2, (result + 3).sum(dim=1), None

        input1 = ms_torch.ones([8, 8])
        input2 = ms_torch.ones([8, 8])
        bias = ms_torch.ones([8])

        input1.requires_grad = True
        input2.requires_grad = True
        bias.requires_grad = True

        def _func(x, y, z):
            return TestFunction.apply(x, y, z, True)
        grads = ms.grad(_func, grad_position=(0, 1, 2))(input1, input2, bias)
        return grads

    def torch_fun():
        class TestFunction(torch.autograd.Function):
            @staticmethod
            def forward(ctx, input1, input2, bias, has_bias):
                result = torch.matmul(input1, input2)
                ctx.save_for_backward(result, bias)
                ctx.has_bias = has_bias

                if has_bias:
                    result = result + bias

                return result.sum()

            @staticmethod
            def backward(ctx, grad_outputs):
                result, bias = ctx.saved_tensors
                has_bias = ctx.has_bias
                result = grad_outputs * result
                if has_bias:
                    result = result + bias
                # return result + 1, result + 2, result + 3, None
                return result + 1, result + 2, (result + 3).sum(dim=1), None

        input1 = torch.ones([8, 8])
        input2 = torch.ones([8, 8])
        bias = torch.ones([8])

        input1.requires_grad = True
        input2.requires_grad = True
        bias.requires_grad = True

        def _func(x, y, z):
            return TestFunction.apply(x, y, z, True)

        res = _func(input1, input2, bias)
        res.backward()
        return input1.grad, input2.grad, bias.grad

    ms_grad = ms_torch_func()
    torch_grad = torch_fun()
    param_compare(ms_grad, torch_grad)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_autograd_funciton()
    # test_autograd_function_bprop_backward()
    test_autograd_function_grad()
    test_autograd_function_grad_bias_None()