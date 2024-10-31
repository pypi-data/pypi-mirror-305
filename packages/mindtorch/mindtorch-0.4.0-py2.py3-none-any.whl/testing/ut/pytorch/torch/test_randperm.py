#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as torch
from mindspore import context

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()
ms.set_seed(123)

def test_randperm1():
    out = torch.randperm(4)
    assert len(out) == 4

def test_randperm2():
    out = torch.randperm(4, dtype=torch.float32)
    assert len(out) == 4
    assert out.dtype == torch.float32

@SKIP_ENV_GRAPH_MODE(reason="`out` shoud be None on graph mode")
def test_randperm3():
    output = torch.tensor([1, 1, 1, 1])
    out = torch.randperm(4, out=output)
    assert len(out) == 4
    assert id(output) == id(out)


if __name__ == '__main__':
    test_randperm1()
    test_randperm2()
    test_randperm3()