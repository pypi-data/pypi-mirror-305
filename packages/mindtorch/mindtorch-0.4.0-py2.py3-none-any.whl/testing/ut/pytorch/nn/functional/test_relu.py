#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config
set_mode_by_env_config()


def test_relu1():
    np_1 = np.random.randn(2, 3, 4, 5)

    ms_tensor = ms_torch.tensor(np_1)
    ms_result = ms_torch.nn.functional.relu(ms_tensor)

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.nn.functional.relu(torch_tensor)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_relu1()
