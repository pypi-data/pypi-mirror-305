#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()


def test_cross1():
    np_1 = np.random.randn(4, 3).astype(np.float32)
    np_2 = np.random.randn(4, 3).astype(np.float32)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.cross(ms_tensor_1, ms_tensor_2)
    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.cross(torch_tensor_1, torch_tensor_2)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_cross2():
    np_1 = np.random.randn(4, 3).astype(np.int32)
    np_2 = np.random.randn(4, 3).astype(np.int32)
    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_tensor_2 = ms_torch.tensor(np_2)
    ms_result = ms_torch.cross(ms_tensor_1, ms_tensor_2)
    torch_tensor_1 = torch.tensor(np_1)
    torch_tensor_2 = torch.tensor(np_2)
    torch_result = torch.cross(torch_tensor_1, torch_tensor_2)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


if __name__ == "__main__":
    set_mode_by_env_config()
    test_cross1()
    test_cross2()
