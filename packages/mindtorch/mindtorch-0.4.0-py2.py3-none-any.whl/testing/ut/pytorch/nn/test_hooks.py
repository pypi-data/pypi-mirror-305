import math
import torch
import numpy as np
import mindspore as ms
import mindtorch.torch as ms_torch
from mindtorch.torch import nn
from mindtorch.torch.tensor import Tensor as adapter_tenosr
from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, param_compare, SKIP_ENV_PYNATIVE_MODE
set_mode_by_env_config()

@SKIP_ENV_PYNATIVE_MODE(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
@SKIP_ENV_GRAPH_MODE(reason="register hooks not supported in GRAPH_MODE")
def test_hooks():
    module = nn.Sigmoid()
    input = ms_torch.ones(5, 5)
    module.set_grad()

    counter = {
        'forwards': 0,
        'backwards': 0
    }

    def fw_hook(inc, h_module, input, output):
        assert isinstance(input, tuple)
        assert isinstance(output, adapter_tenosr)
        assert h_module is module
        np.allclose(input[0].numpy(), ms_torch.ones(5, 5).numpy())
        np.allclose(output.numpy(), ms_torch.full((5, 5), 1 / (1 + 1 / math.e)).numpy())
        counter['forwards'] += inc

    def bw_hook(inc, h_module, grad_input, grad_output):
        assert isinstance(grad_input, tuple)
        # TODO: grad_output is tuple
        assert isinstance(grad_output[0], adapter_tenosr)
        # TODO:
        # assert h_module is module
        np.allclose(grad_output[0].numpy(), (ms_torch.ones(5, 5) * 2).numpy())
        counter['backwards'] += inc

    test_fwd = module.register_forward_hook(lambda *args: fw_hook(1, *args))

    module(input)
    module(input)
    assert counter['forwards'] == 2
    assert counter['backwards'] == 0

    test_bwd = module.register_backward_hook(lambda *args: bw_hook(1, *args))

    module(input)
    assert counter['forwards'] == 3
    assert counter['backwards'] == 0

    grad_all = ms.ops.GradOperation(get_all=True, sens_param=True)
    grad_fn = grad_all(module)

    _ = grad_fn(input, ms_torch.ones(5, 5) * 2)
    assert counter['forwards'] == 3
    assert counter['backwards'] == 1

    # TODO: ms bwd hook has bug when finding higher-order derivative
    # _ = grad_fn(input, ms_torch.ones(5, 5) * 2)
    # assert counter['forwards'] == 3
    # assert counter['backwards'] == 2

@SKIP_ENV_GRAPH_MODE(reason="register hooks not supported in GRAPH_MODE")
def test_hook_forward_preforward_writable():
    input = np.random.randn(5, 5).astype(np.float32)

    def ms_forward_pre_hook(m, input):
        m.test_num1 = 1
        return nn.functional.relu(input[0])

    def torch_forward_pre_hook(m, input):
        return torch.nn.functional.relu(input[0])

    def forward_hook(m, input, output):
        m.test_num2 = 2
        return -output

    ms_module = nn.Sigmoid()
    ms_input = ms_torch.tensor(input)
    ms_module.register_forward_pre_hook(ms_forward_pre_hook)
    ms_module.register_forward_hook(forward_hook)
    ms_output = ms_module(ms_input)

    torch_module = torch.nn.Sigmoid()
    torch_input = torch.tensor(input, requires_grad=True)
    torch_module.register_forward_pre_hook(torch_forward_pre_hook)
    torch_module.register_forward_hook(forward_hook)
    torch_output = torch_module(torch_input)
    assert np.allclose(ms_output.numpy(), torch_output.detach().numpy(), rtol=1e-6, atol=1e-6)

    grad_all = ms.ops.GradOperation(get_all=True, sens_param=True)
    grad_fn = grad_all(ms_module)
    gradient = grad_fn(ms_input, ms.ops.ones((5, 5)) * 2)
    torch_output.backward(torch.ones(5, 5) * 2, retain_graph=True)
    assert np.allclose(gradient[0].numpy(), torch_input.grad.numpy())

    # test if forward hooks successfully modified module
    assert ms_module.test_num1 == 1
    assert ms_module.test_num2 == 2

@SKIP_ENV_GRAPH_MODE(reason="register hooks not supported in GRAPH_MODE")
def test_module_preforward_hook_removable():
    """
    This test is to test when multiple pre-forward hook functions can be
    registered successfully and used correctly, if the handle can be removable
    during the pre-forward hook function call.
    """
    module = nn.Sigmoid()

    def removable_hook(m, input):
        return input

    def removable_hook_2(m, input):
        return input

    handle = module.register_forward_pre_hook(removable_hook)
    handle_2 = module.register_forward_pre_hook(removable_hook_2)

    # make sure hook register is successful
    assert handle.id in module._forward_pre_hooks
    assert handle_2.id in module._forward_pre_hooks
    assert len(module._forward_pre_hooks) == 2

    input = ms_torch.randn(2, 2)
    output = module(input)
    assert np.allclose(ms_torch.sigmoid(input).numpy(), output.numpy())

    handle.remove()
    handle_2.remove()

    # make sure hook removal is successful
    assert handle.id not in module._forward_pre_hooks
    assert handle_2.id not in module._forward_pre_hooks
    assert len(module._forward_pre_hooks) == 0

@SKIP_ENV_GRAPH_MODE(reason="register hooks not supported in GRAPH_MODE")
def test_module_forward_hook_removable():
    """
    This test is to test when multiple pre-forward hook functions can be
    registered successfully and used correctly, if the handle can be removable
    during the pre-forward hook function call.
    """
    module = nn.Sigmoid()

    def removable_hook(m, input, output):
        return output

    def removable_hook_2(m, input, output):
        return output

    handle = module.register_forward_hook(removable_hook)
    handle_2 = module.register_forward_hook(removable_hook_2)

    # make sure hook register is successful
    assert handle.id in module._forward_hooks
    assert handle_2.id in module._forward_hooks
    assert len(module._forward_hooks) == 2

    input = ms_torch.randn(2, 2)
    output = module(input)
    assert np.allclose(ms_torch.sigmoid(input).numpy(), output.numpy())

    handle.remove()
    handle_2.remove()

    # make sure hook removal is successful
    assert handle.id not in module._forward_hooks
    assert handle_2.id not in module._forward_hooks
    assert len(module._forward_hooks) == 0

@SKIP_ENV_GRAPH_MODE(reason="register hooks not supported in GRAPH_MODE")
def test_hook_backward_writeable():
    input = np.random.randn(5, 5).astype(np.float32)

    def ms_bw_hook(module, grad_input, grad_output):
        for grad in grad_input:
            assert isinstance(grad, adapter_tenosr)
        for grad in grad_output:
            assert isinstance(grad, adapter_tenosr)
        return tuple(gi * 2 for gi in grad_input)

    def torch_bw_hook(module, grad_input, grad_output):
        for grad in grad_input:
            assert isinstance(grad, torch.Tensor)
        for grad in grad_output:
            assert isinstance(grad, torch.Tensor)
        return tuple(gi * 2 for gi in grad_input)

    module = ms_torch.nn.Sigmoid()
    ms_input = ms_torch.tensor(input)
    module.register_backward_hook(ms_bw_hook)

    grad_func = ms.ops.grad(module)
    gradient = grad_func(ms_input)

    torch_module = torch.nn.Sigmoid()
    torch_input = torch.tensor(input, requires_grad=True)
    torch_module.register_backward_hook(torch_bw_hook)
    torch_module(torch_input).backward(torch.ones(5, 5))
    param_compare(gradient, torch_input.grad)


@SKIP_ENV_GRAPH_MODE(reason="register hooks not supported in GRAPH_MODE")
def test_register_module_hooks():
    input = np.random.randn(5, 5).astype(np.float32)

    def forward_pre_hook(m, input):
        return tuple(item * 2 + 1 for item in input)

    def forward_hook(m, input, output):
        return -output

    def ms_bw_hook(module, grad_input, grad_output):
        for grad in grad_input:
            assert isinstance(grad, adapter_tenosr)
        for grad in grad_output:
            assert isinstance(grad, adapter_tenosr)
        return tuple(gi * 2 for gi in grad_input)

    def torch_bw_hook(module, grad_input, grad_output):
        for grad in grad_input:
            assert isinstance(grad, torch.Tensor)
        for grad in grad_output:
            assert isinstance(grad, torch.Tensor)
        return tuple(gi * 2 for gi in grad_input)

    module = ms_torch.nn.Sigmoid()
    ms_input = ms_torch.tensor(input)
    ms_forward_pre_hook_handle = ms_torch.nn.modules.module.register_module_forward_pre_hook(forward_pre_hook)
    ms_forward_hook_handle = ms_torch.nn.modules.module.register_module_forward_hook(forward_hook)
    ms_bw_hook_handle = ms_torch.nn.modules.module.register_module_full_backward_hook(ms_bw_hook)

    # TODO: The functions of the new differential scheme need to be adapted, backward_hook need to be refactored.
    # ms_out = module(ms_input)
    # ms_out.backward(torch.ones(5, 5))
    ms_out, gradient = ms.ops.value_and_grad(module, grad_position=0)(ms_input)

    torch_module = torch.nn.Sigmoid()
    torch_input = torch.tensor(input, requires_grad=True)
    torch_forward_pre_hook_handle = torch.nn.modules.module.register_module_forward_pre_hook(forward_pre_hook)
    torch_forward_hook_handle = torch.nn.modules.module.register_module_forward_hook(forward_hook)
    torch_bw_hook_handle = torch.nn.modules.module.register_module_full_backward_hook(torch_bw_hook)

    torch_out = torch_module(torch_input)
    torch_out.backward(torch.ones(5, 5))

    param_compare(ms_out, torch_out.detach())
    # param_compare(ms_input.grad, torch_input.grad)
    param_compare(gradient, torch_input.grad, rtol=1e-6, atol=1e-6)

    ms_forward_pre_hook_handle.remove()
    ms_forward_hook_handle.remove()
    ms_bw_hook_handle.remove()
    torch_forward_pre_hook_handle.remove()
    torch_forward_hook_handle.remove()
    torch_bw_hook_handle.remove()


if __name__ == '__main__':
    test_hooks()
    test_hook_forward_preforward_writable()
    test_module_preforward_hook_removable()
    test_module_forward_hook_removable()
    test_hook_backward_writeable()
    test_register_module_hooks()
