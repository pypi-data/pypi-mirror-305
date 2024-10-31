#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ....utils import set_mode_by_env_config
set_mode_by_env_config()


def test_sigmoid():
    data = np.array([[-1, 0, 1, -2],
                     [2, 2, 3, 4]
                     ]).astype(np.float32)

    ms_input = ms_torch.tensor(data)
    ms_out = ms_torch.nn.functional.sigmoid(ms_input)

    torch_input = torch.tensor(data)
    torch_out = torch.nn.functional.sigmoid(torch_input)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


if __name__ == '__main__':
    set_mode_by_env_config()
    test_sigmoid()
