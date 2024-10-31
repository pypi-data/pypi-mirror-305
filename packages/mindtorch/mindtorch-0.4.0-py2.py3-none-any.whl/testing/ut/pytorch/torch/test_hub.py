#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context
import pytest

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_CPU
set_mode_by_env_config()
@SKIP_ENV_CPU(reason="need stable network")
def test_get_dir():
    ms_hub_dir = ms_torch.hub.get_dir()
    torch_hub_dir = torch.hub.get_dir()
    assert ms_hub_dir == torch_hub_dir

'''
@SKIP_ENV_GRAPH_MODE(reason="no need test on Graph mode")
@pytest.mark.timeout(600)
def test_load_state_dict_from_url():
    target_url = 'https://download.pytorch.org/models/mobilenet_v3_small-047dcff4.pth'
    ms_torch_file_name = 'ms_torch_mobilenet.pth'
    ms_torch_state_dict = ms_torch.hub.load_state_dict_from_url(target_url, model_dir='.', file_name=ms_torch_file_name)
    assert len(ms_torch_state_dict) == 244
    os.remove(os.path.join('.', ms_torch_file_name))
'''
