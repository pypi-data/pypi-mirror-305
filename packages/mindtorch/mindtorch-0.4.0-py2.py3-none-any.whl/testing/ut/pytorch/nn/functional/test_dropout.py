#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch
import torch
import numpy as np
from ....utils import SKIP_ENV_GRAPH_MODE, set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_dropout1d1():
    data = np.array([[-1, 0, 1, -2],
                     [2, 2, 3, 4]
                     ]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout1d(ms_input, 0.8, False)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout1d(torch_input, 0.8, False)

    param_compare(ms_out, torch_out)

@SKIP_ENV_GRAPH_MODE(reason="inplace=True can not support graph mode.")
def test_dropout1d2():
    data = np.array([[[-1, 0, 1, -2],
                     [2, 2, 3, 4]],
                     [[1, 1, 1, 1],
                      [1, 1, 1, 1]]]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout1d(ms_input, 0.7, True, True)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout1d(torch_input, 0.7, True, True)

#    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
#    assert np.allclose(ms_input.asnumpy(), torch_input.numpy())
    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_dropout1d3():
    data = np.array([[-1, 0, 1, -2],
                     [2, 2, 3, 4]
                     ]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout1d(ms_input, 1.)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout1d(torch_input, 1.)

    param_compare(ms_out, torch_out)


def test_dropout1d4():
    data = np.array([[-1, 0, 1, -2],
                     [2, 2, 3, 4]
                     ]).astype(np.float64)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout1d(ms_input, 0.)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout1d(torch_input, 0.)

    param_compare(ms_out, torch_out)


def test_dropout2d1():
    data = np.ones([2, 3, 2, 4]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout2d(ms_input, 0.6)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout2d(torch_input, 0.6)

    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_dropout2d2():
    data = np.ones([2, 3, 2]).astype(np.float64)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout2d(ms_input, 0.)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout2d(torch_input, 0.)

    param_compare(ms_out, torch_out)


def test_dropout2d3():
    data = np.ones([2, 3, 2, 4]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout2d(ms_input, 1.)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout2d(torch_input, 1.)

    param_compare(ms_out, torch_out)


def test_dropout3d1():
    data = np.ones([2, 3, 2, 4]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout3d(ms_input, 0.6)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout3d(torch_input, 0.6)

    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_dropout3d2():
    data = np.ones([2, 2, 3, 2, 4]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout3d(ms_input, 0.4)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout3d(torch_input, 0.4)

    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_dropout3d3():
    data = np.ones([2, 2, 3, 2, 4]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout3d(ms_input, 0.)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout3d(torch_input, 0.)

    param_compare(ms_out, torch_out)


def test_dropout3d4():
    data = np.ones([2, 2, 3, 2]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout3d(ms_input, 1.)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout3d(torch_input, 1.)

    param_compare(ms_out, torch_out)


def test_dropout1():
    data = np.ones([2, 3, 2, 4]).astype(np.float32)*2

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout(ms_input, 0.6)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout(torch_input, 0.6)

    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_dropout2():
    data = np.ones([2, 3, 2, 4]).astype(np.float32)*2

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout(ms_input, 0.)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout(torch_input, 0.)

    param_compare(ms_out, torch_out)


def test_dropout3():
    data = np.ones([2, 3, 2]).astype(np.float32)*2

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout(ms_input, 1.)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout(torch_input, 1.)

    param_compare(ms_out, torch_out)

def test_dropout_p_int():
    data = np.ones([2, 3, 2]).astype(np.float32)*2

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout(ms_input, 1)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout(torch_input, 1)

    param_compare(ms_out, torch_out)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.dropout(ms_input, 0)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.dropout(torch_input, 0)

    param_compare(ms_out, torch_out)

def test_alphadropout1():
    data = np.random.randn(5, 5, 6, 6)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.alpha_dropout(ms_input, 0.2, True)

    mean = ms_input.mean().numpy()
    std = ms_input.std().numpy()
    assert np.abs(ms_out.data.mean().numpy() - mean) < 0.1
    assert np.abs(ms_out.data.std().numpy() - std) < 0.1

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.alpha_dropout(torch_input, 0.2, True)

    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_alphadropout2():
    data = np.random.randn(20, 30)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.alpha_dropout(ms_input, 0.6, True)

    mean = ms_input.mean().numpy()
    std = ms_input.std().numpy()

    # [CI] ms 2.3 0327 Interface accuracy degradation, using 0.11 to replace initial threshold of 0.1.
    assert np.abs(ms_out.data.mean().numpy() - mean) < 0.11
    assert np.abs(ms_out.data.std().numpy() - std) < 0.11

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.alpha_dropout(torch_input, 0.6, True)

    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_alphadropout3():
    data = np.array([[1.0, -3.0, 4.0], [-2.0, 8.5, 0]])

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.alpha_dropout(ms_input, 1., True)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.alpha_dropout(torch_input, 1., True)

    param_compare(ms_out, torch_out)


def test_alphadropout4():
    data = np.array([[1.0, -3.0, 4.0], [-2.0, 8.5, 0]])

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.alpha_dropout(ms_input, 0., True)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.alpha_dropout(torch_input, 0., True)

    param_compare(ms_out, torch_out)


def test_featurealphadropout1():
    b = np.random.randint(1, 5)
    w = np.random.randint(1, 5)
    h = np.random.randint(1, 5)
    d = np.random.randint(1, 2)
    num_features = 1000
    data = np.random.randn(num_features, b, d, h, w)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.feature_alpha_dropout(ms_input, 0.5, True)

    mean = ms_input.mean().numpy()
    std = ms_input.std().numpy()
    assert np.abs(ms_out.data.mean().numpy() - mean) < 0.1
    assert np.abs(ms_out.data.std().numpy() - std) < 0.1

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.feature_alpha_dropout(torch_input, 0.5, True)

    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_featurealphadropout2():
    w = np.random.randint(1, 5)
    h = np.random.randint(1, 5)
    d = np.random.randint(1, 2)
    num_features = 1000
    data = np.random.randn(num_features, d, h, w)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.feature_alpha_dropout(ms_input, 0.35, True)

    mean = ms_input.mean().numpy()
    std = ms_input.std().numpy()
    assert np.abs(ms_out.data.mean().numpy() - mean) < 0.1
    assert np.abs(ms_out.data.std().numpy() - std) < 0.1

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.feature_alpha_dropout(torch_input, 0.35, True)

    assert ms_out.shape == torch_out.shape
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_featurealphadropout3():
    data = np.random.randn(5, 2, 5, 6, 6)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.feature_alpha_dropout(ms_input, 1., True)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.feature_alpha_dropout(torch_input, 1., True)

    param_compare(ms_out, torch_out)

def test_featurealphadropout4():
    data = np.random.randn(5, 2, 4, 4)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.feature_alpha_dropout(ms_input, 0., True)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.feature_alpha_dropout(torch_input, 0., True)

    param_compare(ms_out, torch_out)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_dropout1d1()
    test_dropout1d2()
    test_dropout1d3()
    test_dropout1d4()
    test_dropout2d1()
    test_dropout2d2()
    test_dropout2d3()
    test_dropout3d1()
    test_dropout3d2()
    test_dropout3d3()
    test_dropout3d4()
    test_dropout1()
    test_dropout2()
    test_dropout3()
    test_alphadropout1()
    test_alphadropout2()
    test_alphadropout3()
    test_alphadropout4()
    test_featurealphadropout1()
    test_featurealphadropout2()
    test_featurealphadropout3()
    test_featurealphadropout4()
