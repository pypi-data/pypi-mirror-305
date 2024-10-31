#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import SKIP_ENV_ASCEND, SKIP_ENV_GPU, set_mode_by_env_config

set_mode_by_env_config()

@SKIP_ENV_GPU(reason='upsample not support input dtype as float64')
@SKIP_ENV_ASCEND(reason='upsample not support input dtype as float64')
def test_upsample1_float64():
    np_1 = np.random.randn(2, 3, 4, 5)

    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.nn.functional.upsample(ms_tensor, (3, 3))

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.nn.functional.upsample(torch_tensor, (3, 3))

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_upsample1_float32():
    np_1 = np.random.randn(2, 3, 4, 5).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.nn.functional.upsample(ms_tensor, (3, 3))

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.nn.functional.upsample(torch_tensor, (3, 3))

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

@SKIP_ENV_ASCEND(reason='upsample not support input dtype as float64')
def test_upsample2_float64():
    np_1 = np.random.randn(2, 3, 4)

    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.nn.functional.upsample(ms_tensor, 6, align_corners=True, mode='linear')

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.nn.functional.upsample(torch_tensor, 6, align_corners=True, mode='linear')

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_upsample2_float32():
    np_1 = np.random.randn(2, 3, 4).astype(np.float32)

    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.nn.functional.upsample(ms_tensor, 6, align_corners=True, mode='linear')

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.nn.functional.upsample(torch_tensor, 6, align_corners=True, mode='linear')

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), atol=2e-5)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype


# TODO: default is 'align_corners=False', which is not supported on CPU right now.
'''
def test_upsample3():
    np_1 = np.random.randn(2, 3, 4, 5).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.nn.functional.upsample(ms_tensor, (5, 5), mode='bilinear')

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.nn.functional.upsample(torch_tensor, (5, 5), mode='bilinear')

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy(), atol=1e-1)
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype
'''

if __name__ == '__main__':
    set_mode_by_env_config()
    test_upsample1_float64()
    test_upsample1_float32()
    test_upsample2_float64()
    test_upsample2_float32()
    #test_upsample3()
