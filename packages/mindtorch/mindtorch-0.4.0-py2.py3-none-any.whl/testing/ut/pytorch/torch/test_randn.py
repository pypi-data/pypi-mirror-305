#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_randn1():
    try:
        ms_torch.randn(1, 2, 3)
    except:
        return 1
    return 0

def test_randn2():
    try:
        ms_torch.randn([1, 2, 3])
    except:
        return 1
    return 0

def test_randn3():
    try:
        ms_torch.randn((1, 2, 3))
    except:
        return 1
    return 0


if __name__ == '__main__':
    set_mode_by_env_config()
    test_randn1()
    test_randn2()
    test_randn3()