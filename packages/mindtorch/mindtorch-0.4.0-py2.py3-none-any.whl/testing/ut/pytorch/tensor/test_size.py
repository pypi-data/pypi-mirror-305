import numpy as np
import mindspore as ms
import torch
from mindspore import context
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, TestNet, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()

def test_tensor_size():
    ms_tensor_1 = ms_torch.Tensor(2, 3)
    assert str(ms_tensor_1.size()) == "mindtorch.Size([2, 3])"

    ms_tensor_2 = ms_torch.Tensor(ms_tensor_1.size())

    torch_tensor_1 = torch.Tensor(2, 3)
    torch_tensor_2 = torch.Tensor(torch_tensor_1.size())

    assert ms_tensor_2.numpy().shape == torch_tensor_2.numpy().shape

def test_tensor_size_mul():
    ms_tensor_1 = ms_torch.Tensor(2, 3, 4)
    torch_tensor_1 = torch.Tensor(2, 3, 4)

    assert ms_tensor_1.size().numel() == torch_tensor_1.size().numel()
    assert ms_tensor_1.size() * 2 == torch_tensor_1.size() * 2

def test_parameter_size():
    ms_tensor = ms_torch.Tensor(2, 3)
    ms_param = ms_torch.nn.Parameter(ms_tensor)
    assert str(ms_param.size()) == "mindtorch.Size([2, 3])"

def test_size_reshape():
    ms_tensor_1 = ms_torch.Tensor(2, 1, 3)
    ms_tensor_2 = ms_torch.Tensor(2, 3)
    output = ms_tensor_2.reshape(ms_tensor_1.size())
    assert str(output.size()) == "mindtorch.Size([2, 1, 3])"

@SKIP_ENV_GRAPH_MODE(reason="The custom Size will still be recognized as a tuple in graph mode.")
def test_size_value():
    def size_func(x):
        shape = x.size()
        x = ms_torch.Tensor(shape)
        return x

    msa_net = TestNet(size_func)
    ms_tensor = ms_torch.Tensor(2, 3)
    output = msa_net(ms_tensor)
    assert str(output.size()) == "mindtorch.Size([2, 3])"

if __name__ == '__main__':
    set_mode_by_env_config()
    test_tensor_size()
    test_tensor_size_mul()
    test_parameter_size()
    test_size_reshape()
    test_size_value()
