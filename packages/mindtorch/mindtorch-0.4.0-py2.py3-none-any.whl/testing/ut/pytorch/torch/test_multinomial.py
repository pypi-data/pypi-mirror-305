#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import torch
import mindtorch.torch as ms_torch
from mindspore import context

from ...utils import SKIP_ENV_GRAPH_MODE, set_mode_by_env_config, type_shape_compare
set_mode_by_env_config()
ms.set_seed(123)

def test_multinomial1():
    x = torch.tensor([0, 9, 4, 0], dtype=torch.float)
    out = torch.multinomial(x, 2)

    x_ms = ms_torch.tensor([0, 9, 4, 0], dtype=torch.float)
    out_ms = ms_torch.multinomial(x_ms, 2)

    type_shape_compare(out, out_ms)

def test_multinomial2():
    x = torch.tensor([0, 9, 4, 0], dtype=torch.float)
    out = torch.multinomial(x, 4, replacement=True)

    x_ms = ms_torch.tensor([0, 9, 4, 0], dtype=torch.float)
    out_ms = ms_torch.multinomial(x_ms, 4, replacement=True)
    type_shape_compare(out, out_ms)

@SKIP_ENV_GRAPH_MODE(reason="`out` shoud be None on graph mode")
def test_multinomial3():
    x = torch.tensor([0, 9, 4, 0], dtype=torch.float)
    output = torch.tensor([1, 1, 1, 1])
    out = torch.multinomial(x, 4, replacement=True, out=output)

    x_ms = ms_torch.tensor([0, 9, 4, 0], dtype=torch.float)
    output_ms = ms_torch.tensor([1, 1, 1, 1])
    out_ms = ms_torch.multinomial(x_ms, 4, replacement=True, out=output_ms)
    assert id(output_ms) == id(out_ms)

    type_shape_compare(out, out_ms)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_multinomial1()
    test_multinomial2()
    test_multinomial3()