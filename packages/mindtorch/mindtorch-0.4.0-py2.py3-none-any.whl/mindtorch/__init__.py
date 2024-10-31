#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from mindtorch import torch
from mindtorch.utils import unsupported_attr, pynative_mode_condition
from mindtorch.package_info import __version__, VERSION, version
from mindtorch.module_hooker import torch_enable, torch_disable, torch_pop
from mindspore._c_expression import jit_mode_pi_enable

_BACKWARD_ENV = os.environ.get('ENABLE_BACKWARD')
if _BACKWARD_ENV == "1":
    jit_mode_pi_enable()