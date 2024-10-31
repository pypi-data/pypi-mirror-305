import numpy as np
import mindspore as ms
import torch
from mindspore import context
import mindtorch.torch as ms_torch

from ...utils import SKIP_ENV_GRAPH_MODE, set_mode_by_env_config
set_mode_by_env_config()

def test_neg():
    class Net(ms_torch.nn.Module):
        def forward(self, x):
            return -x
    net = Net()
    x = ms_torch.tensor([1.0, 2.0])
    out = net(x)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-1.0, -2.0])

def test_pos():
    class Net(ms_torch.nn.Module):
        def forward(self, x):
            return +x
    net = Net()
    x = ms_torch.tensor([-2.0, 3.0])
    out = net(x)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 3.0])

def test_invert():
    class Net(ms_torch.nn.Module):
        def forward(self, x):
            return ~x
    net = Net()
    x = ms_torch.tensor([False, True])
    out = net(x)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [True, False])

    y = ms_torch.tensor([5, -3])
    out = net(y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-6, 2])

def test_round():
    class Net(ms_torch.nn.Module):
        def forward(self, x):
            return round(x)
    net = Net()
    x = ms_torch.tensor([0.7, 1.4])
    out = net(x)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [1.0, 1.0])

def test_abs():
    class Net(ms_torch.nn.Module):
        def forward(self, x):
            return abs(x)
    net = Net()
    x = ms_torch.tensor([-0.1, -1.0])
    out = net(x)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [0.1, 1.0])

def test_add():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x+y
    net = Net()
    x = ms_torch.tensor([-0.1, -1.0])
    y = 10.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [9.9, 9.0])

def test_radd():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return y+x
    net = Net()
    x = ms_torch.tensor([-1, 0])
    y = 1
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [0, 1])

def test_iadd():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            x += y
            return x
    net = Net()
    x = ms_torch.tensor([-1, 0])
    y = 1
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [0, 1])

def test_and():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x & y
    net = Net()
    x = ms_torch.tensor([-1, 0])
    y = 1
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [1, 0])

def test_xor():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x ^ y
    net = Net()
    x = ms_torch.tensor([-1, 0])
    y = 1
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2, 1])

def test_or():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x | y
    net = Net()
    x = ms_torch.tensor([-1, 0])
    y = 1
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-1, 1])

def test_sub():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x-y
    net = Net()
    x = ms_torch.tensor([-1.7, 2.9])
    y = 1.3
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-3.0, 1.6])

def test_rsub():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return y - x
    net = Net()
    x = ms_torch.tensor([-1.7, 2.9])
    y = 1.3
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [3.0, -1.6])

def test_isub():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            x-=y
            return x
    net = Net()
    x = ms_torch.tensor([-1.7, 2.9])
    y = 1.3
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-3.0, 1.6])

def test_mul():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x*y
    net = Net()
    x = ms_torch.tensor([-1.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 4.0])

def test_rmul():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return y*x
    net = Net()
    x = ms_torch.tensor([-1.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 4.0])

def test_imul():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            x *= y
            return x
    net = Net()
    x = ms_torch.tensor([-1.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 4.0])

def test_truediv():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x/y
    net = Net()
    x = ms_torch.tensor([-4.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 1.0])

def test_rtruediv():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return y/x
    net = Net()
    x = ms_torch.tensor([-4.0, 2.0])
    y = 8.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 4.0])

def test_floordiv():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x//y
    net = Net()
    x = ms_torch.tensor([-4.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 1.0])

def test_rfloordiv():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return y//x
    net = Net()
    x = ms_torch.tensor([-4.0, 2.0])
    y = 8.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 4.0])

def test_ifloordiv():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            x //=y
            return x
    net = Net()
    x = ms_torch.tensor([-4.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [-2.0, 1.0])

def test_mod():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x%y
    net = Net()
    x = ms_torch.tensor([4.0, 2.0])
    y = 3.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [1.0, 2.0])

def test_rmod():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return y%x
    net = Net()
    x = ms_torch.tensor([4.0, 2.0])
    y = 5.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [1.0, 1.0])

def test_imod():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            x %= y
            return x
    net = Net()
    x = ms_torch.tensor([4.0, 2.0])
    y = 3.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [1.0, 2.0])

def test_pow():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return pow(x, y)
    net = Net()
    x = ms_torch.tensor([-1.0, 2.0])
    y = 2
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [1.0, 4.0])

def test_rpow():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return y**x
    net = Net()
    x = ms_torch.tensor([2, 1])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [4.0, 2.0])

def test_lt():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x < y
    net = Net()
    x = ms_torch.tensor([3.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [False, False])

def test_le():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x <= y
    net = Net()
    x = ms_torch.tensor([3.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [False, True])

def test_gt():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x > y
    net = Net()
    x = ms_torch.tensor([3.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [True, False])

def test_ge():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x >= y
    net = Net()
    x = ms_torch.tensor([3.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [True, True])

def test_eq():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x == y
    net = Net()
    x = ms_torch.tensor([3.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [False, True])

def test_ne():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x != y
    net = Net()
    x = ms_torch.tensor([3.0, 2.0])
    y = 2.0
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [True, False])


def test_getitem():
    class Net(ms_torch.nn.Module):
        def forward(self, x):
            return x[0]
    class Net_bool_index(ms_torch.nn.Module):
        def forward(self, x, index):
            return x[index]
    class Net_bool_index_torch(torch.nn.Module):
        def forward(self, x, index):
            return x[index]
    net = Net()
    net2 = Net_bool_index()
    net2_torch = Net_bool_index_torch()
    x = ms_torch.tensor([3.0, 2.0])

    out = net(x)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), 3.0)
    x2_torch = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    x2_ms = ms_torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    x3_torch = torch.tensor([[1, 2], [3, 4]])
    x3_ms = ms_torch.tensor([[1, 2], [3, 4]])
    index1 = ([[[True, False], [True, False]], [[True, False], [True, False]]], [[True, True], [True, False]], [True, False])
    index2 = (([True, True], [True, True]), (True, True, True, True), ([True, False], [True, False]),
              (True, False, True, False), ([True, False]), (True, False), (True, True, True),
              (True, True, False), True)
    for i in range(len(index1)):
        torch_out = net2_torch(x2_torch, torch.tensor(index1[i]))
        ms_out = net2(x2_ms, ms_torch.tensor(index1[i]))
        assert np.allclose(torch_out.numpy(), ms_out.numpy())
        assert torch_out.numpy().shape == ms_out.numpy().shape
        assert (type(ms_out) is ms_torch.Tensor) 
    for i in range(len(index2)):
        torch_out = net2_torch(x3_torch, index2[i])
        ms_out = net2(x3_ms, index2[i])
        if torch_out.shape[0] != 0:
            assert np.allclose(torch_out.numpy(), ms_out.numpy())
            assert torch_out.numpy().shape == ms_out.numpy().shape 
            assert (type(ms_out) is ms_torch.Tensor) 


def test_getitem_return_0_shape():
    class Net(ms_torch.nn.Module):
        def forward(self, x):
            return x[0]
    class Net_bool_index(ms_torch.nn.Module):
        def forward(self, x, index):
            return x[index]
    class Net_bool_index_torch(torch.nn.Module):
        def forward(self, x, index):
            return x[index]
    net2 = Net_bool_index()
    net2_torch = Net_bool_index_torch()

    index3 = [False, False, False, False]
    x4_torch = torch.tensor([[0.3, 0.2], [0.3, 0.1], [0.2, 0.3], [0.1, 0.3]])
    x4_ms = ms_torch.tensor([[0.3, 0.2], [0.3, 0.1], [0.2, 0.3], [0.1, 0.3]])
    torch_out = net2_torch(x4_torch, torch.tensor(index3))
    ms_out = net2(x4_ms, ms_torch.tensor(index3))
    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().shape == ms_out.numpy().shape
    x5_torch = torch.tensor([[[0.3], [0.2]], [[0.3], [0.1]], [[0.2], [0.3]], [[0.1], [0.3]]])
    x5_ms = ms_torch.tensor([[[0.3], [0.2]], [[0.3], [0.1]], [[0.2], [0.3]], [[0.1], [0.3]]])
    torch_out = net2_torch(x5_torch, torch.tensor(index3))
    ms_out = net2(x5_ms, ms_torch.tensor(index3))
    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().shape == ms_out.numpy().shape
    x6_torch = torch.tensor([[3, 2, 4, 1], [3, 1, 4, 0], [2, 3, 4, 1]])
    x6_ms = ms_torch.tensor([[3, 2, 4, 1], [3, 1, 4, 0], [2, 3, 4, 1]])
    index6_torch = torch.tensor([False, False, False])
    index6_ms = ms_torch.tensor([False, False, False])
    torch_out = x6_torch[index6_torch]
    ms_out = x6_ms[index6_ms]
    torch_out_ = torch_out[:, [0, 2]]
    ms_out_ = ms_out[:, [0, 2]]
    assert np.allclose(torch_out_.numpy(), ms_out_.numpy())
    assert torch_out_.numpy().shape == ms_out_.numpy().shape

def test_setitem():
    class Net(ms_torch.nn.Module):
        def forward(self, x):
            x[1]=1.0
            return x
    net = Net()
    x = ms_torch.tensor([3.0, 2.0])
    out = net(x)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), [3.0, 1.0])

def test_mutmul():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            return x @ y
    net = Net()
    x = ms_torch.tensor([[3.0, 2.0], [3.0, 2.0]])
    y = ms_torch.tensor([[3.0, 2.0], [3.0, 2.0]])
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    assert np.allclose(out.numpy(), x.numpy() @ y.numpy())

def test_imutmul():
    class Net(ms_torch.nn.Module):
        def forward(self, x, y):
            x @= y
            return x
    net = Net()
    x = ms_torch.tensor([[3.0, 2.0], [3.0, 2.0]])
    y = ms_torch.tensor([[3.0, 2.0], [3.0, 2.0]])
    out = net(x, y)
    assert (type(out) is ms_torch.Tensor)
    x_np = x.numpy()
    y_np = y.numpy()
    x_np = x_np @ y_np
    assert np.allclose(out.numpy(), x_np)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_neg()
    test_pos()
    test_invert()
    test_round()
    test_abs()
    test_add()
    test_iadd()
    test_radd()
    test_and()
    test_xor()
    test_or()
    test_sub()
    test_rsub()
    test_isub()
    test_mul()
    test_rmul()
    test_imul()
    test_truediv()
    test_rtruediv()
    test_floordiv()
    test_rfloordiv()
    test_ifloordiv()
    test_mod()
    test_rmod()
    test_imod()
    test_pow()
    test_rpow()
    test_lt()
    test_le()
    test_gt()
    test_ge()
    test_eq()
    test_ne()
    test_getitem()
    test_setitem()
    test_getitem_return_0_shape()
    test_mutmul()
    test_imutmul()

