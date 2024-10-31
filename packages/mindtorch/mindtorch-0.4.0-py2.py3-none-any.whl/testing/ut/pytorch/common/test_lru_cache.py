from functools import lru_cache

import numpy as np

import mindspore as ms
from mindspore.ops.primitive import _primexpr 

import mindtorch.torch as torch
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor
from mindtorch.torch.nn.modules import Module

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, SKIP_ENV_PYNATIVE_MODE

set_mode_by_env_config()

enter_get_const_count = 0
enter_get_const_count_constexpr = 0
enter_get_const_count_lru_cache_constexpr = 0


def _get_const(input_shape):
    global enter_get_const_count
    enter_get_const_count += 1
    return input_shape[0]

@_primexpr
def _get_const_constexpr(input_shape):
    global enter_get_const_count_constexpr
    enter_get_const_count_constexpr += 1
    return input_shape[1]

@_primexpr
@lru_cache(16)
def _get_const_lru_cache_constexpr(input_shape):
    global enter_get_const_count_lru_cache_constexpr
    enter_get_const_count_lru_cache_constexpr += 1
    return input_shape[2]

def my_op(input):
    input = cast_to_ms_tensor(input)
    shape1 = _get_const(input.shape)
    shape2 = _get_const_constexpr(input.shape)
    shape3 = _get_const_lru_cache_constexpr(input.shape)
    output = ms.ops.reshape(input, (shape1, shape2, shape3, -1))
    output = cast_to_adapter_tensor(output)
    return output

class Net(Module):
    def forward(self, input):
        output = ...
        for _ in range(20):
            output = my_op(input)
        return output

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_lru_cache_pynative1():
    global enter_get_const_count
    global enter_get_const_count_constexpr
    global enter_get_const_count_lru_cache_constexpr
    enter_get_const_count = 0
    enter_get_const_count_constexpr = 0
    enter_get_const_count_lru_cache_constexpr = 0
    # clear cache
    _get_const_lru_cache_constexpr.fn.cache_clear()

    net = Net()
    data = np.random.randn(1, 2, 3, 4, 5).astype(np.float32)
    input = torch.tensor(data)
    output = net(input)
    assert output.shape == (1, 2, 3, 20)
    assert enter_get_const_count == 20
    assert enter_get_const_count_constexpr == 20
    assert enter_get_const_count_lru_cache_constexpr == 1

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_lru_cache_pynative2():
    global enter_get_const_count
    global enter_get_const_count_constexpr
    global enter_get_const_count_lru_cache_constexpr
    enter_get_const_count = 0
    enter_get_const_count_constexpr = 0
    enter_get_const_count_lru_cache_constexpr = 0
    # clear cache
    _get_const_lru_cache_constexpr.fn.cache_clear()

    net = Net()
    data = np.random.randn(1, 2, 3, 4, 5).astype(np.float32)
    input = torch.tensor(data)

    output = net(input)
    output = net(input)
    output = net(input)
    output = net(input)
    output = net(input)
    output = net(input)
    assert output.shape == (1, 2, 3, 20)
    assert enter_get_const_count == 120
    assert enter_get_const_count_constexpr == 120
    assert enter_get_const_count_lru_cache_constexpr == 1

@SKIP_ENV_PYNATIVE_MODE(reason="testcase only for graph mode")
def test_lru_cache_graph():
    global enter_get_const_count
    global enter_get_const_count_constexpr
    global enter_get_const_count_lru_cache_constexpr
    enter_get_const_count = 0
    enter_get_const_count_constexpr = 0
    enter_get_const_count_lru_cache_constexpr = 0
    # clear cache
    _get_const_lru_cache_constexpr.fn.cache_clear()

    net = Net()
    data = np.random.randn(1, 2, 3, 4, 5).astype(np.float32)
    input = torch.tensor(data)
    output = net(input)
    assert output.shape == (1, 2, 3, 20)
    # graph mode can not add enter_get_const_count, it is always zero
    # assert enter_get_const_count == 20
    # assert enter_get_const_count_constexpr == 20
    # assert enter_get_const_count_lru_cache_constexpr == 1

if __name__ == '__main__':
    set_mode_by_env_config()
    test_lru_cache_pynative1()
    test_lru_cache_pynative2()
    test_lru_cache_graph()
