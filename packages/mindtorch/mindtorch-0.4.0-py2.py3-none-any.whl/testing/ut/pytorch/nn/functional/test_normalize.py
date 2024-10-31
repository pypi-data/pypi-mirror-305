#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_normalize1():
    data = np.array([[-1, 0, 1, -2],
                     [2, 2, 3, 4]
                     ]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.normalize(ms_input)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.normalize(torch_input)

    param_compare(ms_out, torch_out)


def test_normalize2():
    data = np.array([[[-1, 0, 1, -2],
                     [2, 2, 3, 4]
                     ]]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.normalize(ms_input, 2.2, 0, 10)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.normalize(torch_input, 2.2, 0, 10)

    param_compare(ms_out, torch_out)

def test_local_response_norm1():
    data = np.random.random((4, 4, 4)).astype(np.float32)*10

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.local_response_norm(ms_input, 3, 0.01)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.local_response_norm(torch_input, 3, 0.01)

    if ms.get_context('device_target') == 'Ascend':
        param_compare(ms_out, torch_out, rtol=1e-3, atol=1e-5)
    else:
        param_compare(ms_out, torch_out)


def test_local_response_norm2():
    data = np.random.random((2, 4, 4, 3, 2)).astype(np.float32)*10

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.local_response_norm(ms_input, 3, 0.01)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.local_response_norm(torch_input, 3, 0.01)

    if ms.get_context('device_target') == 'Ascend':
        param_compare(ms_out, torch_out, rtol=1e-3, atol=1e-5)
    else:
        param_compare(ms_out, torch_out)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_normalize1()
    test_normalize2()
    test_local_response_norm1()
    test_local_response_norm2()
