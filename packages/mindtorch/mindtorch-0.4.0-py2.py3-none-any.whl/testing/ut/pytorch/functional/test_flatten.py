#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_flatten1():
    np_1 = np.ones((2,3,4,5)).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.flatten(ms_tensor)

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.flatten(torch_tensor)

    assert ms_result.asnumpy().shape == torch_result.numpy().shape
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), atol=1e-4)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


def test_flatten2():
    np_1 = np.ones((2,3,4,5)).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.flatten(ms_tensor, start_dim=1, end_dim=-2)

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.flatten(torch_tensor, start_dim=1, end_dim=-2)

    assert ms_result.asnumpy().shape == torch_result.numpy().shape
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), atol=1e-4)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_flatten1()
    test_flatten2()
