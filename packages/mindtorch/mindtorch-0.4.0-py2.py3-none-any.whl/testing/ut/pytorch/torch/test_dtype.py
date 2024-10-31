import mindtorch.torch as torch
import mindspore as ms
from mindtorch.torch.tensor import cast_to_adapter_tensor

from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()


@SKIP_ENV_GRAPH_MODE(reason="Do not support when jit_syntax_level=ms.STRICT.")
def test_dtype_mixed_use():
    class Net(torch.nn.Module):
        def forward(self, x):
            x_dtype = x.dtype
            if x_dtype.is_floating_point:
                x = x + 1
            x = x.astype(torch.int64)
            x = cast_to_adapter_tensor(x)
            x_dtype = x.dtype
            if x_dtype.is_signed:
                x = x + 1
            x = x + ms.ops.ones(x.shape, x.dtype)
            x = x.to(ms.float16)
            return x

    input = torch.tensor(3.)
    net = Net()
    out = net(input)
    expect_out = torch.tensor(6.).to(torch.float16)
    param_compare(out, expect_out)


def test_dtype_compare():
    class Net(torch.nn.Module):
        def forward(self, x):
            x_dtype = x.dtype
            if x_dtype == ms.bool_:
                x = x.to(torch.float32) + 1
            return x

    input = torch.tensor(True)
    net = Net()
    out = net(input)
    expect_out = torch.tensor(2.).to(torch.float32)
    param_compare(out, expect_out)


@SKIP_ENV_GRAPH_MODE(reason="Do not support in graph mode.")
def test_dtype_str():
    class Net(torch.nn.Module):
        def forward(self, x):
            x_dtype = x.dtype
            return str(x_dtype)

    net = Net()
    input = torch.nn.Parameter(torch.tensor(True))
    out = net(input)
    assert out == 'mindtorch.bool'


if __name__ == '__main__':
    set_mode_by_env_config()
    test_dtype_mixed_use()
    test_dtype_compare()
    test_dtype_str()
