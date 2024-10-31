#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_reshape1():
    input = np.array([1,2,3,4])

    ms_tensor = ms_torch.tensor(input)
    ms_result = ms_torch.reshape(ms_tensor, [2,2])

    torch_tensor = torch.tensor(input)
    torch_result = torch.reshape(torch_tensor, [2,2])

    assert ms_result.asnumpy().shape == torch_result.numpy().shape
    assert np.allclose(ms_result.numpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_reshape2():
    input = np.array([1,2,3,4])

    ms_tensor = ms_torch.tensor(input)
    ms_result = ms_torch.reshape(ms_tensor, [-1,])

    torch_tensor = torch.tensor(input)
    torch_result = torch.reshape(torch_tensor, [-1,])

    assert ms_result.asnumpy().shape == torch_result.numpy().shape
    assert np.allclose(ms_result.numpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


if __name__ == '__main__':
    set_mode_by_env_config()
    test_reshape1()
    test_reshape2()