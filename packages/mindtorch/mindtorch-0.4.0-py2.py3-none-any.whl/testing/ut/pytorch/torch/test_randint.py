#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as pytorch
from mindspore import context
import torch

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, type_shape_compare
set_mode_by_env_config()
ms.set_seed(123)

def test_randint1():
    out1 = pytorch.randint(0, 10, (2, 2))
    out2 = pytorch.randint(10, (2, 2))
    type_shape_compare(out1, out2)

@SKIP_ENV_GRAPH_MODE(reason="`out` shoud be None on graph mode")
def test_randint2():
    output = pytorch.tensor([1, 1, 1, 1])
    out = pytorch.randint(3, 10, (3, ), out=output)
    assert out.shape == (3, )
    assert id(output) == id(out)

def test_randint3():
    torch_out = torch.randint(0, 10, (2, 2), dtype=torch.float32)
    ms_out = pytorch.randint(0, 10, (2, 2), dtype=ms.float32)
    assert ms_out.shape == torch_out.shape
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

    torch_out = torch.randint(0, 10, (3, 3), dtype=torch.uint8)
    ms_out = pytorch.randint(0, 10, (3, 3), dtype=ms.uint8)
    assert ms_out.shape == torch_out.shape
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

    torch_out = torch.randint(0, 2, (3, 3), dtype=torch.bool)
    ms_out = pytorch.randint(0, 2, (3, 3), dtype=ms.bool_)
    assert ms_out.shape == torch_out.shape
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

def test_randint4():
    out1 = torch.randint(4, size=(2, 2))
    out2 = pytorch.randint(high=4, size=(2, 2))
    type_shape_compare(out1, out2)

def test_randint_size_empty():
    out1 = torch.randint(3, 6, size=())
    out2 = pytorch.randint(3, 6, size=())
    type_shape_compare(out1, out2)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_randint1()
    test_randint2()
    test_randint3()
    test_randint4()
    test_randint_size_empty()