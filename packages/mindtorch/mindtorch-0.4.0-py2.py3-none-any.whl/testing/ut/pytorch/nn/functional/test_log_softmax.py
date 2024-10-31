#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config
set_mode_by_env_config()


def test_log_softmax1():
    ms_result = ms_torch.nn.functional.log_softmax(ms_torch.tensor([1, 2, 3, 4, 5]), \
         dim=0, dtype=ms_torch.float32)
    torch_result = torch.nn.functional.log_softmax(torch.tensor([1, 2, 3, 4, 5]), \
         dim=0, dtype=torch.float32)
    assert torch_result.numpy().dtype == ms_result.asnumpy().dtype
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())

def test_log_softmax2():

    x = np.array([[-0.08082921, -0.13706027, -0.4711177, -0.05606057],
                  [-0.46082982, 1.1761844, -1.016654, -1.743829],
                  [-1.5062045, 0.6910976, 0.4839723, 1.1502692]]).astype(np.float32)
    expect = np.array([[-1.2939762, -1.3502073, -1.6842647, -1.2692076],
                       [-1.9445671, -0.3075528, -2.5003912, -3.2275662],
                       [-3.452001, -1.2546989, -1.4618242, -0.79552734]]).astype(np.float32)
    output = ms_torch.nn.functional.log_softmax(ms_torch.tensor(x), 1)
    assert np.allclose(output.asnumpy(), expect)

def test_log_softmax3():
     input = np.random.randn(2, 2, 3).astype(np.float32)

     torch_input = torch.tensor(input, dtype=torch.float32)
     torch_output = torch.nn.functional.log_softmax(torch_input)
     ms_torch_input = ms_torch.tensor(input, dtype=ms_torch.float32)
     ms_torch_output = ms_torch.nn.functional.log_softmax(ms_torch_input)

     assert torch_output.numpy().dtype == ms_torch_output.asnumpy().dtype
     assert np.allclose(torch_output.numpy(), ms_torch_output.asnumpy())

def test_log_softmax_dim():
     input = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

     torch_input = torch.tensor(input, dtype=torch.float32)
     torch_output = torch.nn.functional.log_softmax(torch_input)
     ms_torch_input = ms_torch.tensor(input, dtype=ms_torch.float32)
     ms_torch_output = ms_torch.nn.functional.log_softmax(ms_torch_input)

     assert torch_output.numpy().dtype == ms_torch_output.asnumpy().dtype
     assert np.allclose(torch_output.numpy(), ms_torch_output.asnumpy())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_log_softmax1()
    test_log_softmax2()
    test_log_softmax3()
    test_log_softmax_dim()

