#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch
import torch


from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE, TestNet

set_mode_by_env_config()

def test_arange1():
    msa_net = TestNet(ms_torch.arange)
    ms_result = msa_net(1, 10)

    torch_result = torch.arange(1, 10)

    param_compare(ms_result, torch_result)

def test_arange2():
    msa_net = TestNet(ms_torch.arange)
    ms_result = msa_net(1.0, 3, 0.5)

    torch_result = torch.arange(1.0, 3, 0.5)

    param_compare(ms_result, torch_result)

def test_arange3():
    msa_net = TestNet(ms_torch.arange)
    ms_result = msa_net(1, 10, 5, dtype=ms_torch.int64)

    torch_result = torch.arange(1, 10, 5, dtype=torch.int64)

    param_compare(ms_result, torch_result)

def test_arange4():
    msa_net = TestNet(ms_torch.arange)
    ms_result = msa_net(2, 2, dtype=ms_torch.float32)

    torch_result = torch.arange(2, 2, dtype=torch.float32)

    param_compare(ms_result, torch_result)

def test_arange5():
    msa_net = TestNet(ms_torch.arange)
    ms_result = msa_net(5, dtype=ms_torch.float64)

    torch_result = torch.arange(5, dtype=torch.float64)

    param_compare(ms_result, torch_result)

def test_arange6():
    msa_net = TestNet(ms_torch.arange)
    ms_result = msa_net(ms_torch.tensor(1), ms_torch.tensor(10), ms_torch.tensor(2))

    torch_result = torch.arange(torch.tensor(1), torch.tensor(10), torch.tensor(2))
    param_compare(ms_result, torch_result)

@SKIP_ENV_GRAPH_MODE(reason='`out` not support graph-mode')
def test_arange_out_different_dtype():
    ms_tensor = ms_torch.tensor(2.)
    msa_net = TestNet(ms_torch.arange)
    ms_result = msa_net(0, 3, out=ms_tensor)

    pt_tensor = torch.tensor(2.)
    pt_result = torch.arange(0, 3, out=pt_tensor)

    param_compare(ms_result, pt_result)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_arange1()
    test_arange2()
    test_arange3()
    test_arange4()
    test_arange5()
    test_arange6()
    test_arange_out_different_dtype()
