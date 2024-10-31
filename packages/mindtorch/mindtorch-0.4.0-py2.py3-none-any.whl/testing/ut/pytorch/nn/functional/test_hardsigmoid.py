#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()


def test_hardsigmoid1():
    data = np.array([[-4, -3, 1, 0, -1.5, 2.8, 3.7, 100]]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.hardsigmoid(ms_input)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.hardsigmoid(torch_input)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


@SKIP_ENV_GRAPH_MODE(reason="inplace=True can not support graph mode.")
def test_hardsigmoid2():
    data = np.array([[-4, -3, 1, 0, -1.5, 2.8, 3.7, 100]]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.hardsigmoid(ms_input, True)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.hardsigmoid(torch_input, True)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


if __name__ == '__main__':
    set_mode_by_env_config()
    test_hardsigmoid1()
    test_hardsigmoid2()