#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.tensor import Tensor
from mindtorch.torch.logging import warning
from mindtorch.utils import unsupported_attr

class Variable(Tensor):
    def __new__(cls, data, requires_grad=None, volatile=None):
        warning("The Variable API has been deprecated, use Tensor instead.")
        unsupported_attr(data)
        unsupported_attr(requires_grad)
        unsupported_attr(volatile)
        obj = Tensor.__new__(cls)
        return obj

    def __init__(self, data, requires_grad=None, volatile=None):
        if volatile:
            warning("UserWarning:volatile was removed (Variable.volatile is always False), "
                    "please use with torch.no_grad() instead.")
        Tensor.__init__(self, data, requires_grad=requires_grad)
