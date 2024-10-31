import os
import pytest
import numpy as np
import math
import mindspore as ms
from mindspore._c_expression import jit_mode_pi_enable, jit_mode_pi_disable
from mindtorch.torch._register_numpy_primitive import _error_msg
import mindtorch.torch as ms_torch

_TEST_ERROR = os.environ.get('TEST_ERROR')

_skip_test_error = False if _TEST_ERROR and _TEST_ERROR.upper() in ('TRUE', '1') else True

def is_test_under_cpu_context():
    return _skip_test_error and ms.context.get_context("device_target").upper() == 'CPU'

def is_test_under_gpu_context():
    return _skip_test_error and ms.context.get_context("device_target").upper() == 'GPU'

def is_test_under_ascend_context():
    return _skip_test_error and ms.context.get_context("device_target").upper() == 'ASCEND'


def SKIP_ENV_CPU(reason):
    return pytest.mark.skipif(condition=is_test_under_cpu_context(), reason=reason)

def SKIP_ENV_GPU(reason):
    return pytest.mark.skipif(condition=is_test_under_gpu_context(), reason=reason)

def SKIP_ENV_ASCEND(reason):
    return pytest.mark.skipif(condition=is_test_under_ascend_context(), reason=reason)


_MODE_ENV = os.environ.get('TEST_MODE')

def set_mode_by_env_config():
    if _MODE_ENV is not None and _MODE_ENV == "1":
        ms.context.set_context(mode=ms.GRAPH_MODE, jit_syntax_level=ms.STRICT, pynative_synchronize=True)
    else:
        ms.context.set_context(mode=ms.PYNATIVE_MODE, jit_syntax_level=ms.STRICT, pynative_synchronize=True)


def is_test_under_graph_context():
    return ms.context.get_context("mode") == ms.GRAPH_MODE

def is_test_under_pynative_context():
    return ms.context.get_context("mode") == ms.PYNATIVE_MODE

def SKIP_ENV_GRAPH_MODE(reason):
    return pytest.mark.skipif(condition=is_test_under_graph_context(), reason=reason)

def SKIP_ENV_PYNATIVE_MODE(reason):
    return pytest.mark.skipif(condition=is_test_under_pynative_context(), reason=reason)

def SKIP_ENV_ASCEND_GRAPH_MODE(reason):
    return pytest.mark.skipif(condition=is_test_under_graph_context() \
        and is_test_under_ascend_context(), reason=reason)

def _param_compare(a1, b1, rtol=1e-5, atol=1e-8, equal_nan=False):
    a1 = a1.numpy()
    b1 = b1.numpy()
    assert a1.dtype == b1.dtype
    assert a1.shape == b1.shape
    assert np.allclose(a1, b1, rtol=rtol, atol=atol, equal_nan=equal_nan)

def param_compare(a1, b1, rtol=1e-5, atol=1e-8, equal_nan=False):
    if isinstance(a1, (tuple, list)) or isinstance(b1, (tuple, list)):
        assert len(a1) == len(b1)
        for i in range(len(a1)):
            _param_compare(a1[i], b1[i], rtol=rtol, atol=atol, equal_nan=equal_nan)
    else:
        _param_compare(a1, b1, rtol=rtol, atol=atol, equal_nan=equal_nan)

def _number_compare(a1, b1, rtol=1e-5, atol=1e-8):
    assert math.isclose(a1, b1, rel_tol=rtol, abs_tol=atol)

def number_compare(a1, b1, rtol=1e-5, atol=1e-8, equal_nan=False):
    if isinstance(a1, (tuple, list)) or isinstance(b1, (tuple, list)):
        assert len(a1) == len(b1)
        for i in range(len(a1)):
            _number_compare(a1[i], b1[i], rtol=rtol, atol=atol)
    else:
        _number_compare(a1, b1, rtol=rtol, atol=atol)

def type_shape_compare(a1, b1):
    a1 = a1.numpy()
    b1 = b1.numpy()
    assert a1.dtype == b1.dtype
    assert a1.shape == b1.shape

def number_shape_compare(a1, b1, rtol=1e-5, atol=1e-8, equal_nan=False):
    a1 = a1.numpy()
    b1 = b1.numpy()
    assert a1.shape == b1.shape
    assert np.allclose(a1, b1, rtol=rtol, atol=atol, equal_nan=equal_nan)

def err_msg_compare(e, func_name):
    error_str = _error_msg.format(func_name)
    graph_error_str = "\'"+error_str+"\'"
    assert error_str == str(e) or graph_error_str == str(e).split('\n')[0]


def grad_test(func_name, func, *input):
    try:
        _ = ms.grad(func)(*input)
        assert False
    except RuntimeError as e:
        err_msg_compare(e, func_name)

class TestNet(ms_torch.nn.Module):
    def __init__(self, fn):
        super().__init__()
        self.fn = fn

    def forward(self, *inputs, **kwargs):
        return self.fn(*inputs, **kwargs)


class graph_lax_level():
    # STRICT = 0, COMPATIBLE = 1, LAX = 2

    def __enter__(self):
        self.prev_jit_level = ms.get_context("jit_syntax_level")
        ms.set_context(jit_syntax_level = ms.LAX)

    def __exit__(self, exc_type, exc_value, traceback):
        ms.set_context(jit_syntax_level = self.prev_jit_level)

class enable_backward():
    def __enter__(self):
        self.prev_enable_backward = os.environ.get('ENABLE_BACKWARD')
        os.environ["ENABLE_BACKWARD"] = "1"
        jit_mode_pi_enable()
        self.pre_pynative_synchronize=ms.get_context("pynative_synchronize")
        ms.set_context(pynative_synchronize=False)


    def __exit__(self, exc_type, exc_value, traceback):
        if self.prev_enable_backward != 1:
            os.environ["ENABLE_BACKWARD"] = "0"
            jit_mode_pi_disable()
            ms.set_context(pynative_synchronize=self.pre_pynative_synchronize)
