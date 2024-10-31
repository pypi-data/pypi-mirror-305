import os
import torch
import mindspore as ms
import mindtorch.torch as ms_torch
import mindtorch.torch.nn as nn
from mindtorch.torch.nn.modules.pooling import MaxPool2d
import numpy as np
from copy import deepcopy
from typing import OrderedDict
import re

from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE, \
    SKIP_ENV_ASCEND, SKIP_ENV_GPU

set_mode_by_env_config()

def test_add_modules():
    layer1 = MaxPool2d(1, 2)
    layer2 = MaxPool2d(1, 2)
    layer1.add_module("layer2", layer2)


def test_named_children1():
    layer1 = MaxPool2d(1, 2)
    layer2 = MaxPool2d(1, 2)
    layer1.add_module("layer2", layer2)
    aa = layer1.named_children()


def test_modules():
    layer1 = MaxPool2d(1, 2)
    layer2 = MaxPool2d(1, 2)
    layer1.add_module("layer2", layer2)
    aa = layer1.modules()


def test_named_parameters():
    layer1 = MaxPool2d(1, 2)
    layer2 = MaxPool2d(1, 2)
    layer1.add_module("layer2", layer2)
    aa = layer1.named_parameters()
    for k, v in aa:
        print(k, v)

def test_named_children2():
    layer1 = MaxPool2d(1, 2)
    layer2 = MaxPool2d(1, 2)
    layer1.add_module("layer2", layer2)
    for k, v in layer1.named_children():
        print(k, v)

def test_modulelist():
    conv = nn.Conv2d(100, 20, 3)
    bn = nn.BatchNorm2d(20)
    relu = nn.ReLU()
    modulelist = nn.ModuleList([bn])
    modulelist.insert(0, conv)
    modulelist.append(relu)
    modulelist.extend([relu, relu])
    print(modulelist)


def test_apply_and_sequential():
    def init_weights(m):
        print(m)
        if type(m) == nn.Linear:
            m.weight = m.weight.fill_adapter(1.0)
            print(m.weight)

    net = nn.Sequential(nn.Conv2d(100, 20, 3), nn.Linear(2, 2), nn.Linear(2, 2))
    net.append(nn.Linear(2, 2))

    net.apply(init_weights)

class MyTorchNet(torch.nn.Module):
    def __init__(self):
        super(MyTorchNet, self).__init__()
        self.conv1 = torch.nn.Conv2d(3,32,3,1,1)
        self.relu1 = torch.nn.ReLU()
        self.max_pooling1 = torch.nn.MaxPool2d(2,1)

        self.conv2 = torch.nn.Conv2d(3,32,2,1,1)
        self.relu2 = torch.nn.ReLU()
        self.max_pooling2 = torch.nn.MaxPool2d(2,1)

        self.dense1 = torch.nn.Linear(32*3*3,128)
        self.dense2 = torch.nn.Linear(128,10)

    def forward(self,x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.max_pooling1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.max_pooling2(x)
        x = self.dense1(x)
        x = self.dense2(x)
        return x

class MyAdapterNet(ms_torch.nn.Module):
    def __init__(self):
        super(MyAdapterNet, self).__init__()
        self.conv1 = ms_torch.nn.Conv2d(3,32,3,1,1)
        self.relu1 = ms_torch.nn.ReLU()
        self.max_pooling1 = ms_torch.nn.MaxPool2d(2,1)

        self.conv2 = ms_torch.nn.Conv2d(3,32,2,1,1)
        self.relu2 = ms_torch.nn.ReLU()
        self.max_pooling2 = ms_torch.nn.MaxPool2d(2,1)

        self.dense1 = ms_torch.nn.Linear(32*3*3,128)
        self.dense2 = ms_torch.nn.Linear(128,10)

    def forward(self,x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.max_pooling1(x)

        x = self.conv2(x)
        x = self.relu2(x)
        x = self.max_pooling2(x)
        x = self.dense1(x)
        x = self.dense2(x)
        return x

def test_module_state_dict():
    torch_model = MyTorchNet()
    ms_torch_model = MyAdapterNet()
    # print(torch_model.state_dict())
    # print(ms_torch_model.state_dict())


def test_module_register():
    class MyTorchModel(torch.nn.Module):
        def __init__(self):
            super(MyTorchModel, self).__init__()
            self.register_buffer('mybuffer1', torch.tensor([2, 2]))
            self.register_parameter('my_param1', torch.nn.Parameter(torch.zeros(3, 3)))
            self.param1 = torch.ones(3, 3)

        def forward(self, x):
            return x
    class MyAdapterModel(ms_torch.nn.Module):
        def __init__(self):
            super(MyAdapterModel, self).__init__()
            self.register_buffer('mybuffer1', ms_torch.tensor([2, 2]))
            self.register_parameter('my_param1', ms_torch.nn.Parameter(ms_torch.zeros(3, 3)))
            self.param1 = ms_torch.ones(3, 3)

        def forward(self, x):
            return x

    torch_model = MyTorchModel()
    ms_mymodel = MyAdapterModel()
    assert torch_model.my_param1.size() == ms_mymodel.my_param1.size()
    assert torch_model.mybuffer1.size() == ms_mymodel.mybuffer1.size()
    assert torch_model.param1.size() == ms_mymodel.param1.size()

def test_named_modules():
    l = nn.Linear(2, 2)
    net = nn.Sequential(l, l)
    str_ms = ()
    for m in net.named_modules(prefix='aaa'):
        str_ms += m
    print(str_ms)


def test_namedbuffer():
    data1 = np.random.randn(3, 4).astype(np.float32)
    data2 = np.random.randn(3, 4).astype(np.float32)
    data3 = np.random.randn(3, 4).astype(np.float32)

    ms_t1 = ms_torch.tensor(data1)
    ms_t2 = ms_torch.tensor(data2)
    ms_t3 = ms_torch.tensor(data3)

    class Ms_Net(ms_torch.nn.Module):
        ...

    ms_net = Ms_Net()
    ms_net.register_buffer('a', ms_t1)
    ms_net.register_buffer('b', ms_t2)
    ms_net.register_buffer('c', ms_t3)

    class Torch_Net(torch.nn.Module):
        ...

    torch_t1 = torch.tensor(data1)
    torch_t2 = torch.tensor(data2)
    torch_t3 = torch.tensor(data3)

    torch_net = Torch_Net()
    torch_net.register_buffer('a', torch_t1)
    torch_net.register_buffer('b', torch_t2)
    torch_net.register_buffer('c', torch_t3)

    ms_name = []
    ms_buffer = []
    for name, buf in ms_net.named_buffers(prefix='cccc'):
        ms_name.append(name)
        ms_buffer.append(buf)

    torch_name = []
    torch_buffer = []
    for name, buf in torch_net.named_buffers(prefix='cccc'):
        torch_name.append(name)
        torch_buffer.append(buf)

    for i in range(len(torch_name)):
        assert ms_name[i] == torch_name[i]
        assert np.allclose(ms_buffer[i].numpy(), torch_buffer[i].numpy())


def test_buffer():
    data1 = np.random.randn(3, 4).astype(np.float32)
    data2 = np.random.randn(3, 4).astype(np.float32)
    data3 = np.random.randn(3, 4).astype(np.float32)

    ms_t1 = ms_torch.tensor(data1)
    ms_t2 = ms_torch.tensor(data2)
    ms_t3 = ms_torch.tensor(data3)

    class Ms_Net(ms_torch.nn.Module):
        ...

    ms_net = Ms_Net()
    ms_net.register_buffer('a', ms_t1)
    ms_net.register_buffer('b', ms_t2)
    ms_net.register_buffer('c', ms_t3)

    class Torch_Net(torch.nn.Module):
        ...

    torch_t1 = torch.tensor(data1)
    torch_t2 = torch.tensor(data2)
    torch_t3 = torch.tensor(data3)

    torch_net = Torch_Net()
    torch_net.register_buffer('a', torch_t1)
    torch_net.register_buffer('b', torch_t2)
    torch_net.register_buffer('c', torch_t3)

    ms_buffer = []
    for buf in ms_net.buffers():
        ms_buffer.append(buf)

    torch_name = []
    torch_buffer = []
    for buf in torch_net.buffers():
        torch_buffer.append(buf)

    for i in range(len(torch_name)):
        assert np.allclose(ms_buffer[i].numpy(), torch_buffer[i].numpy())

def test_register_buffer_allows_overwriting_with_same_name():
    m = nn.Module()
    buffer1 = ms_torch.rand(5)
    buffer2 = buffer1 + 5
    buffer3 = None
    m.register_buffer('buffer_name', buffer1)

    assert np.allclose((m.buffer_name).numpy(), buffer1.numpy())
    m.register_buffer('buffer_name', buffer2)
    assert np.allclose((m.buffer_name).numpy(), buffer2.numpy())
    m.register_buffer('buffer_name', buffer3)
    assert m.buffer_name is None

def test_get_buffer():
    m = nn.Module()
    buffer1 = ms_torch.randn(2, 3)
    buffer2 = ms_torch.randn(4, 5)
    m.register_buffer('foo', buffer1)
    m.register_buffer('bar', buffer2)
    assert np.allclose((m.get_buffer('foo')).numpy(), buffer1.numpy())
    assert np.allclose((m.get_buffer('bar')).numpy(), buffer2.numpy())

def test_get_buffer_from_submodules():
    class MyModule(nn.Module):
        def __init__(self, foo, bar):
            super().__init__()
            self.sub = Sub(foo, bar)

    class Sub(nn.Module):
        def __init__(self, foo, bar):
            super().__init__()
            self.register_buffer('foo', foo)
            self.subsub = SubSub(bar)

    class SubSub(nn.Module):
        def __init__(self, bar):
            super().__init__()
            self.register_buffer('bar', bar)

    foo = ms_torch.randn(2, 3)
    bar = ms_torch.randn(4, 5)
    m = MyModule(foo, bar)
    assert np.allclose((m.get_buffer('sub.foo')).numpy(), foo.numpy())
    assert np.allclose((m.get_buffer('sub.subsub.bar')).numpy(), bar.numpy())

def test_buffer_not_persistent():
    m = nn.Module()
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)
    assert len(list(m.buffers())) == 1
    # unsupported_attr(persistent)
    # assert len(m.state_dict()) == 0

def test_buffer_not_persistent_del():
    m = nn.Module()
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)
    del m.buf
    assert (len(list(m.buffers())) == 0)

def test_buffer_not_persistent_assign():
    m = nn.Module()
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)

    m.buf = None
    assert(len(list(m.buffers())) == 0)
    assert(len(m.state_dict()) == 0)
    m.buf = ms_torch.rand(5)
    assert(len(list(m.buffers())) == 1)
    # assert(len(m.state_dict()) == 0)

    # Assigning a Parameter removes the buffer.
    m.buf = nn.Parameter(ms_torch.rand(5))
    assert(len(list(m.buffers())) == 0)
    assert(len(m.state_dict()) == 1)

def _create_basic_net():
    class Layer(nn.Module):
        def __init__(self):
            super(Layer, self).__init__()
            self.layer_dummy_param = nn.Parameter(ms_torch.empty(3, 5))
            self.register_buffer('layer_dummy_buf', ms_torch.zeros(1, 3, 3, 7))

    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.l1 = Layer()
            self.dummy_param = nn.Parameter(ms_torch.empty(3, 5))
            self.register_buffer('dummy_buf', ms_torch.zeros(7, 3, 3, 1))

    l = Layer()
    n = Net()
    s = nn.Sequential(n, n)
    return l, n, s

def test_buffers_and_named_buffers():
    def names(named_buffers):
        return [k for k, _ in named_buffers]

    l, n, s = _create_basic_net()

    assert(len(list(l.buffers()))== 1)
    assert(names(l.named_buffers()) == ['layer_dummy_buf'])

    assert(len(list(n.buffers()))== 2)
    assert(names(n.named_buffers()) == ['dummy_buf', 'l1.layer_dummy_buf'])

    assert(len(list(n.buffers(recurse=False)))==1)
    assert(names(n.named_buffers(recurse=False))== ['dummy_buf'])

    assert(len(list(s.buffers()))== 2)
    assert(names(s.named_buffers())== ['0.dummy_buf', '0.l1.layer_dummy_buf'])


def test_parameters_and_named_parameters():
    def names(named_parameters):
        return [k for k, _ in named_parameters]

    l, n, s = _create_basic_net()

    assert(len(list(l.parameters()))== 1)
    assert(names(l.named_parameters()) == ['layer_dummy_param'])

    assert(len(list(n.parameters()))== 2)
    assert(names(n.named_parameters())== ['dummy_param', 'l1.layer_dummy_param'])

    assert(len(list(n.parameters(recurse=False)))== 1)
    assert(names(n.named_parameters(recurse=False)) == ['dummy_param'])

    assert(len(list(s.parameters()))== 2)
    assert(names(s.named_parameters()) == ['0.dummy_param', '0.l1.layer_dummy_param'])

def test_register_parameter_allows_overwriting_with_same_name():
    m = nn.Module()
    param1 = nn.Parameter(ms_torch.rand(5))
    param2 = nn.Parameter(param1.data + 5)
    param3 = None
    m.register_parameter('param_name', param1)
    assert np.allclose((m.param_name).numpy(), param1.numpy())
    m.register_parameter('param_name', param2)
    assert np.allclose((m.get_parameter('param_name')).numpy(), param2.numpy())
    m.register_parameter('param_name', param3)
    assert (m.param_name is None)

def test_add_module():
    methods_to_test = ['add_module', 'register_module']
    for fn in methods_to_test:
        l = nn.Linear(10, 20)
        net = nn.Module()
        net.l = l
        net.l2 = l
        getattr(net, fn)('empty', None)
        assert (net.l == l)
        assert (net.l2 == l)
        assert (net.empty is None)
        getattr(net, fn)('l3', l)
        assert (net.l3 == l)
        l3 = nn.Linear(20, 10)
        getattr(net, fn)('l', l3)
        assert (type(net.get_submodule('l')) is nn.Linear)

def test_named_children():
    l1 = nn.Linear(2, 2)
    l2 = nn.Linear(2, 2)
    l3 = nn.Linear(2, 2)
    l4 = nn.Linear(2, 2)
    subnet = nn.Sequential(l3, l4)
    s = nn.Sequential()
    s.add_module('layer1', l1)
    s.add_module('layer2', l2)
    s.add_module('layer3', l1)
    s.add_module('layer4', l2)
    s.add_module('subnet', subnet)
    assert (list(s.named_children()) == [('layer1', l1), ('layer2', l2), ('subnet', subnet)])


def test_named_and_modules():
    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.l1 = l
            self.l2 = l
            self.param = ms_torch.empty(3, 5)
            self.block = block
    l = nn.Linear(10, 20)
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(10, 20)
    block = nn.Sequential()
    block.add_module('linear1', l1)
    block.add_module('linear2', l2)
    n = Net()
    s = nn.Sequential(n, n)
    out = list(s.named_modules())
    assert (out[1][0] == '0')
    assert (out[1][1] == n)
    assert (out[2][0] == '0.l1')
    assert (out[2][1] == l)
    assert (out[3][0] == '0.block')
    assert (out[3][1] == block)
    assert (out[4][0] == '0.block.linear1')
    assert (out[4][1] == l1)
    assert (out[5][0] == '0.block.linear2')
    assert (out[5][1] == l2)


def test_type():
    model = nn.Linear(5, 5)
    original_type = model.weight.dtype
    model.type(ms_torch.float64)
    assert (model.weight.dtype == ms_torch.float64)
    model.type(original_type)
    assert (model.weight.dtype == original_type)

def test_module_to_empty():
    class MyModule(nn.Module):
        def __init__(self, in_features, out_features, dtype=None):
            super().__init__()
            self.weight = nn.Parameter(ms_torch.randn(in_features, out_features, dtype=dtype))

        def forward(self, x):
            return x @ self.weight

    # Test meta module instantiation.
    input = ms_torch.randn(5, 10, dtype=ms_torch.float32)
    m = MyModule(10, 1, dtype=ms_torch.float32)
    m(input)

    # Test materializing meta module on a real device.
    m.to_empty(device="cuda")
    m(input)
    ms_torch.nn.init.kaiming_uniform_(m.weight)
    m(input)

def test_state_dict():
    l = nn.Linear(5, 5)
    block = nn.Module()
    block.conv = nn.Conv2d(3, 3, 3, bias=False)
    net = nn.Module()
    net.linear1 = l
    net.linear2 = l
    net.bn = nn.BatchNorm2d(2)
    net.block = block
    net.add_module('empty', None)

    dicts = net.state_dict()
    state_dict = net.state_dict()
    assert(len(state_dict)== 10)
    assert(len(state_dict._metadata)== 6)
    assert('' in state_dict._metadata)
    assert('linear1' in state_dict._metadata)
    assert('linear1.weight'in state_dict)
    assert('linear1.bias'in state_dict)
    assert('linear2'in state_dict._metadata)
    assert('linear2.weight'in state_dict)
    assert('linear2.bias'in state_dict)
    assert('block'in state_dict._metadata)
    assert('block.conv'in state_dict._metadata)
    assert('block.conv.weight' in state_dict)
    assert('block.conv.weight' in state_dict)
    assert('block.conv.bias' not in state_dict)
    assert('bn' in state_dict._metadata)
    assert('bn.weight' in state_dict)
    assert('bn.bias' in state_dict)
    assert('bn.running_var' in state_dict)
    assert('bn.running_mean' in state_dict)
    assert('bn.num_batches_tracked' in state_dict)
    for k in state_dict.keys():
        assert (not k.startswith('empty'))
    for k, v in state_dict.items():
        param = net
        for component in k.split('.'):
            param = getattr(param, component)
            if isinstance(param, nn.Parameter):
                param = param.data
        assert np.allclose(v.numpy(),param.numpy())

    l = nn.Linear(5, 5)
    state_dict = l.state_dict()
    assert(len(state_dict) == 2)
    assert(len(state_dict._metadata) == 1)
    assert('' in  state_dict._metadata)
    assert(state_dict._metadata['']['version'] >= 0)
    assert np.allclose(state_dict['weight'].detach().numpy(), l.weight.detach().numpy())
    assert np.allclose(state_dict['bias'].detach().numpy(), l.bias.detach().numpy())


def test_load_state_dict():
    # set_seed to avoid nan value.
    ms.set_seed(123)
    l1 = nn.Linear(5, 5)
    l2 = nn.Linear(5, 5)
    block = nn.Module()
    block.conv1 = nn.Conv2d(3, 3, 3, bias=True)
    block.conv2 = nn.Conv2d(3, 3, 3, bias=False)
    net = nn.Module()
    net.linear1 = l1
    net.linear2 = l2
    net.bn = nn.BatchNorm2d(2)
    net.block = block
    net.add_module('empty', None)
    conv1_bias_dtype = block.conv1.bias.dtype

    state_dict = net.state_dict()
    state_dict.update({
        'linear1.weight': ms_torch.ones(5, 5),
        'block.conv1.bias': ms_torch.arange(1, 4, dtype=conv1_bias_dtype),
        'bn.running_mean': ms_torch.randn(2),
    })

    state_dict.update({'extra': ms_torch.ones(5)})
    incompatible_keys = net.load_state_dict(state_dict, strict=False)
    assert(len(incompatible_keys.missing_keys) == 0)
    #print(id(net.linear1.weight), id(net.linear2.weight))
    assert(len(incompatible_keys.unexpected_keys)== 1)
    assert('extra' in incompatible_keys.unexpected_keys)
    assert('Incompatible' in str(incompatible_keys))

    state_dict = net.state_dict()
    state_dict.update({'extra.param': ms_torch.ones(5)})
    incompatible_keys = net.load_state_dict(state_dict, strict=False)
    assert(len(incompatible_keys.missing_keys)  == 0)
    assert(len(incompatible_keys.unexpected_keys)== 1)
    assert('extra.param' in incompatible_keys.unexpected_keys)

    state_dict = net.state_dict()
    del state_dict['linear1.weight']
    incompatible_keys = net.load_state_dict(state_dict, strict=False)
    assert(len(incompatible_keys.missing_keys) == 1)
    assert(len(incompatible_keys.unexpected_keys)== 0)
    assert('linear1.weight' in incompatible_keys.missing_keys)
    state_dict.update({'extra.param': ms_torch.ones(5)})
    incompatible_keys = net.load_state_dict(state_dict, strict=False)
    assert(len(incompatible_keys.missing_keys) == 1)
    assert(len(incompatible_keys.unexpected_keys) == 1)
    assert('linear1.weight' in incompatible_keys.missing_keys)
    assert('extra.param' in incompatible_keys.unexpected_keys)

    state_dict = net.state_dict()
    state_dict.update({'bn.running_mean': ms_torch.rand(14, 4)})  # wrong size

    state_dict = net.state_dict()
    old_state_dict = deepcopy(state_dict)
    state_dict = {
        'linear1.weight': ms_torch.ones(5, 5),
        'block.conv1.bias': ms_torch.arange(1, 4, dtype=conv1_bias_dtype),
        'bn.running_mean': ms_torch.randn(2),
        'nonexistent_key': ms_torch.rand(3)
    }
    net.load_state_dict(state_dict, strict=False)
    assert np.allclose(net.linear1.weight.detach().numpy() ,state_dict['linear1.weight'].detach().numpy())
    assert np.allclose(net.block.conv1.bias.detach().numpy(), state_dict['block.conv1.bias'].detach().numpy())
    assert np.allclose(net.bn.running_mean.detach().numpy(), state_dict['bn.running_mean'].detach().numpy())
    new_state_dict = net.state_dict()
    del old_state_dict['linear1.weight']
    del old_state_dict['block.conv1.bias']
    del old_state_dict['bn.running_mean']
    for k, v, in old_state_dict.items():
        assert np.allclose(new_state_dict[k].numpy(), v.numpy(), equal_nan=True)


def test_children():
    l1 = nn.Linear(2, 2)
    l2 = nn.Linear(2, 2)
    l3 = nn.Linear(2, 2)
    l4 = nn.Linear(2, 2)
    subnet = nn.Sequential(l3, l4)
    s = nn.Sequential(l1, l2, l1, l2, subnet)
    out = list(s.children())
    assert (out[0] == l1)
    assert (out[1] == l2)
    assert (out[2] == subnet)


# nn.LSTM use _DynamicGRUCPUGPU, it has something wrong
def test_load_state_dict_ref_cycle():
    import gc
    m = nn.LSTM(16, 16, bidirectional=True)
    state_dict = m.state_dict()
    gc.collect()
    m_copy = deepcopy(m)
    state_dict = m_copy.state_dict()
    m.load_state_dict(state_dict)
    refcycles = gc.collect()
    # _convert_state_dict, cast_to_ms_tensor, ms.Parameter, load_param_into_net will create some staff that need to refcycles
    # assert(refcycles == 0)


def _create_basic_net():
    class Layer(nn.Module):
        def __init__(self):
            super().__init__()
            self.layer_dummy_param = nn.Parameter(ms_torch.empty(3, 5))
            self.register_buffer('layer_dummy_buf', ms_torch.zeros(1, 3, 3, 7))

    class Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.l1 = Layer()
            self.dummy_param = nn.Parameter(ms_torch.empty(3, 5))
            self.register_buffer('dummy_buf', ms_torch.zeros(7, 3, 3, 1))

    l = Layer()
    n = Net()
    s = nn.Sequential(n, n)

    return l, n, s

def test_requires_grad_():
    m = _create_basic_net()[-1]
    assert len(list(m.buffers())) > 0, 'invalid test'
    assert all(p.requires_grad for p in m.parameters()) > 0, 'invalid test'
    for requires_grad in (False, True):
        m.requires_grad_(requires_grad)
        for p in m.parameters():
            assert p.requires_grad == requires_grad


def test_named_parameters_remove_duplicate():
    def names(named_parameters):
        return [k for k, _ in named_parameters]

    class M1(nn.Module):
        def __init__(self):
            super().__init__()
            self.param1 = nn.Parameter(ms_torch.empty(3, 3))
            self.param2 = self.param1

    m1 = M1()
    assert names(m1.named_parameters()) == ["param1"]
    assert names(m1.named_parameters(remove_duplicate=False)) == ["param1", "param2"]

    class M2(nn.Module):
        def __init__(self):
            super().__init__()
            self.mod1 = nn.Linear(3, 4, bias=False)
            self.mod2 = self.mod1

    m2 = M2()
    assert names(m2.named_parameters()) == ["mod1.weight"]
    assert names(m2.named_parameters(remove_duplicate=False)) == ["mod1.weight", "mod2.weight"]


def test_buffers_and_named_buffers():
    def names(named_buffers):
        return [k for k, _ in named_buffers]

    l, n, s = _create_basic_net()

    assert len(list(l.buffers())) == 1
    assert names(l.named_buffers()) == ['layer_dummy_buf']

    assert len(list(n.buffers())) == 2
    assert names(n.named_buffers()) == ['dummy_buf', 'l1.layer_dummy_buf']

    assert len(list(n.buffers(recurse=False))) == 1
    assert names(n.named_buffers(recurse=False)) == ['dummy_buf']

    assert len(list(s.buffers())) == 2
    assert names(s.named_buffers()) == ['0.dummy_buf', '0.l1.layer_dummy_buf']

    # test remove_duplicate
    class M(nn.Module):
        def __init__(self):
            super().__init__()
            self.register_buffer("buffer1", ms_torch.empty(3, 5))
            self.register_buffer("buffer2", self.buffer1)

    m = M()
    assert names(m.named_buffers()) == ["buffer1"]
    assert names(m.named_buffers(remove_duplicate=False)) == ["buffer1", "buffer2"]

def test_children():
    l1 = nn.Linear(2, 2)
    l2 = nn.Linear(2, 2)
    l3 = nn.Linear(2, 2)
    l4 = nn.Linear(2, 2)
    subnet = nn.Sequential(l3, l4)
    s = nn.Sequential(l1, l2, l1, l2, subnet)
    assert list(s.children()) == [l1, l2, subnet]

def test_dir():
    linear = nn.Linear(2, 2)
    linear._test_submodule = nn.Linear(2, 2)
    linear._test_parameter = nn.Parameter(ms_torch.empty(2, 2))
    linear.register_buffer('_test_buffer', ms_torch.empty(2, 2))
    keys = dir(linear)
    assert '_test_submodule' in keys
    assert '_test_parameter' in keys
    assert '_test_buffer' in keys

def test_repr():
    # no extra information or sub-modules
    empty_sequential = nn.Sequential()
    expected_repr_empty = 'Sequential()'
    assert repr(empty_sequential) == expected_repr_empty

    # one liner extra information
    linear = nn.Linear(1, 1)
    expected_repr_linear = 'Linear(in_features=1, out_features=1, bias=True)'
    assert repr(linear) == expected_repr_linear

    # sub-modules repr
    sequential = nn.Sequential(linear)
    expected_repr_sequential = 'Sequential(\n' \
        '  (0): Linear(in_features=1, out_features=1, bias=True)\n' \
        ')'
    assert repr(sequential) == expected_repr_sequential

def test_dir_digit():
    model = nn.Sequential(nn.Linear(2, 2))
    keys = dir(model)
    assert '0' not in keys

def test_named_children():
    l1 = nn.Linear(2, 2)
    l2 = nn.Linear(2, 2)
    l3 = nn.Linear(2, 2)
    l4 = nn.Linear(2, 2)
    subnet = nn.Sequential(l3, l4)
    s = nn.Sequential()
    try:
        s.add_module('', l1)
        assert False
    except KeyError as e:
        ...
    try:
        s.add_module('name.with.dot', l1)
        assert False
    except KeyError as e:
        ...
    s.add_module('layer1', l1)
    s.add_module('layer2', l2)
    s.add_module('layer3', l1)
    s.add_module('layer4', l2)
    s.add_module('subnet', subnet)
    assert list(s.named_children()) == [('layer1', l1), ('layer2', l2), ('subnet', subnet)]

def test_modules_2():
    class Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.l1 = l
            self.l2 = l
            self.param = torch.empty(3, 5)

    l = nn.Linear(10, 20)
    n = Net()
    s = nn.Sequential(n, n, n, n)
    assert list(s.modules()) == [s, n, l]


def test_named_modules_2():
    class Net(nn.Module):
        def __init__(self):
            super().__init__()
            self.l1 = l
            self.l2 = l
            self.param = torch.empty(3, 5)
            self.block = block
    l = nn.Linear(10, 20)
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(10, 20)
    block = nn.Sequential()
    block.add_module('linear1', l1)
    block.add_module('linear2', l2)
    n = Net()
    s = nn.Sequential(n, n)
    assert list(s.named_modules()) == [('', s), ('0', n), ('0.l1', l),
                                       ('0.block', block), ('0.block.linear1', l1),
                                       ('0.block.linear2', l2)]
    # test the option to not remove duplicate module instances
    assert list(s.named_modules(remove_duplicate=False)) == [
        ('', s), ('0', n), ('0.l1', l), ('0.l2', l),
        ('0.block', block), ('0.block.linear1', l1),
        ('0.block.linear2', l2),
        ('1', n), ('1.l1', l), ('1.l2', l),
        ('1.block', block), ('1.block.linear1', l1),
        ('1.block.linear2', l2)]

def test_register_buffer_raises_error_if_name_is_not_string():
    m = nn.Module()
    expected_error = 'buffer name should be a string. Got '
    try:
        m.register_buffer(1, torch.rand(5))
        assert False
    except TypeError as e:
        assert str(e) == expected_error + '<class \'int\'>'
    try:
        m.register_buffer(None, torch.rand(5))
        assert False
    except TypeError as e:
        assert str(e) == expected_error + '<class \'NoneType\'>'

def test_register_buffer_raises_error_if_attr_exists():
    m = nn.Module()
    m.attribute_name = 5
    expected_error = "\"attribute 'attribute_name' already exists\""
    try:
        m.register_buffer('attribute_name', ms_torch.rand(5))
        assert False
    except KeyError as e:
        assert str(e) == expected_error

    del m.attribute_name
    m.register_parameter('attribute_name', nn.Parameter(ms_torch.Tensor()))
    try:
        m.register_buffer('attribute_name', ms_torch.Tensor())
        assert False
    except KeyError as e:
        assert str(e) == expected_error

    del m.attribute_name
    m.add_module('attribute_name', nn.Module())
    try:
        m.register_buffer('attribute_name', ms_torch.Tensor())
        assert False
    except KeyError as e:
        assert str(e) == expected_error

def test_register_buffer_raises_error_if_not_tensor():
    m = nn.Module()
    error_msg = "cannot assign '<class 'int'>' object to buffer 'attribute_name' (Tensor or None required)"
    try:
        m.register_buffer('attribute_name', 5)
        assert False
    except TypeError as e:
        assert str(e) == error_msg

def test_get_buffer():
    m = nn.Module()
    buffer1 = ms_torch.randn(2, 3)
    buffer2 = ms_torch.randn(4, 5)
    m.register_buffer('foo', buffer1)
    m.register_buffer('bar', buffer2)
    assert np.allclose(buffer1.numpy(), m.get_buffer('foo').numpy())
    assert np.allclose(buffer2.numpy(), m.get_buffer('bar').numpy())

def test_get_buffer_from_submodules():
    class MyModule(nn.Module):
        def __init__(self, foo, bar):
            super().__init__()
            self.sub = Sub(foo, bar)

    class Sub(nn.Module):
        def __init__(self, foo, bar):
            super().__init__()
            self.register_buffer('foo', foo)
            self.subsub = SubSub(bar)

    class SubSub(nn.Module):
        def __init__(self, bar):
            super().__init__()
            self.register_buffer('bar', bar)

    foo = ms_torch.randn(2, 3)
    bar = ms_torch.randn(4, 5)
    m = MyModule(foo, bar)
    assert np.allclose(foo.numpy(), m.get_buffer('sub.foo').numpy())
    assert np.allclose(bar.numpy(), m.get_buffer('sub.subsub.bar').numpy())

def test_buffer_not_persistent():
    m = nn.Module()
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)
    assert len(list(m.buffers())) == 1
    assert len(m.state_dict()) == 0

def test_buffer_not_persistent_del():
    m = nn.Module()
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)
    del m.buf
    assert len(list(m.buffers())) == 0

def test_buffer_not_persistent_overwrite():
    m = nn.Module()
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)
    m.register_buffer('buf', ms_torch.rand(5))

    # can we overwrite a non-persistent buffer with a persistent one?
    assert len(list(m.buffers())) == 1
    assert len(m.state_dict()) == 1

    # can we overwrite a persistent buffer with a non-persistent one?
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)
    assert len(list(m.buffers())) == 1
    assert len(m.state_dict()) == 0

def test_buffer_not_persistent_assign():
    m = nn.Module()
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)

    # Assigning None removes the buffer but if we then assign a new Tensor
    # to the same property, it should still be marked as a buffer.
    m.buf = None
    assert len(list(m.buffers())) == 0
    assert len(m.state_dict()) == 0
    m.buf = ms_torch.rand(5)
    assert len(list(m.buffers())) == 1
    assert len(m.state_dict()) == 0
    # Assigning a Parameter removes the buffer.
    m.buf = nn.Parameter(ms_torch.rand(5))
    assert len(list(m.buffers())) == 0
    assert len(m.state_dict()) == 1

def test_load_state_dict_invalid():
    error_msg = "expected torch.Tensor or Tensor-like object"
    m = nn.Linear(2, 2, bias=False)

    state_dict = {'weight': np.random.randn(2, 2)}
    try:
        m.load_state_dict(state_dict)
        assert False
    except RuntimeError as e:
        assert re.search(error_msg, str(e))
    state_dict = {'weight': ((1., 1.), (2., 2.))}
    try:
        m.load_state_dict(state_dict)
        assert False
    except RuntimeError as e:
        assert re.search(error_msg, str(e))

def test_load_state_dict_type():
    m = nn.Module()
    error_msg = "Expected state_dict to be dict-like"
    try:
        m.load_state_dict("")
        assert False
    except TypeError as e:
        assert re.search(error_msg, str(e))

    try:
        m.load_state_dict(2)
        assert False
    except TypeError as e:
        assert re.search(error_msg, str(e))

def test_buffer_not_persistent_load():
    m = nn.Module()
    m.register_buffer('buf', ms_torch.rand(5), persistent=False)
    m.load_state_dict({})

def test_register_parameter_raises_error_if_name_is_not_string():
    m = nn.Module()
    expected_error = 'parameter name should be a string. Got '
    try:
        m.register_parameter(1, nn.Parameter(ms_torch.Tensor()))
        assert False
    except TypeError as e:
        assert re.search(expected_error, str(e))
    try:
        m.register_parameter(None, nn.Parameter(ms_torch.Tensor()))
        assert False
    except TypeError as e:
        assert re.search(expected_error, str(e))

def test_register_parameter_raises_error_if_attr_exists():
    m = nn.Module()
    m.attribute_name = 5
    error_msg = "attribute 'attribute_name' already exists"

    try:
        m.register_parameter('attribute_name', nn.Parameter(ms_torch.Tensor()))
        assert False
    except KeyError as e:
        assert re.search(error_msg, str(e))

    del m.attribute_name
    m.register_buffer('attribute_name', ms_torch.rand(5))
    try:
        m.register_parameter('attribute_name', nn.Parameter(ms_torch.Tensor()))
        assert False
    except KeyError as e:
        assert re.search(error_msg, str(e))

    del m.attribute_name
    m.add_module('attribute_name', nn.Module())
    try:
        m.register_parameter('attribute_name', nn.Parameter(ms_torch.Tensor()))
        assert False
    except KeyError as e:
        assert re.search(error_msg, str(e))

def test_register_parameter_allows_overwriting_with_same_name():
    m = nn.Module()
    param1 = nn.Parameter(ms_torch.rand(5))
    param2 = nn.Parameter(param1.data + 5)
    param3 = None
    m.register_parameter('param_name', param1)
    assert np.allclose(m.param_name.numpy(), param1.numpy())
    m.register_parameter('param_name', param2)
    assert np.allclose(m.param_name.numpy(), param2.numpy())
    m.register_parameter('param_name', param3)
    assert m.param_name == param3

def test_add_module_raises_error_if_attr_exists():
    methods_to_test = ['add_module', 'register_module']
    error_msg = "already exists"
    for fn in methods_to_test:
        m = nn.Module()
        m.attribute_name = 5
        try:
            getattr(m, fn)('attribute_name', nn.Module())
            assert False
        except KeyError as e:
            assert re.search(error_msg, str(e))

        del m.attribute_name
        m.register_buffer('attribute_name', ms_torch.rand(5))
        try:
            getattr(m, fn)('attribute_name', nn.Module())
            assert False
        except KeyError as e:
            assert re.search(error_msg, str(e))

        del m.attribute_name
        m.register_parameter('attribute_name', nn.Parameter(ms_torch.rand(5)))
        try:
            getattr(m, fn)('attribute_name', nn.Module())
            assert False
        except KeyError as e:
            assert re.search(error_msg, str(e))

def test_getattr_with_property():
    error_msg = "The 'Model' object has no attribute 'some_property'"
    class Model(nn.Module):
        @property
        def some_property(self):
            return self.something_that_doesnt_exist

    model = Model()
    try:
        model.some_property
        assert False
    except AttributeError as e:
        assert re.search(error_msg, str(e))


def test_Sequential_getitem():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(l1, l2, l3, l4)
    assert n[0] == l1
    assert n[1] == l2
    assert n[2] == l3
    assert n[3] == l4
    assert n[ms_torch.tensor(3, dtype=ms_torch.int64)] == l4

    tmp = nn.Sequential(l2, l3, l4)
    n_tmp = n[1:]
    assert len(n_tmp) == 3
    for i in range(len(n_tmp)):
        assert n_tmp[i] == tmp[i]

    tmp = nn.Sequential(l4)
    n_tmp = n[3:]
    assert len(n_tmp) == 1
    for i in range(len(n_tmp)):
        assert n_tmp[i] == tmp[i]

    tmp = nn.Sequential(l1, l2, l3)
    n_tmp = n[:-1]
    assert len(n_tmp) == 3
    for i in range(len(n_tmp)):
        assert n_tmp[i] == tmp[i]

    tmp = nn.Sequential(l1)
    n_tmp = n[:-3]
    assert len(n_tmp) == 1
    for i in range(len(n_tmp)):
        assert n_tmp[i] == tmp[i]

    tmp = nn.Sequential(l4, l3, l2, l1)
    n_tmp = n[::-1]
    assert len(n_tmp) == 4
    for i in range(len(n_tmp)):
        assert n_tmp[i] == tmp[i]

def test_Sequential_setitem():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(l1, l2, l3)
    n[0] = l4
    n[-1] = l4
    n[ms_torch.tensor(1, dtype=ms_torch.int16)] = l1
    assert n[0] == l4
    assert n[1] == l1
    assert n[2] == l4

def test_Sequential_setitem_named():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(OrderedDict([
        ('linear1', l1),
        ('linear2', l2),
        ('linear3', l3),
    ]))

    n[0] = l4
    n[-1] = l4
    assert n.linear1 == l4
    assert n.linear3 == l4

def test_Sequential_delitem():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(l1, l2, l3, l4)

    del n[-1]
    tmp = nn.Sequential(l1, l2, l3)
    assert len(n) == 3
    for i in range(len(n)):
        assert n[i] == tmp[i]

    del n[1::2]
    tmp = nn.Sequential(l1, l3)
    assert len(n) == 2
    for i in range(len(n)):
        assert n[i] == tmp[i]

def test_Sequential_add():
    l1 = nn.Linear(1, 2)
    l2 = nn.Linear(2, 3)
    l3 = nn.Linear(3, 4)
    l4 = nn.Linear(4, 5)
    n = nn.Sequential(l1, l2)
    other = nn.Sequential(l3, l4)

    n += other
    tmp = nn.Sequential(l1, l2, l3, l4)
    assert len(n) == 4
    for i in range(len(n)):
        assert n[i] == tmp[i]

def test_Sequential_iadd():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(l1, l2, l3)
    n2 = nn.Sequential(l4)
    n += n2
    n2 += n

    tmp = nn.Sequential(l1, l2, l3, l4)
    assert len(n) == 4
    for i in range(len(n)):
        assert n[i] == tmp[i]

    tmp = nn.Sequential(l4, l1, l2, l3, l4)
    assert len(n2) == 5
    for i in range(len(n2)):
        assert n2[i] == tmp[i]

def test_Sequential_mul():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(l1, l2, l3, l4)
    n2 = n * 2
    tmp = nn.Sequential(l1, l2, l3, l4, l1, l2, l3, l4)
    assert len(n2) == 8
    for i in range(len(n2)):
        assert n2[i] == tmp[i]


def test_Sequential_rmul():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(l1, l2, l3, l4)
    n2 = 2 * n
    tmp = nn.Sequential(l1, l2, l3, l4, l1, l2, l3, l4)
    assert len(n2) == 8
    for i in range(len(n2)):
        assert n2[i] == tmp[i]

def test_Sequential_imul():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(l1, l2, l3, l4)
    n *= 2

    tmp = nn.Sequential(l1, l2, l3, l4, l1, l2, l3, l4)
    assert len(n) == 8
    for i in range(len(n)):
        assert n[i] == tmp[i]

    n *= 2
    tmp = nn.Sequential(l1, l2, l3, l4, l1, l2, l3, l4, l1, l2, l3, l4, l1, l2, l3, l4)
    assert len(n) == 16
    for i in range(len(n)):
        assert n[i] == tmp[i]

def test_Sequential_append():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n = nn.Sequential(l1, l2, l3)
    n2 = n.append(l4)

    tmp = nn.Sequential(l1, l2, l3, l4)
    assert len(n) == 4
    for i in range(len(n)):
        assert n[i] == tmp[i]

    tmp = nn.Sequential(l1, l2, l3, l4)
    assert len(n2) == 4
    for i in range(len(n2)):
        assert n2[i] == tmp[i]

    n3 = nn.Sequential(l1).append(l2).append(l4)
    tmp = nn.Sequential(l1, l2, l4)
    assert len(n3) == 3
    for i in range(len(n3)):
        assert n3[i] == tmp[i]

def test_Sequential_pop():
    l1 = nn.Linear(1, 2)
    l2 = nn.Linear(2, 3)
    l3 = nn.Linear(3, 4)
    l4 = nn.Linear(4, 5)
    n1 = nn.Sequential(l1, l2, l3, l4)
    assert l4 == n1.pop(3)
    n2 = nn.Sequential(l1, l2, l3)
    assert len(n1) == 3
    for i in range(len(n1)):
        assert n1[i] == n2[i]
    # check order of the index
    for k, mod in zip(range(len(n1)), n1):
        assert n1[k] == mod

def test_Sequential_insert():
    l1 = nn.Linear(1, 2)
    l2 = nn.Linear(2, 3)
    l3 = nn.Linear(3, 4)

    n1 = nn.Sequential(l1, l2, l3)
    module_1 = nn.Linear(4, 5)
    n2 = nn.Sequential(l1, module_1, l2, l3)
    n1.insert(1, module_1)
    assert len(n1) == 4
    for i in range(len(n1)):
        assert n1[i] == n2[i]

    # test for negative support
    n3 = nn.Sequential(l1, l2, l3)
    module_2 = nn.Linear(5, 6)
    n4 = nn.Sequential(l1, module_2, l2, l3)
    n3.insert(-2, module_2)
    assert len(n3) == 4
    for i in range(len(n1)):
        assert n3[i] == n4[i]

def test_Sequential_insert_fail_case():
    error_msg1 = "the value of 'index' must be a number in range"
    error_msg2 = "each cell must be subclass of Cell"

    l1 = nn.Linear(1, 2)
    l2 = nn.Linear(2, 3)
    l3 = nn.Linear(3, 4)

    module = nn.Linear(5, 6)

    # test for error case
    n1 = nn.Sequential(l1, l2, l3)
    try:
        n1.insert(-5, module)
        assert False
    except IndexError as e:
        assert re.search(error_msg1, str(e))

    try:
        n1.insert(1, [nn.Linear(6, 7)])
        assert False
    except TypeError as e:
        assert re.search(error_msg2, str(e))

def test_Sequential_extend():
    l1 = nn.Linear(10, 20)
    l2 = nn.Linear(20, 30)
    l3 = nn.Linear(30, 40)
    l4 = nn.Linear(40, 50)
    n1 = nn.Sequential(l1, l2)
    n2 = nn.Sequential(l3, l4)
    n3 = nn.Sequential(l1, l2)
    for l in n2:
        n1.append(l)
    n3.extend(n2)
    for i in range(len(n1)):
        assert n3[i] == n1[i]

def test_batchnorm_buffer_load():
    a = ms_torch.nn.BatchNorm1d(2)
    b = a.state_dict()
    _num = ms_torch.tensor(np.random.randint(1))
    b['num_batches_tracked'] = _num
    a.load_state_dict(b)
    param_compare(a.num_batches_tracked, _num)

def test_batchnorm_state_dict_no_num_batches_tracked():
    def load_from_torch_checkpoint():
        pt_a = torch.nn.BatchNorm1d(2)
        pt_state = pt_a.state_dict()
        del pt_state['num_batches_tracked']
        torch.save(pt_state, 'a.pth')

        pt_s = ms_torch.load('a.pth')
        a = ms_torch.nn.BatchNorm1d(2)
        a.load_state_dict(pt_s)

    def load_with_unexpected_keys():
        a = ms_torch.nn.BatchNorm1d(2)
        b = a.state_dict()
        a = ms_torch.nn.BatchNorm1d(2, track_running_stats=False)
        try:
            a.load_state_dict(b)
            assert False      # should raise RuntimeError, but not.
        except Exception as e:
            assert ("Unexpected key(s)" in str(e))

    def load_from_torch_checkpoint():
        pt_a = torch.nn.BatchNorm1d(2, track_running_stats=False, affine=False)
        pt_state = pt_a.state_dict()
        torch.save(pt_state, 'a.pth')

        pt_s = ms_torch.load('a.pth')
        a = ms_torch.nn.BatchNorm1d(2, track_running_stats=False, affine=False)
        a.load_state_dict(pt_s)

    load_from_torch_checkpoint()
    load_with_unexpected_keys()
    load_from_torch_checkpoint()
    os.remove('a.pth')

def test_instance_norm_load():
    def test_load_from_pt_state():
        a = torch.nn.InstanceNorm1d(2, track_running_stats=False, affine=True)
        b = a.state_dict()
        torch.save(b, 'a.pth')

        pt_s = ms_torch.load('a.pth')
        a = ms_torch.nn.InstanceNorm1d(2, track_running_stats=False, affine=True)
        a.load_state_dict(pt_s)

    def test_load_from_pt_state_track():
        a = torch.nn.InstanceNorm1d(2, track_running_stats=True, affine=False)
        b = a.state_dict()
        torch.save(b, 'a.pth')

        pt_s = ms_torch.load('a.pth')
        a = ms_torch.nn.InstanceNorm1d(2, track_running_stats=True, affine=False)
        a.load_state_dict(pt_s)

    def test_load_from_ms_state():
        a = ms_torch.nn.InstanceNorm1d(2, track_running_stats=True, affine=False)
        b = a.state_dict()
        ms_torch.save(b, 'a.pth')

        pt_s = ms_torch.load('a.pth')
        a = ms_torch.nn.InstanceNorm1d(2, track_running_stats=True, affine=False)
        a.load_state_dict(pt_s)


    test_load_from_pt_state()
    test_load_from_pt_state_track()
    test_load_from_ms_state()
    os.remove('a.pth')

def test_load_from_state_dict_get_version():
    '''
    testcase for the case that rewrite '_load_from_state_dict' and need 'local_metadata'
    '''
    class BN(ms_torch.nn.Module):
        def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict,
                                  missing_keys, has_load, error_msgs):
            version = local_metadata.get("version", None) # ensure to get local_metadata
            if version is None or version < 2:
                pass
            else:
                # version is None, should not enter this branch.
                assert False
            super()._load_from_state_dict(state_dict, prefix, local_metadata,
                                          strict, missing_keys, has_load, error_msgs)

    bn = BN()
    s = bn.state_dict()
    bn.load_state_dict(s)

def test_register_none_param():
    class PTNet(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.register_parameter('b', None)
            self.c = None

    pt_net = PTNet()
    pt_net.b = torch.nn.Parameter(torch.tensor(1.))
    pt_net.c = torch.nn.Parameter(torch.tensor(2.))

    class MSNet(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.register_parameter('b', None)
            self.c = None

    ms_net = MSNet()
    ms_net.b = ms_torch.nn.Parameter(ms_torch.tensor(1.))
    ms_net.c = ms_torch.nn.Parameter(ms_torch.tensor(2.))

    param_compare(pt_net.b.detach(), ms_net.b.detach())
    param_compare(pt_net.c.detach(), ms_net.c.detach())


def test_modules_duplicate_assign():
    class tr_Net(torch.nn.Module):
        def __init__(self, learn):
            super().__init__()
            self.alpha = 2
            self.register_parameter('c', None)
            if learn:
                self.alpha = torch.nn.Parameter(torch.tensor(2.))
                self.c = torch.nn.Parameter(torch.tensor(1.))
        def forward(self, x):
            return x * self.alpha * self.c

    net = tr_Net(True)
    tr_result = net(torch.tensor(3.))


    class Net(ms_torch.nn.Module):
        def __init__(self, learn):
            super().__init__()
            self.alpha = 2
            self.register_parameter('c', None)
            if learn:
                self.alpha = ms_torch.nn.Parameter(ms_torch.tensor(2.))
                self.c = ms_torch.nn.Parameter(ms_torch.tensor(1.))
        def forward(self, x):
            return x * self.alpha * self.c

    net = Net(True)
    ms_result = net(ms_torch.tensor(3.))

    param_compare(tr_result.detach(), ms_result.detach())


def test_module_lazy_param_name():
    class SubNet(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.register_parameter('a', ms_torch.nn.Parameter(ms_torch.tensor(2.)))
            self.register_parameter('b', None)

    class Net(ms_torch.nn.Module):
        def __init__(self, subnet):
            super().__init__()
            self.sub = subnet

    sub = SubNet()
    net = Net(sub)
    net.sub.b = ms_torch.nn.Parameter(ms_torch.tensor(1.))
    for v in list(net.parameters()):
        prefix = v.name.split(".")[:-1][0]
        assert prefix == "sub"

def test_module_lazy_param_name_2():
    class Net(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.conv = ms_torch.nn.Conv2d(2, 3, 4, bias=False)
            self.bn = ms_torch.nn.BatchNorm2d(3)
            self.linear = ms_torch.nn.Linear(3, 1, bias=False)

    model = Net()
    model.conv.bias = ms_torch.nn.Parameter(ms_torch.tensor(2.))
    model.linear.bias = ms_torch.nn.Parameter(ms_torch.tensor(1.))
    for _, _ in model.named_parameters():
        pass

    name_set = set()

    for v in model.modules():
        for _, p in v.named_parameters(recurse=0):
            assert p.name not in name_set
            name_set.add(p.name)


def test_norm_running_mean_var_not_in_parameters():
    class SubNet(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.bn = ms_torch.nn.BatchNorm2d(3)
    class Net(ms_torch.nn.Module):
        def __init__(self, subnet):
            super().__init__()
            self.bn = ms_torch.nn.BatchNorm2d(2)
            self.sub = subnet

    net = Net(SubNet())

    param_set = set()
    buffer_set = set()

    for name, _ in list(net.named_parameters()):
        _name = name.split('.')[-1]
        param_set.add(_name)

    for name, _ in list(net.named_buffers()):
        _name = name.split('.')[-1]
        buffer_set.add(_name)

    assert "running_mean" not in param_set
    assert "running_var" not in param_set
    assert "running_mean" in buffer_set
    assert "running_var" in buffer_set

def test_other_modules_running_mean_var_in_parameters():
    class SubNet(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.running_mean = ms_torch.nn.Parameter(ms_torch.tensor(3.))
            self.running_var = ms_torch.nn.Parameter(ms_torch.tensor(3.))

    class Net(ms_torch.nn.Module):
        def __init__(self, subnet):
            super().__init__()
            self.running_mean = ms_torch.nn.Parameter(ms_torch.tensor(3.))
            self.running_var = ms_torch.nn.Parameter(ms_torch.tensor(3.))
            self.sub = subnet

    net = Net(SubNet())

    param_set = set()
    buffer_set = set()

    for name, _ in list(net.named_parameters()):
        _name = name.split('.')[-1]
        param_set.add(_name)

    for name, _ in list(net.named_buffers()):
        _name = name.split('.')[-1]
        buffer_set.add(_name)

    assert "running_mean" in param_set
    assert "running_var" in param_set
    assert "running_mean" not in buffer_set
    assert "running_var" not in buffer_set

def test_register_buffer_duplicate():
    """
    testcase to guarantee only subclass of class _NormBase can
    duplicately register_buffer with name in 'running_mean' and 'running_var'.
    Other case will raise error as usual.
    """

    class Net(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.a = torch.nn.Parameter(torch.tensor(2.))
            self.register_buffer('a', torch.tensor(1.))

    try:
        net = Net()
    except Exception as e:
        assert "already exists" in str(e)

    class Net(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.a = ms_torch.nn.Parameter(ms_torch.tensor(2.))
            self.register_buffer('a', ms_torch.tensor(1.))
    try:
        net = Net()
    except Exception as e:
        assert "already exists" in str(e)

    class Net(ms_torch.nn.modules.batchnorm._NormBase):
        def __init__(self):
            super().__init__(3) # allow register buffer and Parameters with name in 'running_mean' and 'running_var' 
    try:
        net = Net()
    except Exception as e:
        assert False, str(e)

    class Net(ms_torch.nn.modules.batchnorm._NormBase):
        def __init__(self):
            super().__init__(3)
            # name beside 'running_mean' and 'running_var' not allow duplicate registration
            self.test_a = ms_torch.nn.Parameter(ms_torch.tensor(2.))
            self.register_buffer('test_a', ms_torch.tensor(1.))
    try:
        net = Net()
    except Exception as e:
        assert "already exists" in str(e)


def test_norm_base_register_buffer_twice():
    class Pt_Net(torch.nn.modules.batchnorm._NormBase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    pt_net = Pt_Net(3)

    class Ms_Net(ms_torch.nn.modules.batchnorm._NormBase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    ms_net = Ms_Net(3)

    def test_with_register_buffer():
        pt_net.register_buffer('running_var', torch.tensor(2.))
        pt_net.register_buffer('running_mean', torch.tensor(4.))
        ms_net.register_buffer('running_var', ms_torch.tensor(2.))
        ms_net.register_buffer('running_mean', ms_torch.tensor(4.))

        param_compare(pt_net.running_var, ms_net.running_var)
        param_compare(pt_net.running_mean, ms_net.running_mean)

        pt_net.register_buffer('running_var', None)
        pt_net.register_buffer('running_mean', None)
        ms_net.register_buffer('running_var', None)
        ms_net.register_buffer('running_mean', None)

        assert pt_net.running_var is None
        assert pt_net.running_mean is None
        assert ms_net.running_var is None
        assert ms_net.running_mean is None

        pt_net.register_buffer('running_var', torch.tensor(2.))
        pt_net.register_buffer('running_mean', torch.tensor(4.))
        ms_net.register_buffer('running_var', ms_torch.tensor(2.))
        ms_net.register_buffer('running_mean', ms_torch.tensor(4.))

        param_compare(pt_net.running_var, ms_net.running_var)
        param_compare(pt_net.running_mean, ms_net.running_mean)

    def test_with_direct_assign():
        pt_net.running_var = torch.tensor(5.)
        ms_net.running_var = ms_torch.tensor(5.)
        pt_net.running_mean = torch.tensor(6.)
        ms_net.running_mean = ms_torch.tensor(6.)
        param_compare(pt_net.running_var, ms_net.running_var)
        param_compare(pt_net.running_mean, ms_net.running_mean)

        pt_net.running_var = None
        ms_net.running_var = None
        pt_net.running_mean = None
        ms_net.running_mean = None
        assert pt_net.running_var is None
        assert pt_net.running_mean is None
        assert ms_net.running_var is None
        assert ms_net.running_mean is None

        pt_net.running_var = torch.tensor(7.)
        ms_net.running_var = ms_torch.tensor(7.)
        pt_net.running_mean = torch.tensor(8.)
        ms_net.running_mean = ms_torch.tensor(8.)
        param_compare(pt_net.running_var, ms_net.running_var)
        param_compare(pt_net.running_mean, ms_net.running_mean)

    def test_delete_attr():
        delattr(pt_net, 'running_mean')
        delattr(pt_net, 'running_var')
        delattr(ms_net, 'running_mean')
        delattr(ms_net, 'running_var')
        pt_net.running_var = torch.tensor(9.)
        ms_net.running_var = ms_torch.tensor(9.)
        pt_net.running_mean = torch.tensor(10.)
        ms_net.running_mean = ms_torch.tensor(10.)
        param_compare(pt_net.running_var, ms_net.running_var)
        param_compare(pt_net.running_mean, ms_net.running_mean)

    test_with_register_buffer()
    test_with_direct_assign()
    test_delete_attr()

def test_parameters_and_modules_property():
    class PT_Sub(torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.test_param2 = torch.nn.Parameter(torch.tensor(2.))
    class PT_Net(torch.nn.Module):
        def __init__(self, sub):
            super().__init__()
            self.sub = sub

    pt_net = PT_Net(PT_Sub())
    pt_net._parameters['test_param'] = torch.nn.Parameter(torch.tensor(3.))
    pt_net._modules['sub']._parameters['test_param2']
    pt_result1 = pt_net._parameters['test_param']
    pt_result2 = pt_net._modules['sub']._parameters['test_param2']

    class MS_Sub(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.test_param2 = ms_torch.nn.Parameter(ms_torch.tensor(2.))
    class MS_Net(ms_torch.nn.Module):
        def __init__(self, sub):
            super().__init__()
            self.sub = sub

    ms_net = MS_Net(MS_Sub())
    ms_net._parameters['test_param'] = ms_torch.nn.Parameter(ms_torch.tensor(3.))
    ms_net._modules['sub']._parameters['test_param2']
    ms_result1 = ms_net._parameters['test_param']
    ms_result2 = ms_net._modules['sub']._parameters['test_param2']

    param_compare(pt_result1.detach(), ms_result1.detach())
    param_compare(pt_result2.detach(), ms_result2.detach())


def test_module_to():
    class Net(ms_torch.nn.Module):
        def __init__(self):
            super().__init__()
            self.para_x = ms_torch.nn.Parameter(ms_torch.tensor(3.))
            self.para_y = ms_torch.nn.Parameter(ms_torch.tensor(3.))
            self.register_buffer('mybuffer', ms_torch.tensor(3.))

        def forward(self, input):
            out = input + self.para_x
            out = out + self.para_y
            out = out + self.mybuffer
            return out

    input = ms_torch.tensor(3.).to(ms_torch.float16)
    net = Net().to(input)
    out = net(input)
    assert out.dtype == ms_torch.float16

@SKIP_ENV_ASCEND(reason="ms.ops.Cast unspport bfloat16 on Ascend.")
@SKIP_ENV_GPU(reason="ms.ops.Cast unspport bfloat16 on GPU.")
def test_module_bfloat16():
    net = MyAdapterNet()
    net.bfloat16()
    for params in net.parameters():
        assert params.dtype == ms_torch.bfloat16

def test_same_name_overwrite_function():
    class Net_mt(ms_torch.nn.Module):
        def __init__(self):
            super(Net_mt, self).__init__()

        def head(self, x):
            return x

        def head2(self, x):
            return x

    class Net1_mt(ms_torch.nn.Module):
        def __init__(self):
            super(Net1_mt, self).__init__()

    class Net2_mt(Net_mt):
        def __init__(self):
            super(Net2_mt, self).__init__()
            self.head = Net1_mt()
            self.head2 = 1

    netmt = Net2_mt()

    class Net_pt(torch.nn.Module):
        def __init__(self):
            super(Net_pt, self).__init__()

        def head(self, x):
            return x

        def head2(self, x):
            return x

    class Net1_pt(torch.nn.Module):
        def __init__(self):
            super(Net1_pt, self).__init__()

    class Net2_pt(Net_pt):
        def __init__(self):
            super(Net2_pt, self).__init__()
            self.head = Net1_pt()
            self.head2 = 1

    netpt = Net2_pt()

    assert type(netmt.head) == type(netpt.head)       # <class 'method'>
    assert type(netmt.head2) == type(netpt.head2)     # <class 'int'>


def test_same_name_not_overwrite_constant():
    class pt_Net(torch.nn.Module):
        head = 3
        def __init__(self):
            super().__init__()
            self.head = torch.nn.Parameter(torch.tensor(3.))

        def head(self):
            pass
    class ms_Net(ms_torch.nn.Module):
        head = 3
        def __init__(self):
            super().__init__()
            self.head = ms_torch.nn.Parameter(ms_torch.tensor(3.))

        def head(self):
            pass

    try:
        pt_Net()
        assert False, "PyTorch did not raise error of name has already existed."
    except:
        ...

    try:
        ms_Net()
        assert False, "MindTorch did not raise error of name has already existed."
    except:
        ...

def test_norm_running_mean_type_parameter_after_to():
    norm = ms_torch.nn.BatchNorm2d(3)
    norm.to(ms_torch.float16)
    assert isinstance(norm.running_mean, ms_torch.nn.Parameter)
    assert norm.running_mean.dtype == ms_torch.float16
    assert isinstance(norm.running_var, ms_torch.nn.Parameter)
    assert norm.running_var.dtype == ms_torch.float16

if __name__ == '__main__':
    set_mode_by_env_config()
    test_named_children1()
    test_add_modules()
    test_named_children2()
    test_modules()
    test_named_parameters()
    test_modulelist()
    test_apply_and_sequential()
    test_module_state_dict()
    test_module_register()
    test_named_modules()
    test_namedbuffer()
    test_buffer()

    test_register_buffer_allows_overwriting_with_same_name()
    test_get_buffer()
    test_get_buffer_from_submodules()
    test_buffer_not_persistent()
    test_buffer_not_persistent_del()
    test_buffer_not_persistent_assign()
    test_buffers_and_named_buffers()
    test_parameters_and_named_parameters()
    test_register_parameter_allows_overwriting_with_same_name()
    test_add_module()
    test_named_children()
    test_named_and_modules()
    test_type()
    test_module_to_empty()
    test_state_dict()
    test_load_state_dict()
    test_children()
    test_load_state_dict_ref_cycle()
    test_requires_grad_()
    test_named_parameters_remove_duplicate()
    test_children()
    test_dir()
    test_repr()
    test_dir_digit()
    test_named_children()
    test_modules_2()
    test_named_modules_2()
    test_register_buffer_raises_error_if_name_is_not_string()
    test_register_buffer_raises_error_if_attr_exists()
    test_register_buffer_raises_error_if_not_tensor()
    test_get_buffer()
    test_get_buffer_from_submodules()
    test_buffer_not_persistent()
    test_buffer_not_persistent_del()
    test_buffer_not_persistent_overwrite()
    test_buffer_not_persistent_assign()
    test_load_state_dict_invalid()
    test_load_state_dict_type()
    test_buffer_not_persistent_load()
    test_register_parameter_raises_error_if_name_is_not_string()
    test_register_parameter_raises_error_if_attr_exists()
    test_register_parameter_allows_overwriting_with_same_name()
    test_add_module_raises_error_if_attr_exists()
    test_getattr_with_property()

    test_Sequential_add()
    test_Sequential_append()
    test_Sequential_delitem()
    test_Sequential_extend()
    test_Sequential_getitem()
    test_Sequential_iadd()
    test_Sequential_imul()
    test_Sequential_insert()
    test_Sequential_insert_fail_case()
    test_Sequential_mul()
    test_Sequential_pop()
    test_Sequential_rmul()

    test_batchnorm_buffer_load()
    test_batchnorm_state_dict_no_num_batches_tracked()
    test_instance_norm_load()
    test_load_from_state_dict_get_version()
    test_register_none_param()
    test_modules_duplicate_assign()
    test_module_lazy_param_name()
    test_norm_running_mean_var_not_in_parameters()
    test_register_buffer_duplicate()
    test_norm_base_register_buffer_twice()
    test_parameters_and_modules_property()
    test_module_to()
    test_module_bfloat16()

    test_same_name_overwrite_function()
    test_same_name_not_overwrite_constant()
    test_norm_running_mean_type_parameter_after_to()
