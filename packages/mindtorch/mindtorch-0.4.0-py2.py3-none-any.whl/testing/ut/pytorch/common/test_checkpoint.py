
import mindtorch.torch as ms_torch
from mindtorch.torch.utils.checkpoint import checkpoint, checkpoint_sequential, \
    detach_variable
    
from ...utils import set_mode_by_env_config

set_mode_by_env_config()

def test_checkpoint():
    inp = ms_torch.randn(20, device='cuda').requires_grad_()
    phase1 = ms_torch.nn.Dropout()
    phase2 = ms_torch.nn.Dropout()

    def run_fn(input):
        return phase2(input)

    out = phase1(inp)
    out = checkpoint(run_fn, out, use_reentrant=False)
    assert out.shape == (20,)

def test_checkpoint_sequential():
    class Noop(ms_torch.nn.Module):
        def forward(self, x):
            return x

    model = ms_torch.nn.Sequential(Noop())
    x = ms_torch.Tensor(1)
    output = checkpoint_sequential(model, 1, x)
    assert output.shape == (1,)


def test_detach_variable():
    a = ms_torch.Tensor(2)
    detach_variable((a,))
    assert a.shape == (2,)

if __name__ == '__main__':
    test_checkpoint()
    test_checkpoint_sequential()
    test_detach_variable()
