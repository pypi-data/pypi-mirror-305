#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()


def test_one_hot1():
    data = np.array([0, 2, 3, 4, 7]).astype(np.int64)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.one_hot(torch_input)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.one_hot(ms_input)

    param_compare(ms_out, torch_out)


def test_one_hot2():
    data = np.array([[[0, 2, 3], [1, 1, 2]]]).astype(np.int64)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.one_hot(input=torch_input, num_classes=5)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.one_hot(input=ms_input, num_classes=5)

    param_compare(ms_out, torch_out)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_one_hot1()
    test_one_hot2()
