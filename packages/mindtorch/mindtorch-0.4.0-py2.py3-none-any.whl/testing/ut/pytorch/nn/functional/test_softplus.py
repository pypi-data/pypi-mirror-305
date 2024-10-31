#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, SKIP_ENV_ASCEND
set_mode_by_env_config()


def test_softplus1():
    data = np.array([[-1, 0, 2, 3, 4, 7]],).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.softplus(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.softplus(ms_input)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_softplus2():
    data = np.array([[-1, 0, 2, 3, 4, 7]],).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.softplus(torch_input, beta=5.2, threshold=16.5)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.softplus(ms_input, beta=5.2, threshold=16.5)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_softplus3():
    data = np.array([[-1, 0, 2, 19.9, 20, 21]],).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.softplus(torch_input, beta=1, threshold=20)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.softplus(ms_input, beta=1, threshold=20)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_ASCEND(reason='softplus not support float64 input on Ascend')
def test_softplus4():
    data = np.random.randn(2, 3)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.softplus(torch_input, beta=0.5, threshold=20)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.softplus(ms_input, beta=0.5, threshold=20)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_softplus1()
    test_softplus2()
    test_softplus3()
    test_softplus4()
