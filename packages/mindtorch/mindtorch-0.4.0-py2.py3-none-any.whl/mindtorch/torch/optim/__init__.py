#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.optim import lr_scheduler
from mindtorch.torch.optim.optimizer import Optimizer
from mindtorch.torch.optim.sgd import SGD
from mindtorch.torch.optim.adam import Adam
from mindtorch.torch.optim.adamw import AdamW

try:
    # [adapt old version ms] use 'try import' to suit mindspore 2.2
    from mindtorch.torch.optim.adadelta import Adadelta
    from mindtorch.torch.optim.adagrad import Adagrad
    from mindtorch.torch.optim.asgd import ASGD
    from mindtorch.torch.optim.adamax import Adamax
    from mindtorch.torch.optim.rmsprop import RMSprop
    from mindtorch.torch.optim.rprop import Rprop
    from mindtorch.torch.optim.nadam import NAdam
    from mindtorch.torch.optim.radam import RAdam
    from mindtorch.torch.optim import _adamw
except ImportError:
    # do nothings here.
    ...
