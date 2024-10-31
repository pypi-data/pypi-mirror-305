import numpy as np
import mindspore as ms
from mindspore import context
import mindtorch.torch as ms_torch
import mindtorch.torch.nn as nn
from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE

set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_tensor_inplace():
    x = ms_torch.tensor([1.0, 2.0])
    y = -1.0

    out = x.add_(y)
    assert (id(out) == id(x))
    assert np.allclose(out.numpy(), [0., 1.0])


@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_nn_inplace():
    input = ms_torch.randn(2)

    nn_relu = nn.ReLU(inplace=True)
    output = nn_relu(input)
    assert (id(output) == id(input))
    assert np.allclose(output.numpy(), input.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_out_param():
    x = ms_torch.tensor([10.0, 2.0])
    out = ms_torch.tensor([1.0, 1.0])

    output = ms_torch.log(x, out=out)
    assert (id(out) == id(output))
    assert np.allclose(output.numpy(), out.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_inplace_param():
    x = ms_torch.tensor([-1, -2, 0, 2, 1], dtype=ms_torch.float16)

    output = nn.functional.relu6(x, inplace=True)
    assert (id(x) == id(output))
    assert np.allclose(output.numpy(), x.numpy())

if __name__ == '__main__':
    set_mode_by_env_config()
    test_tensor_inplace()
    test_nn_inplace()
    test_out_param()
    test_inplace_param()


