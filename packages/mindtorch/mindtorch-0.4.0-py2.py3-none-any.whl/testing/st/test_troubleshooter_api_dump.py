import shutil
import tempfile
from pathlib import Path
import json

import numpy as np
import mindtorch.torch as torch
import mindtorch.torch.nn as nn
import mindtorch.torch.optim as optim
import mindspore as ms

import troubleshooter as ts
from troubleshooter.migrator import api_dump_init, api_dump_start, api_dump_stop, api_dump_compare

ts.fix_random()

def load_pkl(path):
    ret = []
    with open(path, "r") as f:
        while True:
            line = f.readline()
            if not line.strip():
                break
            ret.append(json.loads(line))
    return ret

def get_pkl_list(path):
    pkl = load_pkl(path)
    dump_list = []
    for line in pkl:
        name = line[0]
        dump_list.append(name)
    return dump_list

def get_stack_list(path):
    with open(path, 'r') as f:
        data = json.load(f)
    stack_list = list(data.keys())
    return stack_list


def get_npy_list(path):
    npy_list = []
    for file in Path(path).glob('*.npy'):
        name = file.stem
        npy_list.append(name)
    return npy_list

def get_pkl_npy_stack_list(path, framework):
    print()
    assert framework in {
        'torch', 'mindtorch'}, "framework must in 'torch' or 'mindtorch'"
    pkl_list = get_pkl_list(path/'rank0'/f'{framework}_api_dump_info.pkl')
    npy_list = get_npy_list(path/'rank0'/f'{framework}_api_dump')
    stack_list = get_stack_list(
        path/'rank0'/f'{framework}_api_dump_stack.json')
    return pkl_list, npy_list, stack_list

def generate_data():
    data_path = Path(tempfile.mkdtemp(prefix="test_data"))
    np.save(data_path / 'label.npy',
            np.random.randn(1, 10).astype(np.float32))
    np.save(data_path / 'data.npy',
            np.random.randn(1, 3, 90, 300).astype(np.float32))
    return data_path


class BaseTrainOneStep:
    def __init__(self, net, data_path, dump_path, info_path=None, retain_backward=True, step=1) -> None:
        self.net = net
        self.net.train()
        if info_path:
            ts.migrator.save_net_and_weight_params(self.net, path=info_path)
        self.data = torch.tensor(np.load(data_path/'data.npy'))
        self.label = torch.tensor(np.load(data_path/'label.npy'))
        self.criterion = nn.MSELoss()
        self.optimizer = optim.SGD(self.net.parameters(), lr=0.01)
        # self.optimizer.zero_grad()
        self.step = step
        api_dump_init(self.net, dump_path, retain_backward=retain_backward)

    def __call__(self):
        def forward_fn(data, label):
            out = self.net(data)
            loss = self.criterion(out, label)
            return loss

        # grad_fn = ms.ops.value_and_grad(forward_fn, None, self.optimizer.parameters, has_aux=True)
        grad_fn = ms.ops.value_and_grad(forward_fn, None, self.optimizer.parameters)

        for s in range(self.step):
            api_dump_start()
            loss, grads = grad_fn(self.data, self.label)
            self.optimizer(grads)
            print("step:", s, "   loss:", loss)
            api_dump_stop()


class BaseNet(nn.Module):
    def __init__(self):
        super(BaseNet, self).__init__()
        self.conv = nn.Conv2d(3, 5, kernel_size=3, stride=3, padding=0)
        self.bn = nn.BatchNorm2d(5)
        self.relu = nn.ReLU()
        self.linear = nn.Linear(15000, 10)


def train_mt_one_step_all(data_path, dump_path, info_path=None, retain_backward=True,
                          **api_dump_start_args):
    class Net(BaseNet):
        def forward(self, x):
            api_dump_start(**api_dump_start_args)
            x = self.conv(x)
            x = torch.clip(x, 0.2, 0.5)
            x = self.bn(x)
            x = self.relu(x)
            x = x.reshape(1, -1)
            x = self.linear(x)
            x = self.relu(x)
            return x
    train_one_step = BaseTrainOneStep(
        Net(), data_path, dump_path, info_path, retain_backward)
    train_one_step()

def test_api_dump_mindtorch_all():
    data_path = generate_data()
    dump_path = Path(tempfile.mkdtemp(prefix="mindtorch_all"))
    try:
        train_mt_one_step_all(data_path, dump_path)
        pkl_list, npy_list, stack_list = get_pkl_npy_stack_list(
            dump_path, 'mindtorch')
        assert len(pkl_list) == 25  # 21 apis + 4 layers
        assert set(pkl_list) == set(npy_list)
        assert len(stack_list) == 11 # 7 apis + 4 layers
    finally:
        shutil.rmtree(data_path)
        shutil.rmtree(dump_path)

def test_api_dump_mt_all_with_scalar():
    data_path = generate_data()
    dump_path = Path(tempfile.mkdtemp(prefix="mt_all_with_scalar"))
    try:
        train_mt_one_step_all(data_path, dump_path, filter_data=False)
        pkl_list, npy_list, stack_list = get_pkl_npy_stack_list(
            dump_path, 'mindtorch')
        assert len(pkl_list) == 29  # 25 apis + 4 layers
        assert 'Torch_clip_0_forward_input.1' in pkl_list
        assert 'Torch_clip_0_forward_input.2' in pkl_list
        assert 'Tensor_reshape_0_forward_input.1' in pkl_list
        assert 'Tensor_reshape_0_forward_input.2' in pkl_list
    finally:
        shutil.rmtree(data_path)
        shutil.rmtree(dump_path)

def test_api_dump_mt_all_with_full_stack():
    data_path = generate_data()
    dump_path = Path(tempfile.mkdtemp(prefix="mt_all_with_full_stack"))
    try:
        train_mt_one_step_all(data_path, dump_path, filter_stack=False)
        pkl_list, npy_list, stack_list = get_pkl_npy_stack_list(
            dump_path, 'mindtorch')
        assert len(stack_list) == 11     # 7 apis + 4 layers
    finally:
        shutil.rmtree(data_path)
        shutil.rmtree(dump_path)

'''TODO: uncomment after ts bug fixed

def train_pt_one_step_part(data_path, dump_path, info_path=None, retain_backwad=True, step=1):
    class Net(BaseNet):
        def forward(self, x):
            api_dump_stop()
            x = self.conv(x)
            api_dump_start()
            x = torch.clip(x, 0.2, 0.5)
            api_dump_stop()
            x = self.bn(x)
            x = self.relu(x)
            x = x.reshape(1, -1)
            x = self.linear(x)
            api_dump_start()
            x = self.relu(x)
            api_dump_stop()
            return x
    train_one_step = BaseTrainOneStep(
        Net(), data_path, dump_path, info_path, retain_backwad, step)
    train_one_step()


@pytest.mark.level0
@pytest.mark.platform_x86_gpu_training
@pytest.mark.platform_arm_ascend_training
@pytest.mark.platform_x86_ascend_training
@pytest.mark.env_onecard
def test_api_dump_torch_part():
    data_path = generate_data()
    dump_path = Path(tempfile.mkdtemp(prefix="torch_part"))
    try:
        train_pt_one_step_part(data_path, dump_path)
        pkl_list, npy_list, stack_list = get_pkl_npy_stack_list(
            dump_path, 'torch')
        assert len(pkl_list) == 7   # 6 apis + 1 layer
        assert set(pkl_list) == set(npy_list)
        assert len(stack_list) == 3     # 2 apis + 1 layer
    finally:
        shutil.rmtree(data_path)
        shutil.rmtree(dump_path)


def train_pt_one_step_api_list(data_path, dump_path, info_path=None, retain_backwad=True):
    class Net(BaseNet):
        def forward(self, x):
            api_dump_start(mode='api_list', scope=['relu', 'conv2d'])
            x = self.conv(x)
            x = torch.clip(x, 0.2, 0.5)
            x = self.bn(x)
            x = self.relu(x)
            x = x.reshape(1, -1)
            x = self.linear(x)
            x = self.relu(x)
            return x
    train_one_step = BaseTrainOneStep(
        Net(), data_path, dump_path, info_path, retain_backwad)
    train_one_step()

def test_api_dump_torch_api_list():
    data_path = generate_data()
    dump_path = Path(tempfile.mkdtemp(prefix="torch_api_list"))
    try:
        train_pt_one_step_api_list(data_path, dump_path)
        pkl_list, npy_list, stack_list = get_pkl_npy_stack_list(
            dump_path, 'torch')

        assert len(pkl_list) == 10   # 9 apis + 1 layer
        assert set(pkl_list) == set(npy_list)
        assert len(stack_list) == 4     # 3 apis + 1 layer
    finally:
        shutil.rmtree(data_path)
        shutil.rmtree(dump_path)


def train_pt_one_step_list(data_path, dump_path, info_path=None, retain_backwad=True):
    class Net(BaseNet):
        def forward(self, x):
            api_dump_start(mode='list', scope=[
                           'NN_BatchNorm2d_0', 'NN_ReLU_0'])
            x = self.conv(x)
            x = torch.clip(x, 0.2, 0.5)
            x = self.bn(x)
            x = self.relu(x)
            x = x.reshape(1, -1)
            x = self.linear(x)
            x = self.relu(x)
            return x
    train_one_step = BaseTrainOneStep(
        Net(), data_path, dump_path, info_path, retain_backwad)
    train_one_step()

def test_api_dump_torch_list():
    data_path = generate_data()
    dump_path = Path(tempfile.mkdtemp(prefix="torch_list"))
    try:
        train_pt_one_step_list(data_path, dump_path)
        pkl_list, npy_list, stack_list = get_pkl_npy_stack_list(
            dump_path, 'torch')
        assert len(pkl_list) == 6
        assert set(pkl_list) == set(npy_list)
        assert len(stack_list) == 2
    finally:
        shutil.rmtree(data_path)
        shutil.rmtree(dump_path)


def train_pt_one_step_range(data_path, dump_path, info_path=None, retain_backwad=True):
    class Net(BaseNet):
        def forward(self, x):
            api_dump_start(mode='range', scope=['Torch_clip_0', 'Tensor_reshape_0'])
            x = self.conv(x)
            x = torch.clip(x, 0.2, 0.5)
            x = self.bn(x)
            x = self.relu(x)
            x = x.reshape(1, -1)
            x = self.linear(x)
            x = self.relu(x)
            return x
    train_one_step = BaseTrainOneStep(
        Net(), data_path, dump_path, info_path, retain_backwad)
    train_one_step()

def test_api_dump_torch_range():
    data_path = generate_data()
    dump_path = Path(tempfile.mkdtemp(prefix="torch_range"))
    try:
        train_pt_one_step_range(data_path, dump_path)
        pkl_list, npy_list, stack_list = get_pkl_npy_stack_list(
            dump_path, 'torch')

        assert len(pkl_list) == 14  # 12 apis + 2 layers
        assert set(pkl_list) == set(npy_list)
        assert len(stack_list) == 6 # 4 apis + 2 layers
    finally:
        shutil.rmtree(data_path)
        shutil.rmtree(dump_path)
'''

def test_compare_api_dump_all(capsys):

    data_path = generate_data()
    torch_info_path = Path(tempfile.mkdtemp(prefix="torch_info"))
    torch_dump_path = Path(tempfile.mkdtemp(prefix="torch_dump"))
    ms_dump_path = Path(tempfile.mkdtemp(prefix="ms_dump"))
    try:
        train_mt_one_step_all(data_path, torch_dump_path, torch_info_path)
        train_mt_one_step_all(data_path, ms_dump_path, torch_info_path)
        api_dump_compare(torch_dump_path, ms_dump_path, rtol=1e-3, atol=1e-3)
        result = capsys.readouterr().out
        assert result.count("None") == 0
    finally:
        shutil.rmtree(torch_dump_path)
        shutil.rmtree(torch_info_path)
        shutil.rmtree(ms_dump_path)
        shutil.rmtree(data_path)

if __name__ == '__main__':
    test_api_dump_mindtorch_all()
    test_api_dump_mt_all_with_scalar()
    test_api_dump_mt_all_with_full_stack()
    test_compare_api_dump_all()
