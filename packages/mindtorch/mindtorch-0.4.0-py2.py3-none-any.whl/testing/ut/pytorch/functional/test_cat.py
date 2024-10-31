#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import SKIP_ENV_ASCEND, set_mode_by_env_config, param_compare, TestNet
set_mode_by_env_config()

def test_cat1():
    ms_tensor = ms_torch.tensor([1, 2, 3]).to(ms_torch.uint8)
    msa_net = TestNet(ms_torch.cat)
    ms_result = msa_net((ms_tensor, ms_tensor, ms_tensor, ms_tensor.char()), dim=0)

    torch_tensor = torch.tensor([1, 2, 3]).to(torch.uint8)
    torch_result = torch.cat((torch_tensor, torch_tensor, torch_tensor, torch_tensor.char()), dim=0)
    param_compare(ms_result, torch_result)

def test_cat2():
    ms_tensor = ms_torch.tensor([[1, 2, 3], [1, 2, 3]])
    msa_net = TestNet(ms_torch.cat)
    ms_result = msa_net((ms_tensor.short(), ms_tensor.half(), ms_tensor.short()), axis=1)

    torch_tensor = torch.tensor([[1, 2, 3], [1, 2, 3]])
    torch_result = torch.cat((torch_tensor.short(), torch_tensor.half(), torch_tensor.short()), axis=1)

    param_compare(ms_result, torch_result)

def test_cat3():
    ms_tensor = ms_torch.tensor([[1, 2, 3], [1, 2, 3]])
    msa_net = TestNet(ms_torch.cat)
    ms_result = msa_net([ms_tensor.int(), ms_tensor.long()], dim=0)

    torch_tensor = torch.tensor([[1, 2, 3], [1, 2, 3]])
    torch_result = torch.cat([torch_tensor.int(), torch_tensor.long()], dim=0)

    param_compare(ms_result, torch_result)

@SKIP_ENV_ASCEND(reason='not support complex input on Ascend')
def test_cat_complex():
    real = np.random.randn(2, 3).astype(np.float32)
    img = np.random.randn(2, 3).astype(np.float32)
    # complex128 ms.ops.cat result not correct
    input_np = (real + 1j * img).astype(np.complex64)

    ms_tensor = ms_torch.tensor(input_np)
    msa_net = TestNet(ms_torch.cat)
    ms_result = msa_net([ms_tensor.to(ms_torch.complex64), ms_torch.tensor(real)], dim=0)

    torch_tensor = torch.tensor(input_np)
    torch_result = torch.cat([torch_tensor.to(torch.complex64), torch.tensor(real)], dim=0)

    param_compare(ms_result, torch_result)


@SKIP_ENV_ASCEND(reason="currently concat not support float64 on Ascend")
def test_concat1():
    ms_tensor = ms_torch.tensor([1, 2, 3])
    msa_net = TestNet(ms_torch.concat)
    ms_result = msa_net((ms_tensor.double(), ms_tensor.half()), dim=0)

    torch_tensor = torch.tensor([1, 2, 3])
    torch_result = torch.concat((torch_tensor.double(), torch_tensor.half()), dim=0)

    param_compare(ms_result, torch_result)

def test_concat2():
    ms_tensor = ms_torch.tensor([[1, 2, 3], [1, 2, 3]])
    msa_net = TestNet(ms_torch.concat)
    ms_result = msa_net((ms_tensor, ms_tensor), dim=1)

    torch_tensor = torch.tensor([[1, 2, 3], [1, 2, 3]])
    torch_result = torch.concat((torch_tensor, torch_tensor), dim=1)

    param_compare(ms_result, torch_result)

def test_concat3():
    ms_tensor = ms_torch.tensor([[1, 2, 3], [1, 2, 3]])
    msa_net = TestNet(ms_torch.concat)
    ms_result = msa_net([ms_tensor.bool(), ms_tensor.byte()], dim=-1)

    torch_tensor = torch.tensor([[1, 2, 3], [1, 2, 3]])
    torch_result = torch.concat([torch_tensor.bool(), torch_tensor.byte()], dim=-1)

    param_compare(ms_result, torch_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_cat1()
    test_cat2()
    test_cat3()
    test_concat1()
    test_concat2()
    test_concat3()
