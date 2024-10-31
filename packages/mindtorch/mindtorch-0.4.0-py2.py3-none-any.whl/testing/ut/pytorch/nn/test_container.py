#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict
import re
import numpy as np
import torch
import mindspore as ms
import mindtorch.torch as ms_torch
import mindtorch.torch.nn as nn

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, enable_backward
set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason="Graph mode unsupport custom list/tuple.")
def test_moduledict_methods():
    class Inner(nn.Module):
        def forward(self, x):
            return x + 10
    class Inner2(nn.Module):
        def forward(self, x):
            return x * 2
    class Inner3(nn.Module):
        def forward(self, x):
            return (x - 4) * 3
    class M(nn.Module):
        def __init__(self, name):
            super(M, self).__init__()
            modules = OrderedDict([
                ('one', Inner()),
                ('two', Inner2()),
                ('three', Inner3()),
            ])
            self.sk_name = name
            self.moduledict = nn.ModuleDict(modules)

        def forward(self, x):
            values = []
            names = []
            skip_name = self.sk_name
            for name in self.moduledict:
                names.append(name)

            for name, mod in self.moduledict.items():
                if name != skip_name:
                    names.append(name)
                    x = mod(x)
                    values.append(x)

            for mod in self.moduledict.values():
                x = mod(x)
                values.append(x)

            for key in self.moduledict.keys():
                names.append(key)

            return x, names

    class M2(M):
        def __init__(self, name):
            super(M2, self).__init__(name)
        def forward(self, x):
            values = []
            x2 = x
            iter = 0
            names = []
            skip_name = self.sk_name
            for name in self.moduledict:
                names.append(name)

            for i, (name, mod) in enumerate(self.moduledict.items()):
                iter += i
                if name != skip_name:
                    names.append(name)
                    x = mod(x)
                    values.append(x)

            for i, mod in enumerate(self.moduledict.values()):
                iter += i
                x = mod(x)
                values.append(x)

            for i, key in enumerate(self.moduledict.keys()):
                iter += i
                names.append(key)

            for mod, mod in zip(self.moduledict.values(), self.moduledict.values()):
                iter += i
                x2 = mod(mod(x2))

            return x, x2, names, iter

    for name in ["", "one", "two", "three"]:
        inp = ms_torch.tensor(1)
        out1 = M(name)(inp)
        out2 = M2(name)(inp)
        assert np.allclose(out1[0].numpy(), out2[0].numpy())


def test_module_dict_common():
    class MyTorchModule(torch.nn.Module):
        def __init__(self):
            super(MyTorchModule, self).__init__()
            self.choices = torch.nn.ModuleDict({
                    'conv': torch.nn.Conv2d(10, 10, 3),
                    'pool': torch.nn.MaxPool2d(3)
            })
            self.activations = torch.nn.ModuleDict([
                    ['lrelu', torch.nn.LeakyReLU()],
                    ['prelu', torch.nn.PReLU()]
            ])
            self.function1 = self.choices['pool']
            self.function2 = self.activations['lrelu']

        def forward(self, x):
            x = self.function1(x)
            x = self.function2(x)
            return x

    class MyMsModule(ms_torch.nn.Module):
        def __init__(self):
            super(MyMsModule, self).__init__()
            self.choices = ms_torch.nn.ModuleDict({
                    'conv': ms_torch.nn.Conv2d(10, 10, 3),
                    'pool': ms_torch.nn.MaxPool2d(3)
            })
            self.activations = ms_torch.nn.ModuleDict([
                    ['lrelu', ms_torch.nn.LeakyReLU()],
                    ['prelu', ms_torch.nn.PReLU()]
            ])
            self.function1 = self.choices['pool']
            self.function2 = self.activations['lrelu']

        def forward(self, x):
            x = self.function1(x)
            x = self.function2(x)
            return x

    x = np.random.randint(0, 10, [1, 2, 4, 4])
    torch_net = MyTorchModule()
    torch_out = torch_net(torch.tensor(x, dtype=torch.float32))
    ms_torch_net = MyMsModule()
    ms_torch_out = ms_torch_net(ms_torch.tensor(x, dtype=ms_torch.float32))
    assert np.allclose(torch_out.detach().numpy(), ms_torch_out.detach().numpy())

# current mindspore version not support, should be after 23.08.25
@SKIP_ENV_GRAPH_MODE(reason="construct inputs only supports Tensor on GRAPH mode.")
def test_module_dict():
    class MyTorchModule(torch.nn.Module):
        def __init__(self):
            super(MyTorchModule, self).__init__()
            self.choices = torch.nn.ModuleDict({
                    'conv': torch.nn.Conv2d(10, 10, 3),
                    'pool': torch.nn.MaxPool2d(3)
            })
            self.activations = torch.nn.ModuleDict([
                    ['lrelu', torch.nn.LeakyReLU()],
                    ['prelu', torch.nn.PReLU()]
            ])

        def forward(self, x, choice, act):
            x = self.choices[choice](x)
            x = self.activations[act](x)
            return x

    class MyMsModule(ms_torch.nn.Module):
        def __init__(self):
            super(MyMsModule, self).__init__()
            self.choices = ms_torch.nn.ModuleDict({
                    'conv': ms_torch.nn.Conv2d(10, 10, 3),
                    'pool': ms_torch.nn.MaxPool2d(3)
            })
            self.activations = ms_torch.nn.ModuleDict([
                    ['lrelu', ms_torch.nn.LeakyReLU()],
                    ['prelu', ms_torch.nn.PReLU()]
            ])

        def forward(self, x, choice, act):
            x = self.choices[choice](x)
            x = self.activations[act](x)
            return x

    x = np.random.randint(0, 10, [1, 2, 4, 4])
    torch_net = MyTorchModule()
    torch_out = torch_net(torch.tensor(x, dtype=torch.float32), 'pool', 'lrelu')
    ms_torch_net = MyMsModule()
    ms_torch_out = ms_torch_net(ms_torch.tensor(x, dtype=ms_torch.float32), 'pool', 'lrelu')
    assert np.allclose(torch_out.detach().numpy(), ms_torch_out.detach().numpy())

# current mindspore version not support, should be after 23.08.25
@SKIP_ENV_GRAPH_MODE(reason="ModuleDict unsupport on GRAPH mode.")
def test_module_dict_grad():
    class MyModule(nn.Module):
        def __init__(self):
            super(MyModule, self).__init__()
            self.module_dict = nn.ModuleDict({'linear1': nn.Linear(2, 2), 'linear2': nn.Linear(2, 2)})

        def forward(self, x):
            x = self.module_dict["linear1"](x)
            out = self.module_dict["linear2"](x)
            return out.sum()

    net = MyModule()
    input_np = np.arange(4).reshape(2, 2).astype(np.float32)
    input = ms_torch.tensor(input_np)
    grad = ms.grad(net, grad_position=None, weights=net.trainable_params())(input)
    assert len(grad) == 4


def test_modulelist_methods():
    modules = [nn.ReLU(), nn.Linear(5, 5)]
    module_list = nn.ModuleList(modules)

    def check():
        assert len(module_list) == len(modules)
        for m1, m2 in zip(modules, module_list):
            assert m1 == m2
        for m1, m2 in zip(modules, module_list.children()):
            assert m1 == m2
        for i in range(len(modules)):
            assert module_list[i] == modules[i]

    def assertEqual(a, b):
        for i, cell in enumerate(a):
            assert a[i] == b[i]

    check()
    modules += [nn.Conv2d(3, 4, 3)]
    module_list += [modules[-1]]
    check()
    modules = modules + [nn.Conv2d(3, 4, 3, bias=False), nn.GELU()]
    module_list = module_list + nn.ModuleList(modules[-2:])
    check()
    modules.insert(1, nn.Linear(3, 2))
    module_list.insert(1, modules[1])
    check()
    modules.append(nn.Tanh())
    module_list.append(modules[-1])
    check()
    next_modules = [nn.Linear(5, 5), nn.Sigmoid()]
    modules.extend(next_modules)
    module_list.extend(next_modules)
    check()
    modules[2] = nn.Conv2d(5, 3, 2)
    module_list[2] = modules[2]
    check()
    modules[-1] = nn.Conv2d(5, 2, 1)
    module_list[-1] = modules[-1]
    check()
    idx = ms_torch.tensor(2, dtype=torch.int32)
    modules[2] = nn.Conv2d(5, 3, 2)
    module_list[idx] = modules[2]
    assert module_list[idx] == modules[2]
    check()
    assertEqual(module_list[1:], nn.ModuleList(modules[1:]))
    assertEqual(module_list[3:], nn.ModuleList(modules[3:]))
    assertEqual(module_list[:-1], nn.ModuleList(modules[:-1]))
    assertEqual(module_list[:-3], nn.ModuleList(modules[:-3]))
    assertEqual(module_list[::-1], nn.ModuleList(modules[::-1]))
    del module_list[-1]
    assertEqual(module_list, nn.ModuleList(modules[:-1]))
    del module_list[1::2]
    assertEqual(module_list, nn.ModuleList(modules[:-1][0::2]))

    _error_msg = "should be called with an iterable"
    try:
        module_list += nn.ReLU()
        assert False
    except TypeError as e:
        assert re.search(_error_msg, str(e))

    try:
        module_list.extend(nn.ReLU())
        assert False
    except TypeError as e:
        assert re.search(_error_msg, str(e))

    l1 = nn.Linear(1, 2)
    l2 = nn.Linear(2, 3)
    l3 = nn.Linear(3, 2)
    l4 = nn.Linear(2, 3)
    subnet = nn.Sequential(l3, l4)
    s = nn.Sequential(
        OrderedDict([
            ("layer1", l1),
            ("layer2", l2),
            ("layer3", l3),
            ("layer4", l4),
            ("subnet_layer", subnet)
        ])
    )
    modules = list(s.modules())
    module_list = nn.ModuleList()
    module_list.extend(s.modules())
    check()

    modules = [nn.ReLU(), nn.Linear(5, 5), nn.Conv2d(3, 4, 3)]
    module_list = nn.ModuleList(modules)
    assert modules.pop(1) == module_list.pop(1)
    assertEqual(modules, module_list)
    # check order of the index
    for k, mod in zip(range(len(module_list)), module_list):
        assert module_list[k] == mod

@SKIP_ENV_GRAPH_MODE(reason="Currently not support return class in graph mode")
def test_modulelist_methods2():
    class ModuleListTest(nn.ModuleList):
        def __init__(self, x):
            super().__init__(x)
        def forward(self, Xs):
            return tuple(mani(X) for mani , X in zip(self, Xs))
        def right_inverse(self, Xs):
            return tuple(mani.right_inverse(X) for mani, X in zip(self, Xs))

    class DummyBlock(nn.ReLU):
        expansion = 1

    def _mock_layer(in_features=None, out_features=None, *args, **kwargs):
        if in_features and out_features:
            return nn.Linear(in_features, out_features, **kwargs)
        #TODO: not support return DummyBlock() in graph mode
        return DummyBlock()

    model = ModuleListTest(x=[_mock_layer()], )
    model(ms_torch.rand(4, 4, 4, 4))

def test_module_list_grad():
    class MyModule(nn.Module):
        def __init__(self):
            super(MyModule, self).__init__()
            self.module_list = nn.ModuleList([nn.Linear(2, 2) for _ in range(2)])

        def forward(self, x):
            out = self.module_list[0](x)
            return out.sum()

    net = MyModule()
    input_np = np.arange(4).reshape(2, 2).astype(np.float32)
    input = ms_torch.tensor(input_np)
    grad = ms.grad(net, grad_position=None, weights=net.trainable_params())(input)
    assert len(grad) == 4

def test_module_list_insert_zero():
    ms_ml = ms_torch.nn.ModuleList()
    ms_ml.insert(0, ms_torch.nn.Module())
    assert len(ms_ml) == 1

def test_parameterlist_methods():
    def make_param():
        return nn.Parameter(ms_torch.ones(2, 2))
    parameters = [make_param(), make_param()]
    param_list = nn.ParameterList(parameters)

    def check():
        assert len(parameters) == len(param_list)
        for p1, p2 in zip(parameters, param_list):
            assert id(p1) ==  id(p2)
        for p1, p2 in zip(filter(lambda x: isinstance(x, nn.Parameter), parameters), param_list.parameters()):
            assert id(p1) ==  id(p2)
        for i in range(len(parameters)):
            assert id(parameters[i]) == id(param_list[i])

    check()
    parameters += [make_param()]
    param_list += [parameters[-1]]
    check()
    parameters.append(make_param())
    param_list.append(parameters[-1])
    check()
    next_params = [make_param(), make_param()]
    parameters.extend(next_params)
    param_list.extend(next_params)
    check()
    parameters[2] = make_param()
    param_list[2] = parameters[2]
    check()
    parameters[-1] = make_param()
    param_list[-1] = parameters[-1]
    check()
    idx = ms_torch.tensor(2, dtype=ms_torch.int32)
    parameters[2] = make_param()
    param_list[idx] = parameters[2]
    assert id(param_list[idx]) == id(parameters[2])
    check()

    l1 = nn.Linear(1, 2)
    l2 = nn.Linear(2, 3)
    l3 = nn.Linear(3, 2)
    l4 = nn.Linear(2, 3)
    subnet = nn.Sequential(l3, l4)
    s = nn.Sequential(
        OrderedDict([
            ("layer1", l1),
            ("layer2", l2),
            ("layer3", l3),
            ("layer4", l4),
            ("subnet_layer", subnet)
        ])
    )
    parameters = list(s.parameters())
    param_list = nn.ParameterList()
    param_list.extend(s.parameters())
    check()

    param_list.append(ms_torch.rand(2, 2))
    assert isinstance(param_list[-1], nn.Parameter)
    parameters.append(param_list[-1])

    param_list.extend([ms_torch.rand(2, 2), "foo"])
    assert isinstance(param_list[-2], nn.Parameter)
    assert isinstance(param_list[-1], str)
    parameters.extend(param_list[-2:])

    param_list += ["bar", ms_torch.rand(2, 2)]
    assert isinstance(param_list[-2], str)
    assert isinstance(param_list[-1], nn.Parameter)
    parameters += param_list[-2:]
    check()

@SKIP_ENV_GRAPH_MODE(reason="Graph mode unsupport custom list/tuple.")
def test_parameter_list():
    init_data = np.random.randn(4, 4).astype(np.float32)
    class MyTorchModule(torch.nn.Module):
        def __init__(self):
            super(MyTorchModule, self).__init__()
            self.params = torch.nn.ParameterList([torch.nn.Parameter(torch.tensor(init_data)) for i in range(3)])

        def forward(self, x):
            # ParameterList can act as an iterable, or be indexed using ints
            for i, p in enumerate(self.params):
                x = self.params[i // 2].mm(x) + p.mm(x)
            return x.sum()

    class MyMsModule(ms_torch.nn.Module):
        def __init__(self):
            super(MyMsModule, self).__init__()
            self.params = ms_torch.nn.ParameterList([ms_torch.nn.Parameter(ms_torch.tensor(init_data)) for i in range(3)])

        def forward(self, x):
            # ParameterList can act as an iterable, or be indexed using ints
            for i, p in enumerate(self.params):
                x = self.params[i // 2].mm(x) + p.mm(x)
            return x.sum()

    x = np.random.randn(4, 1).astype(np.float32)
    torch_net = MyTorchModule()
    ms_torch_net = MyMsModule()

    torch_net.params.append(torch.nn.Parameter(torch.tensor(init_data)))
    torch_net.params.extend([torch.nn.Parameter(torch.tensor(init_data))])
    torch_out = torch_net(torch.tensor(x))

    ms_torch_net.params.append(ms_torch.nn.Parameter(ms_torch.tensor(init_data)))
    ms_torch_net.params.extend([ms_torch.nn.Parameter(ms_torch.tensor(init_data))])

    ms_torch_out = ms_torch_net(ms_torch.tensor(x))

    assert np.allclose(torch_out.detach().numpy(), ms_torch_out.detach().numpy())

    #grad
    torch_out.backward()
    torch_grad = torch_net.params[0].grad

    # Automatic differentiation method 1
    ms_grad = ms.grad(ms_torch_net, grad_position=None, weights=ms_torch_net.trainable_params(), has_aux=False)(ms_torch.tensor(x))
    assert torch_grad.size() ==  ms_grad[0].shape
    assert np.allclose(torch_grad.numpy(), ms_grad[0].numpy())


def test_parameter_list_to_list():
    init_data = np.random.randn(4, 4).astype(np.float32)
    class MyMsModule(ms_torch.nn.Module):
        def __init__(self):
            super(MyMsModule, self).__init__()
            self.params = ms_torch.nn.ParameterList([ms_torch.nn.Parameter(ms_torch.tensor(init_data)) for i in range(3)])

        def forward(self, x):
            # ParameterList can act as an iterable, or be indexed using ints
            for i, p in enumerate(self.params):
                x = self.params[i // 2].mm(x) + p.mm(x)
            return x.sum()

    x = np.random.randn(4, 1).astype(np.float32)
    ms_torch_net = MyMsModule()

    ms_torch_net.params.append(ms_torch.nn.Parameter(ms_torch.tensor(init_data)))
    ms_torch_net.params.extend([ms_torch.nn.Parameter(ms_torch.tensor(init_data))])

    ms_torch_net.params = ms_torch_net.params.to_list()  #to avoid graph mode error

    ms_torch_out = ms_torch_net(ms_torch.tensor(x))
    ms_grad = ms.grad(ms_torch_net, grad_position=None, weights=ms_torch_net.trainable_params(), has_aux=False)(ms_torch.tensor(x))


@SKIP_ENV_GRAPH_MODE(reason="Graph mode unsupport custom list/tuple.")
def test_parameter_dict_grad():
    init_data1 = np.random.randn(5, 10).astype(np.float32)
    init_data2 = np.random.randn(5, 10).astype(np.float32)
    class MyTorchModule(torch.nn.Module):
        def __init__(self):
            super(MyTorchModule, self).__init__()
            self.params = torch.nn.ParameterDict({
                    'left': torch.nn.Parameter(torch.tensor(init_data1)),
                    'right': torch.nn.Parameter(torch.tensor(init_data2))
            })
            self.params.update({'left': torch.nn.Parameter(torch.tensor(init_data2))})

        def forward(self, x):
            x = self.params['right'].mm(x)
            return x.sum()

    class MyMsModule(ms_torch.nn.Module):
        def __init__(self):
            super(MyMsModule, self).__init__()
            self.params = ms_torch.nn.ParameterDict({
                    'left': ms_torch.nn.Parameter(ms_torch.tensor(init_data1)),
                    'right': ms_torch.nn.Parameter(ms_torch.tensor(init_data2))
            })
            self.params.update({'left': ms_torch.nn.Parameter(ms_torch.tensor(init_data2))})

        def forward(self, x):
            x = self.params['right'].mm(x)
            return x.sum()

    x = np.random.randn(10, 1).astype(np.float32)
    torch_net = MyTorchModule()
    ms_torch_net = MyMsModule()
    torch_out = torch_net(torch.tensor(x))
    ms_torch_out = ms_torch_net(ms_torch.tensor(x))
    assert np.allclose(torch_out.detach().numpy(), ms_torch_out.detach().numpy())

    #grad
    torch_out.backward()
    torch_grad = torch_net.params['right'].grad

    # Automatic differentiation method 1
    ms_grad = ms.grad(ms_torch_net, grad_position=None, weights=ms_torch_net.trainable_params(), has_aux=False)(ms_torch.tensor(x))
    assert torch_grad.size() ==  ms_grad[1].shape
    assert np.allclose(torch_grad.numpy(), ms_grad[1].numpy())


def test_parameter_dict_to_dict():
    init_data1 = np.random.randn(5, 10).astype(np.float32)
    init_data2 = np.random.randn(5, 10).astype(np.float32)
    class MyMsModule(ms_torch.nn.Module):
        def __init__(self):
            super(MyMsModule, self).__init__()
            self.params = ms_torch.nn.ParameterDict({
                    'left': ms_torch.nn.Parameter(ms_torch.tensor(init_data1)),
                    'right': ms_torch.nn.Parameter(ms_torch.tensor(init_data2))
            })
            self.params.update({'left': ms_torch.nn.Parameter(ms_torch.tensor(init_data2))})
            self.new_params = self.params.to_dict()  #to avoid graph mode error

        def forward(self, x):
            x = self.new_params['right'].mm(x)
            return x

    x = np.random.randn(10, 1).astype(np.float32)
    ms_torch_net = MyMsModule()
    ms_torch_out = ms_torch_net(ms_torch.tensor(x))
    ms_grad = ms.grad(ms_torch_net, grad_position=None, weights=ms_torch_net.trainable_params(), has_aux=False)(ms_torch.tensor(x))

def test_sequential_grad1():
    input_np = np.arange(80).reshape(10, 8).astype(np.float32)
    class Net(ms_torch.nn.Module):
        def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
            super(Net, self).__init__()
            self.layer = ms_torch.nn.Sequential(nn.Linear(in_dim, n_hidden_1),
                                                nn.ReLU(),
                                                nn.Linear(n_hidden_1, n_hidden_2),
                                                nn.ReLU(),
                                                nn.Linear(n_hidden_2, out_dim)
                                                )
        def forward(self, x):
            x = self.layer(x)
            return x.sum()

    net = Net(8, 5, 2, 1)
    input = ms_torch.tensor(input_np)

    grad_func = ms.value_and_grad(net, grad_position=None, weights=net.trainable_params())
    _, weight_grad = grad_func(input)
    assert np.count_nonzero(weight_grad[-1].asnumpy()) != 10

def test_sequential_grad2():
    input_np = np.arange(4).reshape(2, 2).astype(np.float32)
    net = ms_torch.nn.Sequential(nn.Linear(2, 2), nn.ReLU())

    x = ms_torch.tensor(input_np, requires_grad=True)
    grad = ms.grad(net, grad_position=None, weights=net.trainable_params())(x)
    assert len(grad) == 2


if __name__ == '__main__':
    set_mode_by_env_config()
    test_moduledict_methods()
    test_module_dict_common()
    test_module_dict()
    test_module_dict_grad()
    test_modulelist_methods()
    test_module_list_grad()
    test_parameter_list()
    test_parameter_list_to_list()
    test_parameter_dict_grad()
    test_parameter_dict_to_dict()
    test_sequential_grad1()
    test_sequential_grad2()
    test_modulelist_methods2()
    test_module_list_insert_zero()