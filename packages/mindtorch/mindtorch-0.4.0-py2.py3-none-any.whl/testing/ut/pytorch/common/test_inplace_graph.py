import numpy as np
import mindspore as ms
from mindspore import context
import mindtorch.torch as ms_torch
import mindtorch.torch.nn as nn
from ...utils import set_mode_by_env_config, SKIP_ENV_PYNATIVE_MODE

set_mode_by_env_config()

@SKIP_ENV_PYNATIVE_MODE(reason="testcase only for graph mode")
def test_tensor_inplace():
    x = ms_torch.tensor([1.0, 2.0])
    y = -1.0

    try:
        out = x.add_(y)
        assert (id(out) != id(x))
    except RuntimeError as e:
        assert "is not supported to use in MindSpore static graph mode" in str(e)

@SKIP_ENV_PYNATIVE_MODE(reason="testcase only for graph mode")
def test_nn_inplace():
    input = ms_torch.randn(2)

    try:
        nn_relu = nn.ReLU(inplace=True)
        output = nn_relu(input)
        assert (id(output) != id(input))
    except ValueError as e:
        assert "please set inplace=False and use return value instead" in str(e)

@SKIP_ENV_PYNATIVE_MODE(reason="testcase only for graph mode")
def test_out_param():
    x = ms_torch.tensor([10.0, 2.0])
    out = ms_torch.tensor([1.0, 1.0])

    try:
        output = ms_torch.log(x, out=out)
        assert (id(output) != id(out)) 
    except ValueError as e:
        assert "please set out=None and use return value instead" in str(e)

@SKIP_ENV_PYNATIVE_MODE(reason="testcase only for graph mode")
def test_inplace_param():
    x = ms_torch.tensor([-1, -2, 0, 2, 1], dtype=ms_torch.float16)

    try:
        output = nn.functional.relu6(x, inplace=True)
        assert (id(output) != id(x)) 
    except ValueError as e:
        assert "please set inplace=False and use return value instead" in str(e)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_tensor_inplace()
    test_nn_inplace()
    test_out_param()
    test_inplace_param()


