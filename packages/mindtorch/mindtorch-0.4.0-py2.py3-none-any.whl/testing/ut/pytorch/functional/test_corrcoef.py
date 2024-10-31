#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, TestNet, param_compare
set_mode_by_env_config()


def test_corrcoef1():
    np_1 = np.random.randn(3, 3).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.corrcoef)
    ms_result = msa_net(ms_tensor)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.corrcoef(torch_tensor)
    param_compare(ms_result, torch_result, atol=1e-3)

def test_corrcoef2():
    np_1 = np.random.randn(8).astype(np.float32)
    ms_tensor = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.corrcoef)
    ms_result = msa_net(ms_tensor)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.corrcoef(torch_tensor)
    param_compare(ms_result, torch_result)


def test_corrcoef3():
    np_1 = np.random.randint(0, 10, 5).astype(np.int32)
    ms_tensor = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.corrcoef)
    ms_result = msa_net(ms_tensor)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.corrcoef(torch_tensor)
    param_compare(ms_result, torch_result)


def test_corrcoef4():
    np_1 = np.random.randint(0, 10, (3, 5)).astype(np.int32)
    ms_tensor = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.corrcoef)
    ms_result = msa_net(ms_tensor)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch.corrcoef(torch_tensor)
    param_compare(ms_result, torch_result, atol=1e-3)


if __name__ == "__main__":
    set_mode_by_env_config()
    test_corrcoef1()
    test_corrcoef2()
    test_corrcoef3()
    test_corrcoef4()
