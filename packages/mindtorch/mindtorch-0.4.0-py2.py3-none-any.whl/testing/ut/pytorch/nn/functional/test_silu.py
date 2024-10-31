#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE, SKIP_ENV_CPU
set_mode_by_env_config()

def test_silu1():
    data = np.array([[-4, -3, 1, 0, -1.5, 2.8, 3.7, 100]]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.silu(ms_input)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.silu(torch_input)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="inplace=True can not support graph mode.")
def test_silu2():
    data = np.array([[-4, -3, 1, 0, -1.5, 2.8, 3.7, 100]]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.silu(ms_input, True)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.silu(torch_input, True)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert np.allclose(ms_input.asnumpy(), torch_input.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


if __name__ == '__main__':
    set_mode_by_env_config()
    test_silu1()
    test_silu2()