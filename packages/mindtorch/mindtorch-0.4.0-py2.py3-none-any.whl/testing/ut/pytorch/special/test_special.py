import numpy as np
import mindtorch.torch as ms_torch
import torch
from ...utils import param_compare
import math

def test_expm1():
    _data = [0, math.log(2.)]

    torch_tensor = torch.tensor(_data)
    torch_out = torch.special.expm1(torch_tensor)

    ms_tensor = ms_torch.tensor(_data)
    ms_out = ms_torch.special.expm1(ms_tensor)

    param_compare(torch_out, ms_out)


if __name__ == '__main__':
    test_expm1()