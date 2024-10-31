#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_unfold():
    np_input = np.random.randn(7, 8, 9, 10)

    torch_tensor = torch.tensor(np_input)
    torch_unfold = torch.nn.Unfold((2, 3), 1, (1, 2), (2, 1))
    torch_out = torch_unfold(torch_tensor)

    ms_tensor = ms_torch.tensor(np_input)
    ms_unfold = ms_torch.nn.Unfold((2, 3), 1, (1, 2), (2, 1))
    ms_out = ms_unfold(ms_tensor)

    param_compare(ms_out, torch_out, rtol=1e-3, atol=1e-5)


def test_fold():
    np_input1 = np.random.randn(7, 8, 24)
    np_input2 = np.random.randn(18, 6)

    torch_tensor1 = torch.tensor(np_input1)
    torch_tensor2 = torch.tensor(np_input2)
    torch_fold1 = torch.nn.Fold((4, 5), (2, 2), 1, (1, 2), (2, 1))
    torch_fold2 = torch.nn.Fold((7, 4), 3, 2, 2, 3)
    torch_out1 = torch_fold1(torch_tensor1)
    torch_out2 = torch_fold2(torch_tensor2)

    ms_tensor1 = ms_torch.tensor(np_input1)
    ms_tensor2 = ms_torch.tensor(np_input2)
    ms_fold1 = ms_torch.nn.Fold((4, 5), (2, 2), 1, (1, 2), (2, 1))
    ms_fold2 = ms_torch.nn.Fold((7, 4), 3, 2, 2, 3)
    ms_out1 = ms_fold1(ms_tensor1)
    ms_out2 = ms_fold2(ms_tensor2)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert ms_out1.asnumpy().shape == torch_out1.numpy().shape
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), rtol=1e-3, atol=1e-5)
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert ms_out2.asnumpy().shape == torch_out2.numpy().shape


if __name__ == '__main__':
    set_mode_by_env_config()
    test_unfold()
    test_fold()
