import os
import shutil
import numpy as np
import mindtorch.torch as ms_torch
from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE

set_mode_by_env_config()

class Conv2dNet(ms_torch.nn.Module):
    def __init__(self, stride=1, padding=0, dilation=1, padding_mode='zeros'):
        super(Conv2dNet, self).__init__()
        self.conv = ms_torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 5), stride=stride,
                                       padding=padding, dilation=dilation, padding_mode=padding_mode)

    def forward(self, inputs):
        x = self.conv(inputs)
        return x


def test_auto_mixed_precision():
    input_init = np.random.randn(1, 3, 16, 50).astype(np.float32)
    input = ms_torch.tensor(input_init)
    net = Conv2dNet()
    amp_net = ms_torch.amp.auto_mixed_precision(net, amp_level="O2")
    assert isinstance(amp_net, ms_torch.nn.Module) == True

    output = amp_net(input)
    assert isinstance(output, ms_torch.Tensor) == True
    if os.path.isdir('./rewritten_network'):
        shutil.rmtree('./rewritten_network')


@SKIP_ENV_GRAPH_MODE(reason="Error testing, unnecessary for Graph mode")
def test_autocast():
    a_float32 = ms_torch.tensor([3, 2], dtype=ms_torch.float32)
    b_float32 = ms_torch.tensor([2, 3], dtype=ms_torch.float32)

    try:
        with ms_torch.cpu.amp.autocast():
            e_float16 = ms_torch.mm(a_float32, b_float32)
            assert e_float16.dtype is not ms_torch.float16  #unsupport autocast now
    except Exception as e:
        assert "The use of `with autocast` is not currently supported" in str(e)


@SKIP_ENV_GRAPH_MODE(reason="Error testing, unnecessary for Graph mode")
def test_custom_autocast():
    try:
        class CustomNet(ms_torch.autograd.Function):
            @staticmethod
            @ms_torch.cuda.amp.custom_fwd
            def forward(ctx, a, b):
                ctx.save_for_backward(a, b)
                return a.mm(b)

            @staticmethod
            @ms_torch.cuda.amp.custom_fwd
            def backward(ctx, grad):
                a, b = ctx.saved_tensors
                return grad.mm(b.t()), a.t().mm(grad)

        a_float32 = ms_torch.tensor([3, 2], dtype=ms_torch.float32)
        b_float32 = ms_torch.tensor([2, 3], dtype=ms_torch.float32)
        net = CustomNet()
        out = net(a_float32, b_float32)
        assert out.dtype is not ms_torch.float16  #unsupport autocast now
    except Exception as e:
        assert "The use of `@custom_fwd` is not currently supported" in str(e)

    if os.path.isdir('./rewritten_network'):
        shutil.rmtree('./rewritten_network')

if __name__ == '__main__':
    test_auto_mixed_precision()
    test_autocast()
    test_custom_autocast()
