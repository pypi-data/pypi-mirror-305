
import mindtorch.torch as ms_torch
from ...utils import set_mode_by_env_config, graph_lax_level

set_mode_by_env_config()

def test_device_class():
    device1 = ms_torch.device('cpu')
    device2 = ms_torch.device('cuda', 0)
    device3 = ms_torch.device('cuda:0')
    device4 = ms_torch.device(1)
    assert device2 == device3

def test_device_type():
    x1 = ms_torch.device
    assert isinstance(x1, type)
    x2 = ms_torch.device(1)
    assert isinstance(x2, ms_torch.device)

    data = ms_torch.tensor(1)
    x3 = data.device
    assert type(x3) is ms_torch.device

def test_device_func():
    class Net(ms_torch.nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.device1 = ms_torch.device('cpu')

        def forward(self, input1=None):
            device = input1.device if input1 is not None else self.device1
            return device
    net = Net()
    data = ms_torch.tensor(1)
    with graph_lax_level():
        out = net(data)
    assert type(out) == ms_torch.device

if __name__ == '__main__':
    test_device_class()
    test_device_type()
    test_device_func()
