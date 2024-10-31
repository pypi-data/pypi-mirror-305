#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_sqrt1():
    np_1 = np.array([1, 2, 3])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.sqrt(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.sqrt(torch_tensor_1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_sqrt2():
    np_1 = np.array([1.0, 2.0, 3.0])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.sqrt(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.sqrt(torch_tensor_1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_sqrt3():
    np_1 = np.array([4, 9, 16])

    ms_tensor_1 = ms_torch.tensor(np_1)
    ms_result = ms_torch.sqrt(ms_tensor_1)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch.sqrt(torch_tensor_1)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_sqrt1()
    test_sqrt2()
    test_sqrt3()
