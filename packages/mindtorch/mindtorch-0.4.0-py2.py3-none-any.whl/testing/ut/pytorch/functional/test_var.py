#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import mindspore as ms
import torch
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_var_unbiased_True():
    input = np.array([[-0.8166, -1.3802, -0.3560]])
    input_pt = torch.tensor(input)
    output_pt = torch.var(input_pt, unbiased=True)

    input_ms = ms_torch.tensor(input)
    output_ms = ms_torch.var(input_ms, unbiased=True)

    assert np.allclose(output_pt.numpy(), output_ms.numpy())
    assert output_pt.numpy().dtype == output_ms.numpy().dtype


def test_var_unbiased_False():
    input = np.array([[-0.8166, -1.3802, -0.3560]])
    input_pt = torch.tensor(input, dtype=torch.float16)
    output_pt = torch.var(input_pt, unbiased=False)

    input_ms = ms_torch.tensor(input, dtype=torch.float16)
    output_ms = ms_torch.var(input_ms, unbiased=False)

    assert np.allclose(output_pt.numpy(), output_ms.numpy())
    assert output_pt.numpy().dtype == output_ms.numpy().dtype


def test_var_dim():
    input = np.random.random((3,4)).astype(np.float32)
    input_pt = torch.tensor(input)
    output_pt = torch.var(input_pt, dim=1, unbiased=True, keepdim=False)

    input_ms = ms_torch.tensor(input)
    output_ms = ms_torch.var(input_ms, dim=1, unbiased=True, keepdim=False)

    assert np.allclose(output_pt.numpy(), output_ms.numpy())


def test_var_keepdim():
    input = np.random.random((3,4)).astype(np.float32)
    input_pt = torch.tensor(input)
    output_pt = torch.var(input_pt, dim=0, unbiased=False, keepdim=True)

    input_ms = ms_torch.tensor(input)
    output_ms = ms_torch.var(input_ms, dim=0, unbiased=False, keepdim=True)

    assert np.allclose(output_pt.numpy(), output_ms.numpy())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_var_unbiased_True()
    test_var_unbiased_False()
    test_var_dim()
    test_var_keepdim()