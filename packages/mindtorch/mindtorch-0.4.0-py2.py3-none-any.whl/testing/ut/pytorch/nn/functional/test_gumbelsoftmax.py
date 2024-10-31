#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
import random

from ....utils import set_mode_by_env_config
set_mode_by_env_config()


def test_gumbel_softmax():
    data = np.array([[-1, 0, 2, 3, 4, 7]],).astype(np.float32)
#    seed = 10

    ms_input = ms_torch.tensor(data)
#    random.seed(seed)
    ms_out = ms_torch.nn.functional.gumbel_softmax(ms_input)

    torch_input = torch.tensor(data)
#    torch.manual_seed(seed)
    torch_out = torch.nn.functional.gumbel_softmax(torch_input)

#    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


if __name__ == '__main__':
    set_mode_by_env_config()
    test_gumbel_softmax()
