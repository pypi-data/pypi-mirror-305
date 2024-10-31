import os
import numpy as np
import torch
import mindtorch.torch as pytorch
from ...utils import  set_mode_by_env_config, param_compare, SKIP_ENV_CPU, SKIP_ENV_GPU, SKIP_ENV_ASCEND

set_mode_by_env_config()

def test_save_load_1():
    state_dict_torch ={}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64,64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.tensor(a)
    state_dict_torch["b"] = torch.tensor(b)
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.tensor(a)
    state_dict_mindtorch["b"] = pytorch.tensor(b)
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_1_torch.pth")
    pytorch.save(state_dict_mindtorch, "test_save_load_1_mindtorch.pth")

    state_dict_torch = torch.load("test_save_load_1_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_1_mindtorch.pth")
    os.remove("test_save_load_1_torch.pth")
    os.remove("test_save_load_1_mindtorch.pth")
    param_compare(state_dict_torch["a"], state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"], state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

def test_save_load_2():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.tensor(a)
    state_dict_torch["b"] = torch.tensor(b)
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.tensor(a)
    state_dict_mindtorch["b"] = pytorch.tensor(b)
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_2_torch.pth", _use_new_zipfile_serialization=False)
    pytorch.save(state_dict_mindtorch, "test_save_load_2_mindtorch.pth", _use_new_zipfile_serialization=False)

    state_dict_torch = torch.load("test_save_load_2_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_2_mindtorch.pth")
    os.remove("test_save_load_2_torch.pth")
    os.remove("test_save_load_2_mindtorch.pth")
    param_compare(state_dict_torch["a"], state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"], state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

def test_save_load_3():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.tensor(a)
    state_dict_torch["b"] = torch.tensor(b)
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.tensor(a)
    state_dict_mindtorch["b"] = pytorch.tensor(b)
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_3_torch.pth")

    state_dict_torch = torch.load("test_save_load_3_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_3_torch.pth")
    os.remove("test_save_load_3_torch.pth")

    param_compare(state_dict_torch["a"], state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"], state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

def test_save_load_4():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.tensor(a)
    state_dict_torch["b"] = torch.tensor(b)
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.tensor(a)
    state_dict_mindtorch["b"] = pytorch.tensor(b)
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_4_torch.pth", _use_new_zipfile_serialization=False)

    state_dict_torch = torch.load("test_save_load_4_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_4_torch.pth")
    os.remove("test_save_load_4_torch.pth")

    param_compare(state_dict_torch["a"], state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"], state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

def test_save_load_bf16_1():
    state_dict_mindtorch = {}
    a = pytorch.tensor(800000, dtype=pytorch.bfloat16)
    b = pytorch.tensor([[800000, 2.5],[4.5, 5.5]], dtype=pytorch.bfloat16)
    c = 1

    state_dict_mindtorch["a"] = a
    state_dict_mindtorch["b"] = b
    state_dict_mindtorch["c"] = c

    pytorch.save(state_dict_mindtorch, "test_save_load_bf16_1.pth", _use_new_zipfile_serialization=False)

    state_dict_mindtorch = pytorch.load("test_save_load_bf16_1.pth")
    os.remove("test_save_load_bf16_1.pth")
    assert a.dtype == state_dict_mindtorch["a"].dtype
    assert b.dtype == state_dict_mindtorch["b"].dtype
    param_compare(a.to(pytorch.float32), state_dict_mindtorch["a"].to(pytorch.float32))
    param_compare(b.to(pytorch.float32), state_dict_mindtorch["b"].to(pytorch.float32))
    assert c == state_dict_mindtorch["c"]

def test_save_load_bf16_2():
    state_dict_mindtorch = {}
    a = pytorch.tensor(800000, dtype=pytorch.bfloat16)
    b = pytorch.tensor([[800000, 2.5],[4.5, 5.5]], dtype=pytorch.bfloat16)
    c = 1

    state_dict_mindtorch["a"] = a
    state_dict_mindtorch["b"] = b
    state_dict_mindtorch["c"] = c

    pytorch.save(state_dict_mindtorch, "test_save_load_bf16_2.pth", _use_new_zipfile_serialization=True)

    state_dict_mindtorch = pytorch.load("test_save_load_bf16_2.pth")
    os.remove("test_save_load_bf16_2.pth")
    assert a.dtype == state_dict_mindtorch["a"].dtype
    assert b.dtype == state_dict_mindtorch["b"].dtype
    param_compare(a.to(pytorch.float32), state_dict_mindtorch["a"].to(pytorch.float32))
    param_compare(b.to(pytorch.float32), state_dict_mindtorch["b"].to(pytorch.float32))
    assert c == state_dict_mindtorch["c"]

def test_save_load_bf16_3():
    state_dict_mindtorch = {}
    a = torch.tensor(800000, dtype=torch.bfloat16)
    b = torch.tensor([[800000, 2.5],[4.5, 5.5]], dtype=torch.bfloat16)
    c = 1

    state_dict_mindtorch["a"] = a
    state_dict_mindtorch["b"] = b
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_mindtorch, "test_save_load_bf16_3.pth", _use_new_zipfile_serialization=False)

    state_dict_mindtorch = pytorch.load("test_save_load_bf16_3.pth")
    os.remove("test_save_load_bf16_3.pth")
    param_compare(a.to(torch.float32), state_dict_mindtorch["a"].to(pytorch.float32))
    param_compare(b.to(torch.float32), state_dict_mindtorch["b"].to(pytorch.float32))
    assert c == state_dict_mindtorch["c"]

def test_save_load_bf16_4():
    state_dict_mindtorch = {}
    a = torch.tensor(800000, dtype=torch.bfloat16)
    b = torch.tensor([[800000, 2.5],[4.5, 5.5]], dtype=torch.bfloat16)
    c = 1

    state_dict_mindtorch["a"] = a
    state_dict_mindtorch["b"] = b
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_mindtorch, "test_save_load_bf16_4.pth", _use_new_zipfile_serialization=True)

    state_dict_mindtorch = pytorch.load("test_save_load_bf16_4.pth")
    os.remove("test_save_load_bf16_4.pth")
    param_compare(a.to(torch.float32), state_dict_mindtorch["a"].to(pytorch.float32))
    param_compare(b.to(torch.float32), state_dict_mindtorch["b"].to(pytorch.float32))
    assert c == state_dict_mindtorch["c"]

def test_save_load_parameter_1():
    state_dict_torch ={}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64,64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.nn.Parameter(torch.tensor(a))
    state_dict_torch["b"] = torch.nn.Parameter(torch.tensor(b))
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.nn.Parameter(pytorch.tensor(a))
    state_dict_mindtorch["b"] = pytorch.nn.Parameter(pytorch.tensor(b))
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_parameter_1_torch.pth")
    pytorch.save(state_dict_mindtorch, "test_save_load_parameter_1_mindtorch.pth")

    state_dict_torch = torch.load("test_save_load_parameter_1_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_parameter_1_mindtorch.pth")
    os.remove("test_save_load_parameter_1_torch.pth")
    os.remove("test_save_load_parameter_1_mindtorch.pth")
    param_compare(state_dict_torch["a"].detach(), state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"].detach(), state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

def test_save_load_parameter_2():
    state_dict_torch ={}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64,64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.nn.Parameter(torch.tensor(a))
    state_dict_torch["b"] = torch.nn.Parameter(torch.tensor(b))
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.nn.Parameter(pytorch.tensor(a))
    state_dict_mindtorch["b"] = pytorch.nn.Parameter(pytorch.tensor(b))
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_parameter_2_torch.pth", _use_new_zipfile_serialization=False)
    pytorch.save(state_dict_mindtorch, "test_save_load_parameter_2_mindtorch.pth", _use_new_zipfile_serialization=False)

    state_dict_torch = torch.load("test_save_load_parameter_2_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_parameter_2_mindtorch.pth")
    os.remove("test_save_load_parameter_2_torch.pth")
    os.remove("test_save_load_parameter_2_mindtorch.pth")
    param_compare(state_dict_torch["a"].detach(), state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"].detach(), state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]


def test_save_load_parameter_3():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.nn.Parameter(torch.tensor(a))
    state_dict_torch["b"] = torch.nn.Parameter(torch.tensor(b))
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.nn.Parameter(pytorch.tensor(a))
    state_dict_mindtorch["b"] = pytorch.nn.Parameter(pytorch.tensor(b))
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_parameter_3_torch.pth")

    state_dict_torch = torch.load("test_save_load_parameter_3_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_parameter_3_torch.pth")
    os.remove("test_save_load_parameter_3_torch.pth")

    param_compare(state_dict_torch["a"].detach(), state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"].detach(), state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

def test_save_load_parameter_4():
    state_dict_torch = {}
    state_dict_mindtorch = {}
    a = np.random.rand(3, 3).astype(np.float32)
    b = np.random.rand(1, 64, 64, 3).astype(np.float32)
    c = 1
    state_dict_torch["a"] = torch.nn.Parameter(torch.tensor(a))
    state_dict_torch["b"] = torch.nn.Parameter(torch.tensor(b))
    state_dict_torch["c"] = c

    state_dict_mindtorch["a"] = pytorch.nn.Parameter(pytorch.tensor(a))
    state_dict_mindtorch["b"] = pytorch.nn.Parameter(pytorch.tensor(b))
    state_dict_mindtorch["c"] = c

    torch.save(state_dict_torch, "test_save_load_parameter_4_torch.pth", _use_new_zipfile_serialization=False)

    state_dict_torch = torch.load("test_save_load_parameter_4_torch.pth")
    state_dict_mindtorch = pytorch.load("test_save_load_parameter_4_torch.pth")
    os.remove("test_save_load_parameter_4_torch.pth")

    param_compare(state_dict_torch["a"].detach(), state_dict_mindtorch["a"])
    param_compare(state_dict_torch["b"].detach(), state_dict_mindtorch["b"])
    assert state_dict_torch["c"] == state_dict_mindtorch["c"]

def test_save_load_net():
    import torch
    import torch.nn as nn
    class Net(nn.Module):
        def __init__(self, num_classes: int = 10) -> None:
            super(Net, self).__init__()

            self.features = nn.Sequential(
                nn.Conv2d(3, 64, (11, 11), (4, 4), (2, 2), bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(),
                nn.MaxPool2d((3, 3), (2, 2)),
            )

            self.avgpool = nn.AdaptiveAvgPool2d((6, 6))

            self.classifier = nn.Sequential(
                nn.Dropout(0.5),
                nn.Linear(256 * 6 * 6, 4096),
            )

    net = Net()
    state_dict = {
        'net': net.state_dict(),
    }

    torch.save(state_dict, 'torch_module.pt', _use_new_zipfile_serialization=True)

    torch.save(state_dict, 'torch_module_oldfile.pt', _use_new_zipfile_serialization=False)

    import mindtorch.torch as pytorch
    import mindtorch.torch.nn as nn
    class Net(nn.Module):
        def __init__(self, num_classes: int = 10) -> None:
            super(Net, self).__init__()

            self.features = nn.Sequential(
                nn.Conv2d(3, 64, (11, 11), (4, 4), (2, 2), bias=False),
                nn.BatchNorm2d(64),
                nn.ReLU(),
                nn.MaxPool2d((3, 3), (2, 2)),
            )

            self.avgpool = nn.AdaptiveAvgPool2d((6, 6))

            self.classifier = nn.Sequential(
                nn.Dropout(0.5),
                nn.Linear(256 * 6 * 6, 4096),
            )

    net = Net()
    state = pytorch.load("torch_module.pt")
    net.load_state_dict(state['net'])
    os.remove("torch_module.pt")
    state_dict = {
        'net': net.state_dict(),
    }
    pytorch.save(state_dict, 'mindtorch_module.pt', _use_new_zipfile_serialization=True)
    os.remove("mindtorch_module.pt")

    state = pytorch.load("torch_module_oldfile.pt")
    net.load_state_dict(state['net'])
    os.remove("torch_module_oldfile.pt")
    state_dict = {
        'net': net.state_dict(),
    }
    pytorch.save(state_dict, 'mindtorch_module_oldfile.pt', _use_new_zipfile_serialization=False)
    os.remove('mindtorch_module_oldfile.pt')


@SKIP_ENV_ASCEND(reason="This function need torch version >= 2.1.0")
@SKIP_ENV_GPU(reason="This function need torch version >= 2.1.0")
@SKIP_ENV_CPU(reason="This function need torch version >= 2.1.0")
def test_save_load_5():
    a = torch.tensor(2.)
    a.kkk = 3
    torch.save(a, 'a.pth')
    tensor = pytorch.load('a.pth')
    os.remove('a.pth')
    assert tensor.kkk == a.kkk
    param_compare(a, tensor)


def test_save_load_6():
    a = pytorch.tensor(2.)
    a.kkk = 3
    pytorch.save(a, 'a.pth')
    tensor = pytorch.load('a.pth')
    os.remove('a.pth')
    assert tensor.kkk == a.kkk
    param_compare(a, tensor)


@SKIP_ENV_ASCEND(reason="This function need torch version >= 2.1.0")
@SKIP_ENV_GPU(reason="This function need torch version >= 2.1.0")
@SKIP_ENV_CPU(reason="This function need torch version >= 2.1.0")
def test_save_load_7():
    a = torch.nn.Parameter(torch.tensor(2.))
    a.kkk = 3
    torch.save(a, 'a.pth')
    tensor = pytorch.load('a.pth')
    os.remove('a.pth')
    assert tensor.kkk == a.kkk
    param_compare(a.detach(), tensor)


def test_save_load_8():
    a = pytorch.nn.Parameter(pytorch.tensor(2.))
    a.kkk = 3
    pytorch.save(a, 'a.pth')
    tensor = pytorch.load('a.pth')
    os.remove('a.pth')
    assert tensor.kkk == a.kkk
    param_compare(a, tensor)


def test_save_load_sequential_1():
    model = torch.nn.Sequential(
                  torch.nn.Conv2d(1,20,5),
                  torch.nn.ReLU(),
                  torch.nn.Conv2d(20,64,5),
                  torch.nn.ReLU()
                )
    torch.save(model, 'sequential1.pt',  _use_new_zipfile_serialization=True)
    torch_params = model.state_dict()
    mindtorch_model = pytorch.load('sequential1.pt')
    os.remove('sequential1.pt')
    pytorch_params = mindtorch_model.state_dict()
    for key in torch_params.keys():
        param_compare(torch_params[key], pytorch_params[key])


def test_save_load_sequential_2():
    model = torch.nn.Sequential(
                  torch.nn.Conv2d(1,20,5),
                  torch.nn.ReLU(),
                  torch.nn.Conv2d(20,64,5),
                  torch.nn.ReLU()
                )
    torch.save(model, 'sequential2.pt',  _use_new_zipfile_serialization=False)
    torch_params = model.state_dict()
    mindtorch_model = pytorch.load('sequential2.pt')
    os.remove('sequential2.pt')
    pytorch_params = mindtorch_model.state_dict()
    for key in torch_params.keys():
        param_compare(torch_params[key], pytorch_params[key])

def test_save_load_sequential_3():
    model = pytorch.nn.Sequential(
                  pytorch.nn.Conv2d(1,20,5),
                  pytorch.nn.ReLU(),
                  pytorch.nn.Conv2d(20,64,5),
                  pytorch.nn.ReLU()
                )
    pytorch.save(model, 'sequential3.pt',  _use_new_zipfile_serialization=True)
    pytorch_params1 = model.state_dict()
    mindtorch_model = pytorch.load('sequential3.pt')
    os.remove('sequential3.pt')
    pytorch_params2 = mindtorch_model.state_dict()
    for key in pytorch_params1.keys():
        param_compare(pytorch_params1[key], pytorch_params2[key])


def test_save_load_sequential_4():
    model = pytorch.nn.Sequential(
                  pytorch.nn.Conv2d(1,20,5),
                  pytorch.nn.ReLU(),
                  pytorch.nn.Conv2d(20,64,5),
                  pytorch.nn.ReLU()
                )
    pytorch.save(model, 'sequential4.pt',  _use_new_zipfile_serialization=False)
    pytorch_params1 = model.state_dict()
    mindtorch_model = pytorch.load('sequential4.pt')
    os.remove('sequential4.pt')
    pytorch_params2 = mindtorch_model.state_dict()
    for key in pytorch_params1.keys():
        param_compare(pytorch_params1[key], pytorch_params2[key])


def test_save_load_modulelist_1():
    model = torch.nn.ModuleList([torch.nn.Linear(10, 10) for i in range(10)])
    torch.save(model, 'modulelist1.pt',  _use_new_zipfile_serialization=True)
    torch_params = model.state_dict()
    mindtorch_model = pytorch.load('modulelist1.pt')
    os.remove('modulelist1.pt')
    pytorch_params = mindtorch_model.state_dict()
    for key in torch_params.keys():
        param_compare(torch_params[key], pytorch_params[key])


def test_save_load_modulelist_2():
    model = torch.nn.ModuleList([torch.nn.Linear(10, 10) for i in range(10)])
    torch.save(model, 'modulelist2.pt',  _use_new_zipfile_serialization=False)
    torch_params = model.state_dict()
    mindtorch_model = pytorch.load('modulelist2.pt')
    os.remove('modulelist2.pt')
    pytorch_params = mindtorch_model.state_dict()
    for key in torch_params.keys():
        param_compare(torch_params[key], pytorch_params[key])

def test_save_load_modulelist_3():
    model = pytorch.nn.ModuleList([pytorch.nn.Linear(10, 10) for i in range(10)])
    pytorch.save(model, 'sequential3.pt',  _use_new_zipfile_serialization=True)
    pytorch_params1 = model.state_dict()
    mindtorch_model = pytorch.load('sequential3.pt')
    os.remove('sequential3.pt')
    pytorch_params2 = mindtorch_model.state_dict()
    for key in pytorch_params1.keys():
        param_compare(pytorch_params1[key], pytorch_params2[key])


def test_save_load_modulelist_4():
    model = pytorch.nn.ModuleList([pytorch.nn.Linear(10, 10) for i in range(10)])
    pytorch.save(model, 'modulelist4.pt',  _use_new_zipfile_serialization=False)
    pytorch_params1 = model.state_dict()
    mindtorch_model = pytorch.load('modulelist4.pt')
    os.remove('modulelist4.pt')
    pytorch_params2 = mindtorch_model.state_dict()
    for key in pytorch_params1.keys():
        param_compare(pytorch_params1[key], pytorch_params2[key])


def test_save_load_moduledict_1():
    model = torch.nn.ModuleDict({
                        'conv': torch.nn.Conv2d(10, 10, 3),
                        'pool': torch.nn.MaxPool2d(3)
                })
    torch.save(model, 'moduledict1.pt',  _use_new_zipfile_serialization=True)
    torch_params = model.state_dict()
    mindtorch_model = pytorch.load('moduledict1.pt')
    os.remove('moduledict1.pt')
    pytorch_params = mindtorch_model.state_dict()
    for key in torch_params.keys():
        param_compare(torch_params[key], pytorch_params[key])


def test_save_load_moduledict_2():
    model = torch.nn.ModuleDict({
                        'conv': torch.nn.Conv2d(10, 10, 3),
                        'pool': torch.nn.MaxPool2d(3)
                })
    torch.save(model, 'moduledict2.pt',  _use_new_zipfile_serialization=False)
    torch_params = model.state_dict()
    mindtorch_model = pytorch.load('moduledict2.pt')
    os.remove('moduledict2.pt')
    pytorch_params = mindtorch_model.state_dict()
    for key in torch_params.keys():
        param_compare(torch_params[key], pytorch_params[key])

def test_save_load_moduledict_3():
    model = pytorch.nn.ModuleDict({
                        'conv': pytorch.nn.Conv2d(10, 10, 3),
                        'pool': pytorch.nn.MaxPool2d(3)
                })
    pytorch.save(model, 'sequential3.pt',  _use_new_zipfile_serialization=True)
    pytorch_params1 = model.state_dict()
    mindtorch_model = pytorch.load('sequential3.pt')
    os.remove('sequential3.pt')
    pytorch_params2 = mindtorch_model.state_dict()
    for key in pytorch_params1.keys():
        param_compare(pytorch_params1[key], pytorch_params2[key])


def test_save_load_moduledict_4():
    model = pytorch.nn.ModuleDict({
                        'conv': pytorch.nn.Conv2d(10, 10, 3),
                        'pool': pytorch.nn.MaxPool2d(3)
                })
    pytorch.save(model, 'moduledict4.pt',  _use_new_zipfile_serialization=False)
    pytorch_params1 = model.state_dict()
    mindtorch_model = pytorch.load('moduledict4.pt')
    os.remove('moduledict4.pt')
    pytorch_params2 = mindtorch_model.state_dict()
    for key in pytorch_params1.keys():
        param_compare(pytorch_params1[key], pytorch_params2[key])


if __name__ == '__main__':
    test_save_load_1()
    test_save_load_2()
    test_save_load_3()
    test_save_load_4()
    test_save_load_bf16_1()
    test_save_load_bf16_2()
    test_save_load_bf16_3()
    test_save_load_bf16_4()
    test_save_load_parameter_1()
    test_save_load_parameter_2()
    test_save_load_parameter_3()
    test_save_load_parameter_4()
    test_save_load_net()
    test_save_load_5()
    test_save_load_6()
