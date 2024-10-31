import torch
import mindtorch.torch as ms_torch
# import mindtorch.torch as ms_torch
import numpy as np
from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE, \
    graph_lax_level
import mindspore as ms
# from mindtorch.torch.tensor import cast_to_adapter_tensor
from mindtorch.torch.tensor import cast_to_adapter_tensor

set_mode_by_env_config()


def test_vjp():
    data = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x):
        return x.exp().sum(dim=1)

    inputs = ms_torch.tensor(data)
    v = ms_torch.ones(4)
    ms_out, ms_vjp_out = ms_torch.autograd.functional.vjp(exp_reducer, inputs, v)

    inputs = torch.tensor(data)
    v = torch.ones(4)
    torch_out, torch_vjp_out = torch.autograd.functional.vjp(exp_reducer, inputs, v)

    param_compare(ms_out, torch_out)
    param_compare(ms_vjp_out, torch_vjp_out)

def test_vjp_None():
    data = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x):
        return x.exp().sum()

    inputs = ms_torch.tensor(data)
    ms_out, ms_vjp_out = ms_torch.autograd.functional.vjp(exp_reducer, inputs, None)

    inputs = torch.tensor(data)
    torch_out, torch_vjp_out = torch.autograd.functional.vjp(exp_reducer, inputs, None)

    param_compare(ms_out, torch_out)
    param_compare(ms_vjp_out, torch_vjp_out)

def test_vjp_None_jit():
    data = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x):
        return x.exp().sum()

    inputs = ms_torch.tensor(data)
    @ms.jit
    def func(inputs):
        return ms_torch.autograd.functional.vjp(exp_reducer, inputs, None)
    ms_out, ms_vjp_out = func(inputs)

    inputs = torch.tensor(data)
    torch_out, torch_vjp_out = torch.autograd.functional.vjp(exp_reducer, inputs, None)

    param_compare(ms_out, torch_out)
    param_compare(ms_vjp_out, torch_vjp_out)

@SKIP_ENV_GRAPH_MODE(reason="torch result not correct")
@SKIP_ENV_PYNATIVE_MODE(reason="torch result not correct")
def test_vjp_vjp():
    data = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x):
        return x.sum(1)

    inputs = torch.tensor(data)
    v = torch.ones(4)
    _, torch_vjp_out = torch.autograd.functional.vjp(exp_reducer, inputs, v, create_graph=True)
    _, pt_out = torch.autograd.functional.vjp(exp_reducer, torch_vjp_out, v)

    inputs = ms_torch.tensor(data)
    v = ms_torch.ones(4)
    def exp_reducer_wrap(inputs):
        _, ms_vjp_out = ms_torch.autograd.functional.vjp(exp_reducer, inputs, v, create_graph=True)
        return exp_reducer(ms_vjp_out)
    
    _, ms_vjp_out = ms_torch.autograd.functional.vjp(exp_reducer_wrap, inputs, v)

    param_compare(pt_out, ms_vjp_out)


def test_vjp_2_input():
    data1 = np.random.randn(4, 4).astype(np.float32)
    data2 = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x1, x2):
        return x1.exp().sum(dim=1) + x2.exp().sum(dim=1)

    inputs = (torch.tensor(data1), torch.tensor(data2))
    v = torch.ones(4)
    torch_out, torch_vjp_out = torch.autograd.functional.vjp(exp_reducer, inputs, v)

    inputs = (ms_torch.tensor(data1), ms_torch.tensor(data2))
    v = ms_torch.ones(4)
    ms_out, ms_vjp_out = ms_torch.autograd.functional.vjp(exp_reducer, inputs, v)

    param_compare(ms_out, torch_out)
    param_compare(ms_vjp_out, torch_vjp_out)


def test_vjp_2_output():
    data1 = np.random.randn(4, 4).astype(np.float32)
    data2 = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x1, x2):
        return x1.exp().sum(dim=1), x2.exp().sum(dim=1)

    inputs = (torch.tensor(data1), torch.tensor(data2))
    v = (torch.ones(4), torch.ones(4))
    torch_out, torch_vjp_out = torch.autograd.functional.vjp(exp_reducer, inputs, v)

    inputs = (ms_torch.tensor(data1), ms_torch.tensor(data2))
    v = (ms_torch.ones(4), ms_torch.ones(4))
    ms_out, ms_vjp_out = ms_torch.autograd.functional.vjp(exp_reducer, inputs, v)

    param_compare(ms_out, torch_out)
    param_compare(ms_vjp_out, torch_vjp_out)

def test_jvp():
    data = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x):
        return x.exp().sum(dim=1)

    inputs = ms_torch.tensor(data)
    v = ms_torch.ones(4, 4)
    ms_out, ms_jvp_out = ms_torch.autograd.functional.jvp(exp_reducer, inputs, v)

    inputs = torch.tensor(data)
    v = torch.ones(4, 4)
    torch_out, torch_jvp_out = torch.autograd.functional.jvp(exp_reducer, inputs, v)

    param_compare(ms_out, torch_out)
    param_compare(ms_jvp_out, torch_jvp_out)

def test_jvp_jit():
    data = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x):
        return x.exp().sum(dim=1)

    inputs = ms_torch.tensor(data)
    v = ms_torch.ones(4, 4)
    @ms.jit
    def func(inputs, v):
        return ms_torch.autograd.functional.jvp(exp_reducer, inputs, v)
    ms_out, ms_jvp_out = func(inputs, v)

    inputs = torch.tensor(data)
    v = torch.ones(4, 4)
    torch_out, torch_jvp_out = torch.autograd.functional.jvp(exp_reducer, inputs, v)

    param_compare(ms_out, torch_out)
    param_compare(ms_jvp_out, torch_jvp_out)

def test_jvp_v_None():
    data = np.random.randn(1).astype(np.float32)

    def exp_reducer(x):
        return x.exp().sum()

    inputs = ms_torch.tensor(data)
    ms_out, ms_jvp_out = ms_torch.autograd.functional.jvp(exp_reducer, inputs, None)

    inputs = torch.tensor(data)
    torch_out, torch_jvp_out = torch.autograd.functional.jvp(exp_reducer, inputs, None)

    param_compare(ms_out, torch_out)
    param_compare(ms_jvp_out, torch_jvp_out)

def test_jvp_2_input():
    data1 = np.random.randn(4, 4).astype(np.float32)
    data2 = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x1, x2):
        return x1.exp().sum(dim=1) + x2.exp().sum(dim=1)

    inputs = (torch.tensor(data1), torch.tensor(data2))
    v = torch.ones(4, 4)
    torch_out, torch_vjp_out = torch.autograd.functional.jvp(exp_reducer, inputs, (v, v))

    inputs = (ms_torch.tensor(data1), ms_torch.tensor(data2))
    v = ms_torch.ones(4, 4)
    ms_out, ms_vjp_out = ms_torch.autograd.functional.jvp(exp_reducer, inputs, (v, v))

    param_compare(ms_out, torch_out)
    param_compare(ms_vjp_out, torch_vjp_out)

def test_jvp_2_output():
    data1 = np.random.randn(4, 4).astype(np.float32)
    data2 = np.random.randn(4, 4).astype(np.float32)

    def exp_reducer(x1, x2):
        return x1.exp().sum(dim=1), x2.exp().sum(dim=1)

    inputs = (torch.tensor(data1), torch.tensor(data2))
    v = (torch.ones(4, 4), torch.ones(4, 4))
    torch_out, torch_jvp_out = torch.autograd.functional.jvp(exp_reducer, inputs, v)

    inputs = (ms_torch.tensor(data1), ms_torch.tensor(data2))
    v = (ms_torch.ones(4, 4), ms_torch.ones(4, 4))
    ms_out, ms_jvp_out = ms_torch.autograd.functional.jvp(exp_reducer, inputs, v)

    param_compare(ms_out, torch_out)
    param_compare(ms_jvp_out, torch_jvp_out)

def test_jacobian_reverse_mode():
    data1 = np.random.randn(2, 2).astype(np.float32)
    data2 = np.random.randn(2, 2).astype(np.float32)

    def exp_reducer(x, x2):
        return x.exp().mean(1) + x2.exp().mean(1)

    inputs1 = torch.tensor(data1, requires_grad=True)
    inputs2 = torch.tensor(data2, requires_grad=True)
    pt_j1, pt_j2 = torch.autograd.functional.jacobian(exp_reducer, (inputs1, inputs2))

    inputs1 = ms_torch.tensor(data1, requires_grad=True)
    inputs2 = ms_torch.tensor(data2, requires_grad=True)

    ms_j1, ms_j2 = ms_torch.autograd.functional.jacobian(exp_reducer, (inputs1, inputs2))

    param_compare(pt_j1, ms_j1)
    param_compare(pt_j2, ms_j2)

def test_jacobian_reverse_mode_2_input_2_output():
    data1 = np.random.randn(2, 2).astype(np.float32)
    data2 = np.random.randn(2, 2).astype(np.float32)

    def exp_reducer(x, x2):
        return x.exp().mean(1), x2.exp().mean(1)

    inputs1 = torch.tensor(data1, requires_grad=True)
    inputs2 = torch.tensor(data2, requires_grad=True)
    pt_j1, pt_j2 = torch.autograd.functional.jacobian(exp_reducer, (inputs1, inputs2))

    inputs1 = ms_torch.tensor(data1, requires_grad=True)
    inputs2 = ms_torch.tensor(data2, requires_grad=True)

    ms_j1, ms_j2 = ms_torch.autograd.functional.jacobian(exp_reducer, (inputs1, inputs2))

    param_compare(pt_j1, ms_j1)
    param_compare(pt_j2, ms_j2)

@SKIP_ENV_GRAPH_MODE(reason="RuntimeError: The pointer[abs] is null.")
def test_jacobian_reverse_mode_jit():
    # ms.set_context(save_graphs=2, save_graphs_path='./ir')
    data1 = np.random.randn(2, 2).astype(np.float32)
    data2 = np.random.randn(2, 2).astype(np.float32)

    def exp_reducer(x, x2):
        return x.exp().mean(1) + x2.exp().mean(1)

    inputs1 = torch.tensor(data1, requires_grad=True)
    inputs2 = torch.tensor(data2, requires_grad=True)
    pt_j1, pt_j2 = torch.autograd.functional.jacobian(exp_reducer, (inputs1, inputs2))

    inputs1 = ms_torch.tensor(data1, requires_grad=True)
    inputs2 = ms_torch.tensor(data2, requires_grad=True)

    @ms.jit
    def func(inputs):
        return ms_torch.autograd.functional.jacobian(exp_reducer, inputs)
    ms_j1, ms_j2 = func((inputs1, inputs2))

    param_compare(pt_j1, ms_j1)
    param_compare(pt_j2, ms_j2)

def test_jacobian_forward_mode():
    data1 = np.random.randn(2, 2).astype(np.float32)
    data2 = np.random.randn(2, 2).astype(np.float32)

    def exp_reducer(x, x2):
        return x.exp().mean(1) + x2.exp().mean(1)

    inputs1 = torch.tensor(data1, requires_grad=True)
    inputs2 = torch.tensor(data2, requires_grad=True)
    pt_j1, pt_j2 = torch.autograd.functional.jacobian(
        exp_reducer, (inputs1, inputs2), vectorize=True, strategy="forward-mode")

    inputs1 = ms_torch.tensor(data1, requires_grad=True)
    inputs2 = ms_torch.tensor(data2, requires_grad=True)

    ms_j1, ms_j2 = ms_torch.autograd.functional.jacobian(
        exp_reducer, (inputs1, inputs2), vectorize=True, strategy="forward-mode")

    param_compare(pt_j1.detach(), ms_j1)
    param_compare(pt_j2.detach(), ms_j2)

@SKIP_ENV_GRAPH_MODE(reason="second_grad compile raise 'The pointer[abs] is null'")
def test_jacobian_second_grad():
    data1 = np.random.randn(2, 2).astype(np.float32)
    data2 = np.random.randn(2, 2).astype(np.float32)

    def exp_reducer(x, x2):
        return x.exp().mean(1) + x2.exp().mean(1)

    inputs1 = torch.tensor(data1, requires_grad=True)
    inputs2 = torch.tensor(data2, requires_grad=True)
    pt_j1, pt_j2 = torch.autograd.functional.jacobian(exp_reducer, (inputs1, inputs2), create_graph=True)
    pt_j1 = pt_j1.sum()
    pt_j2 = pt_j2.sum()
    pt_j1.backward()
    pt_j2.backward()
    pt_grads1 = inputs1.grad
    pt_grads2 = inputs2.grad

    inputs1 = ms_torch.tensor(data1, requires_grad=True)
    inputs2 = ms_torch.tensor(data2, requires_grad=True)

    def func(input1, input2):
        ms_j1, ms_j2 = ms_torch.autograd.functional.jacobian(exp_reducer, (input1, input2))
        return ms_j1.sum(), ms_j2.sum()
    ms_grad1, ms_grad2 = ms.ops.grad(func, grad_position=(0, 1))(inputs1, inputs2)

    param_compare(pt_grads1, ms_grad1)
    param_compare(pt_grads2, ms_grad2)


if __name__ == '__main__':
    test_vjp()
    test_vjp_vjp()
    test_vjp_None()
    test_vjp_2_input()
    test_vjp_2_output()
    test_vjp_None_jit()
    test_jvp()
    test_jvp_v_None()
    test_jvp_2_input()
    test_jvp_2_output()
    test_jvp_jit()
    test_jacobian_reverse_mode()
    test_jacobian_second_grad()
    test_jacobian_forward_mode()
    test_jacobian_reverse_mode_jit()
