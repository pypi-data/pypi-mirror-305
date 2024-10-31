#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import torch

from mindspore import context
import mindspore as ms

import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_layer_norm1():
    batch, sentence_length, embedding_dim = 20, 5, 10
    data = np.random.randn(batch, sentence_length, embedding_dim).astype(np.float32)

    torch_embedding = torch.tensor(data)
    torch_layer_norm = torch.nn.LayerNorm(embedding_dim)
    torch_output = torch_layer_norm(torch_embedding)

    ms_torch_embedding = ms_torch.tensor(data)
    ms_torch_layer_norm = ms_torch.nn.LayerNorm(embedding_dim)
    ms_torch_output = ms_torch_layer_norm(ms_torch_embedding)

    assert np.allclose(ms_torch_output.asnumpy(), torch_output.detach().numpy(), atol=1e-3)

def test_layer_norm2():
    N, C, H, W = 20, 5, 10, 10

    data = np.random.randn(N, C, H, W).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_layer_norm = torch.nn.LayerNorm([C, H, W])
    torch_output = torch_layer_norm(torch_input)

    ms_torch_input = ms_torch.tensor(data)
    ms_torch_layer_norm = ms_torch.nn.LayerNorm([C, H, W])
    ms_torch_output = ms_torch_layer_norm(ms_torch_input)

    assert np.allclose(ms_torch_output.asnumpy(), torch_output.detach().numpy(), atol=1e-5)


def test_group_norm1():
    N, C, H, W = 2, 5, 2, 2

    data = np.random.randn(N, C, H, W).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_layer_norm = torch.nn.GroupNorm(num_groups=5, num_channels=5)
    torch_output = torch_layer_norm(torch_input)

    ms_torch_input = ms_torch.tensor(data)
    ms_torch_layer_norm = ms_torch.nn.GroupNorm(num_groups=5, num_channels=5)
    ms_torch_output = ms_torch_layer_norm(ms_torch_input)

    assert np.allclose(ms_torch_output.asnumpy(), torch_output.detach().numpy(), atol=1e-5)


def test_group_norm2():
    N, C, H, W = 2, 10, 2, 2

    data = np.random.randn(N, C, H, W).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_layer_norm = torch.nn.GroupNorm(num_groups=5, num_channels=10, affine=False)
    torch_output = torch_layer_norm(torch_input)

    ms_torch_input = ms_torch.tensor(data)
    ms_torch_layer_norm = ms_torch.nn.GroupNorm(num_groups=5, num_channels=10, affine=False)
    ms_torch_output = ms_torch_layer_norm(ms_torch_input)

    assert np.allclose(ms_torch_output.asnumpy(), torch_output.detach().numpy(), atol=1e-5)

def test_group_norm_input_5D():
    N, C, D, H, W = 2, 4, 3, 3, 3

    data = np.random.randn(N, C, D, H, W).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_layer_norm = torch.nn.GroupNorm(num_groups=2, num_channels=4, affine=False)
    torch_output = torch_layer_norm(torch_input)

    ms_torch_input = ms_torch.tensor(data)
    ms_torch_layer_norm = ms_torch.nn.GroupNorm(num_groups=2, num_channels=4, affine=False)
    ms_torch_output = ms_torch_layer_norm(ms_torch_input)

    assert np.allclose(ms_torch_output.asnumpy(), torch_output.detach().numpy(), atol=1e-5)

def test_group_norm_input_5D_affine_True():
    N, C, D, H, W = 2, 4, 3, 3, 3

    data = np.random.randn(N, C, D, H, W).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_layer_norm = torch.nn.GroupNorm(num_groups=2, num_channels=4)
    torch_output = torch_layer_norm(torch_input)

    ms_torch_input = ms_torch.tensor(data)
    ms_torch_layer_norm = ms_torch.nn.GroupNorm(num_groups=2, num_channels=4)
    ms_torch_output = ms_torch_layer_norm(ms_torch_input)

    assert np.allclose(ms_torch_output.asnumpy(), torch_output.detach().numpy(), atol=1e-5)


def test_local_response_norm1():
    data = np.random.random((4, 4, 4)).astype(np.float32)*10

    ms_input = ms_torch.tensor(data)
    ms_torch_layer_norm = ms_torch.nn.LocalResponseNorm(size=3, alpha=0.01)
    ms_out = ms_torch_layer_norm(ms_input)

    torch_input = torch.tensor(data)
    torch_layer_norm = torch.nn.LocalResponseNorm(size=3, alpha=0.01)
    torch_out = torch_layer_norm(torch_input)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_local_response_norm2():
    data = np.random.random((2, 4, 4, 3, 2)).astype(np.float32)*10

    ms_input = ms_torch.tensor(data)
    ms_torch_layer_norm = ms_torch.nn.LocalResponseNorm(3, 0.01)
    ms_out = ms_torch_layer_norm(ms_input)

    torch_input = torch.tensor(data)
    torch_layer_norm = torch.nn.LocalResponseNorm(3, 0.01)
    torch_out = torch_layer_norm(torch_input)

    if ms.get_context('device_target') == 'Ascend':
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), rtol=1e-3, atol=1e-5)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


if __name__ == '__main__':
    set_mode_by_env_config()
    test_layer_norm1()
    test_layer_norm2()

    test_group_norm1()
    test_group_norm2()

    test_local_response_norm1()
    test_local_response_norm2()

    test_group_norm_input_5D()
    test_group_norm_input_5D_affine_True()
