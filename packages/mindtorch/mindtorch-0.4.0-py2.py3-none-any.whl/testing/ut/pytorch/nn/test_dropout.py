#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch
from mindtorch.torch import tensor

from mindspore import context
import mindspore as ms
import numpy as np
import torch
from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, param_compare, enable_backward
set_mode_by_env_config()



def _get_error_with_count_nonzero(ms_tensor, torch_tensor):
    nonzero_ms_output = np.count_nonzero(ms_tensor.asnumpy())
    nonzero_torch_output = np.count_nonzero(torch_tensor.numpy())
    if nonzero_ms_output > nonzero_torch_output:
        error = nonzero_ms_output - nonzero_torch_output
    else:
        error = nonzero_torch_output - nonzero_ms_output
    return error

def test_dropout_compare1():
    input = np.random.random((5, 5)).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.Dropout(p=0.5)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.Dropout(p=0.5)
    ms_output = ms_dropout(ms_tensor)

    error = _get_error_with_count_nonzero(ms_output, torch_output)
    kErrorThreshold = 5
    # assert error < kErrorThreshold

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_dropout_compare2():
    input = np.random.random((5, 5)).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.Dropout(p=0.2, inplace=True)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.Dropout(p=0.2, inplace=True)
    ms_output = ms_dropout(ms_tensor)

    error_input = _get_error_with_count_nonzero(ms_tensor, torch_tensor)
    error_output = _get_error_with_count_nonzero(ms_output, torch_output)
    kErrorThreshold = 5
    assert error_input == error_output
    # assert error_output < kErrorThreshold


def test_dropout2d_compare1():
    input = np.random.random((2, 25, 1, 1)).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.Dropout2d(p=0.5)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.Dropout2d(p=0.5)
    ms_output = ms_dropout(ms_tensor)

    error = _get_error_with_count_nonzero(ms_output, torch_output)
    kErrorThreshold = 10
    # assert error < kErrorThreshold

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_dropout2d_compare2():
    input = np.random.random((2, 25, 1, 1)).astype(np.float32)
    torch_tensor = torch.tensor(input)
    ms_tensor = tensor(input)

    torch_dropout = torch.nn.Dropout2d(p=0.5, inplace=True)
    torch_output = torch_dropout(torch_tensor)

    ms_dropout = mindtorch.torch.nn.Dropout2d(p=0.5, inplace=True)
    ms_output = ms_dropout(ms_tensor)

    error_input = _get_error_with_count_nonzero(ms_tensor, torch_tensor)
    error_output = _get_error_with_count_nonzero(ms_output, torch_output)
    kErrorThreshold = 10
    assert error_input == error_output
    # assert error_output < kErrorThreshold


def test_dropout3d_compare1():
    input = np.random.random((2, 25, 1, 1, 1)).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.Dropout3d(p=0.5)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.Dropout3d(p=0.5)
    ms_output = ms_dropout(ms_tensor)

    error = _get_error_with_count_nonzero(ms_output, torch_output)
    kErrorThreshold = 10
    # assert error < kErrorThreshold

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_dropout3d_compare2():
    input = np.random.random((2, 25, 1, 1, 1)).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.Dropout3d(inplace=True)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.Dropout3d(inplace=True)
    ms_output = ms_dropout(ms_tensor)

    error_input = _get_error_with_count_nonzero(ms_tensor, torch_tensor)
    error_output = _get_error_with_count_nonzero(ms_output, torch_output)
    kErrorThreshold = 10
    assert error_input == error_output
    # assert error_output < kErrorThreshold

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_alphadropout1():
    input = np.random.random([2, 3, 2, 4]).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.AlphaDropout(p=0.4, inplace=True)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.AlphaDropout(p=0.4, inplace=True)
    ms_output = ms_dropout(ms_tensor)

    assert np.allclose(ms_tensor.asnumpy(), ms_output.numpy())

def test_alphadropout2():
    input = np.random.random([2, 3, 2, 4]).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.AlphaDropout(p=0.4)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.AlphaDropout(p=0.4)
    ms_output = ms_dropout(ms_tensor)

    assert torch_output.shape == ms_output.shape

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_featurealphadropout1():
    input = np.random.random([2, 3, 2, 4]).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.FeatureAlphaDropout(p=0.4, inplace=True)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.FeatureAlphaDropout(p=0.4, inplace=True)
    ms_output = ms_dropout(ms_tensor)

    assert np.allclose(ms_tensor.asnumpy(), ms_output.numpy())

def test_featurealphadropout2():
    input = np.random.random([2, 3, 2, 4]).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.FeatureAlphaDropout(p=0.4)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.FeatureAlphaDropout(p=0.4)
    ms_output = ms_dropout(ms_tensor)

    assert torch_output.shape == ms_output.shape

@SKIP_ENV_GRAPH_MODE(reason="inpalce=True only support on pynative mode.")
def test_dropout1d():
    input = np.random.random([2, 3, 4]).astype(np.float32)
    torch_tensor = torch.tensor(input)
    torch_dropout = torch.nn.Dropout1d(p=0.4, inplace=True)
    torch_output = torch_dropout(torch_tensor)

    ms_tensor = tensor(input)
    ms_dropout = mindtorch.torch.nn.Dropout1d(p=0.4, inplace=True)
    ms_output = ms_dropout(ms_tensor)

    assert np.allclose(ms_tensor.asnumpy(), ms_output.numpy())


# TODO: The functions of the new differential scheme need to be adapted, does not support op with multiple outputs.
# def test_dropout_grad():
#     with enable_backward():
#         input = np.random.random([2, 3, 4]).astype(np.float32)
#         torch_tensor = torch.tensor(input).requires_grad_()
#         torch_dropout = torch.nn.Dropout(p=0.4)
#         torch_output = torch_dropout(torch_tensor)
#         torch_output.sum().backward()
#
#         ms_tensor = mindtorch.torch.tensor(input).requires_grad_()
#         ms_dropout = mindtorch.torch.nn.Dropout(p=0.4)
#         ms_output = ms_dropout(ms_tensor)
#         ms_output.sum().backward()
#
#         assert torch_tensor.grad.size() == ms_tensor.grad.size()


if __name__ == '__main__':
    set_mode_by_env_config()
    test_dropout_compare1()
    test_dropout_compare2()
    test_dropout2d_compare1()
    test_dropout2d_compare2()
    test_dropout3d_compare1()
    test_dropout3d_compare2()
    test_alphadropout1()
    test_alphadropout2()
    test_featurealphadropout1()
    test_featurealphadropout2()
    test_dropout1d()
    test_dropout_grad()
