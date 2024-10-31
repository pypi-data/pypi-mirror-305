#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import set_mode_by_env_config, TestNet
set_mode_by_env_config()

def test_chunk1():
    np_1 = np.arange(12)

    ms_tensor = ms_torch.tensor(np_1)
    msa_net = TestNet(ms_torch.chunk)
    ms_result = msa_net(ms_tensor, 6)

    torch_tensor = torch.tensor(np_1)
    torch_result = torch.chunk(torch_tensor, 6)

    for i in range(6):
        assert np.allclose(ms_result[i].asnumpy(), torch_result[i].numpy())
        assert ms_result[i].asnumpy().dtype == torch_result[i].numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_chunk1()
