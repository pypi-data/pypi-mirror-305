import numpy as np
import torch

from mindspore import context
import mindspore as ms

import mindtorch
from mindtorch.torch import tensor

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_flatten_pynative():
    input = np.array([[[1.2, 2.1], [2.2, 3.2], [2.0, 3.0]]]).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_flatten = torch.nn.Flatten()
    torch_output = torch_flatten(torch_tensor)

    ms_tensor = tensor(input)
    ms_flatten = mindtorch.torch.nn.Flatten()
    ms_output = ms_flatten(ms_tensor)
    assert torch_output.shape == ms_output.shape
    assert np.all(torch_output.numpy() == ms_output.asnumpy())


def test_flatten_graph():
    input = np.array([[[1.2, 2.1], [2.2, 3.2], [2.0, 3.0]]]).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_flatten = torch.nn.Flatten()
    torch_output = torch_flatten(torch_tensor)

    ms_tensor = tensor(input)
    ms_flatten = mindtorch.torch.nn.Flatten()
    ms_output = ms_flatten(ms_tensor)
    assert torch_output.shape == ms_output.shape
    assert np.all(torch_output.numpy() == ms_output.asnumpy())


def test_unflatten_pynative():
    input = np.random.randn(2, 3, 4, 5).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_flatten = torch.nn.Unflatten(1, (1, 3))
    torch_output = torch_flatten(torch_tensor)

    ms_tensor = tensor(input)
    ms_flatten = mindtorch.torch.nn.Unflatten(1, (1, 3))
    ms_output = ms_flatten(ms_tensor)
    assert torch_output.shape == ms_output.shape
    assert np.allclose(torch_output.numpy(), ms_output.asnumpy())


def test_unflatten_graph():
    input = np.random.randn(2, 3, 4, 5).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_flatten = torch.nn.Unflatten(1, (1, 3))
    torch_output = torch_flatten(torch_tensor)

    ms_tensor = tensor(input)
    ms_flatten = mindtorch.torch.nn.Unflatten(1, (1, 3))
    ms_output = ms_flatten(ms_tensor)
    assert torch_output.shape == ms_output.shape
    assert np.allclose(torch_output.numpy(), ms_output.asnumpy())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_flatten_pynative()
    test_flatten_graph()
    test_unflatten_pynative()
    test_unflatten_graph()
