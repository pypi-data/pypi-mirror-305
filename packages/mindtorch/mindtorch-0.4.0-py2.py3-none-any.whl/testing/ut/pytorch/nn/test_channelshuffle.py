#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import torch
import mindtorch.torch as ms_torch

from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_channelshuffle():
    np_data1 = np.random.randn(2, 9, 3, 4)
    np_data2 = np.random.randn(1, 6, 12, 2, 2)

    torch_input1 = torch.tensor(np_data1)
    torch_input2 = torch.tensor(np_data2)
    ms_input1 = ms_torch.tensor(np_data1)
    ms_input2 = ms_torch.tensor(np_data2)

    torch_shuffle = torch.nn.ChannelShuffle(3)
    ms_shuffle = ms_torch.nn.ChannelShuffle(3)

    torch_out1 = torch_shuffle(torch_input1)
    torch_out2 = torch_shuffle(torch_input2)
    ms_out1 = ms_shuffle(ms_input1)
    ms_out2 = ms_shuffle(ms_input2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_channelshuffle()