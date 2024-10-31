import mindtorch.torch as pytorch
import numpy as np
import torch
from mindspore import context
import mindspore as ms
from ...utils import SKIP_ENV_ASCEND, SKIP_ENV_GPU, SKIP_ENV_GRAPH_MODE, set_mode_by_env_config, param_compare, \
                     SKIP_ENV_PYNATIVE_MODE, SKIP_ENV_ASCEND_GRAPH_MODE, type_shape_compare, is_test_under_pynative_context, \
                     is_test_under_gpu_context, is_test_under_ascend_context, grad_test, is_test_under_cpu_context, \
                     SKIP_ENV_CPU, graph_lax_level, type_shape_compare

from mindtorch.torch._register_numpy_primitive import _error_msg
from mindtorch.utils import pynative_mode_condition, is_under_cpu_context, FP64_MAX

set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_add_():
    value = np.array([[1.0, 1.0],[1.0,1.0]]).astype(np.float32)
    py_tensor = torch.tensor(value)
    py_tensor.add_(1.5)
    ms_tensor = pytorch.tensor(value)
    ms_tensor.add_(1.5)
    assert np.allclose(ms_tensor.numpy(), py_tensor.numpy())


def test_mul():
    tensor = np.array([[1.0, 1.0],[1.0,1.0]])
    ms_tensor = pytorch.tensor(tensor)
    torch_tensor = torch.tensor(tensor)

    ms_result = ms_tensor.mul(2.0)
    torch_result = torch_tensor.mul(2.0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())

    tensor = np.random.random((3, 3)).astype(np.float32)
    value = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_value = torch.tensor(value)
    ms_value = pytorch.tensor(value)
    torch_output = torch_tensor.mul(torch_value)
    ms_output = ms_tensor.mul(ms_value)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_mul_():
    tensor = np.array([[1.0, 1.0],[1.0,1.0]])
    ms_tensor = pytorch.tensor(tensor)
    torch_tensor = torch.tensor(tensor)

    ms_tensor.mul_(2.0)
    torch_tensor.mul_(2.0)
    assert np.allclose(ms_tensor.numpy(), torch_tensor.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_fill_():
    input = np.array([[1.0, 1.0],[1.0,1.0]]).astype(np.float32)
    py_tensor = torch.tensor(input)
    ms_tensor = pytorch.tensor(input)
    py_tensor.fill_(3.0)
    ms_tensor.fill_(3.0)
    param_compare(ms_tensor, py_tensor)

    py_tensor.fill_(2)
    ms_tensor.fill_(2)
    param_compare(ms_tensor, py_tensor)

    py_tensor.fill_(False)
    ms_tensor.fill_(False)
    param_compare(ms_tensor, py_tensor)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_fill_tensor():
    input = np.random.randn(2, 3).astype(np.float32)
    py_tensor = torch.tensor(input)
    ms_tensor = pytorch.tensor(input)

    py_tensor.fill_(torch.tensor(2.0))
    ms_tensor.fill_(pytorch.tensor(2.0))
    param_compare(ms_tensor, py_tensor)

def test_size_with_dim():
    input = np.random.random((3, 4, 5)).astype(np.float32)
    torch_tensor = torch.tensor(input)
    ms_tensor = pytorch.tensor(input)

    torch_size = torch_tensor.size(dim=1)
    ms_size = ms_tensor.size(dim=1)

    assert np.allclose(ms_size, torch_size)

def test_size():
    input = np.random.random((3, 4, 5)).astype(np.float32)
    torch_tensor = torch.tensor(input)
    ms_tensor = pytorch.tensor(input)

    torch_size = torch_tensor.size()
    ms_size = ms_tensor.size()

    assert np.allclose(ms_size, torch_size)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_zero_():
    input = np.array([[1.0, 1.0],[1.0,1.0]])
    py_tensor = torch.tensor(input)
    py_tensor.zero_()

    ms_tensor = pytorch.tensor(input)
    ms_tensor.zero_()

    assert np.allclose(ms_tensor.numpy(), py_tensor.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_PYNATIVE_MODE(reason="normal_ returns random output on 2.1")
def test_normal_():
    input = np.array([[1.0, 1.0],[1.0,1.0]]).astype(np.float64)
    py_tensor = torch.tensor(input)
    py_tensor.normal_(1.0, 0.5)

    ms_tensor = pytorch.tensor(input)
    ms.set_seed(2)
    ms_tensor.normal_(1.0, 0.5)
    ms_out1 = ms_tensor.clone()
    ms.set_seed(2)
    ms_tensor.normal_(1.0, 0.5)
    ms_out2 = ms_tensor.clone()
    ms_tensor.normal_(1.0, 0.5)
    ms_out3 = ms_tensor.clone()

    assert ms_tensor.asnumpy().dtype == py_tensor.numpy().dtype
    assert ms_tensor.asnumpy().shape == py_tensor.numpy().shape
    assert np.allclose(ms_out1.numpy(), ms_out2.numpy())
    #TODO: Validate the testcase after fixing the dyn shape
    #assert not np.allclose(ms_out2.numpy(), ms_out3.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_uniform_():
    input = np.array([[1.0, 1.0],[1.0,1.0]])

    py_tensor = torch.tensor(input)
    py_tensor.uniform_(0.5, 1.0)
    ms_tensor = pytorch.tensor(input)
    ms_tensor.uniform_(0.5, 1.0)

    type_shape_compare(py_tensor, ms_tensor)
    assert np.all(ms_tensor.numpy() > 0.5) and np.all(ms_tensor.numpy() < 1.0)


    ms.set_seed(2)
    ms_tensor.uniform_(2, 5)
    ms_out1 = ms_tensor.clone()
    ms.set_seed(2)
    ms_tensor.uniform_(2, 5)
    ms_out2 = ms_tensor.clone()

    assert np.allclose(ms_out1.numpy(), ms_out2.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_uniform_range():
    input = np.random.randn(10)

    py_tensor = torch.tensor(input)
    py_tensor.uniform_()
    ms_tensor = pytorch.tensor(input)
    ms_tensor.uniform_()
    type_shape_compare(py_tensor, ms_tensor)
    assert np.all(ms_tensor.numpy() > 0.0) and np.all(ms_tensor.numpy() < 1.0)

    py_tensor = torch.tensor(input)
    py_tensor.uniform_(5, 10)
    ms_tensor = pytorch.tensor(input)
    ms_tensor.uniform_(5, 10)
    type_shape_compare(py_tensor, ms_tensor)
    assert np.all(ms_tensor.numpy() > 5) and np.all(ms_tensor.numpy() < 10)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_erfinv_():
    tensor = pytorch.tensor(np.array([[1.0, 1.0],[1.0,1.0]]).astype(np.float32))
    output = tensor.erfinv_()
    param_compare(tensor, output)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="erfinv_ currently not support float64 on Ascend")
def test_erfinv_fp64():
    tensor = pytorch.tensor(np.random.randn(2, 2))
    output = tensor.erfinv_()
    param_compare(tensor, output, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_clamp_():
    input = np.array([[1.0, 5.0],[10.0, 20.0]]).astype(np.float32)
    py_tensor = torch.tensor(input)
    py_tensor.clamp_(min=5.0)

    ms_tensor = pytorch.tensor(input)
    ms_tensor.clamp_(min=5.0)
    assert np.allclose(ms_tensor.numpy(), py_tensor.numpy())

    py_tensor_2 = torch.tensor(input)
    py_tensor_2.clamp_(max=10.0)

    ms_tensor_2 = pytorch.tensor(input)
    ms_tensor_2.clamp_(max=10.0)
    assert np.allclose(ms_tensor_2.numpy(), py_tensor_2.numpy())


    py_tensor_3 = torch.tensor(input)
    py_tensor_3.clamp_(min=10.0, max=5.0)

    ms_tensor_3 = pytorch.tensor(input)
    ms_tensor_3.clamp_(min=10.0, max=5.0)
    assert np.allclose(ms_tensor_3.numpy(), py_tensor_3.numpy())

def test_permute1():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.permute(1,0,2)
    ms_output = ms_tensor.permute(1,0,2)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

def test_permute2():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.permute([1,0,2])
    ms_output = ms_tensor.permute([1,0,2])
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_copy_():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    src = np.random.random((3, 4, 4)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_src = torch.tensor(src)
    ms_src = pytorch.tensor(src)
    torch_tensor.copy_(torch_src)
    ms_tensor.copy_(ms_src)
    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_copy_scalar():
    tensor = np.random.random(1).item()
    src = np.random.random(1).item()
    torch_tensor = torch.tensor(tensor).to(torch.float32)
    ms_tensor = pytorch.tensor(tensor).to(pytorch.float32)
    torch_src = torch.tensor(src).to(torch.float16)
    ms_src = pytorch.tensor(src).to(pytorch.float16)
    torch_tensor.copy_(torch_src)
    ms_tensor.copy_(ms_src)
    param_compare(ms_tensor, torch_tensor)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_copy_adapter_scalar():
    tensor = np.random.random(1).item()
    src = np.random.random(1).item()
    torch_tensor = torch.tensor(tensor).to(torch.float32)
    ms_tensor = pytorch.tensor(tensor).to(pytorch.float32)
    torch_src = torch.tensor(src).to(torch.float16)
    ms_src = pytorch.tensor(src).to(pytorch.float16)
    torch_tensor.copy_(torch_src)
    ms_result = ms_tensor.copy_adapter(ms_src)
    param_compare(ms_result, torch_tensor)

def test_expand():
    tensor = np.random.random((1, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.expand(4, -1)
    ms_output = ms_tensor.expand(4, -1)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

    torch_tensor = torch.tensor([True, False])
    ms_tensor = pytorch.tensor([True, False])
    torch_output = torch_tensor.expand(2, 2)
    ms_output = ms_tensor.expand(2, 2)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

def test_sigmoid():
    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.sigmoid()
    ms_output = ms_tensor.sigmoid()
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_sigmoid_():
    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_tensor.sigmoid_()
    ms_tensor.sigmoid_()
    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())

def test_float():
    tensor = np.random.random((3, 3)).astype(np.int64)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.float()
    ms_output = ms_tensor.float()
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

def test_flip():
    tensor = np.random.random((3, 3)).astype(np.int64)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.flip(0)
    ms_output = ms_tensor.flip(0)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

    torch_output = torch_tensor.flip([0,1])
    ms_output = ms_tensor.flip([0,1])
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

def test_sign():
    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.sign()
    ms_output = ms_tensor.sign()
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_sign_():
    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_tensor.sign_()
    ms_tensor.sign_()
    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype

def test_signbit():
    np_array1 = np.array([[-3, -2, -0.0, 0.0, 2, 3]]).astype(np.float16)

    torch_tensor1 = torch.tensor(np_array1)
    torch_out1 = torch.signbit(torch_tensor1)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_out1 = pytorch.signbit(ms_tensor1)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype

def test_div():
    tensor = np.random.random((3, 3)).astype(np.int64)
    value = np.random.random((3, 3)).astype(np.float32)
    torch_value = torch.tensor(value)
    ms_value = pytorch.tensor(value)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.div(torch_value)
    ms_output = ms_tensor.div(ms_value)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

def test_div2():
    tensor = np.array([3, 3]).astype(np.float16)
    value = np.array([2, 2]).astype(np.int32)
    torch_value = torch.tensor(value)
    ms_value = pytorch.tensor(value)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.div(torch_value, rounding_mode='floor')
    ms_output = ms_tensor.div(ms_value, rounding_mode='floor')
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

def test_div3():
    tensor = np.array([-3, 3]).astype(np.int32)
    value = np.array([2, 2]).astype(np.float32)
    torch_value = torch.tensor(value)
    ms_value = pytorch.tensor(value)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.div(torch_value, rounding_mode='trunc')
    ms_output = ms_tensor.div(ms_value, rounding_mode='trunc')
    param_compare(torch_output, ms_output)

@SKIP_ENV_ASCEND(reason="div currently not support float64 on Ascend")
def test_div3_fp64():
    tensor = np.array([-3, 3]).astype(np.float64)
    value = np.array([2, 2]).astype(np.float64)
    torch_value = torch.tensor(value)
    ms_value = pytorch.tensor(value)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.div(torch_value, rounding_mode='trunc')
    ms_output = ms_tensor.div(ms_value, rounding_mode='trunc')
    param_compare(torch_output, ms_output)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_div_():
    x = np.array([ 0.3810,  1.2774, -0.2972, -0.3719,  0.4637]).astype(np.float16)

    a = np.array([[-0.3711, -1.9353, -0.4605, -0.2917],
                    [ 0.1815, -1.0111,  0.9805, -1.5923],
                    [ 0.1062,  1.4581,  0.7759, -1.2344],
                    [-0.1830, -0.0313,  1.1908, -1.4757]]).astype(np.float32)
    b = np.array([ 0.8032,  0.2930, -0.8113, -0.2308]).astype(np.float16)
    c = np.random.randint(0, 10, size=(4, 4)).astype(np.int64)

    torch_x = torch.tensor(x)
    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_c = torch.tensor(c)
    ms_x = pytorch.tensor(x)
    ms_a = pytorch.tensor(a)
    ms_b = pytorch.tensor(b)
    ms_c = pytorch.tensor(c)

    torch_x.div_(0.5)
    ms_x.div_(0.5)
    assert np.allclose(torch_x.numpy(), ms_x.numpy(), equal_nan=True)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

    torch_a.div_(torch_b)
    ms_a.div_(ms_b)
    param_compare(torch_a, ms_a, equal_nan=True)

    torch_a.div_(torch_b, rounding_mode='trunc')
    ms_a.div_(ms_b, rounding_mode='trunc')
    param_compare(torch_a, ms_a, equal_nan=True)

    torch_a.div_(torch_b, rounding_mode='floor')
    ms_a.div_(ms_b, rounding_mode='floor')
    param_compare(torch_a, ms_a, equal_nan=True)

    torch_a.div_(torch_c)
    ms_a.div_(ms_c)
    param_compare(torch_a, ms_a, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="div_ currently not support float64 on Ascend")
def test_div_fp64():
    a = np.random.randn(2, 2)
    b = np.random.randn(2).astype(np.float16)
    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    ms_a = pytorch.tensor(a)
    ms_b = pytorch.tensor(b)

    torch_a.div_(torch_b)
    ms_a.div_(ms_b)
    param_compare(torch_a, ms_a, equal_nan=True)
    torch_a.div_(torch_b, rounding_mode='trunc')
    ms_a.div_(ms_b, rounding_mode='trunc')
    param_compare(torch_a, ms_a, equal_nan=True)

def test_max():
    tensor = np.random.random((3, 3)).astype(np.int32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.max()
    ms_output = ms_tensor.max()
    param_compare(torch_output, ms_output)

    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.max(dim = 1)
    ms_output = ms_tensor.max(dim = 1)
    param_compare(torch_output, ms_output)

    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.max(1, True)
    ms_output = ms_tensor.max(1, True)
    param_compare(torch_output, ms_output)

    tensor = np.random.random((3, 3))
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.max(1, True)
    ms_output = ms_tensor.max(1, True)
    param_compare(torch_output, ms_output)


def test_numel():
    tensor = np.zeros((1, 2, 3, 4, 5))
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.numel()
    ms_output = ms_tensor.numel()
    assert np.allclose(ms_output, torch_output)

def test_sum():

    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.sum()
    ms_output = ms_tensor.sum()
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.sum(dim = 1)
    ms_output = ms_tensor.sum(dim = 1)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

def test_sum2():

    int8_max = np.iinfo(np.int8).max
    torch_output = torch.tensor([int8_max, int8_max]).sum(dtype=torch.int8)
    ms_output = pytorch.tensor([int8_max, int8_max]).sum(dtype=pytorch.int8)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

    torch_output = torch.tensor([int8_max, int8_max]).sum(dtype=torch.int64)
    ms_output = pytorch.tensor([int8_max, int8_max]).sum(dtype=pytorch.int64)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

def test_sum3():

    torch_tensor = torch.tensor([True, True, False])
    ms_tensor = pytorch.tensor([True, True, False])
    torch_output = torch_tensor.sum()
    ms_output = ms_tensor.sum()
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

    torch_tensor = torch.tensor([-1, 1], dtype=torch.bool)
    ms_tensor = pytorch.tensor([-1, 1], dtype=pytorch.bool)
    torch_output = torch_tensor.sum()
    ms_output = ms_tensor.sum()
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

    torch_tensor = torch.tensor([-1, 1])
    ms_tensor = pytorch.tensor([-1, 1])
    torch_output = torch_tensor.sum(dtype=torch.bool)
    ms_output = ms_tensor.sum(dtype=pytorch.bool)
    assert np.allclose(ms_output.asnumpy(), torch_output.numpy())
    assert ms_output.asnumpy().dtype == torch_output.numpy().dtype

def test_split():

    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.split(1, 0)
    ms_output = ms_tensor.split(1, 0)
    for i in range(3):
        assert np.allclose(ms_output[i].asnumpy(), torch_output[i].numpy())
        assert ms_output[i].asnumpy().dtype == torch_output[i].numpy().dtype

def test_numpy():
    tensor = np.random.random((3, 3)).astype(np.float32)
    torch_tensor_np = torch.tensor(tensor).numpy()
    ms_tensor_np = pytorch.tensor(tensor).numpy()
    assert np.allclose(ms_tensor_np, torch_tensor_np)
    assert ms_tensor_np.dtype == torch_tensor_np.dtype

def test_ndimension():
    x = np.ones((1, 2, 3))
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_output = torch_tensor.ndimension()
    ms_output = ms_tensor.ndimension()
    assert np.allclose(ms_output, torch_output)

def test_pow():
    x = np.random.random((2, 3)).astype(np.float32)
    exponent_float = 2.0
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_output = torch_tensor.pow(exponent_float)
    ms_output = ms_tensor.pow(exponent_float)
    assert np.allclose(ms_output.numpy(), torch_output.numpy())

    x_tensor = np.random.random((1, 4)).astype(np.float32)
    exponent_tensor = np.arange(1.0, 5.0)
    torch_tensor = torch.tensor(x_tensor)
    torch_exp = torch.tensor(exponent_tensor)
    torch_output = torch_tensor.pow(torch_exp)

    ms_tensor = pytorch.tensor(x_tensor)
    ms_exp = pytorch.tensor(exponent_tensor)
    ms_output = ms_tensor.pow(ms_exp)
    assert np.allclose(ms_output.numpy(), torch_output.numpy())

def test_repeat():
    torch_x = torch.tensor([1, 2, 3])
    torch_out1 = torch_x.repeat(4, 2)
    torch_out2 = torch_x.repeat([4, 2, 1])
    torch_out3 = torch_x.repeat((4, 2, 2))

    ms_x = pytorch.tensor([1, 2, 3])
    ms_out1 = ms_x.repeat(4, 2)
    ms_out2 = ms_x.repeat([4, 2, 1])
    ms_out3 = ms_x.repeat((4, 2, 2))
    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)

def test_repeat2():
    torch_out = torch.tensor([]).reshape(0,1,2,3).repeat((10, 20, 30, 40, 50, 60, 7))
    ms_out = pytorch.tensor([]).reshape(0,1,2,3).repeat((10, 20, 30, 40, 50, 60, 7))
    param_compare(ms_out, torch_out)

    torch_out = torch.tensor([]).repeat((5))
    ms_out = pytorch.tensor([]).repeat((5))
    param_compare(ms_out, torch_out)

def test_repeat_interleave():
    pytorch_x = torch.tensor([[1, 2, 3], [2, 4, 6]])
    pytorch_out = pytorch_x.repeat_interleave(2)
    ms_x = pytorch.tensor([[1, 2, 3], [2, 4, 6]])
    ms_out = ms_x.repeat_interleave(2)
    assert np.allclose(pytorch_out.numpy(), ms_out.asnumpy())

    pytorch_y = torch.tensor([[1, 2], [3, 4]])
    pytorch_out = pytorch_y.repeat_interleave(3, dim=1)
    ms_y = pytorch.tensor([[1, 2], [3, 4]])
    ms_out = ms_y.repeat_interleave(3, dim=1)
    assert np.allclose(pytorch_out.numpy(), ms_out.asnumpy())

    pytorch_out = pytorch_y.repeat_interleave(torch.tensor([1, 2]), dim=0)
    ms_out = ms_y.repeat_interleave(pytorch.tensor([1, 2]), dim=0)
    assert np.allclose(pytorch_out.numpy(), ms_out.asnumpy())

def test_reshape():
    x = np.ones((2, 3, 4))

    torch_tensor = torch.tensor(x)
    torch_output = torch_tensor.reshape(2,3,4)
    ms_tensor = pytorch.tensor(x)
    ms_output = ms_tensor.reshape(2,3,4)
    assert np.allclose(ms_output.numpy(), torch_output.numpy())

    torch_output = torch_tensor.reshape((6,4))
    ms_output = ms_tensor.reshape((6,4))
    assert np.allclose(ms_output.numpy(), torch_output.numpy())

    torch_output = torch_tensor.new().reshape((0,1,2,3))
    ms_output = ms_tensor.new().reshape((0,1,2,3))
    assert np.allclose(ms_output.size(), torch_output.size())

def test_reshape_as():
    x = [[-0.1, 0.3, 3.6], [0.4, 0.5, -3.2]]
    y = np.arange(6).reshape(3,2)

    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_y = torch.tensor(y)
    torch_out = torch_x.reshape_as(torch_y)
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_y = pytorch.tensor(y)
    ms_out = ms_x.reshape_as(ms_y)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_det():
    x = [[[-4.5, -1.5], [7.0, 6.0]], [[2.5, 0.5], [3.0, 9.0]]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.det()
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.det()
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_negative():
    x = [1, 2, -1, 2, 0, -3.5]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.negative()
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.negative()
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_abs():
    x = np.random.randn(2, 3, 4) * 20
    x1 = x.astype(np.int32)
    x2 = x.astype(np.uint8)
    torch_x1 = torch.tensor(x1)
    torch_x2 = torch.tensor(x2)
    ms_x1 = pytorch.tensor(x1)
    ms_x2 = pytorch.tensor(x2)
    torch_out1 = torch_x1.abs()
    torch_out2 = torch_x2.abs()
    ms_out1 = ms_x1.abs()
    ms_out2 = ms_x2.abs()
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_abs_():
    x = (np.random.randn(2, 3, 4) * 20).astype(np.float32)
    torch_x1 = torch.tensor(x)
    ms_x1 = pytorch.tensor(x)
    torch_x1.abs_()
    ms_x1.abs_()
    param_compare(torch_x1, ms_x1)

def test_ndim():
    x = [[[[[1], [2]]], [[[3], [4]]]]]
    torch_x = torch.tensor(x)
    torch_out = torch_x.ndim
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.ndim

    assert ms_out == torch_out

def test_amax():
    x = np.random.randn(1, 4, 4).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_out = torch_x.amax(None, True)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.amax(None, True)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="amax currently not support float64 on Ascend")
def test_amax_fp64():
    x = np.random.randn(4, 4)
    torch_x = torch.tensor(x)
    torch_out = torch_x.amax(-1, True)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.amax(-1, True)

    param_compare(torch_out, ms_out)


def test_amin():
    x = np.random.randn(1, 4, 4).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_out = torch_x.amin(-1, False)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.amin(-1, False)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="amin currently not support float64 on Ascend")
def test_amin_fp64():
    x = np.random.randn(2, 2)
    torch_x = torch.tensor(x)
    torch_out = torch_x.amin(None, False)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.amin(None, False)

    param_compare(torch_out, ms_out)

def test_as_strided():
    x = np.arange(0,16).reshape(4, 4).astype(np.int64)*2
    torch_x = torch.tensor(x)
    torch_out = torch_x.as_strided((2, 2, 3), (1, 2, 4), 1)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.as_strided((2, 2, 3), (1, 2, 4), 1)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_bmm():
    x = np.random.randn(3, 4, 5).astype(np.float32)
    y = np.random.randn(3, 5, 2).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.bmm(torch_y)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out = ms_x.bmm(ms_y)

    assert np.allclose(ms_out.numpy(), torch_out.numpy(), rtol=1e-4, atol=1e-6)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_clamp():
    x = np.random.randn(3, 3).astype(np.float64)
    torch_x = torch.tensor(x)
    torch_out = torch_x.clamp(0.3, 0.6)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.clamp(0.3, 0.6)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_dim():
    x = [[[[[1], [2]]], [[[3], [4]]]]]
    torch_x = torch.tensor(x)
    torch_out = torch_x.dim()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.dim()

    assert ms_out == torch_out

def test_expand_as():
    x = np.random.randn(3, 3)
    y = np.random.randn(2, 2, 3, 3)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.expand_as(torch_y)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out = ms_x.expand_as(ms_y)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_item():
    x = np.random.randn(1, 1).astype(np.half)
    torch_x = torch.tensor(x)
    torch_out = torch_x.item()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.item()

    assert ms_out == torch_out
    assert type(ms_out)==type(torch_out)

@SKIP_ENV_ASCEND(reason="on ascend not support inf and nan")
def test_log():
    x = [[0, -1, 1, 2, 2.71828, 3.5]]
    torch_x = torch.tensor(x)
    torch_out = torch_x.log()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.log()
    assert np.allclose(ms_out.numpy(), torch_out.numpy(), rtol=1e-4, atol=1e-5, equal_nan=True)

@SKIP_ENV_GPU(reason="testcase for ascend only, because ascend not support inf and nan, gpu test will be covered by test_log.")
@SKIP_ENV_CPU(reason="testcase for ascend only, because ascend not support inf and nan, cpu test will be covered by test_log.")
def test_log_ascend():
    x = [[1, 2, 2.71828, 3.5]]
    torch_x = torch.tensor(x)
    torch_out = torch_x.log()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.log()
    assert np.allclose(ms_out.numpy(), torch_out.numpy(), rtol=1e-4, atol=1e-5, equal_nan=True)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="on ascend not support inf and nan, test_log_ascend will cover the test")
def test_log_():
    x = [[0, -1, 1, 2, 2.71828, 3.5]]
    torch_x = torch.tensor(x)
    torch_x.log_()
    ms_x = pytorch.tensor(x)
    ms_x.log_()
    assert np.allclose(ms_x.numpy(), torch_x.numpy(), rtol=1e-4, atol=1e-5, equal_nan=True)

@SKIP_ENV_ASCEND(reason="on ascend not support inf and nan")
def test_log2():
    x = [[0, -1, 1, 2, 2.71828, 3.5]]
    torch_x = torch.tensor(x)
    torch_out = torch_x.log2()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.log2()
    assert np.allclose(ms_out.numpy(), torch_out.numpy(), rtol=1e-4, atol=1e-5, equal_nan=True)

@SKIP_ENV_GPU(reason="testcase for ascend only, gpu test will be covered by test_log2")
@SKIP_ENV_CPU(reason="testcase for ascend only, cpu test will be covered by test_log2")
def test_log2_ascend():
    x = [[1, 2, 2.71828, 3.5]]
    torch_x = torch.tensor(x)
    torch_out = torch_x.log2()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.log2()
    assert np.allclose(ms_out.numpy(), torch_out.numpy(), rtol=1e-4, atol=1e-5, equal_nan=True)

def test_matmul():
    x = np.random.randn(3, 4, 5).astype(np.float32)
    y = np.random.randn(5, 2).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.matmul(torch_y)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out = ms_x.matmul(ms_y)

    param_compare(ms_out, torch_out)

def test_squeeze():
    x = np.random.randn(1, 2, 3, 1)
    torch_x = torch.tensor(x)
    torch_out = torch_x.squeeze(-1)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.squeeze(-1)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_stride():
    x = np.arange(0,32).reshape(2, 4, 4).astype(np.half)
    torch_x = torch.tensor(x)
    torch_out = torch_x.stride(1)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.stride(1)

    assert ms_out == torch_out
    assert type(ms_out) == type(torch_out)

def test_sub():
    x = np.random.randn(3, 4).astype(np.half)
    y = np.random.randn(3, 4).astype(np.half)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.sub(torch_y, alpha=2)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out = ms_x.sub(ms_y, alpha=2)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_subtract():
    np_array1 = np.random.rand(1, 2, 3).astype(np.float32)
    np_other1 = np.random.rand(1, 2, 3).astype(np.float32)
    np_array2 = np.arange(10).astype(np.int16)
    np_other2 = np.arange(10, 20).astype(np.uint8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_other1 = torch.tensor(np_other1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_other2 = torch.tensor(np_other2)
    torch_out1 = torch_tensor1.subtract(torch_other1)
    torch_out2 = torch_tensor2.subtract(torch_other2, alpha=3)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_other1 = pytorch.tensor(np_other1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_other2 = pytorch.tensor(np_other2)
    ms_out1 = ms_tensor1.subtract(ms_other1)
    ms_out2 = ms_tensor2.subtract(ms_other2, alpha=3)
    assert np.allclose(ms_out1.numpy(), torch_out1.numpy())
    assert np.allclose(ms_out2.numpy(), torch_out2.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_subtract_():
    np_array = np.random.rand(1, 2, 3).astype(np.float32)
    np_other = np.random.rand(1, 2, 3).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_tensor.subtract_(torch_other, alpha=3)

    ms_tensor = pytorch.tensor(np_array)
    ms_other = pytorch.tensor(np_other)
    ms_tensor.subtract_(ms_other, alpha=3)

    assert np.allclose(ms_tensor.numpy(), torch_tensor.numpy())


def test_sum_to_size():
    np_array = np.random.rand(3, 4, 5, 6).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.sum_to_size(3, 1, 5, 1)

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.sum_to_size(3, 1, 5, 1)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

def test_trace():
    data = np.random.randn(5, 3).astype(np.float32)
    a1 = torch.tensor(data)
    a2 = pytorch.tensor(data)
    torch_out = a1.trace()
    ms_out = a2.trace()
    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())

def test_ceil():
    np_array = np.array([[1.501, 0.5, 1000.8],[-0.9, -2.5, -24.49]]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.ceil()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.ceil()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_ceil_():
    np_array = np.array([[1.501, 0.5, 1000.8],[-0.9, -2.5, -24.49]]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_tensor.ceil_()

    ms_tensor = pytorch.tensor(np_array)
    ms_tensor.ceil_()

    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype

def test_conj():
    x = torch.tensor([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_out = x.conj()

    y = pytorch.tensor(x.numpy())
    ms_out = y.conj()

    # TODO: pytorch error msg: Can't call numpy() on Tensor that has conjugate bit set.
    # Use tensor.resolve_conj().numpy() instead.
    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy())

def test_is_conj():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_out = torch_tensor.conj()
    ms_out = ms_tensor.conj()

    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy())
    assert ms_out.is_conj() == torch_out.is_conj()

@SKIP_ENV_GRAPH_MODE("graph mode not support assigning attr to tensor")
@SKIP_ENV_PYNATIVE_MODE("ms.jit forced to use graph mode, which not support assigning attr to tensor")
def test_is_conj_jit():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_out = torch_tensor.conj()
    ms_out = ms_tensor.conj()

    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy())
    assert ms_out.is_conj() == torch_out.is_conj()

def test_resolve_conj():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_out = torch_tensor.conj()
    torch_out1 = torch_out.resolve_conj()
    ms_out = ms_tensor.conj()
    ms_out1 = ms_out.resolve_conj()

    assert np.allclose(torch_out1.resolve_conj().numpy(), ms_out1.numpy())
    assert ms_out1.is_conj() == torch_out1.is_conj()

@SKIP_ENV_GRAPH_MODE("graph mode not support assigning attr to tensor")
@SKIP_ENV_PYNATIVE_MODE("ms.jit forced to use graph mode, which not support assigning attr to tensor")
def test_resolve_conj_jit():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_out = torch_tensor.conj()
    torch_out1 = torch_out.resolve_conj()

    @ms.jit
    def conj_func(ms_tensor):
        ms_out = ms_tensor.conj()
        ms_out1 = ms_out.resolve_conj()
        return ms_out1

    ms_out1 = conj_func(ms_tensor)
    assert np.allclose(torch_out1.resolve_conj().numpy(), ms_out1.numpy())
    assert ms_out1.is_conj() == torch_out1.is_conj()

def test_ger():
    v1 = torch.arange(1., 5.)
    v2 = torch.arange(1., 4.)
    torch_out = torch.ger(v1, v2)

    k1 = pytorch.tensor(v1.numpy())
    k2 = pytorch.tensor(v2.numpy())
    ms_out = k1.ger(k2)

    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

    v1 = torch.arange(1, 5)
    v2 = torch.arange(1, 4)
    torch_out = torch.ger(v1, v2)

    k1 = pytorch.tensor(v1.numpy())
    k2 = pytorch.tensor(v2.numpy())
    ms_out = k1.ger(k2)

    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

def test_moveaxis():
    t = torch.randn(3,2,1)
    torch_out1 = t.moveaxis(1, 0)
    torch_out2 = t.moveaxis((1, 2), (0, 1))

    t2 = pytorch.tensor(t.numpy())
    ms_out1 = t2.moveaxis(1, 0)
    ms_out2 = t2.moveaxis((1, 2), (0, 1))

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

def test_movedim():
    t = torch.randn(3,2,1)
    torch_out1 = t.movedim(1, 0)
    torch_out2 = t.movedim((1, 2), (0, 1))

    t2 = pytorch.tensor(t.numpy())
    ms_out1 = t2.movedim(1, 0)
    ms_out2 = t2.movedim((1, 2), (0, 1))

    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)

def test_others_tensor():
    tensor = pytorch.ByteTensor()
    tensor = pytorch.ByteTensor(3, 5)
    assert tensor.shape == (3, 5)
    assert tensor.dtype == pytorch.uint8
    tensor = pytorch.ByteTensor([1, 2, 3])
    assert tensor.shape == (3,)
    assert tensor.dtype == pytorch.uint8

    tensor = pytorch.CharTensor()
    tensor = pytorch.CharTensor(3, 5)
    assert tensor.shape == (3, 5)
    assert tensor.dtype == pytorch.int8
    tensor = pytorch.CharTensor([1, 2, 3])
    assert tensor.shape == (3,)
    assert tensor.dtype == pytorch.int8

    tensor = pytorch.ShortTensor()
    tensor = pytorch.ShortTensor(3, 5)
    assert tensor.shape == (3, 5)
    assert tensor.dtype == pytorch.int16
    tensor = pytorch.ShortTensor([1, 2, 3])
    assert tensor.shape == (3,)
    assert tensor.dtype == pytorch.int16

    tensor = pytorch.IntTensor()
    tensor = pytorch.IntTensor(3, 5)
    assert tensor.shape == (3, 5)
    assert tensor.dtype == pytorch.int32
    tensor = pytorch.IntTensor([1, 2, 3])
    assert tensor.shape == (3,)
    assert tensor.dtype == pytorch.int32

    tensor = pytorch.HalfTensor()
    tensor = pytorch.HalfTensor(3, 5)
    assert tensor.shape == (3, 5)
    assert tensor.dtype == pytorch.float16
    tensor = pytorch.HalfTensor([1, 2, 3])
    assert tensor.shape == (3,)
    assert tensor.dtype == pytorch.float16

    tensor = pytorch.FloatTensor()
    tensor = pytorch.FloatTensor(3, 5)
    assert tensor.shape == (3, 5)
    assert tensor.dtype == pytorch.float32
    tensor = pytorch.FloatTensor([1, 2, 3])
    assert tensor.shape == (3,)
    assert tensor.dtype == pytorch.float32

    tensor = pytorch.DoubleTensor()
    tensor = pytorch.DoubleTensor(3, 5)
    assert tensor.shape == (3, 5)
    assert tensor.dtype == pytorch.float64
    tensor = pytorch.DoubleTensor([1, 2, 3])
    assert tensor.shape == (3,)
    assert tensor.dtype == pytorch.float64

    tensor = pytorch.BoolTensor(3, 5)
    assert tensor.shape == (3, 5)
    assert tensor.dtype == pytorch.bool
    tensor = pytorch.BoolTensor([1, 2, 3])
    assert tensor.shape == (3,)
    assert tensor.dtype == pytorch.bool

def test_is_floating_point():
    x = [1, 2, -1, 2, 0, -3.5]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.is_floating_point()
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.is_floating_point()
    assert np.allclose(ms_out, torch_out)
    torch_x = torch.tensor(x, dtype=torch.int32)
    torch_out = torch_x.is_floating_point()
    ms_x = pytorch.tensor(x, dtype=pytorch.int32)
    ms_out = ms_x.is_floating_point()
    assert np.allclose(ms_out, torch_out)

def test_unbind():
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.unbind(1)
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.unbind(1)
    for ms_out_, torch_out_ in zip(ms_out, torch_out):
        assert np.allclose(ms_out_.numpy(), torch_out_.numpy())

def test_unsqueeze():
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.unsqueeze(1)
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.unsqueeze(1)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_is_signed():
    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.is_signed()
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.is_signed()
    np.allclose(ms_out, torch_out)

def test_transpose1():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.transpose(0, 2)
    ms_output = ms_tensor.transpose(0, 2)
    assert np.allclose(ms_output.numpy(), torch_output.numpy())


def test_transpose2():
    tensor = np.random.random((1, 3, 4, 4)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.transpose(1,  2)
    ms_output = ms_tensor.transpose(1,  2)
    assert np.allclose(ms_output.numpy(), torch_output.numpy())

def test_transpose3():
    torch_tensor = torch.randn(2, 0, 0)
    ms_tensor = pytorch.randn(2, 0, 0)
    torch_output = torch_tensor.transpose(1, 0)
    ms_output = ms_tensor.transpose(1, 0)
    assert np.allclose(ms_output.numpy(), torch_output.numpy())
    assert ms_output.numpy().dtype == torch_output.numpy().dtype
    assert ms_output.numpy().shape == torch_output.numpy().shape

def test_floor():
    tensor = np.random.random((1, 3, 4, 4)).astype(np.float32)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.floor()
    ms_output = ms_tensor.floor()
    assert np.allclose(ms_output.numpy(), torch_output.numpy())

def test_isfinite():
    x = [1, float('inf'), 2, float('-inf'), float('nan')]
    torch_x = torch.tensor(x)
    torch_out = torch_x.isfinite()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.isfinite()
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_isnan():
    x = [1, float('nan'), 2]
    torch_x = torch.tensor(x)
    torch_out = torch_x.isnan()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.isnan()
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_expand1():
    x = [[1], [2], [3]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.expand(3, 4)
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.expand(3, 4)
    param_compare(ms_out, torch_out)

def test_expand_list():
    x = [[1], [2], [3]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out1 = torch_x.expand([3, 4])
    torch_out2 = torch_x.expand((3, 4))
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out1 = ms_x.expand([3, 4])
    ms_out2 = ms_x.expand((3, 4))
    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)


def test_clone():
    def fun(x):
        b = x.clone()
        return 2 * x + 3 * b

    x = [8]
    torch_x = torch.tensor(x, dtype=torch.float32, requires_grad=True)
    torch_out = fun(torch_x)
    ms_x = pytorch.tensor(x, dtype=pytorch.float32, requires_grad=True)
    ms_out = fun(ms_x)
    assert np.allclose(ms_out.asnumpy(), torch_out.detach().numpy())

    torch_out.backward()
    torch_grad = torch_x.grad

    # Automatic differentiation method 1
    ms_grad = ms.grad(fun)(ms_x)
    assert np.allclose(torch_grad.detach().numpy(), ms_grad.asnumpy())


def test_detach():
    def fun(x):
        b = x.detach()
        return 2 * x + 3 * b

    x = [8]
    torch_x = torch.tensor(x, dtype=torch.float32, requires_grad=True)
    torch_out = fun(torch_x)
    ms_x = pytorch.tensor(x, dtype=pytorch.float32, requires_grad=True)
    ms_out = fun(ms_x)
    assert np.allclose(ms_out.asnumpy(), torch_out.detach().numpy())

    torch_out.backward()
    torch_grad = torch_x.grad

    # Automatic differentiation method 1
    ms_grad = ms.grad(fun)(ms_x)
    assert np.allclose(torch_grad.detach().numpy(), ms_grad.asnumpy())


def test_new_zeros():
    x = [[1], [2], [3]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.new_zeros((3, 5), dtype=torch.int32)
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.new_zeros((3, 5), dtype=pytorch.int32)
    param_compare(torch_out, ms_out)

    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_out = torch_x.new_zeros(3, 5)
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_out = ms_x.new_zeros(3, 5)
    param_compare(torch_out, ms_out)
    torch_out = torch_x.new_zeros(size=(3, 5))
    ms_out = ms_x.new_zeros(size=(3, 5))
    param_compare(torch_out, ms_out)

def test_sort():
    x = [[0, 1, 2, 0, 1, 2], [5, 4, 3, 5, 4, 3]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_x_int = torch.tensor(x, dtype=torch.int64)
    torch_out1, torch_out2 = torch_x.sort()
    torch_out1_int, torch_out2_int = torch_x_int.sort()
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_x_int = pytorch.tensor(x, dtype=pytorch.int64)
    ms_out1, ms_out2 = ms_x.sort()
    ms_out1_int, ms_out2_int = ms_x_int.sort()
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(ms_out2.numpy(), torch_out2.numpy())
    assert np.allclose(torch_out1_int.numpy(), ms_out1_int.numpy())
    assert np.allclose(ms_out2_int.numpy(), torch_out2_int.numpy())
    assert torch_out1_int.numpy().dtype == ms_out1_int.numpy().dtype
    assert torch_out2_int.numpy().dtype == ms_out2_int.numpy().dtype

    torch_out1, torch_out2 = torch_x.sort(0, True)
    ms_out1, ms_out2 = ms_x.sort(0, True)
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(ms_out2.numpy(), torch_out2.numpy())

def test_msort():
    x = [[0, 1, 2, 0, 1, 2], [5, 4, 3, 5, 4, 3]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_x_int = torch.tensor(x, dtype=torch.int64)
    torch_out = torch_x.msort()
    torch_out_int = torch_x_int.msort()
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_x_int = pytorch.tensor(x, dtype=pytorch.int64)
    ms_out = ms_x.msort()
    ms_out_int = ms_x_int.msort()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert np.allclose(torch_out_int.numpy(), ms_out_int.numpy())
    assert torch_out_int.numpy().dtype == ms_out_int.numpy().dtype

def test_argsort():
    x = [[0, 1, 2, 0, 1, 2], [5, 4, 3, 5, 4, 3]]
    torch_x = torch.tensor(x, dtype=torch.float32)
    torch_x_int = torch.tensor(x, dtype=torch.int64)
    torch_out = torch_x.argsort(-1, True)
    torch_out_int = torch_x_int.argsort()
    ms_x = pytorch.tensor(x, dtype=pytorch.float32)
    ms_x_int = pytorch.tensor(x, dtype=pytorch.int64)
    ms_out = ms_x.argsort(-1, True)
    ms_out_int = ms_x_int.argsort()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert np.allclose(torch_out_int.numpy(), ms_out_int.numpy())
    assert torch_out_int.numpy().dtype == ms_out_int.numpy().dtype

def test_sqrt():
    x = [2.0755,  1.0226,  0.0831,  0.4806]
    torch_x = torch.tensor(x, dtype=torch.float64)
    torch_out = torch_x.sqrt()
    ms_x = pytorch.tensor(x, dtype=pytorch.float64)
    ms_out = ms_x.sqrt()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_rsqrt1():
    x = [2.0755, 1.0226, 0.0831, 0.4806]
    torch_x = torch.tensor(x, dtype=torch.float64)
    torch_out = torch_x.rsqrt()
    ms_x = pytorch.tensor(x, dtype=pytorch.float64)
    ms_out = ms_x.rsqrt()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_rsqrt2():
    x = [2, 1, 3, 6]
    torch_x = torch.tensor(x, dtype=torch.int64)
    torch_out = torch_x.rsqrt()
    ms_x = pytorch.tensor(x, dtype=pytorch.int64)
    ms_out = ms_x.rsqrt()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_rsqrt3():
    x = [True, False, True, True]
    torch_x = torch.tensor(x, dtype=torch.bool)
    torch_out = torch_x.rsqrt()
    ms_x = pytorch.tensor(x, dtype=pytorch.bool)
    ms_out = ms_x.rsqrt()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_to():
    ms_x = pytorch.tensor([[1], [2], [3]], dtype=pytorch.float32)
    ms_y = pytorch.tensor([2], dtype=pytorch.int32)
    assert ms_x.dtype == pytorch.float32
    ms_x = ms_x.to(ms_y)
    assert ms_x.dtype == pytorch.int32
    ms_x = ms_x.to("cpu")
    assert ms_x.dtype == pytorch.int32
    ms_x = ms_x.to("cpu", pytorch.float32)
    assert ms_x.dtype == pytorch.float32
    ms_x = ms_x.to(other=ms_y)
    assert ms_x.dtype == pytorch.int32
    ms_x = ms_x.to(dtype=pytorch.float32)
    assert ms_x.dtype == pytorch.float32
    ms_x = ms_x.to(device="CUDA", dtype=pytorch.int32)
    assert ms_x.dtype == pytorch.int32
    ms_x = ms_x.to("CUDA", dtype=pytorch.float32)
    assert ms_x.dtype == pytorch.float32
    ms_x = ms_x.to(pytorch.int32)
    assert ms_x.dtype == pytorch.int32
    ms_x = ms_x.to(device="CPU")
    assert ms_x.dtype == pytorch.int32

def test_to_device_index():
    a = pytorch.tensor(2)
    b = pytorch.tensor(3)
    a.to(b.device.index)

def test_resize():
    x = np.array([[1, 2, 3], [4, 5, 6]])

    torch_x = torch.tensor(x)
    torch_out = torch_x.resize(3, 2)

    ms_x = pytorch.tensor(x)
    ms_out = ms_x.resize(3, 2)
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

    if is_test_under_pynative_context():
        torch_out = torch_x.new().resize_(2, 2)
        ms_out = ms_x.new().resize_(2, 2)
        assert np.allclose(torch_out.size(), ms_out.size())
        torch_out = torch_x.new().resize_((1, 4))
        ms_out = ms_x.new().resize_((1, 4))
        assert np.allclose(torch_out.size(), ms_out.size())

def test_resize_as():
    # In torch.Tensor.resize_as(input), input.numel() should be equal to origin tensor's
    # So here, we don't test the need padding case

    a = np.array([[1, 2, 3],[4, 5, 6]])
    b = np.array([[1, 2],[3, 4], [5, 6]])
    c = np.array([1, 2, 3, 4, 5, 6])

    ms_a = pytorch.tensor(a)
    ms_b = pytorch.tensor(b)
    ms_c = pytorch.tensor(c)
    ms_out1 = ms_a.resize_as(ms_b)
    ms_out2 = ms_a.resize_as(ms_c)

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_c = torch.tensor(c)
    torch_out1 = torch_a.resize_as(torch_b)
    torch_out2 = torch_a.resize_as(torch_c)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())

    if is_test_under_pynative_context():
        torch_out = ms_c.new().resize_as_(ms_b)
        ms_out = torch_c.new().resize_as_(torch_b)
        assert np.allclose(torch_out.size(), ms_out.size())


def test_index_fill():
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    index = np.array([0, 2])

    ms_x = pytorch.tensor(x)
    ms_index = pytorch.tensor(index)
    ms_out = ms_x.index_fill(1, ms_index, -1)

    torch_x = torch.tensor(x)
    torch_index = torch.tensor(index, dtype=torch.int64)
    torch_out = torch_x.index_fill(1, torch_index, -1)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_index_fill_():
    x = np.zeros((4, 4))
    index = np.array([3, 2, 1, 0])

    ms_x = pytorch.tensor(x)
    ms_index = pytorch.tensor(index)
    ms_x.index_fill_(1, ms_index, -1)

    torch_x = torch.tensor(x)
    torch_index = torch.tensor(index, dtype=torch.int64)
    torch_x.index_fill_(1, torch_index, -1)

    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype


def test_data():
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def func(x):
        return x.data * x.data

    ms_x = pytorch.tensor(x)
    ms_x_data = ms_x.data
    grad_func = ms.ops.grad(func)
    grads = grad_func(ms_x)
    torch_x = torch.tensor(x)
    torch_x_data = torch_x.data

    assert np.allclose(ms_x_data.numpy(), torch_x_data.numpy())
    assert np.allclose(grads.asnumpy(), np.zeros((3, 3)))

def test_new():
    x = np.array([1, 2])

    ms_x = pytorch.tensor(x)
    torch_x = torch.tensor(x)

    ms_out = ms_x.new(3, 4, 5)
    torch_out = torch_x.new(3, 4, 5)
    assert ms_out.shape == torch_out.shape
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

    ms_out = ms_x.new([1, 2, 3, 4])
    torch_out = torch_x.new([1, 2, 3, 4])
    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

    ms_out = ms_x.new()
    torch_out = torch_x.new()
    assert ms_out.shape == torch_out.shape
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

    ms_out = ms_x.new(x)
    torch_out = torch_x.new(x)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

def test_cuda():
    x = pytorch.tensor([1])
    x.cuda(device=None, non_blocking=False, memory_format=None)

def test_t1():
    x = np.random.randn(3, 4)

    torch_x = torch.tensor(x)

    ms_x = pytorch.tensor(x)

    torch_out = torch_x.t()
    ms_out = ms_x.t()

    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_t2():
    x = np.random.randn(4)

    torch_x = torch.tensor(x)

    ms_x = pytorch.tensor(x)

    torch_out = torch_x.t()
    ms_out = ms_x.t()

    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_T():
    x = np.random.randn(2,3,4)

    torch_x = torch.tensor(x)

    ms_x = pytorch.tensor(x)

    torch_out = torch_x.T
    ms_out = ms_x.T

    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_T2():

    torch_out = torch.tensor([]).reshape(3,0,4).T
    ms_out = pytorch.tensor([]).reshape(3,0,4).T

    param_compare(torch_out, ms_out)

def test_T3():

    torch_out = torch.tensor([]).reshape(0,3,4).T
    ms_out = pytorch.tensor([]).reshape(0,3,4).T

    param_compare(torch_out, ms_out)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_t_():
    data = np.random.randn(2, 3).astype(np.float32)

    torch_tensor = torch.tensor(data)
    ms_tensor = pytorch.tensor(data)

    torch_tensor.t_()
    ms_tensor.t_()

    assert np.allclose(torch_tensor.numpy(), ms_tensor.numpy())

def test_along_dim():
    data = np.random.randn(2, 3).astype(np.float32)

    a = torch.tensor(data)
    torch_out1 = a.take_along_dim(torch.tensor([0, 5]))
    torch_out2 = a.take_along_dim(torch.tensor([[0], [2]]), dim=1)

    b = pytorch.tensor(data)
    ms_out1 = b.take_along_dim(pytorch.tensor([0, 5]))
    ms_out2 = b.take_along_dim(pytorch.tensor([[0], [2]]), dim=1)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())

def test_mean1():
    ms_tensor = pytorch.tensor([[1., 2, 3], [1, 2, 3]])
    ms_result = ms_tensor.mean(dim=0)

    torch_tensor = torch.tensor([[1., 2, 3], [1, 2, 3]])
    torch_result = torch_tensor.mean(dim=0)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_mean2():
    ms_tensor = pytorch.tensor([[1., 2, 3], [1, 2, 3]])
    ms_result = ms_tensor.mean(dim=(0, -1))

    torch_tensor = torch.tensor([[1., 2, 3], [1, 2, 3]])
    torch_result = torch_tensor.mean(dim=(0, -1))

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_prod1():
    ms_tensor = pytorch.tensor([[1., 2, 3], [1, 2, 3]])
    ms_result = ms_tensor.prod(dim=0)

    torch_tensor = torch.tensor([[1., 2, 3], [1, 2, 3]])
    torch_result = torch_tensor.prod(dim=0)

    param_compare(ms_result, torch_result)

def test_prod_bool():
    ms_tensor = pytorch.tensor([False, True])
    ms_result = ms_tensor.prod()

    torch_tensor = torch.tensor([False, True])
    torch_result = torch_tensor.prod()

    print("ms_result: ", ms_result, ms_result.dtype)
    print("torch_result: ", torch_result, torch_result.dtype)
    param_compare(ms_result, torch_result)


def test_index_select():
    data = np.random.randn(3, 4 ,5)

    x_torch = torch.tensor(data)
    indices = torch.tensor([0, 2])
    torch_out = x_torch.index_select(1, indices)

    x_ms = pytorch.tensor(data)
    indices = pytorch.tensor([0, 2])
    ms_out = x_ms.index_select(1, indices)

    param_compare(ms_out, torch_out)


def test_index_select_scaler():
    data = np.random.randn(2, 3)
    x_torch = torch.tensor(data)
    indices = torch.tensor(1)
    torch_out = x_torch.index_select(1, indices)

    x_ms = pytorch.tensor(data)
    indices = pytorch.tensor(1)
    ms_out = x_ms.index_select(1, indices)

    param_compare(ms_out, torch_out)

def nonzero():
    np_array = np.random.random((2,3,4)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.nonzero()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.nonzero()

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

def bool():
    np_array = np.random.random((2, 3, 4)).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.bool()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.bool()
    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

def test_std():
    x = np.random.randn(2, 2, 3, 4)
    x2 = np.random.randn(2, 1, 3, 4)
    #x2 = np.array([[[[1-1j, -2j]], [[3+4j, 5]]]])

    torch_x = torch.tensor(x)
    torch_x2 = torch.tensor(x2)

    ms_x = pytorch.tensor(x)
    ms_x2 = pytorch.tensor(x2)

    torch_out1 = torch_x.std(-2, False)
    ms_out1 = ms_x.std(-2, False)
    torch_out2 = torch_x2.std((3, 1), True, True)
    ms_out2 = ms_x2.std((3, 1), True, True)
    torch_out3 = torch_x.std()
    ms_out3 = ms_x.std()

    assert np.allclose(ms_out1.numpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.numpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.numpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

def test_exp():
    x = np.random.randn(2, 2, 3, 4)

    torch_x = torch.tensor(x)
    torch_out = torch_x.exp()

    ms_x = pytorch.tensor(x)
    ms_out = ms_x.exp()

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_exp_():
    x = np.random.randn(2, 2, 3, 4)

    torch_x = torch.tensor(x)
    torch_x.exp_()

    ms_x = pytorch.tensor(x)
    ms_x.exp_()

    assert np.allclose(ms_x.numpy(), torch_x.numpy())
    assert ms_x.asnumpy().dtype == torch_x.numpy().dtype

@SKIP_ENV_ASCEND(reason="masked_fill do not support float64 input")
def test_masked_fill_float64():
    x = np.random.randn(2, 2, 3, 4)
    mask = np.random.randn(2, 2, 3, 4) * 2
    mask = mask.astype(np.int16).astype(np.bool8)

    torch_x = torch.tensor(x)
    torch_mask = torch.tensor(mask)
    torch_out = torch_x.masked_fill(torch_mask, 2)

    ms_x = pytorch.tensor(x)
    ms_mask = pytorch.tensor(mask)
    ms_out = ms_x.masked_fill(ms_mask, 2)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GPU(reason="test is cover by test_masked_fill_float64, no need to run")
@SKIP_ENV_CPU(reason="test is cover by test_masked_fill_float64, no need to run")
def test_masked_fill():
    x = np.random.randn(2, 2, 3, 4).astype(np.float32)
    mask = np.random.randn(2, 2, 3, 4) * 2
    mask = mask.astype(np.int16).astype(np.bool8)

    torch_x = torch.tensor(x)
    torch_mask = torch.tensor(mask)
    torch_out = torch_x.masked_fill(torch_mask, 2)

    ms_x = pytorch.tensor(x)
    ms_mask = pytorch.tensor(mask)
    ms_out = ms_x.masked_fill(ms_mask, 2)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_tolist():
    ms_tensor = pytorch.tensor([[1., 2, 3], [1, 2, 3]])
    ms_result = ms_tensor.tolist()

    torch_tensor = torch.tensor([[1., 2, 3], [1, 2, 3]])
    torch_result = torch_tensor.tolist()

    assert np.allclose(ms_result, torch_result)

    ms_tensor = ms_tensor[0, 0]
    ms_result = ms_tensor.tolist()

    torch_tensor = torch_tensor[0, 0]
    torch_result = torch_tensor.tolist()

    assert ms_result == torch_result

def test_chunk():
    x1 = np.arange(11)
    x2 = np.arange(12)
    x3 = np.arange(13)
    x4 = np.arange(24).reshape(2, 12)

    torch_x1 = torch.tensor(x1)
    torch_x2 = torch.tensor(x2)
    torch_x3 = torch.tensor(x3)
    torch_x4 = torch.tensor(x4)
    torch_out1 = torch_x1.chunk(6)
    torch_out2 = torch_x2.chunk(6)
    torch_out3 = torch_x3.chunk(6)
    torch_out4 = torch_x4.chunk(6, 1)
    torch_out = [torch_out1, torch_out2, torch_out3, torch_out4]
    ms_x1 = pytorch.tensor(x1)
    ms_x2 = pytorch.tensor(x2)
    ms_x3 = pytorch.tensor(x3)
    ms_x4 = pytorch.tensor(x4)
    ms_out1 = ms_x1.chunk(6)
    ms_out2 = ms_x2.chunk(6)
    ms_out3 = ms_x3.chunk(6)
    ms_out4 = ms_x4.chunk(6, 1)
    ms_out = [ms_out1, ms_out2, ms_out3, ms_out4]

    for i in range(4):
        assert len(ms_out[i]) == len(torch_out[i])
        for j in range(len(ms_out[i])):
            assert np.allclose(ms_out[i][j].numpy(), torch_out[i][j].numpy())
            assert np.allclose(ms_out[i][j].shape, torch_out[i][j].shape)

def test_cumsum():
    x = [-0.8286, -0.4890,  0.5155,  0.8443,  0.1865, -0.1752, -2.0595,
         0.1850, -1.1571, -0.4243]

    torch_x = torch.tensor(x)
    torch_out = torch_x.cumsum(0)

    ms_x = pytorch.tensor(x)
    ms_out = ms_x.cumsum(0)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_cumsum_():
    x = [-0.8286, -0.4890,  0.5155,  0.8443,  0.1865, -0.1752, -2.0595,
         0.1850, -1.1571, -0.4243]

    torch_x = torch.tensor(x)
    torch_x.cumsum_(0)

    ms_x = pytorch.tensor(x)
    ms_x.cumsum_(0)

    assert np.allclose(ms_x.numpy(), torch_x.numpy())
    assert ms_x.numpy().dtype == torch_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_absolute_():
    x = [-1, -2, 3]
    torch_x = torch.tensor(x)
    torch_out = torch_x.absolute_()

    ms_x = pytorch.tensor(x)
    ms_out = ms_x.absolute_()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_addcdiv():
    t = np.random.rand(1, 3).astype(np.float32)
    t1 = np.random.rand(3, 1).astype(np.float32)
    t2 = np.random.rand(1, 3).astype(np.float32)

    torch_t = torch.tensor(t)
    torch_t1 = torch.tensor(t1)
    torch_t2 = torch.tensor(t2)
    torch_out = torch_t.addcdiv(torch_t1, torch_t2, value=0.1)

    ms_t = pytorch.tensor(t)
    ms_t1 = pytorch.tensor(t1)
    ms_t2 = pytorch.tensor(t2)
    ms_out = ms_t.addcdiv(ms_t1, ms_t2, value=0.1)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_gather():
    input = [[1, 2], [3, 4]]
    index = [[0, 0], [1, 1]]

    torch_input = torch.tensor(input)
    torch_index = torch.tensor(index)
    torch_out = torch.gather(torch_input, 0, torch_index)

    ms_input = pytorch.tensor(input)
    ms_index = pytorch.tensor(index)
    ms_out = pytorch.gather(ms_input, 0, ms_index)
    assert np.allclose(torch_out.size(), ms_out.size())
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_fmod():
    x = [-3., -2, -1, 1, 2, 3]
    torch_x = torch.tensor(x)
    torch_out = torch_x.fmod(2)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.fmod(2)
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

    x = [1, 2, 3, 4, 5]
    divisor = [-1.5, 1.0, -1.0, -2.0, 2.5]
    torch_x = torch.tensor(x)
    tourch_divisor = torch.tensor(divisor)
    torch_out = torch_x.fmod(tourch_divisor)
    ms_x = pytorch.tensor(x)
    ms_divisor = pytorch.tensor(divisor)
    ms_out = ms_x.fmod(ms_divisor)
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_addcdiv_fp64():
    t = np.random.rand(1, 3)
    t1 = np.random.rand(3, 1)
    t2 = np.random.rand(1, 3)

    torch_t = torch.tensor(t)
    torch_t1 = torch.tensor(t1)
    torch_t2 = torch.tensor(t2)
    torch_out = torch_t.addcdiv(torch_t1, torch_t2, value=0.1)

    ms_t = pytorch.tensor(t)
    ms_t1 = pytorch.tensor(t1)
    ms_t2 = pytorch.tensor(t2)
    ms_out = ms_t.addcdiv(ms_t1, ms_t2, value=0.1)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_argmin():
    x = np.random.randn(4, 4)
    torch_x = torch.tensor(x)
    torch_out = torch_x.argmin(-1, False)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.argmin(-1, False)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    # TODO: assert ms_out.dtype == torch_out.dtype

    torch_out = torch_x.argmin(0, True)
    ms_out = ms_x.argmin(0, True)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

    torch_out = torch_x.argmin()
    ms_out = ms_x.argmin()
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_argmax():
    x = np.random.randn(1, 4, 4)
    torch_x = torch.tensor(x)
    torch_out = torch_x.argmax(-1, False)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.argmax(-1, False)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype

    torch_out = torch_x.argmin(0, True)
    ms_out = ms_x.argmin(0, True)
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

    torch_out = torch_x.argmin()
    ms_out = ms_x.argmin()
    assert np.allclose(ms_out.numpy(), torch_out.numpy())

def test_baddbmm():
    x = np.ones([1, 3, 3]).astype(np.float32)
    b1 = np.ones([1, 3, 4]).astype(np.float32)
    b2 = np.ones([1, 4, 3]).astype(np.float32)

    torch_input = torch.tensor(x, dtype=torch.float32)
    torch_batch1 = torch.tensor(b1, dtype=torch.float32)
    torch_batch2 = torch.tensor(b2, dtype=torch.float32)
    torch_out = torch_input.baddbmm(torch_batch1, torch_batch2)

    ms_torch_input = pytorch.tensor(x, dtype=pytorch.float32)
    ms_torch_batch1 = pytorch.tensor(b1, dtype=pytorch.float32)
    ms_torch_batch2 = pytorch.tensor(b2, dtype=pytorch.float32)
    ms_torch_out = ms_torch_input.baddbmm(ms_torch_batch1, ms_torch_batch2)
    param_compare(torch_out, ms_torch_out)

@SKIP_ENV_ASCEND(reason="baddbmm currently not support float64 on Ascend")
def test_baddbmm_fp64():
    x = np.random.randn(2, 2, 2)
    b1 = np.random.randn(2, 2, 2)
    b2 = np.random.randn(2, 2, 2)

    torch_input = torch.tensor(x)
    torch_batch1 = torch.tensor(b1)
    torch_batch2 = torch.tensor(b2)
    torch_out = torch_input.baddbmm(torch_batch1, torch_batch2)

    ms_torch_input = pytorch.tensor(x)
    ms_torch_batch1 = pytorch.tensor(b1)
    ms_torch_batch2 = pytorch.tensor(b2)
    ms_torch_out = ms_torch_input.baddbmm(ms_torch_batch1, ms_torch_batch2)
    param_compare(torch_out, ms_torch_out)

def test_topk():
    x = np.random.randn(10).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_v, torch_i = torch_x.topk(3)
    ms_x = pytorch.tensor(x)
    ms_v, ms_i = ms_x.topk(3)
    if is_test_under_ascend_context():
        assert np.allclose(torch_v.numpy(), ms_v.numpy(), atol=1e-3)
    else:
        assert np.allclose(torch_v.numpy(), ms_v.numpy())
    assert np.allclose(torch_i.numpy(), ms_i.numpy())

@SKIP_ENV_GRAPH_MODE(reason="graph-mode not support nametuple")
def test_topk_name_tuple():
    x = np.random.randn(10).astype(np.float32)
    torch_x = torch.tensor(x)
    pt_result = torch_x.topk(3)
    ms_x = pytorch.tensor(x)
    ms_result = ms_x.topk(3)
    if is_test_under_ascend_context():
        assert np.allclose(pt_result.values.numpy(), ms_result.values.numpy(), atol=1e-3)
    else:
        assert np.allclose(pt_result.values.numpy(), ms_result.values.numpy())
    assert np.allclose(pt_result.indices.numpy(), ms_result.indices.numpy())

def test_slice():
    x = np.ones([2, 3])
    torch_input = torch.tensor(x, dtype=torch.float32)
    ms_torch_input = pytorch.tensor(x, dtype=pytorch.float32)

    torch_input[0][0] = 2
    ms_torch_input[0][0] = 2
    assert np.allclose(torch_input.numpy(), ms_torch_input.numpy())

    mask = [True, False]
    torch_out = torch_input[mask]
    ms_torch_out = ms_torch_input[mask]
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy())

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.maximum not result wrong on Ascend.")
def test_maximum():
    a = [1, 2, -1]
    b = [3, 0, 4]
    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_out = torch_a.maximum(torch_b)
    ms_torch_a = pytorch.tensor(a)
    ms_torch_b = pytorch.tensor(b)
    ms_torch_out = ms_torch_a.maximum(ms_torch_b)
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy())

    a = [float('nan'), float('inf'), -float('inf'), 3.14]
    b = [-1, 0, 1, 5]

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_out = torch_a.maximum(torch_b)
    ms_torch_a = pytorch.tensor(a)
    ms_torch_b = pytorch.tensor(b)
    ms_torch_out = ms_torch_a.maximum(ms_torch_b)
    # NAN is diff
    # assert np.allclose(torch_out.numpy(), ms_torch_out.numpy(), equal_nan=True)

def test_max_int():
    np_array = np.array([[1, 2],[3, 4]]).astype(np.int64)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)

    torch_out1 = torch_tensor.max()
    torch_out2, torch_indices = torch_tensor.max(dim=1, keepdim=True)
    ms_out1 = ms_tensor.max()
    ms_out2, ms_indices = ms_tensor.max(dim=1, keepdim=True)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_indices, ms_indices)

def test_max2():
    np_array1 = np.random.randn(2, 3, 3).astype(np.float32)
    np_array2 = np.random.randn(2, 3, 3).astype(np.float32)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)

    torch_out = torch_tensor1.max(other=torch_tensor2)
    ms_out = ms_tensor1.max(other=ms_tensor2)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="max currently not support float64 on Ascend")
def test_max2_fp64():
    np_array1 = np.random.randn(2, 2)
    np_array2 = np.random.randn(2, 2)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)

    torch_out = torch_tensor1.max(torch_tensor2)
    ms_out = ms_tensor1.max(ms_tensor2)

    param_compare(torch_out, ms_out)

def test_min():
    np_array = np.random.randn(2, 3, 3).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)

    torch_out1 = torch_tensor.min()
    torch_out2, torch_indices2 = torch_tensor.min(dim=2, keepdim=True)
    ms_out1 = ms_tensor.min()
    ms_out2, ms_indices2 = ms_tensor.min(dim=2, keepdim=True)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_indices2, ms_indices2)

def test_min_int():
    np_array = np.random.randn(3, 3).astype(np.int64)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)

    torch_out, torch_indices = torch_tensor.min(dim=-1, keepdim=True)
    ms_out, ms_indices = ms_tensor.min(dim=-1, keepdim=True)

    param_compare(torch_out, ms_out)
    param_compare(torch_indices, ms_indices)

def test_min2():
    np_array1 = np.random.randn(2, 3, 3).astype(np.float32)
    np_array2 = np.random.randn(2, 3, 3).astype(np.float32)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)

    torch_out = torch_tensor1.min(other=torch_tensor2)
    ms_out = ms_tensor1.min(other=ms_tensor2)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="min currently not support float64 on Ascend")
def test_min2_fp64():
    np_array1 = np.random.randn(2, 3, 3)
    np_array2 = np.random.randn(2, 3, 3)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)

    torch_out = torch_tensor1.min(torch_tensor2)
    ms_out = ms_tensor1.min(ms_tensor2)

    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.minimum not result wrong on Ascend.")
def test_minimum():
    a = [1, 2, -1]
    b = [3, 0, 4]
    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_out = torch_a.minimum(torch_b)
    ms_torch_a = pytorch.tensor(a)
    ms_torch_b = pytorch.tensor(b)
    ms_torch_out = ms_torch_a.minimum(ms_torch_b)
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy())

    a = [float('nan'), float('inf'), -float('inf'), 3.14]
    b = [-1, 0, 1, 5]

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_out = torch_a.minimum(torch_b)
    ms_torch_a = pytorch.tensor(a)
    ms_torch_b = pytorch.tensor(b)
    ms_torch_out = ms_torch_a.minimum(ms_torch_b)
    # NAN is diff
    # assert np.allclose(torch_out.numpy(), ms_torch_out.numpy(), equal_nan=True)

def test_multiply():
    x = [0.2015, -0.4255,  2.6087]
    y = 100

    torch_x = torch.tensor(x)
    torch_out = torch_x.multiply(y)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.multiply(y)
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_neg():
    x = [0.0090, -0.2262, -0.0682, -0.2866, 0.3940]
    torch_x = torch.tensor(x)
    torch_out = torch_x.neg()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.neg()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_ravel():
    x = [[[1, 2],[3, 4]], [[5, 6], [7, 8]]]
    torch_x = torch.tensor(x)
    torch_out = torch_x.ravel()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.ravel()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_select():
    x = np.random.rand(1,2,3,4)
    torch_x = torch.tensor(x)
    torch_out = torch_x.select(dim=1, index=1)
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.select(dim=1, index=1)
    assert np.allclose(torch_out.shape, ms_out.shape)
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

def test_square():
    x = [-2.0755,  1.0226,  0.0831,  0.4806]
    torch_x = torch.tensor(x)
    torch_out = torch_x.square()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.square()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

    torch_x = torch.tensor(x, dtype=torch.float64)
    torch_out = torch_x.square()
    ms_x = pytorch.tensor(x, dtype=pytorch.float64)
    ms_out = ms_x.square()
    param_compare(torch_out, ms_out)


def test_broadcast_to():
    x = [1, 2, 3]
    torch_x = torch.tensor(x)
    torch_out1 = torch_x.broadcast_to((3,3))
    torch_out2 = torch_x.broadcast_to([3,3])
    ms_x = pytorch.tensor(x)
    ms_out1 = ms_x.broadcast_to((3,3))
    ms_out2 = ms_x.broadcast_to([3,3])
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

def test_divide():
    x = [ 0.3810,  1.2774, -0.2972, -0.3719,  0.4637]
    y = 0.5
    torch_x = torch.tensor(x).long()
    torch_out = torch_x.divide(y).double()
    ms_x = pytorch.tensor(x).long()
    ms_out = ms_x.divide(y).double()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

def test_div_scalar():
    ms_result = pytorch.tensor(3).div(4)
    torch_result = torch.tensor(3).div(4)
    param_compare(ms_result, torch_result)

def test_mm():
    x = np.random.rand(2, 3).astype(np.float32)
    y = np.random.rand(3, 4).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.mm(torch_y)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out = ms_x.mm(ms_y)
    param_compare(torch_out, ms_out)

@SKIP_ENV_ASCEND(reason="mm currently not support float64 on Ascend")
def test_mm_fp64():
    x = np.random.rand(2, 3)
    y = np.random.rand(3, 4)
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.mm(torch_y)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out = ms_x.mm(ms_y)
    param_compare(torch_out, ms_out)

def test_view():
    torch_x = torch.Tensor(2,3)
    torch_out = torch_x.view((3,2))
    ms_torch_x = pytorch.Tensor(2,3)
    ms_torch_out = ms_torch_x.view((3,2))
    assert np.allclose(torch_out.size(), ms_torch_out.size())

    torch_out = torch_x.new().view((-1,2,3))
    ms_torch_out = ms_torch_x.new().view((-1,2,3))
    assert np.allclose(torch_out.size(), ms_torch_out.size())

def test_view_dtype():
    torch_x = torch.Tensor(2,3)
    torch_out = torch_x.view(dtype=torch.float32)
    ms_torch_x = pytorch.Tensor(2,3)
    ms_torch_out = ms_torch_x.view(dtype=pytorch.float32)
    type_shape_compare(torch_out, ms_torch_out)

def test_view_as():
    torch_x = torch.Tensor(2, 3)
    other = torch.Tensor(3, 2)
    torch_out = torch_x.view_as(other)
    ms_torch_x = pytorch.Tensor(2, 3)
    other = torch.Tensor(3, 2)
    ms_torch_out = ms_torch_x.view_as(other)
    assert np.allclose(torch_out.size(), ms_torch_out.size())

def test_logsumexp():
    x = np.random.randn(3, 4, 5).astype(np.float32)
    torch_x = torch.tensor(x)
    torch_out = torch_x.logsumexp(dim=1, keepdim=False)
    ms_torch_x = pytorch.tensor(x)
    ms_torch_out = ms_torch_x.logsumexp(dim=1, keepdim=False)
    assert np.allclose(torch_out.size(), ms_torch_out.size())
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy(), rtol=1e-04)

    x = np.random.randn(2, 3, 2).astype(np.int32)
    torch_x = torch.tensor(x)
    torch_out = torch_x.logsumexp(dim=2, keepdim=True)
    ms_torch_x = pytorch.tensor(x)
    ms_torch_out = ms_torch_x.logsumexp(dim=2, keepdim=True)
    assert np.allclose(torch_out.size(), ms_torch_out.size())
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy(), rtol=1e-04)

def test_addmv():
    M = np.random.randn(2).astype(np.float32)
    mat = np.random.randn(2, 3).astype(np.float32)
    vec = np.random.randn(3).astype(np.float32)

    torch_M = torch.tensor(M)
    torch_mat = torch.tensor(mat)
    torch_vec = torch.tensor(vec)
    torch_out = torch_M.addmv(torch_mat, torch_vec, beta=False, alpha=0.5)

    ms_torch_M = pytorch.tensor(M)
    ms_torch_mat = pytorch.tensor(mat)
    ms_torch_vec = pytorch.tensor(vec)
    ms_torch_out = ms_torch_M.addmv(ms_torch_mat, ms_torch_vec, beta=False, alpha=0.5)
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_addmv_():
    M = np.random.randn(2).astype(np.float32)
    mat = np.random.randn(2, 3).astype(np.float32)
    vec = np.random.randn(3).astype(np.float32)

    torch_M = torch.tensor(M)
    torch_mat = torch.tensor(mat)
    torch_vec = torch.tensor(vec)
    torch_M.addmv(torch_mat, torch_vec, beta=False, alpha=0.5)

    ms_torch_M = pytorch.tensor(M)
    ms_torch_mat = pytorch.tensor(mat)
    ms_torch_vec = pytorch.tensor(vec)
    ms_torch_M.addmv(ms_torch_mat, ms_torch_vec, beta=False, alpha=0.5)
    assert np.allclose(torch_M.numpy(), ms_torch_M.numpy())

def test_dot():
    x = [2, 3]
    y = [2, 1]
    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out = torch_x.dot(torch_y)
    ms_torch_x = pytorch.tensor(x)
    ms_torch_y = pytorch.tensor(y)
    ms_torch_out = ms_torch_x.dot(ms_torch_y)
    assert np.allclose(torch_out.numpy(), ms_torch_out.numpy())

def test_inverse():
    A1 = np.random.randn(4, 4).astype(np.float64)
    torch_A1 = torch.tensor(A1)
    torch_out1 = torch_A1.inverse()
    ms_torch_A1 = pytorch.tensor(A1)
    ms_torch_out1 = ms_torch_A1.inverse()
    assert np.allclose(torch_out1.numpy(), ms_torch_out1.numpy())

    A2 = np.random.randn(2, 3, 4, 4).astype(np.float32)
    torch_A2 = torch.tensor(A2)
    torch_out2 = torch_A2.inverse()
    ms_torch_A2 = pytorch.tensor(A2)
    ms_torch_out2 = ms_torch_A2.inverse()
    assert np.allclose(torch_out2.numpy(), ms_torch_out2.numpy(), rtol=1e-3, atol=1e-06)

def test_count_nonzero():
    x = [[0, 1, 2, 0, 9],[0, 1, 0, 0, 0]]
    torch_x = torch.tensor(x)
    torch_out = torch_x.count_nonzero()
    ms_x = pytorch.tensor(x)
    ms_out = ms_x.count_nonzero()
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

    torch_out = torch_x.count_nonzero(0)
    ms_out = ms_x.count_nonzero(0)
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="scatter not support reduce='add' on Ascend")
def test_scatter_1():
    ms_out = pytorch.full((2, 4), 2.).scatter_(1, pytorch.tensor([[2], [3]]),
            1.23, reduce='add')

    torch_out = torch.full((2, 4), 2.).scatter_(1, torch.tensor([[2], [3]]),
           1.23, reduce='add')

    assert np.allclose(ms_out.numpy(), torch_out.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_scatter_2():
    ms_out = pytorch.full((2, 4), 2.).scatter_(1, pytorch.tensor([[2], [3]]),
            1.23)

    torch_out = torch.full((2, 4), 2.).scatter_(1, torch.tensor([[2], [3]]),
           1.23)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())

# TODO: To support index.shape != src.shape
'''
@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_scatter_3():
    src = torch.arange(1, 11).reshape((2, 5))
    index = torch.tensor([[0, 1, 2, 0]])
    torch_out = torch.zeros(3, 5, dtype=src.dtype).scatter_(0, index, src)

    src = pytorch.arange(1, 11).reshape((2, 5))
    index = pytorch.tensor([[0, 1, 2, 0]])
    ms_out = pytorch.zeros(3, 5, dtype=src.dtype).scatter_(0, index, src)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_scatter_4():
    src = torch.arange(1, 11).reshape((2, 5))
    index = torch.tensor([[0, 1, 2], [0, 1, 4]])
    torch_out = torch.zeros(3, 5, dtype=src.dtype).scatter_(1, index, src)

    src = pytorch.arange(1, 11).reshape((2, 5))
    index = pytorch.tensor([[0, 1, 2], [0, 1, 4]])
    ms_out = pytorch.zeros(3, 5, dtype=src.dtype).scatter_(1, index, src)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
'''

def test_new_ones():
    tensor = torch.tensor((), dtype=torch.int32)
    torch_out = tensor.new_ones((2, 3))

    tensor = pytorch.tensor((), dtype=pytorch.int32)
    ms_out = tensor.new_ones((2, 3))

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_new_empty():
    tensor = torch.ones(())
    torch_out = tensor.new_empty((2, 3))

    tensor = pytorch.ones(())
    ms_out = tensor.new_empty((2, 3))

    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_addcmul():
    np_array = np.array([1, 1, 1]).astype(np.float32)
    np_x = np.array([[1], [2], [3]]).astype(np.float32)
    np_y = np.array([[1, 2, 3]]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_x = torch.tensor(np_x)
    torch_y = torch.tensor(np_y)
    torch_out = torch_tensor.addcmul(torch_x, torch_y, value=2.1)

    ms_tensor = pytorch.tensor(np_array)
    ms_x = pytorch.tensor(np_x)
    ms_y = pytorch.tensor(np_y)
    ms_out = ms_tensor.addcmul(ms_x, ms_y, value=2.1)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_addcmul_():
    np_array = np.array([1, 1, 1]).astype(np.float32)
    np_x = np.array([1, 2, 3]).astype(np.float32)
    np_y = np.array([1, 2, 3]).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_x = torch.tensor(np_x)
    torch_y = torch.tensor(np_y)
    torch_out = torch_tensor.addcmul_(torch_x, torch_y, value=2.1)

    ms_tensor = pytorch.tensor(np_array)
    ms_x = pytorch.tensor(np_x)
    ms_y = pytorch.tensor(np_y)
    ms_out = ms_tensor.addcmul_(ms_x, ms_y, value=2.1)

    assert np.allclose(ms_tensor.numpy(), torch_tensor.numpy())
    assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
    assert torch_tensor.numpy().shape == ms_tensor.numpy().shape

def test_bitwise_not():
    np_array1 = np.arange(-5, 12).astype(np.uint8)
    np_array2 = np.arange(-10, 10).astype(np.int16)
    np_array3 = np.array([[[False, True, True, False, False]]])

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor3 = torch.tensor(np_array3)
    torch_out1 = torch_tensor1.bitwise_not()
    torch_out2 = torch_tensor2.bitwise_not()
    torch_out3 = torch_tensor3.bitwise_not()

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_tensor3 = pytorch.tensor(np_array3)
    ms_out1 = ms_tensor1.bitwise_not()
    ms_out2 = ms_tensor2.bitwise_not()
    ms_out3 = ms_tensor3.bitwise_not()

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype


def test_bitwise():
    np_array1 = np.arange(-5, 11).reshape(1, 2, 2, 4).astype(np.bool8)
    np_array2 = np.arange(-10, 6).reshape(2, 2, 4).astype(np.bool8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch_tensor1.bitwise_and(torch_tensor2)
    torch_out2 = torch_tensor1.bitwise_or(torch_tensor2)
    torch_out3 = torch_tensor1.bitwise_xor(torch_tensor2)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_out1 = ms_tensor1.bitwise_and(ms_tensor2)
    ms_out2 = ms_tensor1.bitwise_or(ms_tensor2)
    ms_out3 = ms_tensor1.bitwise_xor(ms_tensor2)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_bitwise_():
    np_array1 = np.arange(-5, 11).reshape(1, 2, 2, 4).astype(np.bool_)
    np_array2 = np.arange(-10, 6).reshape(2, 2, 4).astype(np.bool_)

    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor2 = pytorch.tensor(np_array2)

    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor1 = pytorch.tensor(np_array1)
    torch_tensor1.bitwise_and_(torch_tensor2)
    ms_tensor1.bitwise_and_(ms_tensor2)
    assert np.allclose(ms_tensor1.numpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor1 = pytorch.tensor(np_array1)
    torch_tensor1.bitwise_or_(torch_tensor2)
    ms_tensor1.bitwise_or_(ms_tensor2)
    assert np.allclose(ms_tensor1.numpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor1 = pytorch.tensor(np_array1)
    torch_tensor1.bitwise_xor_(torch_tensor2)
    ms_tensor1.bitwise_xor_(ms_tensor2)
    assert np.allclose(ms_tensor1.numpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

def test_addbmm():
    M_ = np.random.randn(3, 5).astype(np.float32)
    batch1_ = np.random.randn(10, 3, 4).astype(np.float32)
    batch2_ = np.random.randn(10, 4, 5).astype(np.float32)

    M = torch.tensor(M_)
    batch1 = torch.tensor(batch1_)
    batch2 = torch.tensor(batch2_)
    torch_output = M.addbmm(batch1, batch2, alpha=2, beta=3)

    M = pytorch.tensor(M_)
    batch1 = pytorch.tensor(batch1_)
    batch2 = pytorch.tensor(batch2_)
    ms_output = M.addbmm(batch1, batch2, alpha=2, beta=3)

    param_compare(torch_output, ms_output, atol=1e-4)

@SKIP_ENV_ASCEND(reason="addbmm currently not support float64 on Ascend")
def test_addbmm_fp64():
    M_ = np.random.randn(2, 3)
    batch1_ = np.random.randn(3, 2, 4)
    batch2_ = np.random.randn(3, 4, 3)

    M = torch.tensor(M_)
    batch1 = torch.tensor(batch1_)
    batch2 = torch.tensor(batch2_)
    torch_output = M.addbmm(batch1, batch2, alpha=2, beta=3)

    M = pytorch.tensor(M_)
    batch1 = pytorch.tensor(batch1_)
    batch2 = pytorch.tensor(batch2_)
    ms_output = M.addbmm(batch1, batch2, alpha=2, beta=3)

    param_compare(torch_output, ms_output)

def test_addr():
    vec1 = np.arange(1., 4.)
    vec2 = np.arange(1., 3.)
    vec1_pt = torch.tensor(vec1)
    vec2_pt = torch.tensor(vec2)
    M = torch.zeros(3, 2)
    torch_output = M.addr(vec1_pt, vec2_pt, alpha=2, beta=3)

    vec1_ms = pytorch.tensor(vec1)
    vec2_ms = pytorch.tensor(vec2)
    M = pytorch.zeros(3, 2)
    ms_output = M.addr(vec1_ms, vec2_ms, alpha=2, beta=3)

    assert np.allclose(ms_output.numpy(), torch_output.numpy())

@SKIP_ENV_CPU(reason="[CI] ms2.4.0 0920 still not pass, Unsupported op [ReduceAll] on CPU under this dtype.")
def test_all():
    a_ms = pytorch.rand(1, 2).bool()
    a1 = a_ms.all()
    b_ms = pytorch.arange(0, 3)
    b1 = b_ms.all()

    a_np = a_ms.asnumpy()
    b_np = b_ms.asnumpy()
    a_pt = torch.tensor(a_np).bool()
    a2 = a_pt.all()
    b_pt = torch.tensor(b_np)
    b2 = b_pt.all()

    assert np.allclose(a1.numpy(), a2.numpy())
    assert np.allclose(b1.numpy(), b2.numpy())

@SKIP_ENV_ASCEND(reason="allclose not support equal_nan==False on Ascend")
def test_allclose():
    a1 = pytorch.tensor([10000., 1e-07]).allclose(pytorch.tensor([10000.1, 1e-08]))
    b1 = pytorch.tensor([10000., 1e-08]).allclose(pytorch.tensor([10000.1, 1e-09]))
    c1 = pytorch.tensor([1.0, float('nan')]).allclose(pytorch.tensor([1.0, float('nan')]))

    a2 = torch.tensor([10000., 1e-07]).allclose(torch.tensor([10000.1, 1e-08]))
    b2 = torch.tensor([10000., 1e-08]).allclose(torch.tensor([10000.1, 1e-09]))
    c2 = torch.tensor([1.0, float('nan')]).allclose(torch.tensor([1.0, float('nan')]))

    assert a1 == a2
    assert b1 == b2
    assert c1 == c2

def test_allclose_equal_nan_true():
    d1 = pytorch.tensor([1.0, float('nan')]).allclose(pytorch.tensor([1.0, float('nan')]), equal_nan=True)
    d2 = torch.tensor([1.0, float('nan')]).allclose(torch.tensor([1.0, float('nan')]), equal_nan=True)
    assert d1 == d2

@SKIP_ENV_ASCEND(reason="isclose not support equal_nan==False on Ascend")
def test_isclose():
    a1 = pytorch.tensor((1., 2, 3)).isclose(pytorch.tensor((1 + 1e-10, 3, 4)))
    b1 = pytorch.tensor((float('inf'), 4)).isclose(pytorch.tensor((float('inf'), 6)), rtol=.5)

    a2 = torch.tensor((1., 2, 3)).isclose(torch.tensor((1 + 1e-10, 3, 4)))
    b2 = torch.tensor((float('inf'), 4)).isclose(torch.tensor((float('inf'), 6)), rtol=.5)

    assert np.allclose(a1.numpy(), a2.numpy())
    assert np.allclose(b1.numpy(), b2.numpy())

def test_isclose_equal_nan():
    a1 = pytorch.tensor((1., 2, 3)).isclose(pytorch.tensor((1 + 1e-10, 3, 4)), equal_nan=True)
    a2 = torch.tensor((1., 2, 3)).isclose(torch.tensor((1 + 1e-10, 3, 4)), equal_nan=True)
    assert np.allclose(a1.numpy(), a2.numpy())

def test_addmm():
    _M = np.random.randn(2, 3).astype(np.float32)
    _mat1 = np.random.randn(2, 3).astype(np.float32)
    _mat2 = np.random.randn(3, 3).astype(np.float32)

    M = pytorch.tensor(_M)
    mat1 = pytorch.tensor(_mat1)
    mat2 = pytorch.tensor(_mat2)
    a1 = M.addmm(mat1, mat2, alpha=2, beta=3)

    M = torch.tensor(_M)
    mat1 = torch.tensor(_mat1)
    mat2 = torch.tensor(_mat2)
    a2 = M.addmm(mat1, mat2, alpha=2, beta=3)

    assert np.allclose(a1.numpy(), a2.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_addmm_():
    _M = np.random.randn(2, 3).astype(np.float32)
    _mat1 = np.random.randn(2, 3).astype(np.float32)
    _mat2 = np.random.randn(3, 3).astype(np.float32)

    M_ms = pytorch.tensor(_M)
    mat1 = pytorch.tensor(_mat1)
    mat2 = pytorch.tensor(_mat2)
    M_ms.addmm_(mat1, mat2, alpha=2, beta=3)

    M_torch = torch.tensor(_M)
    mat1 = torch.tensor(_mat1)
    mat2 = torch.tensor(_mat2)
    M_torch.addmm_(mat1, mat2, alpha=2, beta=3)
    param_compare(M_ms, M_torch)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="addmm_ currently not support float64 on Ascend")
def test_addmm_fp64():
    _M = np.random.randn(2, 3)
    _mat1 = np.random.randn(2, 3)
    _mat2 = np.random.randn(3, 3)

    M_ms = pytorch.tensor(_M)
    mat1 = pytorch.tensor(_mat1)
    mat2 = pytorch.tensor(_mat2)
    M_ms.addmm_(mat1, mat2, alpha=2.5, beta=3.5)

    M_torch = torch.tensor(_M)
    mat1 = torch.tensor(_mat1)
    mat2 = torch.tensor(_mat2)
    M_torch.addmm_(mat1, mat2, alpha=2.5, beta=3.5)

    param_compare(M_ms, M_torch)

def test_cholesky():
    _data1 = np.random.randn(3, 3).astype(np.float32)
    _data2 = np.random.randn(3, 2, 2).astype(np.float32)

    a = torch.tensor(_data1)
    a = a @ a.mT + 1e-3
    torch_out1 = a.cholesky()

    a = torch.tensor(_data2)
    a = a @ a.mT + 1e-03
    torch_out2 = a.cholesky()

    a = pytorch.tensor(_data1)
    a = a @ a.mT + 1e-3
    ms_out1 = a.cholesky()

    a = pytorch.tensor(_data2)
    a = a @ a.mT + 1e-03
    ms_out2 = a.cholesky()

    param_compare(torch_out1, ms_out1, atol=1e-5)
    param_compare(torch_out2, ms_out2, atol=1e-5)


@SKIP_ENV_ASCEND(reason="cholesky currently not support float64 on Ascend")
def test_cholesky_fp64():
    _data1 = np.random.randn(2, 2)

    a = torch.tensor(_data1)
    a = a @ a.mT + 1e-3
    torch_out1 = a.cholesky()

    a = pytorch.tensor(_data1)
    a = a @ a.mT + 1e-3
    ms_out1 = a.cholesky()
    param_compare(torch_out1, ms_out1)


def test_aminmax():
    t = torch.arange(0, 10).view(2, 5)
    c1, d1 = t.aminmax(dim=0, keepdim=True)
    t = pytorch.arange(0, 10).view(2, 5)
    c2, d2 = t.aminmax(dim=0, keepdim=True)
    assert np.allclose(c1.numpy(), c2.numpy())
    assert np.allclose(d1.numpy(), d2.numpy())

def test_any():
    data1 = np.random.randn(1, 2)
    data2 = np.random.randn(4, 2)

    a = pytorch.tensor(data1).bool()
    a1 = a.any()
    a = pytorch.arange(0, 3)
    b1 = a.any()
    a = pytorch.tensor(data2) < 0
    c1 = a.any(1)
    d1 = a.any(0)

    a = torch.tensor(data1).bool()
    a2 = a.any()
    a = torch.arange(0, 3)
    b2 = a.any()
    a = torch.tensor(data2) < 0
    c2 = a.any(1)
    d2 = a.any(0)

    assert np.allclose(a1.numpy(), a2.numpy())
    assert np.allclose(b1.numpy(), b2.numpy())
    assert np.allclose(c1.numpy(), c2.numpy())
    assert np.allclose(d1.numpy(), d2.numpy())


def test_bincount1():
    np_array = np.random.randint(0, 8, (7,)).astype(np.uint8)
    weight_array = np.linspace(0, 2, len(np_array))

    torch_tensor = torch.tensor(np_array)
    torch_weight = torch.tensor(weight_array)
    torch_out = torch_tensor.bincount(torch_weight)

    ms_tensor = pytorch.tensor(np_array)
    ms_weight = pytorch.tensor(weight_array)
    ms_out = ms_tensor.bincount(ms_weight)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_bincount2():
    np_array = np.random.randint(0, 4, (8,)).astype(np.int64)

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.bincount(minlength=5)

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.bincount(minlength=5)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_bitwise_shift():
    np_array1 = np.arange(-5, 11).reshape(2, 2, 4).astype(np.int8)
    np_array2 = np.array([1,2,7,1,2,5,1,2,-1,-3,-4,0,2,1,0,0]).reshape(2, 2, 4).astype(np.int8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch_tensor1.bitwise_left_shift(torch_tensor2)
    torch_out2 = torch_tensor1.bitwise_right_shift(3)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_out1 = ms_tensor1.bitwise_left_shift(ms_tensor2)
    ms_out2 = ms_tensor1.bitwise_right_shift(3)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_bitwise_shift_():
    np_array1 = np.arange(-5, 11).reshape(2, 2, 4).astype(np.int8)
    np_array2 = np.array([1,2,7,1,2,5,1,2,-1,-3,-4,0,2,1,0,0]).reshape(2, 2, 4).astype(np.int8)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor1.bitwise_left_shift_(torch_tensor2)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_tensor1.bitwise_left_shift_(ms_tensor2)

    assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor1.bitwise_right_shift_(3)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor1.bitwise_right_shift_(3)

    assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

@SKIP_ENV_GPU(reason="Unsupport on GPU.")
def test_cholesky_inverse():
    _data = np.random.randn(3, 3).astype(np.float32)
    print("_data:", _data)

    a = torch.tensor(_data)
    a = torch.mm(a, a.t()) + 1e-05 * torch.eye(3)
    u = torch.cholesky(a)
    torch_out = u.cholesky_inverse()

    a = pytorch.tensor(_data)
    a = pytorch.mm(a, a.t()) + 1e-05 * pytorch.eye(3)
    u = pytorch.cholesky(a)
    ms_out = u.cholesky_inverse()

    param_compare(torch_out, ms_out, rtol=2e-3, atol=1e-4)

@SKIP_ENV_GPU(reason="Unsupport on GPU.")
@SKIP_ENV_ASCEND(reason="cholesky_inverse currently not support float64 on Ascend")
def test_cholesky_inverse_fp64():
    _data = np.random.randn(2, 2)

    a = torch.tensor(_data)
    a = torch.mm(a, a.t()) + 1e-05 * torch.eye(2)
    u = torch.cholesky(a)
    torch_out = u.cholesky_inverse()

    a = pytorch.tensor(_data)
    a = pytorch.mm(a, a.t()) + 1e-05 * pytorch.eye(2)
    u = pytorch.cholesky(a)
    ms_out = u.cholesky_inverse()

    param_compare(torch_out, ms_out, rtol=1e-3, atol=1e-4)

def test_cholesky_solve():
    data1 = np.random.randn(2, 3, 2).astype(np.float32)
    data2 = np.random.randn(2, 3, 3).astype(np.float32)

    a_t = torch.tensor(data1)
    b_t = torch.tensor(data2)
    torch_out1 = a_t.cholesky_solve(b_t)
    torch_out2 = a_t.cholesky_solve(b_t, True)

    a_ms = pytorch.tensor(data1)
    b_ms = pytorch.tensor(data2)
    ms_out1 = a_ms.cholesky_solve(b_ms)
    ms_out2 = a_ms.cholesky_solve(b_ms, True)
    param_compare(torch_out1, ms_out1, atol=1e-4)
    param_compare(torch_out2, ms_out2, atol=1e-4)

def test_clip():
    np_array = np.random.rand(1, 2, 3, 4).astype(np.float32)
    min = 0.35
    max = 0.65
    torch_tensor = torch.tensor(np_array)
    torch_out1 = torch_tensor.clip(torch.tensor(min), torch.tensor(max))
    torch_out2 = torch_tensor.clip(0.85, max)
    torch_out3 = torch_tensor.clip(None, max)

    ms_tensor = pytorch.tensor(np_array)
    ms_out1 = ms_tensor.clip(pytorch.tensor(min), pytorch.tensor(max))
    ms_out2 = ms_tensor.clip(0.85, max)
    ms_out3 = ms_tensor.clip(None, max)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_clip_():
    np_array = np.random.rand(1, 2, 3, 4).astype(np.float32)
    min = 0.35
    max = 0.65
    torch_tensor = torch.tensor(np_array)
    torch_tensor.clip_(torch.tensor(min), torch.tensor(max))

    ms_tensor = pytorch.tensor(np_array)
    ms_tensor.clip_(pytorch.tensor(min), pytorch.tensor(max))

    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype

def test_copysign():
    np_other = np.array([[0.0, -0.0, 1, 1.5, -0.5, -20]]).astype(np.half)
    np_array = np.array([0, -0, 0, 1, 1, 1]).astype(np.int32)

    for type_input in (np.int32, np.half, np.float32):
        torch_tensor = torch.tensor(np_array.astype(type_input))
        ms_tensor = pytorch.tensor(np_array.astype(type_input))
        for type_other in (np.half, np.int8, np.int32):
            torch_other = torch.tensor(np_other.astype(type_other))
            torch_out1 = torch_tensor.copysign(torch_other)
            ms_other = pytorch.tensor(np_other.astype(type_other))
            ms_out1 = ms_tensor.copysign(ms_other)
            param_compare(torch_out1, ms_out1)
        torch_out2 = torch_tensor.copysign(-0)
        ms_out2 = ms_tensor.copysign(-0)
        param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason='currently not support float64 on Ascend')
def test_copysign_fp64():
    np_other = np.random.randn(1, 6, 6).astype(np.float64)
    np_array = np.random.randn(6).astype(np.float64)

    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)
    torch_other = torch.tensor(np_other)
    torch_out1 = torch_tensor.copysign(torch_other)
    ms_other = pytorch.tensor(np_other)
    ms_out1 = ms_tensor.copysign(ms_other)
    torch_out2 = torch_tensor.copysign(-0)
    ms_out2 = ms_tensor.copysign(-0)
    torch_out3 = torch_tensor.copysign(1)
    ms_out3 = ms_tensor.copysign(1)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

def test_copysign_shape():
    np_other1 = np.random.randn(2, 6, 6).astype(np.float32)
    np_array1 = np.random.randn(6).astype(np.float32)
    np_other2 = np.random.randn(2, 3, 4).astype(np.float32)
    np_array2 = np.random.randn(3, 4).astype(np.float32)
    np_other3 = np.random.randn(3).astype(np.float32)
    np_array3 = np.random.randn(1, 3, 3).astype(np.float32)
    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor1 = pytorch.tensor(np_array1)
    torch_other1 = torch.tensor(np_other1)
    ms_other1 = pytorch.tensor(np_other1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor2 = pytorch.tensor(np_array2)
    torch_other2 = torch.tensor(np_other2)
    ms_other2 = pytorch.tensor(np_other2)
    torch_tensor3 = torch.tensor(np_array3)
    ms_tensor3 = pytorch.tensor(np_array3)
    torch_other3 = torch.tensor(np_other3)
    ms_other3 = pytorch.tensor(np_other3)
    torch_out1 = torch_tensor1.copysign(torch_other1)
    torch_out2 = torch_tensor2.copysign(torch_other2)
    torch_out3 = torch_tensor3.copysign(torch_other3)
    ms_out1 = ms_tensor1.copysign(ms_other1)
    ms_out2 = ms_tensor2.copysign(ms_other2)
    ms_out3 = ms_tensor3.copysign(ms_other3)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

def test_cos():
    x = torch.tensor([0.24, 0.83, 0.31, 0.09], dtype=torch.float32)
    t_r = x.cos()

    y = pytorch.tensor([0.24, 0.83, 0.31, 0.09], pytorch.float32)
    ms_r = y.cos()

    assert np.allclose(t_r.numpy(), ms_r.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_cos_():
    x = torch.tensor([0.24, 0.83, 0.31, 0.09], dtype=torch.float32)
    x.cos_()

    y = pytorch.tensor([0.24, 0.83, 0.31, 0.09], pytorch.float32)
    y.cos_()

    assert np.allclose(x.numpy(), y.numpy())

def test_cosh():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64) - 0.5
    np_array = np_array * 20
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.cosh()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.cosh()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_cosh_():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float64) - 0.5
    np_array = np_array * 20
    torch_tensor = torch.tensor(np_array)
    torch_tensor.cosh_()

    ms_tensor = pytorch.tensor(np_array)
    ms_tensor.cosh_()

    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype
    assert ms_tensor.asnumpy().shape == torch_tensor.numpy().shape

@SKIP_ENV_ASCEND(reason="not support cummax on Ascend")
def test_cummax():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = pytorch.tensor(np_1)
    ms_result_1, ms_result_2 = ms_tensor.cummax(dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result_1, torch_result_2 = torch_tensor.cummax(dim=0)
    assert np.allclose(ms_result_1.asnumpy(), torch_result_1.numpy())
    assert ms_result_1.asnumpy().dtype == torch_result_1.numpy().dtype
    assert np.allclose(ms_result_2.asnumpy(), torch_result_2.numpy())
    assert ms_result_2.asnumpy().dtype == torch_result_2.numpy().dtype

def test_cummin():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = pytorch.tensor(np_1)
    ms_result_1, ms_result_2 = ms_tensor.cummin(dim=0)
    torch_tensor = torch.tensor(np_1)
    torch_result_1, torch_result_2 = torch_tensor.cummin(dim=0)
    assert np.allclose(ms_result_1.asnumpy(), torch_result_1.numpy())
    assert ms_result_1.asnumpy().dtype == torch_result_1.numpy().dtype
    assert np.allclose(ms_result_2.asnumpy(), torch_result_2.numpy())
    assert ms_result_2.asnumpy().dtype == torch_result_2.numpy().dtype

def test_cumprod():
    np_1 = np.random.randn(3, 4).astype(np.float32)
    ms_tensor = pytorch.tensor(np_1)
    ms_result = ms_tensor.cumprod(dim=0)
    torch_tensor = pytorch.tensor(np_1)
    torch_result = torch_tensor.cumprod(dim=0)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_cumprod_():
    np_1 = np.random.randn(3, 4).astype(np.float64)
    ms_tensor = pytorch.tensor(np_1)
    ms_tensor.cumprod_(dim=0)
    torch_tensor = pytorch.tensor(np_1)
    torch_tensor.cumprod_(dim=0)
    assert np.allclose(ms_tensor.numpy(), torch_tensor.numpy())
    assert ms_tensor.numpy().dtype == torch_tensor.numpy().dtype

def test_deg2rad():
    np_array = np.array([[180, -180, 360, 30, 0, 57, 80]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.deg2rad()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.deg2rad()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_ASCEND(reason="diag: ms.numpy.diag has bug on Ascend")
def test_diag():
    np_1 = np.array([1, 2, 3])

    ms_tensor_1 = pytorch.tensor(np_1)
    ms_result = ms_tensor_1.diag()

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch_tensor_1.diag()

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_diagonal():
    np_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    ms_tensor_1 = pytorch.tensor(np_1)
    ms_result = ms_tensor_1.diagonal(0)

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch_tensor_1.diagonal(0)

    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_diagflat():
    np_1 = np.random.randn(8).astype(np.float32)
    ms_tensor = pytorch.tensor(np_1)
    ms_result = ms_tensor.diagflat(offset=-1)
    torch_tensor = torch.tensor(np_1)
    torch_result = torch_tensor.diagflat(offset=-1)
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_iscomplex():
    a = pytorch.tensor([1+1j, 2, 3])
    assert a.is_complex() == True
    a = pytorch.tensor([1, 2, 3])
    assert a.is_complex() == False

def test_isinf():
    data = [1, float('inf'), 2, float('-inf'), float('nan')]
    a = torch.tensor(data).isinf()
    b = pytorch.tensor(data).isinf()
    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_isneginf():
    data = [-float('inf'), float('inf'), 1.2]
    a = torch.tensor(data).isneginf()
    b = pytorch.tensor(data).isneginf()
    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_isposinf():
    data = [-float('inf'), float('inf'), 1.2]
    a = torch.tensor(data).isposinf()
    b = pytorch.tensor(data).isposinf()
    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_isreal():
    data = [1, 1+1j, 2+0j]
    a = torch.tensor(data).isreal()
    b = pytorch.tensor(data).isreal()
    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_diff():
    np_1 = np.random.randn(7, 8).astype(np.float32)
    np_2 = np.random.randn(7, 8).astype(np.float32)
    ms_tensor_1 = pytorch.tensor(np_1)
    ms_tensor_2 = pytorch.tensor(np_2)
    ms_result = ms_tensor_1.diff(n=3, dim=-1, append=ms_tensor_2)

    torch_tensor_1 = pytorch.tensor(np_1)
    torch_tensor_2 = pytorch.tensor(np_2)
    torch_result = torch_tensor_1.diff(n=3, dim=-1, append=torch_tensor_2)
    param_compare(ms_result, torch_result, atol=1e-6)


def test_digamma():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    np_array = np_array * 20
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.digamma()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.digamma()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), atol=1e-5)
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_digamma_():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    np_array = np_array * 20
    torch_tensor = torch.tensor(np_array)
    torch_tensor.digamma_()

    ms_tensor = pytorch.tensor(np_array)
    ms_tensor.digamma_()

    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy(), atol=1e-5)
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype
    assert ms_tensor.asnumpy().shape == torch_tensor.numpy().shape

def test_dist():
    _data1 = np.random.randn(4).astype(np.float16)
    _data2 = np.random.randn(4).astype(np.float32)

    x = torch.tensor(_data1)
    y = torch.tensor(_data2)

    # TODO: Not support float p yet
    #a1 = torch.dist(x, y, 3.5)
    b1 = x.dist(y, 3)
    c1 = x.dist(y, 0)
    d1 = x.dist(y, 1)

    x = pytorch.tensor(_data1)
    y = pytorch.tensor(_data2)
    #a2 = ms_torch.dist(x, y, 3.5)
    b2 = x.dist(y, 3)
    c2 = x.dist(y, 0)
    d2 = x.dist(y, 1)

    #assert np.allclose(a1.numpy(), a2.numpy())
    assert np.allclose(b1.numpy(), b2.numpy())
    assert b1.numpy().dtype == b2.numpy().dtype
    assert np.allclose(c1.numpy(), c2.numpy())
    assert c1.numpy().dtype == c2.numpy().dtype
    assert np.allclose(d1.numpy(), d2.numpy())
    assert d1.numpy().dtype == d2.numpy().dtype

def test_dsplit():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    index_array = (1, 2, 3)
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.dsplit(index_array)
    ms_output = ms_tensor.dsplit(index_array)
    for i in range(3):
        assert np.allclose(ms_output[i].asnumpy(), torch_output[i].numpy())
        assert ms_output[i].asnumpy().dtype == torch_output[i].numpy().dtype

def test_erf():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    np_array = np_array * 4
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.erf()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.erf()

    if is_test_under_ascend_context():
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), atol=1e-4)
    else:
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_erf_():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    np_array = np_array * 4
    torch_tensor = torch.tensor(np_array)
    torch_tensor.erf_()

    ms_tensor = pytorch.tensor(np_array)
    ms_tensor.erf_()

    if is_test_under_ascend_context():
        assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy(), atol=1e-4)
    else:
        assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype

def test_erfc():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    np_array = np_array * 4
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.erfc()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.erfc()

    if is_test_under_ascend_context():
        assert np.allclose(ms_out.asnumpy(), torch_out.numpy(), atol=1e-4)
    else:
        assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_erfc_():
    np_array = np.random.rand(1, 1, 1, 1, 2, 3, 2).astype(np.float32) - 0.5
    np_array = np_array * 4
    torch_tensor = torch.tensor(np_array)
    torch_tensor.erfc_()

    ms_tensor = pytorch.tensor(np_array)
    ms_tensor.erfc_()

    if is_test_under_ascend_context():
        assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy(), atol=1e-4)
    else:
        assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype

@SKIP_ENV_ASCEND(reason="ascend not support inf")
def test_erfinv():
    np_array = np.random.rand(2, 3, 4).astype(np.float32) - 0.5
    np_array = np_array * 1.9
    np_array[0, 0, 0:3] = [-1, 1, 0.98]

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.erfinv()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.erfinv()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_CPU(reason="testcase for ascend only, cpu test will be covered by test_erfinv.")
@SKIP_ENV_GPU(reason="testcase for ascend only, gpu test will be covered by test_erfinv.")
def test_erfinv_ascend():
    np_array = np.array([-0.5, -0.3, 0.1, 0.7]).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.erfinv()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.erfinv()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_expm1():
    np_array = np.random.rand(2, 3, 4).astype(np.float32) - 0.5
    np_array = np_array * 10
    np_array[0, 0, 0:3] = [0, 10, 25]

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.expm1()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.expm1()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

def test_trunc():
    np_array1 = np.random.randn(10).astype(np.float32) * 5
    np_array2 = np.random.randn(10).astype(np.float32) * 5

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch_tensor1.trunc()
    torch_out2 = torch_tensor2.trunc()

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_out1 = ms_tensor1.trunc()
    ms_out2 = ms_tensor2.trunc()

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_trunc_():
    np_array1 = np.random.randn(10).astype(np.float32) * 5
    np_array2 = np.random.randn(10).astype(np.float32) * 5

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor1.trunc_()
    torch_tensor2.trunc_()

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_tensor1.trunc_()
    ms_tensor2.trunc_()

    assert np.allclose(ms_tensor1.numpy(), torch_tensor1.numpy())
    assert ms_tensor1.numpy().dtype == torch_tensor1.numpy().dtype
    assert np.allclose(ms_tensor2.numpy(), torch_tensor2.numpy())
    assert ms_tensor2.numpy().dtype == torch_tensor2.numpy().dtype

def test_fix():
    np_array = np.random.rand(3, 4, 5).astype(np.float32) * 10 - 5

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.fix()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.fix()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_fix_():
    np_array = np.random.rand(3, 4, 5).astype(np.float32) * 10 - 5

    torch_tensor = torch.tensor(np_array)
    torch_tensor.fix_()

    ms_tensor = pytorch.tensor(np_array)
    ms_tensor.fix_()

    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype

def test_fliplr():
    np_1 = np.random.randn(4, 5, 6, 7).astype(np.float32)
    ms_tensor_1 = pytorch.tensor(np_1)
    ms_result = ms_tensor_1.fliplr()

    torch_tensor_1 = torch.tensor(np_1)
    torch_result = torch_tensor_1.fliplr()
    assert np.allclose(ms_result.asnumpy(), torch_result.numpy())
    assert ms_result.asnumpy().dtype == torch_result.numpy().dtype

def test_float_power():
    np_array = np.random.rand(3, 4, 5).astype(np.float32)*5
    np_exponent = np.random.rand(4, 5).astype(np.float32)*5
    np_array = np_array.astype(np.float32)
    np_exponent = np_exponent.astype(np.int32)

    torch_tensor = torch.tensor(np_array)
    torch_exponent = torch.tensor(np_exponent)
    torch_out1 = torch_tensor.float_power(torch_exponent)

    ms_tensor = pytorch.tensor(np_array)
    ms_exponent = pytorch.tensor(np_exponent)
    ms_out1 = ms_tensor.float_power(ms_exponent)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype

def test_xlogy():
    np_array1 = np.random.randn(10).astype(np.float64) * 5
    np_array2 = np.random.randn(10).astype(np.float32) * 5
    np_array1[0:2] = 0
    np_array2[1:3] = np.nan
    np_array2[5] = np.inf
    np_array2[0] = 2

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch_tensor1.xlogy(torch_tensor2)
    torch_out2 = torch_tensor1.xlogy(2)
    torch_out3 = torch_tensor1.xlogy(3.0)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_out1 = ms_tensor1.xlogy(ms_tensor2)
    ms_out2 = ms_tensor1.xlogy(2)
    ms_out3 = ms_tensor1.xlogy(3.0)

    if is_test_under_cpu_context():
        assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
        assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy(), equal_nan=True)
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_xlogy_():
    np_array1 = np.random.randn(10).astype(np.float64) * 5
    np_array2 = np.random.randn(10).astype(np.float32) * 5
    np_array1[0:2] = 0
    np_array2[1:3] = np.nan
    np_array2[5] = np.inf
    np_array2[0] = 2

    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor2 = pytorch.tensor(np_array2)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor1.xlogy_(ms_tensor2)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor1.xlogy_(torch_tensor2)
    if is_test_under_cpu_context():
        assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy(), equal_nan=True)
        assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor1.xlogy_(2)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor1.xlogy_(2)
    assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy(), equal_nan=True)
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor1.xlogy_(3.0)
    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor1.xlogy_(3.0)
    assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy(), equal_nan=True)
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

def test_vsplit():
    tensor = np.random.random((3, 4, 4)).astype(np.float32)
    index_array = [1, 2]
    torch_tensor = torch.tensor(tensor)
    ms_tensor = pytorch.tensor(tensor)
    torch_output = torch_tensor.vsplit(index_array)
    ms_output = ms_tensor.vsplit(index_array)
    for i in range(3):
        assert np.allclose(ms_output[i].asnumpy(), torch_output[i].numpy())
        assert ms_output[i].asnumpy().dtype == torch_output[i].numpy().dtype

@SKIP_ENV_ASCEND(reason="vdot not support float64 on Ascend")
def test_vdot_float64():
    data1_1 = np.array([2., 3, 4])
    data1_2 = np.array([1, 2., 3])

    a = torch.tensor(data1_1)
    b = torch.tensor(data1_2)
    torch_out = a.vdot(b)

    a = pytorch.tensor(data1_1)
    b = pytorch.tensor(data1_2)
    ms_out = a.vdot(b)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

def test_vdot_float():
    data1_1 = np.array([2., 3, 4]).astype(np.float32)
    data1_2 = np.array([1, 2., 3]).astype(np.float32)

    a = torch.tensor(data1_1)
    b = torch.tensor(data1_2)
    torch_out = a.vdot(b)

    a = pytorch.tensor(data1_1)
    b = pytorch.tensor(data1_2)
    ms_out = a.vdot(b)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GPU(reason="Unsupport int type on GPU.")
def test_vdot_int():
    data1_1 = np.array([2])
    data1_2 = np.array([3])

    a = torch.tensor(data1_1)
    b = torch.tensor(data1_2)
    torch_out = a.vdot(b)

    a = pytorch.tensor(data1_1)
    b = pytorch.tensor(data1_2)
    ms_out = a.vdot(b)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_ASCEND(reason="vdot not support complex on Ascend")
def test_vdot_complex():
    data1_1 = np.array([2, 3+1j, 4])
    data1_2 = np.array([1, 2+1j, 3])

    a = torch.tensor(data1_1)
    b = torch.tensor(data1_2)
    torch_out = a.vdot(b)

    a = pytorch.tensor(data1_1)
    b = pytorch.tensor(data1_2)
    ms_out = a.vdot(b)

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype


def test_where():
    x = torch.randn(3, 2)
    y = torch.ones(3, 2)
    output1 = x.where(x > 0, y)

    x_m = pytorch.Tensor(x.numpy())
    y_m = pytorch.Tensor(y.numpy())
    output1_ms = x_m.where(x_m > 0, y_m)

    assert np.allclose(output1.numpy(), output1_ms.numpy())

def test_where2():
    np_array1 = np.array([[-4, -3, -5],[-6, -7, -8]])
    np_array2 = np.array([1, 1, 2])
    x1 = torch.tensor(np_array1)
    y1 = torch.tensor(np_array2)
    x1_m = pytorch.tensor(np_array1)
    y1_m = pytorch.tensor(np_array2)

    output1 = x1.where(x1 > 0, y1)
    output1_ms = x1_m.where(x1_m > 0, y1_m)

    for i in range(len(output1_ms)):
        assert np.allclose(output1_ms[i].numpy(), output1[i].numpy())
        assert output1_ms[i].numpy().dtype == output1[i].numpy().dtype

def test_true_divide():
    np_array1 = np.random.randn(10).astype(np.float64) * 5
    np_array2 = np.random.randn(10).astype(np.float32) * 5
    # ascend not support inf and nan
    if is_test_under_ascend_context():
        np_array2 = np.where(np.abs(np_array2) < 1, 1, np_array2)
    for x_dtype in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
        np_array1_ = np_array1.astype(x_dtype)
        torch_tensor1 = torch.tensor(np_array1_)
        ms_tensor1 = pytorch.tensor(np_array1_)
        for y_dtype in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
            np_array2_ = np_array2.astype(y_dtype)
            torch_tensor2 = torch.tensor(np_array2_)
            ms_tensor2 = pytorch.tensor(np_array2_)
            torch_out1 = torch_tensor1.true_divide(torch_tensor2)
            ms_out1 = ms_tensor1.true_divide(ms_tensor2)
            assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), equal_nan=True)
            assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
        torch_out2 = torch_tensor1.true_divide(2)
        torch_out3 = torch_tensor1.true_divide(2.0)
        ms_out2 = ms_tensor1.true_divide(2)
        ms_out3 = ms_tensor1.true_divide(2.0)
        assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy(), equal_nan=True)
        assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
        assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy(), equal_nan=True)
        assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_true_divide_():
    a_torch = torch.tensor([1, 2, 3], dtype=torch.float16)
    a_ms = pytorch.tensor([1, 2, 3], dtype=torch.float16)

    a_torch.true_divide_(2)
    a_ms.true_divide_(2)

    assert np.allclose(a_ms.asnumpy(), a_torch.numpy(), equal_nan=True)
    assert a_ms.asnumpy().dtype == a_torch.numpy().dtype

def test_triu():
    a = torch.randn(3, 3)
    t_r = a.triu()
    t_r1 = a.triu(1)
    t_r2 = a.triu(-1)

    a = pytorch.tensor(a.numpy())
    ms_r = a.triu()
    ms_r1 = a.triu(1)
    ms_r2 = a.triu(-1)

    param_compare(ms_r, t_r)
    param_compare(ms_r1, t_r1)
    param_compare(ms_r2, t_r2)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_triu_():
    a = torch.randn(3, 3)
    b = pytorch.tensor(a.numpy())
    a.triu_()
    b.triu_()
    param_compare(a, b)

    a = torch.randn(3, 3)
    b = pytorch.tensor(a.numpy())
    a.triu_(1)
    b.triu_(1)
    param_compare(a, b)

    a = torch.randn(3, 3)
    b = pytorch.tensor(a.numpy())
    a.triu_(-1)
    b.triu_(-1)
    param_compare(a, b)

def test_tril():
    a = torch.randn(3, 3)
    t_r = a.tril()
    t_r1 = a.tril(1)
    t_r2 = a.tril(-1)

    a = pytorch.tensor(a.numpy())
    ms_r = a.tril()
    ms_r1 = a.tril(1)
    ms_r2 = a.tril(-1)

    assert np.allclose(t_r.numpy(), ms_r.numpy())
    assert np.allclose(t_r1.numpy(), ms_r1.numpy())
    assert np.allclose(t_r2.numpy(), ms_r2.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_tril_():
    a = torch.randn(3, 3)
    b = pytorch.tensor(a.numpy())
    a.tril_()
    b.tril_()
    assert np.allclose(a.numpy(), b.numpy())

    a = torch.randn(3, 3)
    b = pytorch.tensor(a.numpy())
    a.tril_(1)
    b.tril_(1)
    assert np.allclose(a.numpy(), b.numpy())

    a = torch.randn(3, 3)
    b = pytorch.tensor(a.numpy())
    a.tril_(-1)
    b.tril_(-1)
    assert np.allclose(a.numpy(), b.numpy())

def test_heaviside():
    x = np.array([-1.5, 0, 2.0], dtype=np.double)
    x2 = np.array([1.2, -2.0, 3.5], dtype=np.single)
    values = np.array([0.5])
    values2 = np.array([1, -3, -5.5], dtype=np.single)

    torch_input = torch.tensor(x)
    torch_input2 = torch.tensor(x2)
    torch_values = torch.tensor(values)
    torch_values2 = torch.tensor(values2)
    torch_out1 = torch_input.heaviside(torch_values)
    torch_out2 = torch_input2.heaviside(torch_values2)

    ms_input = pytorch.tensor(x)
    ms_input2 = pytorch.tensor(x2)
    ms_values = pytorch.tensor(values)
    ms_values2 = pytorch.tensor(values2)
    ms_out1 = ms_input.heaviside(ms_values)
    ms_out2 = ms_input2.heaviside(ms_values2)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype

def test_flipud():
    x = np.arange(4).reshape(2, 2).astype(np.double)
    x2 = np.arange(1, 9).reshape((2, 2, 2)).astype(np.complex64)

    torch_x1 = torch.tensor(x)
    torch_x2 = torch.tensor(x2)
    torch_out1 = torch_x1.flipud()
    torch_out2 = torch_x2.flipud()

    ms_x1 = pytorch.tensor(x)
    ms_x2 = pytorch.tensor(x2)
    ms_out1 = ms_x1.flipud()
    ms_out2 = ms_x2.flipud()

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())

def test_tile():
    x1 = np.arange(1, 9).reshape(4, 2).astype(np.float16)
    x2 = np.random.random((8, 6, 4, 2)).astype(np.float32)
    torch_tensor1 = torch.tensor(x1)
    torch_tensor2 = torch.tensor(x2)
    torch_out1 = torch_tensor1.tile(3, 3, 2, 2)
    torch_out2 = torch_tensor2.tile((2, 2))
    torch_out3 = torch_tensor2.tile(2, 2)
    torch_out4 = torch_tensor1.tile([3, 3, 2, 2])
    torch_out5 = torch_tensor1.tile([1,1,1,1,1,1])

    ms_tensor1 = pytorch.tensor(x1)
    ms_tensor2 = pytorch.tensor(x2)
    ms_out1 = ms_tensor1.tile(3, 3, 2, 2)
    ms_out2 = ms_tensor2.tile((2, 2))
    ms_out3 = ms_tensor2.tile(2, 2)
    ms_out4 = ms_tensor1.tile([3, 3, 2, 2])
    ms_out5 = ms_tensor1.tile([1,1,1,1,1,1])

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)
    param_compare(torch_out4, ms_out4)
    param_compare(torch_out5, ms_out5)

@SKIP_ENV_ASCEND(reason='tile not support int16 on Ascend')
def test_tile_int16():
    x1 = np.arange(1, 9).reshape(4, 2).astype(np.int16)
    torch_tensor1 = torch.tensor(x1)
    torch_out1 = torch_tensor1.tile(3, 3, 2, 2)
    ms_tensor1 = pytorch.tensor(x1)
    ms_out1 = ms_tensor1.tile(3, 3, 2, 2)
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())


def test_tile_uint8():
    x1 = np.arange(1, 9).reshape(4, 2).astype(np.uint8)
    torch_tensor1 = torch.tensor(x1)
    torch_out1 = torch_tensor1.tile(3, 3, 2, 2)
    ms_tensor1 = pytorch.tensor(x1)
    ms_out1 = ms_tensor1.tile(3, 3, 2, 2)
    param_compare(torch_out1, ms_out1)

def test_real():
    np_array = np.array([[1+5j, 2-1j, 3.0, -4j, -0j]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.real

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.real

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_pow_():
    x = np.random.random((2, 3)).astype(np.float32)
    exponent_float = 2.0
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_tensor.pow_(exponent_float)
    ms_tensor.pow_(exponent_float)
    assert np.allclose(ms_tensor.numpy(), torch_tensor.numpy())

    x_tensor = np.random.random((1, 4)).astype(np.float32)
    exponent_tensor = np.arange(1.0, 5.0)
    torch_tensor = torch.tensor(x_tensor)
    torch_exp = torch.tensor(exponent_tensor)
    torch_tensor.pow_(torch_exp)

    ms_tensor = pytorch.tensor(x_tensor)
    ms_exp = pytorch.tensor(exponent_tensor)
    ms_tensor.pow_(ms_exp)
    assert np.allclose(ms_tensor.numpy(), torch_tensor.numpy())

def test_rad2deg():
    np_array = np.array([[3.14, 1.57, 0, -1.57, -1, 20]])

    torch_tensor = torch.tensor(np_array)
    torch_out = torch_tensor.rad2deg()

    ms_tensor = pytorch.tensor(np_array)
    ms_out = ms_tensor.rad2deg()

    assert np.allclose(ms_out.asnumpy(), torch_out.numpy())
    assert ms_out.asnumpy().dtype == torch_out.numpy().dtype
    assert ms_out.asnumpy().shape == torch_out.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_reciprocal_():
    np_array1 = np.array([[1, 1, 2]]).astype(np.float32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor1.reciprocal_()

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor1.reciprocal_()

    assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

def test_remainder():
    np_array1 = np.array([[-3., -2, -1, 1, 2, 3]]).astype(np.float16)
    np_array2 = np.array([[1, 2, 3, 4, 5]]).astype(np.int16)
    np_other = np.array([[6, 7, 3, 4, 5]]).astype(np.float32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_other = torch.tensor(np_other)
    torch_out1 = torch_tensor1.remainder(2)
    torch_out2 = torch_tensor2.remainder(3)
    torch_out3 = torch_tensor2.remainder(torch_other)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_out1 = ms_tensor1.remainder(2)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_out2 = ms_tensor2.remainder(3)
    ms_other = pytorch.tensor(np_other)
    ms_out3 = ms_tensor2.remainder(ms_other)

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy())
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype
    assert np.allclose(ms_out2.asnumpy(), torch_out2.numpy())
    assert ms_out2.asnumpy().dtype == torch_out2.numpy().dtype
    assert np.allclose(ms_out3.asnumpy(), torch_out3.numpy())
    assert ms_out3.asnumpy().dtype == torch_out3.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_remainder_():
    np_array1 = np.array([[-3., -2, -1, 1, 2, 3]]).astype(np.float16)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor1.remainder_(2)

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor1.remainder_(2)

    assert np.allclose(ms_tensor1.asnumpy(), torch_tensor1.numpy())
    assert ms_tensor1.asnumpy().dtype == torch_tensor1.numpy().dtype

@SKIP_ENV_ASCEND_GRAPH_MODE("Ascend encapsulate numpy func, which has PyInterpret problem on Graph mode")
def test_svd():
    data = np.random.randn(5, 3).astype(np.float32)
    a1 = torch.tensor(data)
    a2 = pytorch.tensor(data)
    u1, s1, v1 = a1.svd()
    u2, s2, v2 = a2.svd()
    u3, s3, v3 = a1.svd(compute_uv=False)
    u4, s4, v4 = a2.svd(compute_uv=False)
    u5, s5, v5 = a1.svd(some=False)
    u6, s6, v6 = a2.svd(some=False)

    dist1 = torch.dist(a1, torch.mm(torch.mm(u1, torch.diag(s1)), v1.t()))
    dist3 = torch.dist(a1, torch.mm(torch.mm(u3[:, :3], torch.diag(s3)), v3.t()))
    dist5 = torch.dist(a1, torch.mm(torch.mm(u5[:, :3], torch.diag(s5)), v5.t()))
    dist2 = pytorch.dist(a2, pytorch.mm(pytorch.mm(u2, pytorch.diag(s2)), v2.t()))
    dist4 = pytorch.dist(a2, pytorch.mm(pytorch.mm(u4[:, :3], pytorch.diag(s4)), v4.t()))
    dist6 = pytorch.dist(a2, pytorch.mm(pytorch.mm(u6[:, :3], pytorch.diag(s6)), v6.t()))

    type_shape_compare(u1,u2)
    type_shape_compare(s1,s2)
    type_shape_compare(v1,v2)
    param_compare(u3,u4)
    type_shape_compare(s3,s4)
    param_compare(v3,v4)
    type_shape_compare(u5,u6)
    type_shape_compare(s5,s6)
    type_shape_compare(v5,v6)
    assert np.allclose(dist1.numpy(), dist2.numpy(), atol=3e-6)
    assert np.allclose(dist3.numpy(), dist4.numpy(), atol=3e-6)
    assert np.allclose(dist5.numpy(), dist6.numpy(), atol=3e-6)


def test_swapaxes():
    data = np.random.randn(5, 3).astype(np.float32)

    a = torch.tensor(data)
    torch_out = a.swapaxes(1, 0)

    a = pytorch.tensor(data)
    ms_out = a.swapaxes(1, 0)

    param_compare(ms_out, torch_out)

@SKIP_ENV_ASCEND(reason='ms tensor of shape 0 not supported on Ascend')
def test_swapaxes2():
    a = torch.randn(2, 3, 1, 0)
    torch_out = a.swapaxes(1, 0)

    a = pytorch.randn(2, 3, 1, 0)
    ms_out = a.swapaxes(1, 0)

    param_compare(ms_out, torch_out)

def test_swapdims():
    data = np.random.randn(5, 3).astype(np.float32)

    a = torch.tensor(data)
    torch_out = a.swapdims(1, 0)

    a = pytorch.tensor(data)
    ms_out = a.swapdims(1, 0)

    param_compare(ms_out, torch_out)


@SKIP_ENV_ASCEND(reason='mindspore.ops.unique_consecutive has some problem on ascend.')
def test_unique_consecutive():
    x = np.ones((3, 5)).astype(np.float32)

    torch_tensor1 = torch.tensor(x)
    torch_out1 = torch_tensor1.unique_consecutive()
    torch_out2, torch_indices = torch_tensor1.unique_consecutive(return_inverse=True)
    torch_out3, torch_counts = torch_tensor1.unique_consecutive(return_counts=True)

    ms_tensor1 = pytorch.tensor(x)
    ms_out1 = ms_tensor1.unique_consecutive()
    ms_out2, ms_indices = ms_tensor1.unique_consecutive(return_inverse=True)
    ms_out3, ms_counts = ms_tensor1.unique_consecutive(return_counts=True)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert np.allclose(torch_indices.numpy(), ms_indices.numpy())
    assert np.allclose(torch_counts.numpy(), ms_counts.numpy())

def test_tensor_split():
    x = torch.arange(0, 8)
    torch_out1 = x.tensor_split(3)

    x = torch.arange(0, 7)
    torch_out2 = x.tensor_split(3)
    torch_out3 = x.tensor_split((1, 6))

    x = torch.arange(0, 14).reshape(2, 7)
    torch_out4 = x.tensor_split(3, dim=1)
    torch_out5 = x.tensor_split((1, 6), dim=1)

    x = pytorch.arange(0, 8)
    ms_out1 = x.tensor_split(3)

    x = pytorch.arange(0, 7)
    ms_out2 = x.tensor_split(3)
    ms_out3 = x.tensor_split((1, 6))

    x = pytorch.arange(0, 14).reshape(2, 7)
    ms_out4 = x.tensor_split(3, dim=1)
    ms_out5 = x.tensor_split((1, 6), dim=1)

    for i, _ in enumerate(torch_out1):
        assert np.allclose(torch_out1[i].numpy(), ms_out1[i].numpy())

    for i, _ in enumerate(torch_out2):
        assert np.allclose(torch_out2[i].numpy(), ms_out2[i].numpy())

    for i, _ in enumerate(torch_out3):
        assert np.allclose(torch_out3[i].numpy(), ms_out3[i].numpy())

    for i, _ in enumerate(torch_out4):
        assert np.allclose(torch_out4[i].numpy(), ms_out4[i].numpy())

    for i, _ in enumerate(torch_out5):
        assert np.allclose(torch_out5[i].numpy(), ms_out5[i].numpy())

def test_tanh():
    data1 = np.random.randn(4).astype(np.float32)

    a = torch.tensor(data1)
    torch_out1 = a.tanh()

    a = torch.tensor(2)
    torch_out2 = a.tanh()

    a = pytorch.tensor(data1)
    ms_out1 = a.tanh()

    a = pytorch.tensor(2)
    ms_out2 = a.tanh()

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_tanh_():
    data1 = np.random.randn(4).astype(np.float32)

    a = torch.tensor(data1)
    a.tanh_()

    b = pytorch.tensor(data1)
    b.tanh_()

    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_tan():
    data1 = np.random.randn(4).astype(np.float32)

    a = torch.tensor(data1)
    torch_out1 = a.tan()

    a = torch.tensor(2)
    torch_out2 = a.tan()

    a = pytorch.tensor(data1)
    ms_out1 = a.tan()

    a = pytorch.tensor(2)
    ms_out2 = a.tan()

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_tan_():
    data1 = np.random.randn(4).astype(np.float32)

    a = torch.tensor(data1)
    a.tan_()

    b = pytorch.tensor(data1)
    b.tan_()

    assert np.allclose(a.numpy(), b.numpy())
    assert a.numpy().dtype == b.numpy().dtype

def test_take():
    data = np.array([[4, 3, 5],
                    [6, 7, 8]])

    # On windows, torch only support indices's dtype is np.int64
    indices = np.array([0, 2, 5]).astype(np.int64)

    src = torch.tensor(data)
    torch_out = src.take(torch.tensor(indices))

    src = pytorch.tensor(data)
    ms_out = src.take(pytorch.tensor(indices))

    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

def test_sinc():
    data = np.random.random(4).astype(np.float32)
    t = torch.tensor(data)
    torch_out = t.sinc()

    t = pytorch.tensor(data)
    ms_out = t.sinc()

    param_compare(torch_out, ms_out, atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_sinc_():
    data = np.random.random(4).astype(np.float32)
    t1 = torch.tensor(data)
    t1.sinc_()

    t2 = pytorch.tensor(data)
    t2.sinc_()

    param_compare(t1, t2, atol=1e-5)

def test_sinh():
    data = np.random.random(4).astype(np.float32)
    t = torch.tensor(data)
    torch_out = t.sinh()

    t = pytorch.tensor(data)
    ms_out = t.sinh()

    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_sinh_():
    data = np.random.random(4).astype(np.float32)
    t1 = torch.tensor(data)
    t1.sinh_()

    t2 = pytorch.tensor(data)
    t2.sinh_()

    assert np.allclose(t1.numpy(), t2.numpy())
    assert t1.numpy().dtype == t2.numpy().dtype


def test_hardshrink():
    x = np.random.randn(2, 3, 4)
    x = x.astype(np.float32)

    torch_x = torch.tensor(x)
    ms_x = pytorch.tensor(x)

    torch_out1 = torch_x.hardshrink(lambd=0.8)
    ms_out1 = ms_x.hardshrink(lambd=0.8)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())

def test_hsplit():
    x = np.arange(16.0).reshape(4,4)

    torch_tensor1 = torch.tensor(x)
    torch_out1 = torch_tensor1.hsplit(2)
    torch_out2 = torch_tensor1.hsplit([3, 6])

    ms_tensor1 = pytorch.tensor(x)
    ms_out1 = ms_tensor1.hsplit(2)
    ms_out2 = torch_tensor1.hsplit([3, 6])

    for i in range(2):
        assert np.allclose(ms_out1[i].numpy(), torch_out1[i].numpy())
        assert ms_out1[i].numpy().dtype == torch_out1[i].numpy().dtype
    for i in range(3):
        assert np.allclose(ms_out2[i].numpy(), torch_out2[i].numpy())
        assert ms_out2[i].numpy().dtype == torch_out2[i].numpy().dtype

@SKIP_ENV_ASCEND(reason='mindspore.ops.hypot result not correct on ascend.')
def test_hypot():
    x1 = np.array([4.0]).astype(np.float16)
    x2 = np.array([3.0, 4.0, 5.0]).astype(np.float32)

    torch_tensor1 = torch.tensor(x1)
    torch_tensor2 = torch.tensor(x2)
    torch_out1 = torch_tensor1.hypot(torch_tensor2)
    torch_out2 = torch_tensor2.hypot(torch_tensor2)

    ms_tensor1 = pytorch.tensor(x1)
    ms_tensor2 = pytorch.tensor(x2)
    ms_out1 = ms_tensor1.hypot(ms_tensor2)
    ms_out2 = ms_tensor2.hypot(ms_tensor2)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())

def test_log10():
    x = np.random.rand(3, 5)
    x_log10 = x.astype(np.float32)

    torch_tensor1 = torch.tensor(x_log10)
    torch_out1 = torch_tensor1.log10()

    ms_tensor1 = pytorch.tensor(x_log10)
    ms_out1 = ms_tensor1.log10()

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy(), atol=1e-5)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_log10_():
    x = np.random.rand(3, 5)
    x_log10 = x.astype(np.float32)

    torch_tensor1 = torch.tensor(x_log10)
    torch_tensor1.log10_()

    ms_tensor1 = pytorch.tensor(x_log10)
    ms_tensor1.log10_()

    assert np.allclose(torch_tensor1.numpy(), ms_tensor1.numpy(), atol=1e-5)

def test_outer():
    v1 = np.arange(1., 5.)
    v2 = np.arange(1., 4.)
    v3 = np.array([1, 2, 3], dtype=np.int32)
    v4 = np.array([-1, -2, -3], dtype=np.int32)

    torch_v1 = torch.tensor(v1)
    torch_v2 = torch.tensor(v2)
    torch_v3 = torch.tensor(v3)
    torch_v4 = torch.tensor(v4)
    torch_out1 = torch_v1.outer(torch_v2)
    torch_out2 = torch_v3.outer(torch_v4)

    ms_v1 = pytorch.tensor(v1)
    ms_v2 = pytorch.tensor(v2)
    ms_v3 = pytorch.tensor(v3)
    ms_v4 = pytorch.tensor(v4)
    ms_out1 = ms_v1.outer(ms_v2)
    ms_out2 = ms_v3.outer(ms_v4)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_logical_xor():
    torch_out1 = torch.tensor([True, False, True]).logical_xor(torch.tensor([True, False, False]))
    a = torch.tensor([0, 1, 10, 0], dtype=torch.int8)
    b = torch.tensor([4, 0, 1, 0], dtype=torch.int8)
    torch_out2 = a.logical_xor(b)

    ms_out1 = pytorch.tensor([True, False, True]).logical_xor(pytorch.tensor([True, False, False]))
    a = pytorch.tensor([0, 1, 10, 0], dtype=pytorch.int8)
    b = pytorch.tensor([4, 0, 1, 0], dtype=pytorch.int8)
    ms_out2 = a.logical_xor(b)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_log1p():
    x = np.random.rand(3, 5)
    x_log1p = (x - 1).astype(np.float32)

    torch_tensor = torch.tensor(x_log1p)
    torch_out = torch_tensor.log1p()

    ms_tensor = pytorch.tensor(x_log1p)
    ms_out = ms_tensor.log1p()

    assert np.allclose(torch_out.numpy(), ms_out.numpy(), atol=1e-5)

def test_logaddexp():
    x1, y1 = np.array([-1.0]).astype(np.float32), np.array([-1.0, -2, -3]).astype(np.float32)
    x2, y2 = np.array([-100.0, -200, -300]).astype(np.float32), np.array([-1.0, -2, -3]).astype(np.float32)
    x3, y3 = np.array([1.0, 2000, 30000]).astype(np.float32), np.array([-1.0, -2, -3]).astype(np.float32)

    torch_x1, torch_y1 = torch.tensor(x1), torch.tensor(y1)
    torch_x2, torch_y2 = torch.tensor(x2), torch.tensor(y2)
    torch_x3, torch_y3 = torch.tensor(x3), torch.tensor(y3)
    torch_out1 = torch_x1.logaddexp(torch_y1)
    torch_out2 = torch_x2.logaddexp(torch_y2)
    torch_out3 = torch_x3.logaddexp(torch_y3)

    ms_x1, ms_y1 = pytorch.tensor(x1), pytorch.tensor(y1)
    ms_x2, ms_y2 = pytorch.tensor(x2), pytorch.tensor(y2)
    ms_x3, ms_y3 = pytorch.tensor(x3), pytorch.tensor(y3)
    ms_out1 = ms_x1.logaddexp(ms_y1)
    ms_out2 = ms_x2.logaddexp(ms_y2)
    ms_out3 = ms_x3.logaddexp(ms_y3)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert ms_out1.asnumpy().shape == torch_out1.numpy().shape
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert ms_out2.asnumpy().shape == torch_out2.numpy().shape
    # TODO: ms.ops.logaddexp support large input
    # assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    # assert ms_out3.asnumpy().shape == torch_out3.numpy().shape

@SKIP_ENV_ASCEND(reason="logaddexp currently not support float64 on Ascend")
def test_logaddexp_fp64():
    x1, y1 = np.array([-1.0]), np.array([-1.0, -2, -3])

    torch_x1, torch_y1 = torch.tensor(x1), torch.tensor(y1)
    torch_out1 = torch_x1.logaddexp(torch_y1)

    ms_x1, ms_y1 = pytorch.tensor(x1), pytorch.tensor(y1)
    ms_out1 = ms_x1.logaddexp(ms_y1)

    param_compare(torch_out1, ms_out1)

def test_logdet():
    x = np.random.randn(2, 3, 3)
    x = x.astype(np.float32)

    torch_tensor1 = torch.tensor(x)
    torch_out1 = torch_tensor1.logdet()

    ms_tensor1 = pytorch.tensor(x)
    ms_out1 = ms_tensor1.logdet()

    #TODO: logdet not accurate in Graph mode
    if is_test_under_ascend_context():
        # ms not support nan output
        if np.isnan(torch_out1.numpy()).any():
            return True

    assert np.allclose(ms_out1.asnumpy(), torch_out1.numpy(), atol=1e-5, equal_nan=True)
    assert ms_out1.asnumpy().dtype == torch_out1.numpy().dtype

def test_logical_not():
    x1 = np.array([True, False])
    x2 = np.array([0, 1, -10], dtype=np.int8)
    x3 = np.array([0., 1.5, -10.], dtype=np.double)
    x4 = np.array([0., 1., -10.], dtype=np.double)

    torch_tensor1 = torch.tensor(x1)
    torch_tensor2 = torch.tensor(x2)
    torch_tensor3 = torch.tensor(x3)
    torch_tensor4 = torch.tensor(x4)
    torch_out1 = torch_tensor1.logical_not()
    torch_out2 = torch_tensor2.logical_not()
    torch_out3 = torch_tensor3.logical_not()

    ms_tensor1 = pytorch.tensor(x1)
    ms_tensor2 = pytorch.tensor(x2)
    ms_tensor3 = pytorch.tensor(x3)
    ms_tensor4 = pytorch.tensor(x4)
    ms_out1 = ms_tensor1.logical_not()
    ms_out2 = ms_tensor2.logical_not()
    ms_out3 = ms_tensor3.logical_not()

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

def test_logical_or():
    x1, y1 = np.array([True, False, True]), np.array([True, False, False])
    x2, y2 = np.array([0, 1, 10, 0], dtype=np.int8), np.array([4, 0, 1, 0], dtype=np.int8)

    torch_x1 = torch.tensor(x1)
    torch_y1 = torch.tensor(y1)
    torch_x2 = torch.tensor(x2)
    torch_y2 = torch.tensor(y2)
    torch_out1 = torch_x1.logical_or(torch_y1)
    torch_out2 = torch_x2.logical_or(torch_y2)
    torch_out3 = torch_x2.double().logical_or(torch_y2.double())
    torch_out4 = torch_x2.double().logical_or(torch_y2)

    ms_x1 = pytorch.tensor(x1)
    ms_y1 = pytorch.tensor(y1)
    ms_x2 = pytorch.tensor(x2)
    ms_y2 = pytorch.tensor(y2)
    ms_out1 = ms_x1.logical_or(ms_y1)
    ms_out2 = ms_x2.logical_or(ms_y2)
    ms_out3 = ms_x2.double().logical_or(ms_y2.double())
    ms_out4 = ms_x2.double().logical_or(ms_y2)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(torch_out4.numpy(), ms_out4.numpy())
    assert torch_out4.numpy().dtype == ms_out4.numpy().dtype

def test_adjoint():
    x = np.array([[0.+0.j, 1.+1.j],[2.+2.j, 3.+3.j]])

    torch_x = torch.tensor(x)
    torch_out = torch_x.adjoint()

    ms_x = pytorch.tensor(x)
    ms_out = ms_x.adjoint()

    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy())

def test_lerp():
    start = np.arange(1., 5.).astype(np.float32)
    end = np.empty(4).astype(np.float32)
    end.fill(10)

    torch_start = torch.tensor(start)
    torch_end = torch.tensor(end)
    torch_out1 = torch_start.lerp(torch_end, float(0.5))
    torch_out2 = torch_start.lerp(torch_end, int(3))
    torch_out3 = torch_start.lerp(torch_end, torch.tensor(3, dtype=torch.float32))
    torch_out4 = torch_start.lerp(torch_end, torch.full_like(torch_start, 0.5))

    ms_start = pytorch.tensor(start)
    ms_end = pytorch.tensor(end)
    ms_out1 = ms_start.lerp(ms_end, 0.5)
    ms_out2 = ms_start.lerp(ms_end, int(3))
    ms_out3 = ms_start.lerp(ms_end, pytorch.tensor(3, dtype=pytorch.float32))
    ms_out4 = ms_start.lerp(ms_end, pytorch.full_like(ms_start, 0.5))

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)
    param_compare(torch_out4, ms_out4)

@SKIP_ENV_ASCEND(reason='currently not support float64 on Ascend')
def test_lerp_fp64():
    start = np.arange(1., 5.)
    end = np.empty(4)
    end.fill(10)
    torch_start = torch.tensor(start)
    torch_end = torch.tensor(end)
    torch_out1 = torch_start.lerp(torch_end, 0.5)
    ms_start = pytorch.tensor(start)
    ms_end = pytorch.tensor(end)
    ms_out1 = ms_start.lerp(ms_end, 0.5)
    param_compare(torch_out1, ms_out1)


def test_masked_select():
    x = np.array([1, 2, 3, 4], dtype=np.int64)
    mask = np.array([1, 0, 1, 0], dtype=np.bool_)

    torch_x = torch.tensor(x)
    torch_mask = torch.tensor(mask)
    torch_out1 = torch_x.masked_select(torch_mask)

    ms_x = pytorch.tensor(x)
    ms_mask = pytorch.tensor(mask)
    ms_out1 = ms_x.masked_select(ms_mask)

    param_compare(ms_out1, torch_out1)

def test_angle():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])

    torch_x = torch.tensor(x)
    torch_out = torch_x.angle()*180/3.14159

    ms_x = pytorch.tensor(x)
    ms_out = ms_x.angle()*180/3.14159

    assert np.allclose(torch_out.resolve_conj().numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

def test_element_size():
    x1 = np.array([])
    x2 = np.random.randn(1, 2, 3)
    x3 = np.array(1)
    for type_input in (np.int16, np.int32, np.uint8, np.half, np.double, np.single):
        torch_x1 = torch.from_numpy(x1.astype(type_input))
        torch_x2 = torch.from_numpy(x2.astype(type_input))
        torch_x3 = torch.from_numpy(x3.astype(type_input))
        torch_out1 = torch_x1.element_size()
        torch_out2 = torch_x2.element_size()
        torch_out3 = torch_x3.element_size()

        ms_x1 = pytorch.from_numpy(x1.astype(type_input))
        ms_x2 = pytorch.from_numpy(x2.astype(type_input))
        ms_x3 = pytorch.from_numpy(x3.astype(type_input))
        ms_out1 = ms_x1.element_size()
        ms_out2 = ms_x2.element_size()
        ms_out3 = ms_x3.element_size()

        assert ms_out1 == torch_out1
        assert type(ms_out1) == type(torch_out1)
        assert ms_out2 == torch_out2
        assert type(ms_out2) == type(torch_out2)
        assert ms_out3 == torch_out3
        assert type(ms_out3) == type(torch_out3)

def test_positive():
    x = np.random.randn(5)

    torch_x = torch.tensor(x)
    torch_out1 = torch_x.positive()

    ms_x = pytorch.tensor(x)
    ms_out1 = ms_x.positive()

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype

def test_sgn():
    t = torch.tensor([3+4j, 7-24j, 0, 1+2j], dtype=torch.complex64)
    m = pytorch.tensor([3+4j, 7-24j, 0, 1+2j], dtype=pytorch.complex64)
    t_out = t.sgn()
    m_out = m.sgn()
    assert np.allclose(t_out.numpy(), m_out.numpy())
    assert t_out.numpy().dtype == m_out.numpy().dtype

    t = torch.tensor([2, 3])
    m = pytorch.tensor([2, 3])
    t_out = t.sgn()
    m_out = m.sgn()
    assert np.allclose(t_out.numpy(), m_out.numpy())
    assert t_out.numpy().dtype == m_out.numpy().dtype

    t = torch.tensor([2., 3])
    m = pytorch.tensor([2., 3])
    t_out = t.sgn()
    m_out = m.sgn()
    assert np.allclose(t_out.numpy(), m_out.numpy())
    assert t_out.numpy().dtype == m_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_sgn_():
    t = torch.tensor([3+4j, 7-24j, 0, 1+2j], dtype=torch.complex64)
    m = pytorch.tensor([3+4j, 7-24j, 0, 1+2j], dtype=pytorch.complex64)
    t.sgn_()
    m.sgn_()
    assert np.allclose(t.numpy(), m.numpy())
    assert t.numpy().dtype == m.numpy().dtype

    t = torch.tensor([2, 3])
    m = pytorch.tensor([2, 3])
    t.sgn_()
    m.sgn_()
    assert np.allclose(t.numpy(), m.numpy())
    assert t.numpy().dtype == m.numpy().dtype

    t = torch.tensor([2., 3])
    m = pytorch.tensor([2., 3])
    t.sgn_()
    m.sgn_()
    assert np.allclose(t.numpy(), m.numpy())
    assert t.numpy().dtype == m.numpy().dtype

def test_logical_and():
    a = np.array([0, 1, 10, 0], dtype=np.int8)
    b = np.array([4, 0, 1, 0], dtype=np.int8)

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    ms_a = pytorch.tensor(a)
    ms_b = pytorch.tensor(b)

    torch_out1 = torch.tensor([True, False, True]).logical_and(torch.tensor([True, False, False]))
    torch_out2 = torch_a.logical_and(torch_b)
    torch_out3 = torch_a.double().logical_and(torch_b.double())
    torch_out4 = torch_a.double().logical_and(torch_b)

    ms_out1 = pytorch.tensor([True, False, True]).logical_and(pytorch.tensor([True, False, False]))
    ms_out2 = ms_a.logical_and(ms_b)
    ms_out3 = ms_a.double().logical_and(ms_b.double())
    ms_out4 = ms_a.double().logical_and(ms_b)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(torch_out4.numpy(), ms_out4.numpy())
    assert torch_out4.numpy().dtype == ms_out4.numpy().dtype

def test_igamma():
    np_array = np.random.rand(2, 3, 4, 5) * 3 + 1
    np_other = np.random.rand(4, 5) * 3 + 1

    torch_tensor1 = torch.tensor(np_array.astype(np.float16))
    torch_other1 = torch.tensor(np_other.astype(np.float64))
    torch_tensor2 = torch.tensor(np_array.astype(np.float64))
    torch_other2 = torch.tensor(np_other.astype(np.float32))
    torch_out1 = torch_tensor1.igamma(torch_other1)
    torch_out2 = torch_tensor2.igamma(torch_other2)

    ms_tensor1 = pytorch.tensor(np_array.astype(np.float16))
    ms_other1 = pytorch.tensor(np_other.astype(np.float64))
    ms_tensor2 = pytorch.tensor(np_array.astype(np.float64))
    ms_other2 = pytorch.tensor(np_other.astype(np.float32))
    ms_out1 = ms_tensor1.igamma(ms_other1)
    ms_out2 = ms_tensor2.igamma(ms_other2)

    param_compare(torch_out1, ms_out1, equal_nan=True)
    param_compare(torch_out2, ms_out2, equal_nan=True)

def test_igammac():
    np_array = np.random.rand(2, 3, 4, 5) * 3 + 1
    np_other = np.random.rand(4, 5) * 3 + 1

    torch_tensor1 = torch.tensor(np_array.astype(np.float16))
    torch_other1 = torch.tensor(np_other.astype(np.float64))
    torch_tensor2 = torch.tensor(np_array.astype(np.float64))
    torch_other2 = torch.tensor(np_other.astype(np.float32))
    torch_out1 = torch_tensor1.igammac(torch_other1)
    torch_out2 = torch_tensor2.igammac(torch_other2)

    ms_tensor1 = pytorch.tensor(np_array.astype(np.float16))
    ms_other1 = pytorch.tensor(np_other.astype(np.float64))
    ms_tensor2 = pytorch.tensor(np_array.astype(np.float64))
    ms_other2 = pytorch.tensor(np_other.astype(np.float32))
    ms_out1 = ms_tensor1.igammac(ms_other1)
    ms_out2 = ms_tensor2.igammac(ms_other2)

    param_compare(torch_out1, ms_out1, equal_nan=True)
    param_compare(torch_out2, ms_out2, equal_nan=True)


@SKIP_ENV_GRAPH_MODE(reason="inpalce operation only support on pynative mode")
def test_igamma_():
    np_array = np.random.rand(3, 3) * 3 + 1
    np_other = np.random.rand(3, 3) * 3 + 1

    torch_tensor1 = torch.tensor(np_array.astype(np.float16))
    torch_other1 = torch.tensor(np_other.astype(np.float16))
    torch_tensor1.igamma_(torch_other1)

    ms_tensor1 = pytorch.tensor(np_array.astype(np.float16))
    ms_other1 = pytorch.tensor(np_other.astype(np.float16))
    ms_tensor1.igamma_(ms_other1)
    param_compare(torch_tensor1, ms_tensor1, equal_nan=True, atol=1e-3)

@SKIP_ENV_GRAPH_MODE(reason="inpalce operation only support on pynative mode")
def test_igammac_():
    np_array = np.random.rand(3, 3) * 3 + 1
    np_other = np.random.rand(3, 3) * 3 + 1

    torch_tensor1 = torch.tensor(np_array.astype(np.float32))
    torch_other1 = torch.tensor(np_other.astype(np.float64))
    torch_tensor1.igammac_(torch_other1)

    ms_tensor1 = pytorch.tensor(np_array.astype(np.float32))
    ms_other1 = pytorch.tensor(np_other.astype(np.float64))
    ms_tensor1.igammac_(ms_other1)
    param_compare(torch_tensor1, ms_tensor1, equal_nan=True)

def test_roll():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=np.float32)
    torch_tensor = torch.tensor(x).view(4, 2)
    ms_tensor =pytorch.tensor(x).view(4, 2)

    torch_out1 = torch_tensor.roll(1)
    torch_out2 = torch_tensor.roll(1, 0)
    torch_out3 = torch_tensor.roll(-1, 0)
    torch_out4 = torch_tensor.roll(shifts=(2, 1), dims=(0, 1))

    ms_out1 = ms_tensor.roll(1)
    ms_out2 = ms_tensor.roll(1, 0)
    ms_out3 = ms_tensor.roll(-1, 0)
    ms_out4 = ms_tensor.roll(shifts=(2, 1), dims=(0, 1))

    assert np.allclose(ms_out1.numpy(), torch_out1.numpy())
    assert np.allclose(ms_out2.numpy(), torch_out2.numpy())
    assert np.allclose(ms_out3.numpy(), torch_out3.numpy())
    assert np.allclose(ms_out4.numpy(), torch_out4.numpy())
    assert ms_out1.numpy().dtype == torch_out1.numpy().dtype
    assert ms_out2.numpy().dtype == torch_out2.numpy().dtype
    assert ms_out3.numpy().dtype == torch_out3.numpy().dtype
    assert ms_out4.numpy().dtype == torch_out4.numpy().dtype
    assert ms_out1.numpy().shape == torch_out1.numpy().shape
    assert ms_out2.numpy().shape == torch_out2.numpy().shape
    assert ms_out3.numpy().shape == torch_out3.numpy().shape
    assert ms_out4.numpy().shape == torch_out4.numpy().shape

def test_lcm():
    a = np.arange(15).reshape(3, 5)
    c = np.array([3])

    torch_a = torch.tensor(a)
    torch_c = torch.tensor(c)
    torch_out1 = torch_a.lcm(torch_c)
    torch_out2 = torch_a.lcm(torch.tensor([0]))
    torch_out3 = torch.tensor([0]).lcm(torch.tensor([0]))

    ms_a = pytorch.tensor(a)
    ms_c = pytorch.tensor(c)
    ms_out1 = ms_a.lcm(ms_c)
    ms_out2 = ms_a.lcm(pytorch.tensor([0]))
    ms_out3 = pytorch.tensor([0]).lcm(pytorch.tensor([0]))

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_lcm_():
    a = np.array([5, 10, 15])
    b = np.array([3, 4, 5])
    c = np.array([3])

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_c = torch.tensor(c)
    ms_a = pytorch.tensor(a)
    ms_b = pytorch.tensor(b)
    ms_c = pytorch.tensor(c)

    torch_a.lcm_(torch_b)
    ms_a.lcm_(ms_b)
    assert np.allclose(torch_a.numpy(), ms_a.numpy())
    assert torch_a.numpy().dtype == ms_a.numpy().dtype

    torch_a.lcm_(torch_c)
    ms_a.lcm_(ms_c)
    assert np.allclose(torch_a.numpy(), ms_a.numpy())
    assert torch_a.numpy().dtype == ms_a.numpy().dtype

@SKIP_ENV_ASCEND(reason="Tensor.inner doesn't support inputs of int type on Ascend")
def test_inner_int64():
    a1 = np.array([1, 2, 3])
    b1 = np.array([0, 2, 1])
    torch_a1 = torch.tensor(a1)
    torch_b1 = torch.tensor(b1)
    ms_a1 = pytorch.tensor(a1)
    ms_b1 = pytorch.tensor(b1)
    torch_out1 = torch_a1.inner(torch_b1)
    ms_out1 = ms_a1.inner(ms_b1)
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype

def test_inner():
    a2 = np.random.randn(2, 3).astype(np.float32)
    b2 = np.random.randn(2, 4, 3).astype(np.float32)

    torch_a2 = torch.tensor(a2)
    torch_b2 = torch.tensor(b2)
    ms_a2 = pytorch.tensor(a2)
    ms_b2 = pytorch.tensor(b2)

    torch_out2 = torch_a2.inner(torch_b2)
    torch_out3 = torch_a2.inner(torch.tensor(2, dtype=torch.float32))
    ms_out2 = ms_a2.inner(ms_b2)
    ms_out3 = ms_a2.inner(pytorch.tensor(2, dtype=pytorch.float32))

    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

def test_multinomial():
    x = np.array([0, 9, 4, 0], dtype=np.float32)
    torch_tensor = torch.tensor(x)
    ms_tensor =pytorch.tensor(x)

    torch_out1 = torch_tensor.multinomial(2)
    torch_out2 = torch_tensor.multinomial(4)
    torch_out3 = torch_tensor.multinomial(4, True)
    ms_out1 = ms_tensor.multinomial(2)
    ms_out2 = ms_tensor.multinomial(4)
    ms_out3 = ms_tensor.multinomial(4, True)

    type_shape_compare(ms_out1, torch_out1)
    type_shape_compare(ms_out2, torch_out2)
    type_shape_compare(ms_out3, torch_out3)

def test_lgamma():
    np_array = np.random.rand(1, 4, 5, 6)*10-2
    np_array1 = np_array.astype(np.float32)
    np_array2 = np.arange(0.5, 2, 0.5)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch_tensor1.lgamma()
    torch_out2 = torch_tensor2.lgamma()

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_out1 = ms_tensor1.lgamma()
    ms_out2 = ms_tensor2.lgamma()

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_cov():
    x = np.array([[0, 2], [1, 1], [2, 0]]).T
    fw = np.random.randint(1, 10, (3,))
    aw = np.random.rand(3).astype(np.float32)
    # aw = np.random.rand(3)

    torch_x = torch.tensor(x)
    torch_fw = torch.tensor(fw)
    torch_aw = torch.tensor(aw)
    torch_out1 = torch_x.cov()
    torch_out2 = torch_x.cov(correction=0)
    torch_out3 = torch_x.cov(fweights=torch_fw, aweights=torch_aw)

    ms_x = pytorch.tensor(x)
    ms_fw = pytorch.tensor(fw)
    ms_aw = pytorch.tensor(aw)
    ms_out1 = ms_x.cov()
    ms_out2 = ms_x.cov(correction=0)
    ms_out3 = ms_x.cov(fweights=ms_fw, aweights=ms_aw)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype

def test_rot90():
    np_array = np.array([[0, 1],[2, 3]], dtype=np.float32)
    dims1 = [0, 1]
    dims2 = [1, 0]
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)

    torch_out1 = torch_tensor.rot90(1,dims1)
    torch_out2 = torch_tensor.rot90(2,dims1)
    torch_out3 = torch_tensor.rot90(-1,dims1)
    torch_out4 = torch_tensor.rot90(1,dims2)
    ms_out1 = ms_tensor.rot90(1,dims1)
    ms_out2 = ms_tensor.rot90(2,dims1)
    ms_out3 = ms_tensor.rot90(-1,dims1)
    ms_out4 = ms_tensor.rot90(1,dims2)
    param_compare(ms_out1, torch_out1)
    param_compare(ms_out2, torch_out2)
    param_compare(ms_out3, torch_out3)
    param_compare(ms_out4, torch_out4)


def test_median_common1():
    data = np.array([[0.57, 0.11, 0.21],[0.38, 0.50, 0.57], [0.36, 0.16, 0.44]])
    for tensor_type in (np.int16, np.int32, np.int64, np.float32, np.float64):
        np_array = data.astype(tensor_type)
        torch_tensor = torch.tensor(np_array)
        ms_tensor = pytorch.tensor(np_array)

        torch_out2 = torch_tensor.median(-2,False)
        ms_out2 = ms_tensor.median(-2,False)

        param_compare(ms_out2[0], torch_out2[0])

def test_median_common2():
    data = np.array([[0.57, 0.11, 0.21],[0.38, 0.50, 0.57], [0.36, 0.16, 0.44]])
    for tensor_type in (np.int16, np.int32, np.int64, np.float32, np.float64):
        np_array = data.astype(tensor_type)
        torch_tensor = torch.tensor(np_array)
        ms_tensor = pytorch.tensor(np_array)

        torch_out1 = torch_tensor.median()
        ms_out1 = ms_tensor.median()

        assert np.allclose(ms_out1.numpy(), torch_out1.numpy())
        assert ms_out1.numpy().dtype == torch_out1.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="graph cannot support collections.namedtuple.")
def test_median():
    np_array = np.array([[0.57, 0.11, 0.21],[0.38, 0.50, 0.57], [0.36, 0.16, 0.44]])
    for tensor_type in (np.int16, np.int32, np.int64, np.float32, np.float64):
        np_array = np_array.astype(tensor_type)
        torch_tensor = torch.tensor(np_array)
        ms_tensor = pytorch.tensor(np_array)

        torch_out1 = torch_tensor.median()
        torch_out2 = torch_tensor.median(-2,False)
        torch_out3 = torch_tensor.median(1,True)
        ms_out1 = ms_tensor.median()
        ms_out2 = ms_tensor.median(-2,False)
        ms_out3 = ms_tensor.median(1,True)

        param_compare(ms_out1, torch_out1)
        param_compare(ms_out2.values, torch_out2.values)
        param_compare(ms_out3.values, torch_out3.values)

def test_frac():
    np_array1 = np.random.randn(4).astype(np.float32)
    np_array2 = np_array1.astype(np.float16)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch_tensor1.frac()
    torch_out2 = torch_tensor2.frac()

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_out1 = ms_tensor1.frac()
    ms_out2 = ms_tensor2.frac()
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason="frac currently not support float64 on Ascend")
def test_frac_fp64():
    np_array1 = np.array([1, 2.5, -3.2])

    torch_tensor1 = torch.tensor(np_array1)
    torch_out1 = torch_tensor1.frac()

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_out1 = ms_tensor1.frac()
    param_compare(torch_out1, ms_out1)


@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_frac_():
    np_array1 = (np.random.randn(2, 3, 4) * 5).astype(np.float32)
    np_array1 = np_array1.astype(np.float16)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor1.frac_()

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor1.frac_()

    assert np.allclose(torch_tensor1.numpy(), ms_tensor1.numpy())
    assert torch_tensor1.numpy().dtype == ms_tensor1.numpy().dtype

def test_gcd():
    np_array1 = np.random.randint(10, size=(2,3,4))
    np_array2 = np.random.randint(10, size=(4))

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_out1 = torch_tensor1.gcd(torch_tensor2)
    torch_out2 = torch.tensor([0]).gcd(torch.tensor([0]))

    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_out1 = ms_tensor1.gcd(ms_tensor2)
    ms_out2 = pytorch.tensor([0]).gcd(pytorch.tensor([0]))

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_gcd_():
    np_array1 = np.random.randint(10, size=(2,3,4))
    np_array2 = np.random.randint(10, size=(4))

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    torch_tensor1.gcd_(torch_tensor2)
    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)
    ms_tensor1.gcd_(ms_tensor2)

    assert np.allclose(torch_tensor1.numpy(), ms_tensor1.numpy())
    assert torch_tensor1.numpy().dtype == ms_tensor1.numpy().dtype

    torch_tensor1.gcd_(torch.tensor([0]))
    ms_tensor1.gcd_(pytorch.tensor([0]))

    assert np.allclose(torch_tensor1.numpy(), ms_tensor1.numpy())
    assert torch_tensor1.numpy().dtype == ms_tensor1.numpy().dtype

def test_imag():
    np_array = np.array([[0.0916+2.5208j, 5.5607+8.1229j, 9.2464+3.1815j],
                         [3.9400+9.4030j, 8.6251+3.6491j, 9.4455+7.3204j]])

    torch_tensor1 = torch.tensor(np_array)
    torch_out1 = torch_tensor1.imag

    ms_tensor1 = pytorch.tensor(np_array)
    ms_out1 = ms_tensor1.imag

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype

def test_ldexp():
    torch_out1 = torch.tensor([1.]).ldexp(torch.tensor([1]))
    torch_out2 = torch.tensor([1.0]).ldexp(torch.tensor([1, 2, 3, 4]))
    ms_out1 = pytorch.tensor([1.]).ldexp(pytorch.tensor([1]))
    ms_out2 = pytorch.tensor([1.0]).ldexp(pytorch.tensor([1, 2, 3, 4]))

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_ldexp_():
    x = np.random.randn(2, 3, 4) * 5
    y = np.random.randint(0, 10, 4)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_x.ldexp_(torch_y)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_x.ldexp_(ms_y)

    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_lerp_():
    start = (np.random.rand(2,3) * 10).astype(np.float32)
    end = (np.random.rand(3) * 10).astype(np.float32)

    torch_start = torch.tensor(start)
    torch_end = torch.tensor(end)
    torch_start.lerp_(torch_end, 3.)

    ms_start = pytorch.tensor(start)
    ms_end = pytorch.tensor(end)
    ms_start.lerp_(ms_end, 3.)

    param_compare(torch_start, ms_start)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="lerp_ currently not support float64 on Ascend")
def test_lerp1_fp64():
    start = np.random.randn(2, 2)
    end = np.random.randn(2)

    torch_start = torch.tensor(start)
    torch_end = torch.tensor(end)
    torch_start.lerp_(torch_end, 5.)

    ms_start = pytorch.tensor(start)
    ms_end = pytorch.tensor(end)
    ms_start.lerp_(ms_end, 5.)

    param_compare(torch_start, ms_start)

def test_mv():
    x = (np.random.randn(2, 2) * 5).astype(np.float32)
    y = np.random.randn(2).astype(np.float32)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out1 = torch_x.mv(torch_y)

    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out1 = ms_x.mv(ms_y)

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="mv currently not support float64 on Ascend")
def test_mv_fp64():
    x = np.random.randn(2, 2)
    y = np.random.randn(2)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out1 = torch_x.mv(torch_y)

    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out1 = ms_x.mv(ms_y)

    param_compare(torch_out1, ms_out1)

def test_geqrf():
    # x = np.random.randn(2, 3, 3) * 5
    x = np.random.randn(3, 3) * 5

    torch_x = torch.tensor(x)
    torch_out1 = torch_x.geqrf()

    ms_x = pytorch.tensor(x)
    ms_out1 = ms_x.geqrf()

    assert np.allclose(torch_out1[0].numpy(), ms_out1[0].numpy())
    assert torch_out1[0].numpy().dtype == ms_out1[0].numpy().dtype
    assert np.allclose(torch_out1[1].numpy(), ms_out1[1].numpy())
    assert torch_out1[1].numpy().dtype == ms_out1[1].numpy().dtype

@SKIP_ENV_CPU(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_logaddexp2():
    x = (np.random.randn(2, 3, 4) * 5).astype(np.float32)
    y = np.random.randn(3, 4).astype(np.float32)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out1 = torch_x.logaddexp2(torch_y)

    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out1 = ms_x.logaddexp2(ms_y)

    param_compare(torch_out1, ms_out1, atol=1e-4, rtol = 1e-04)

@SKIP_ENV_ASCEND(reason="logaddexp2 currently not support float64 on Ascend")
def test_logaddexp2_fp64():
    x = np.random.randn(3, 4)
    y = np.random.randn(3, 4)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_out1 = torch_x.logaddexp2(torch_y)

    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_out1 = ms_x.logaddexp2(ms_y)

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="ascend log1p not support float64 and nan result")
def test_log1p_():
    x = np.random.randn(5)

    torch_x = torch.tensor(x)
    torch_x.log1p_()
    ms_x = pytorch.tensor(x)
    ms_x.log1p_()

    assert np.allclose(torch_x.numpy(), ms_x.numpy(), equal_nan=True)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_ascend_log1p_():
    x = (np.random.rand(5) * 2 - 1).astype(np.float32)

    torch_x = torch.tensor(x)
    torch_x.log1p_()
    ms_x = pytorch.tensor(x)
    ms_x.log1p_()

    assert np.allclose(torch_x.numpy(), ms_x.numpy(), equal_nan=True)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_log2_():
    x = np.random.randn(5).astype(np.float64)

    torch_x = torch.tensor(x)
    torch_x.log2_()
    ms_x = pytorch.tensor(x)
    ms_x.log2_()

    assert np.allclose(torch_x.numpy(), ms_x.numpy(), equal_nan=True)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="nn.cell currently has memcpy problem in graph mode")
def test_lstsq():
    def fun(input_ms, A):
        b = input_ms.lstsq(A)
        return b

    for type1 in (np.float32, np.float64):
        x1 = np.random.randn(3,2).astype(type1)
        A1 = np.random.randn(3,4).astype(type1)
        x2 = np.random.randn(4,7).astype(type1)
        A2 = np.random.randn(4,7).astype(type1)
        torch_a1 = torch.tensor(A1)
        torch_x1 = torch.tensor(x1)
        ms_a1 = pytorch.tensor(A1)
        ms_x1 = pytorch.tensor(x1)
        torch_a2 = torch.tensor(A2)
        torch_x2 = torch.tensor(x2)
        ms_a2 = pytorch.tensor(A2)
        ms_x2 = pytorch.tensor(x2)

        #TODO: lstsq not support return qr as the second result, currently set to zeros
        torch_output1, torch_qr1 = torch_x1.lstsq(torch_a1)
        ms_output1, ms_qr1 = ms_x1.lstsq(ms_a1)
        torch_output2, torch_qr2 = torch_x2.lstsq(torch_a2)
        ms_output2, ms_qr2 = ms_x2.lstsq(ms_a2)
        assert np.allclose(torch_output1.numpy(), ms_output1.numpy(), atol=1e-4)
        assert torch_output1.numpy().shape == ms_output1.numpy().shape
        assert torch_output1.numpy().dtype == ms_output1.numpy().dtype
        assert np.allclose(torch_output2.numpy(), ms_output2.numpy(), atol=1e-4)
        assert torch_output2.numpy().shape == ms_output2.numpy().shape
        assert torch_output2.numpy().dtype == ms_output2.numpy().dtype
        #TODO: cpu use ops.lstsq, which doe not support bprop
        if not is_under_cpu_context():
            grad_test('lstsq', fun, ms_a1, ms_x1)



@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_logical_not_():
    x = np.random.randn(5).astype(np.int32)

    torch_x = torch.tensor(x)
    torch_x.logical_not_()
    ms_x = pytorch.tensor(x)
    ms_x.logical_not_()

    assert np.allclose(torch_x.numpy(), ms_x.numpy(), equal_nan=True)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_logical_and_():
    x = np.random.randn(2, 5).astype(np.int16)
    y = np.random.randn(2, 5).astype(np.float16)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_x.logical_and_(torch_y)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_x.logical_and_(ms_y)

    assert np.allclose(torch_x.numpy(), ms_x.numpy(), equal_nan=True)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_logical_or_():
    x = np.random.randn(2, 5).astype(np.float16)
    y = np.random.randn(2, 5).astype(np.float64)

    torch_x = torch.tensor(x)
    torch_y = torch.tensor(y)
    torch_x.logical_or_(torch_y)
    ms_x = pytorch.tensor(x)
    ms_y = pytorch.tensor(y)
    ms_x.logical_or_(ms_y)

    assert np.allclose(torch_x.numpy(), ms_x.numpy(), equal_nan=True)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

def test_lu_solve():
        lu_array = np.random.randn(2, 4, 4).astype(np.float32)
        b_array = np.random.randn(2, 4, 3).astype(np.float32)
        p_array = np.random.randint(1, 4, size=(2, 4)).astype(np.int32)

        torch_lu = torch.tensor(lu_array)
        torch_b = torch.tensor(b_array)
        torch_pivot = torch.tensor(p_array)

        ms_lu = pytorch.tensor(lu_array)
        ms_b = pytorch.tensor(b_array)
        ms_pivot = pytorch.tensor(p_array)

        torch_out = torch_b.lu_solve(torch_lu, torch_pivot)
        ms_out = ms_b.lu_solve(ms_lu, ms_pivot)
        param_compare(torch_out, ms_out, atol=1e-5)
        @ms.jit
        def lu_solve_test(b, lu, pivot):
            out = b.lu_solve(lu, pivot)
            return out
        ms_out1 = lu_solve_test(ms_b, ms_lu, ms_pivot)
        param_compare(torch_out, ms_out1, atol=1e-5)


@SKIP_ENV_GRAPH_MODE(reason='lu not support on graph mode')
def test_lu():
    #TODO: Currently not support 3-D (*, M, N) input
    for type1 in (np.float32, np.float64):
        np_array1 = np.random.randn(3, 3).astype(type1)
        np_array2 = np.random.randn(6, 6).astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        ms_tensor1 = pytorch.tensor(np_array1)
        torch_tensor2 = torch.tensor(np_array2)
        ms_tensor2 = pytorch.tensor(np_array2)

        torch_lu1, torch_pivot1 = torch_tensor1.lu()
        torch_lu2, torch_pivot2 = torch_tensor2.lu()
        torch_lu3, torch_pivot3, torch_info = torch_tensor1.lu(get_infos=True)
        ms_lu1, ms_pivot1 = ms_tensor1.lu()
        ms_lu2, ms_pivot2 = ms_tensor2.lu()
        ms_lu3, ms_pivot3, ms_info = ms_tensor1.lu(get_infos=True)

        param_compare(torch_lu1, ms_lu1)
        param_compare(torch_lu2, ms_lu2, atol=1e-5)
        param_compare(torch_lu3, ms_lu3)
        param_compare(torch_pivot1, ms_pivot1)
        param_compare(torch_pivot2, ms_pivot2)
        param_compare(torch_pivot3, ms_pivot3)
        assert torch_info == ms_info

@SKIP_ENV_CPU(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_floor_divide():
    a = np.array([4.0, 3.0]).astype(np.int16)
    b = np.array([2.0, 2.0]).astype(np.float16)
    c = np.array([2, 4, -1]).astype(np.int32)
    d = np.array([3, 3, 3]).astype(np.uint8)

    torch_a = torch.tensor(a)
    torch_b = torch.tensor(b)
    torch_c = torch.tensor(c)
    torch_d = torch.tensor(d)
    torch_out1 = torch_a.floor_divide(torch_b)
    torch_out2 = torch_c.floor_divide(torch_d)

    ms_a = pytorch.tensor(a)
    ms_b = pytorch.tensor(b)
    ms_c = pytorch.tensor(c)
    ms_d = pytorch.tensor(d)
    ms_out1 = ms_a.floor_divide(ms_b)
    ms_out2 = ms_c.floor_divide(ms_d)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    if torch.__version__ < '1.13.0':
        assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
        assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_floor_divide_():
    a = np.array([4.0, 3.0]).astype(np.float32)

    torch_a = torch.tensor(a)
    torch_a.floor_divide_(-1.4)

    ms_a = pytorch.tensor(a)
    ms_a.floor_divide_(-1.4)

    param_compare(torch_a, ms_a, atol=1e-4)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="floor_divide_ currently not support float64 on Ascend")
def test_floor_divide_fp64():
    a = np.random.randn(2, 3)

    torch_a = torch.tensor(a)
    torch_a.floor_divide_(2)

    ms_a = pytorch.tensor(a)
    ms_a.floor_divide_(2)

    param_compare(torch_a, ms_a)


@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_expm1_():
    np_array = np.array([0, np.log(2.)])

    torch_tensor = torch.tensor(np_array)
    torch_tensor.expm1_()
    ms_tensor = pytorch.tensor(np_array)
    ms_tensor.expm1_()

    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype
    assert ms_tensor.asnumpy().shape == torch_tensor.numpy().shape

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_float_power_():
    a = np.random.randint(10, size=(4,))
    b = np.arange(1, 5)
    exp = np.array([2, -3, 4, -5])

    torch_a = torch.tensor(a).double()
    torch_b = torch.tensor(b).double()
    torch_exp = torch.tensor(exp)
    torch_a.float_power_(2)
    torch_b.float_power_(torch_exp)

    ms_a = pytorch.tensor(a).double()
    ms_b = pytorch.tensor(b).double()
    ms_exp = pytorch.tensor(exp)
    ms_a.float_power_(2)
    ms_b.float_power_(ms_exp)

    assert np.allclose(ms_a.asnumpy(), torch_a.numpy())
    assert ms_a.asnumpy().dtype == torch_a.numpy().dtype
    assert np.allclose(ms_b.asnumpy(), torch_b.numpy())
    assert ms_b.asnumpy().dtype == torch_b.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_hypot_():
    x1 = np.random.randn(2, 4).astype(np.float64)
    x2 = np.random.randn(4,).astype(np.float64)

    torch_tensor = torch.tensor(x1)
    torch_tensor2 = torch.tensor(x2)
    torch_tensor.hypot_(torch_tensor2)

    ms_tensor = pytorch.tensor(x1)
    ms_tensor2 = pytorch.tensor(x2)
    ms_tensor.hypot_(ms_tensor2)

    assert np.allclose(ms_tensor.asnumpy(), torch_tensor.numpy())
    assert ms_tensor.asnumpy().dtype == torch_tensor.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_square_():
    a = np.random.randn(4)

    torch_a = torch.tensor(a).double()
    torch_a.square_()
    ms_a = pytorch.tensor(a).double()
    ms_a.square_()

    assert np.allclose(torch_a.numpy(), ms_a.numpy())
    assert torch_a.numpy().dtype == ms_a.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_logical_xor_():
    torch_a = torch.tensor([0, 1, 10, 0], dtype=torch.int32)
    torch_b = torch.tensor([4, 0, 1, 0], dtype=torch.int32)
    torch_a.logical_xor_(torch_b)

    ms_a = pytorch.tensor([0, 1, 10, 0], dtype=pytorch.int32)
    ms_b = pytorch.tensor([4, 0, 1, 0], dtype=pytorch.int32)
    ms_a.logical_xor_(ms_b)

    assert np.allclose(torch_a.numpy(), ms_a.numpy())
    assert torch_a.numpy().dtype == ms_a.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_lgamma_():
    np_array1 = np.arange(0.5, 2, 0.5).astype(np.float64)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor1.lgamma_()
    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor1.lgamma_()

    assert np.allclose(torch_tensor1.numpy(), ms_tensor1.numpy())
    assert torch_tensor1.numpy().dtype == ms_tensor1.numpy().dtype

def test_qr():
    np_array = np.random.randn(4,8).astype(np.float32)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)
    torch_q1, torch_r1 = torch_tensor.qr()
    ms_q1, ms_r1 = ms_tensor.qr()
    torch_q2, torch_r2 = torch_tensor.qr(some=False)
    ms_q2, ms_r2 = ms_tensor.qr(some=False)
    param_compare(torch_q1, ms_q1, atol=1e-6)
    param_compare(torch_q2, ms_q2, atol=1e-6)
    param_compare(torch_r1, ms_r1, atol=1e-6)
    param_compare(torch_r2, ms_r2, atol=1e-6)

def test_renorm():
    np_array = (np.random.randn(2, 3) * 5).astype(np.float32)

    torch_x = torch.tensor(np_array)
    torch_out1 = torch.renorm(torch_x, 2., 1, 10.)
    ms_x = pytorch.tensor(np_array)
    ms_out1 = pytorch.renorm(ms_x, 2., 1, 10.)

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_ASCEND(reason="baddbmm currently not support float64 on Ascend")
def test_renorm_fp64():
    np_array = (np.random.randn(2, 3) * 5)

    torch_x = torch.tensor(np_array)
    torch_out1 = torch.renorm(torch_x, 3., 1, 10.)
    ms_x = pytorch.tensor(np_array)
    ms_out1 = pytorch.renorm(ms_x, 3., 1, 10.)

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_renorm_():
    np_array = (np.random.randn(2, 3) * 5).astype(np.float32)

    torch_x = torch.tensor(np_array)
    torch_x.renorm_(1., 0, 10)
    ms_x = pytorch.tensor(np_array)
    ms_x.renorm_(1., 0, 10)

    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

def test_round():
    x1 = (4.7, -2.3, 9.1, -7.7)
    x3 = [0.1234567]

    torch_x1 = torch.tensor(x1)
    torch_x3 = torch.tensor(x3)
    torch_out1 = torch_x1.round()
    torch_out2 = torch_x3.round(decimals=3)

    ms_x1 = pytorch.tensor(x1)
    ms_x3 = pytorch.tensor(x3)
    ms_out1 = ms_x1.round()
    ms_out2 = ms_x3.round(decimals=3)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_round_():
    x2 = [-0.5, 0.5, 1.5, 2.5]
    x4 = [1200.1234567]

    torch_x2 = torch.tensor(x2)
    torch_x4 = torch.tensor(x4)
    torch_x2.round_()
    torch_x4.round_(decimals=-3)

    ms_x2 = pytorch.tensor(x2)
    ms_x4 = pytorch.tensor(x4)
    ms_x2.round_()
    ms_x4.round_(decimals=-3)

    assert np.allclose(torch_x2.numpy(), ms_x2.numpy())
    assert torch_x2.numpy().dtype == ms_x2.numpy().dtype
    assert np.allclose(torch_x4.numpy(), ms_x4.numpy())
    assert torch_x4.numpy().dtype == ms_x4.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_floor_():
    x = (np.random.randn(4) * 5).astype(np.float32)

    torch_x = torch.tensor(x)
    torch_x.floor_()
    ms_x = pytorch.tensor(x)
    ms_x.floor_()

    param_compare(torch_x, ms_x)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="floor_ currently not support float64 on Ascend")
def test_floor_fp64():
    x = np.random.randn(2, 3) * 5

    torch_x = torch.tensor(x)
    torch_x.floor_()
    ms_x = pytorch.tensor(x)
    ms_x.floor_()

    param_compare(torch_x, ms_x)

def test_mvlgamma():
    x = np.random.uniform(1, 2, size=(2,3))

    torch_x = torch.tensor(x)
    torch_out = torch.mvlgamma(torch_x, 2)
    ms_x = pytorch.tensor(x)
    ms_out = pytorch.mvlgamma(ms_x, 2)

    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_mvlgamma_():
    p = 3
    x = np.random.rand(4, 3) + (p-1)/2

    torch_x = torch.tensor(x)
    torch_x.mvlgamma_(p)
    ms_x = pytorch.tensor(x)
    ms_x.mvlgamma_(p)

    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

def test_orgqr():
    h = np.random.randn(4, 3, 2).astype(np.complex64)
    tau = np.random.randn(4, 2).astype(np.complex64)

    torch_h = torch.tensor(h)
    torch_tau = torch.tensor(tau)
    torch_out1 = torch_h.orgqr(torch_tau)

    ms_h = pytorch.tensor(h)
    ms_tau = pytorch.tensor(tau)
    ms_out1 = ms_h.orgqr(ms_tau)

    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_random_():
    input = np.array([[1.0, 1.0],[1.0,1.0]]).astype(np.float64)
    py_tensor = torch.tensor(input)
    py_tensor.random_(1, 10)

    ms_tensor = pytorch.tensor(input)
    ms.set_seed(2)
    ms_tensor.random_(1, 10)
    assert not np.any((ms_tensor.numpy() < 1) | (ms_tensor.numpy() > 9))
    ms_out1 = ms_tensor.clone()

    ms.set_seed(2)
    ms_tensor.random_(from_alias=1, to=10)
    assert not np.any((ms_tensor.numpy() < 1) | (ms_tensor.numpy() > 9))
    ms_out2 = ms_tensor.clone()
    ms_tensor.random_(from_alias=1, to=10)
    assert not np.any((ms_tensor.numpy() < 1) | (ms_tensor.numpy() > 9))
    ms_out3 = ms_tensor.clone()

    assert ms_tensor.asnumpy().dtype == py_tensor.numpy().dtype
    assert ms_tensor.asnumpy().shape == py_tensor.numpy().shape
    assert np.allclose(ms_out1.numpy(), ms_out2.numpy())
    assert not np.allclose(ms_out2.numpy(), ms_out3.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_random_range():
    input = np.random.randn(10)
    py_tensor = torch.tensor(input)
    ms_tensor = pytorch.tensor(input)

    py_tensor.random_()
    ms_tensor.random_()
    assert not np.any((ms_tensor.numpy() < 0) | (ms_tensor.numpy() > FP64_MAX))
    type_shape_compare(py_tensor, ms_tensor)
    py_tensor.random_(5, 10)
    ms_tensor.random_(5, 10)
    assert not np.any((ms_tensor.numpy() < 5) | (ms_tensor.numpy() > 9))
    type_shape_compare(py_tensor, ms_tensor)
    py_tensor.random_(to=5)
    ms_tensor.random_(to=5)
    assert not np.any((ms_tensor.numpy() < 0) | (ms_tensor.numpy() > 4))
    type_shape_compare(py_tensor, ms_tensor)

def test_bernoulli():
    a = pytorch.empty(3, 3).uniform_adapter(0, 1)  # generate a uniform random matrix with range [0, 1]
    assert a.bernoulli().shape == (3, 3)

    a = pytorch.ones(3, 3) # probability of drawing "1" is 1
    b = torch.tensor(a.numpy())
    assert np.allclose(a.bernoulli().numpy(), pytorch.ones_like(a).numpy())
    assert np.allclose(pytorch.bernoulli(a).numpy(), torch.bernoulli(b).numpy())

    a = pytorch.zeros(3, 3)
    b = torch.tensor(a.numpy())
    assert np.allclose(a.bernoulli().numpy(), pytorch.zeros_like(a).numpy()) # probability of drawing "1" is 0
    assert np.allclose(pytorch.bernoulli(a).numpy(), torch.bernoulli(b).numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_bernoulli_():
    input = np.random.randn(3, 3).astype(np.float64)
    torch_tensor = torch.tensor(input)
    ms_tensor = pytorch.tensor(input)

    torch_tensor.bernoulli_(torch.empty(3, 3).uniform_(0, 1))
    ms.set_seed(2)
    ms_tensor.bernoulli_(pytorch.empty(3, 3).uniform_(0, 1))
    ms_out1 = ms_tensor.clone()
    ms.set_seed(2)
    ms_tensor.bernoulli_(pytorch.empty(3, 3).uniform_(0, 1))
    ms_out2 = ms_tensor.clone()
    assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
    assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
    assert np.allclose(ms_out1.numpy(), ms_out2.numpy())

    torch_tensor.bernoulli_(p=torch.ones(3, 3))
    ms_tensor.bernoulli_(p=pytorch.ones(3, 3))
    assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
    assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
    assert np.allclose(torch_tensor.numpy(), ms_tensor.numpy())

    torch_tensor.bernoulli_(p=0)
    ms_tensor.bernoulli_(p=0)
    assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
    assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
    assert np.allclose(torch_tensor.numpy(), ms_tensor.numpy())

def test_i0():
    for type1 in (np.float32, np.float64, np.int32, np.int64):
        np_array = np.random.rand(2, 3, 4, 5).astype(type1)
        np_array2 = np.arange(12).reshape(3, 4) - 6

        torch_tensor = torch.tensor(np_array)
        torch_tensor2 = torch.tensor(np_array2)
        torch_out = torch_tensor.i0()
        torch_out2 = torch_tensor2.i0()

        ms_tensor = pytorch.tensor(np_array)
        ms_tensor2 = pytorch.tensor(np_array2)
        ms_out = ms_tensor.i0()
        ms_out2 = ms_tensor2.i0()

        param_compare(torch_out, ms_out)
        param_compare(torch_out2, ms_out2)

def test_matrix_power():
    np_array = np.random.rand(4, 4, 4)
    for type1 in (np.float64, np.float32):
        np_array1 = np_array.astype(type1)
        torch_tensor1 = torch.tensor(np_array1)
        ms_tensor1 = pytorch.tensor(np_array1)
        torch_out1 = torch_tensor1.matrix_power(0)
        torch_out2 = torch_tensor1.matrix_power(3)
        ms_out1 = ms_tensor1.matrix_power(0)
        ms_out2 = ms_tensor1.matrix_power(3)
        #TODO: GPU currently not support n < 0
        if not is_test_under_gpu_context():
            torch_out3 = torch_tensor1.matrix_power(-3)
            ms_out3 = ms_tensor1.matrix_power(-3)
            param_compare(ms_out3, torch_out3, rtol=1e-3, atol=1e-4)
        param_compare(ms_out1, torch_out1)
        param_compare(ms_out2, torch_out2)

@SKIP_ENV_ASCEND(reason="Currently not support Eigh on Ascend")
def test_symeig():
    def fun(input_ms):
        b = input_ms.symeig()
        return b
    np_array = np.random.randn(5, 5)
    torch_tensor1 = torch.tensor(np_array)
    torch_tensor = torch_tensor1 + torch_tensor1.t()
    ms_tensor1 = pytorch.tensor(np_array)
    ms_tensor = ms_tensor1 + ms_tensor1.t()

    torch_val1, _ = torch_tensor.symeig()
    torch_val2, torch_vec2 = torch_tensor.symeig(eigenvectors=True)
    torch_val3, _ = torch_tensor.symeig(upper=False)

    with graph_lax_level():
        ms_val1, _ = ms_tensor.symeig()
        ms_val2, ms_vec2 = ms_tensor.symeig(eigenvectors=True)
        ms_val3, _ = ms_tensor.symeig(upper=False)

    param_compare(torch_val1, ms_val1)
    param_compare(torch_val2, ms_val2)
    param_compare(torch_val3, ms_val3)
    param_compare(torch_vec2.abs(), ms_vec2.abs())

    #TODO: mindspore has problem supporting numpy trans to ms.Tensor
    '''
    grad_test('symeig', fun, ms_tensor)
    '''


@SKIP_ENV_GRAPH_MODE(reason="graph mode cannot support collections.namedtuple.")
@SKIP_ENV_ASCEND(reason="Currently not support Eigh on Ascend")
def test_symeig_namedtuple():
    np_array = np.random.randn(5, 5)
    torch_tensor1 = torch.tensor(np_array)
    torch_tensor = torch_tensor1 + torch_tensor1.t()
    ms_tensor1 = pytorch.tensor(np_array)
    ms_tensor = ms_tensor1 + ms_tensor1.t()

    torch_val = torch_tensor.symeig(eigenvectors=True).eigenvalues
    torch_vec = torch_tensor.symeig(eigenvectors=True).eigenvectors
    with graph_lax_level():
        ms_val = ms_tensor.symeig(eigenvectors=True).eigenvalues
        ms_vec = ms_tensor.symeig(eigenvectors=True).eigenvectors

    param_compare(torch_val, ms_val)
    param_compare(torch_vec.abs(), ms_vec.abs())

def test_index_add():
    x = np.ones((5, 3), dtype=np.float32)
    t = np.arange(15).reshape(5,3).astype(np.float32)
    index = np.array([4, 4, 0, 3, 1])

    torch_x = torch.tensor(x)
    torch_t = torch.tensor(t)
    torch_index = torch.tensor(index)
    torch_out1 = torch.index_add(torch_x, 0, torch_index, torch_t)
    torch_out2 = torch.index_add(torch_x, 0, torch_index, torch_t, alpha=-1)

    ms_x = pytorch.tensor(x)
    ms_t = pytorch.tensor(t)
    ms_index = pytorch.tensor(index)
    ms_out1 = pytorch.index_add(ms_x, 0, ms_index, ms_t)
    ms_out2 = pytorch.index_add(ms_x, 0, ms_index, ms_t, alpha=-1)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason="index_add currently not support float64 on Ascend")
def test_index_add_fp64():
    x = np.ones((3, 3), dtype=np.float64)
    t = np.arange(9).reshape(3,3).astype(np.float64)
    index = np.array([0, 2, 1])

    torch_x = torch.tensor(x)
    torch_t = torch.tensor(t)
    torch_index = torch.tensor(index)
    torch_out1 = torch.index_add(torch_x, 0, torch_index, torch_t)

    ms_x = pytorch.tensor(x)
    ms_t = pytorch.tensor(t)
    ms_index = pytorch.tensor(index)
    ms_out1 = pytorch.index_add(ms_x, 0, ms_index, ms_t)

    param_compare(torch_out1, ms_out1)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_index_add_():
    x = np.ones((5, 3), dtype=np.int32)
    t = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int32)
    index = np.array([0, 4, 2])

    torch_x = torch.tensor(x)
    torch_t = torch.tensor(t)
    torch_index = torch.tensor(index)
    ms_x = pytorch.tensor(x)
    ms_t = pytorch.tensor(t)
    ms_index = pytorch.tensor(index)

    ms_x.index_add_(0, ms_index, ms_t)
    torch_x.index_add_(0, torch_index, torch_t)
    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

    ms_x.index_add_(0, ms_index, ms_t, alpha=-1)
    torch_x.index_add_(0, torch_index, torch_t, alpha=-1)
    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

def test_scatter_add():
    np_src = np.random.randn(5).astype(np.float32) * 5
    np_index = np.random.randint(0, 4, (5))
    np_input = np.array([1., 2., 3., 4.]).astype(np.float32)

    torch_src = torch.tensor(np_src)
    torch_index = torch.tensor(np_index)
    torch_input = torch.tensor(np_input)

    ms_src = pytorch.tensor(np_src)
    ms_index = pytorch.tensor(np_index)
    ms_input = pytorch.tensor(np_input)

    torch_out0 = torch_input.scatter_add(0, torch_index, torch_src)
    ms_out0 = ms_input.scatter_add(0, ms_index, ms_src)

    param_compare(ms_out0, torch_out0)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_scatter_add_():
    np_src = np.random.randn(1, 5).astype(np.float32) * 5
    np_index = np.random.randint(0, 2, (1, 5))
    np_input = np.array([[1., 2., 3., 4.], [1., 2., 3., 4.]]).astype(np.float32)

    torch_src = torch.tensor(np_src)
    torch_index = torch.tensor(np_index)
    torch_input = torch.tensor(np_input)

    ms_src = pytorch.tensor(np_src)
    ms_index = pytorch.tensor(np_index)
    ms_input = pytorch.tensor(np_input)

    torch_input.scatter_add_(1, torch_index, torch_src)
    ms_input.scatter_add_(1, ms_index, ms_src)
    param_compare(ms_input, torch_input)

def test_index_copy():
    x = np.zeros((5, 3)).astype(np.float32)
    t = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float32)
    index = np.array([0, 4, 2])

    torch_x = torch.tensor(x)
    torch_t = torch.tensor(t)
    torch_index = torch.tensor(index)
    torch_out = torch_x.index_copy(0, torch_index, torch_t)

    ms_x = pytorch.tensor(x)
    ms_t = pytorch.tensor(t)
    ms_index = pytorch.tensor(index)
    ms_out = ms_x.index_copy(0, ms_index, ms_t)

    param_compare(ms_out, torch_out)
    # test if adapter wrongly uses in-place operation
    assert np.allclose(torch_x.numpy(), ms_x.numpy())

@SKIP_ENV_ASCEND(reason="index_copy currently not support float64 on Ascend")
def test_index_copy_fp64():
    x = np.zeros((5, 3))
    t = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float64)
    index = np.array([0, 4, 2])

    torch_x = torch.tensor(x)
    torch_t = torch.tensor(t)
    torch_index = torch.tensor(index)
    torch_out = torch_x.index_copy(0, torch_index, torch_t)

    ms_x = pytorch.tensor(x)
    ms_t = pytorch.tensor(t)
    ms_index = pytorch.tensor(index)
    ms_out = ms_x.index_copy(0, ms_index, ms_t)

    param_compare(ms_out, torch_out)
    # test if adapter wrongly uses in-place operation
    assert np.allclose(torch_x.numpy(), ms_x.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_index_copy_():
    x = np.ones((3, 4, 5)).astype(np.float32)
    index = np.array([0, 4, 1])
    source = np.arange(36).reshape(3,4,3).astype(np.float32)

    torch_x = torch.tensor(x)
    torch_source = torch.tensor(source)
    torch_index = torch.tensor(index)
    torch_x.index_copy_(2, torch_index, torch_source)

    ms_x = pytorch.tensor(x)
    ms_source = pytorch.tensor(source)
    ms_index = pytorch.tensor(index)
    ms_x.index_copy_(2, ms_index, ms_source)

    assert torch_x.numpy().dtype == ms_x.numpy().dtype
    assert np.allclose(torch_x.numpy(), ms_x.numpy())

def test_diag_embed():
    input = np.random.randn(2, 3)
    torch_tensor = torch.tensor(input)
    ms_tensor = pytorch.tensor(input)
    torch_out1 = torch_tensor.diag_embed()
    ms_out1 = ms_tensor.diag_embed()
    torch_out2 = torch_tensor.diag_embed(offset=1, dim1=0, dim2=2)
    ms_out2 = ms_tensor.diag_embed(offset=1, dim1=0, dim2=2)

    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)


def test_resolve_neg():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_out = torch_tensor.imag
    torch_out1 = torch_out.resolve_neg()
    ms_out = ms_tensor.imag
    ms_out1 = ms_out.resolve_neg()

    assert np.allclose(torch_out1.resolve_neg().numpy(), ms_out1.numpy())
    assert ms_out1.is_neg() == torch_out1.is_neg()

@SKIP_ENV_GRAPH_MODE("graph mode not support assigning attr to tensor")
@SKIP_ENV_PYNATIVE_MODE("ms.jit forced to use graph mode, which not support assigning attr to tensor")
def test_resolve_neg_jit():
    x = np.array([-1 + 1j, -2 + 2j, 3 - 3j])
    torch_tensor = torch.tensor(x)
    ms_tensor = pytorch.tensor(x)
    torch_out = torch_tensor.imag
    torch_out1 = torch_out.resolve_neg()

    @ms.jit
    def neg_func(ms_tensor):
        ms_out = ms_tensor.imag
        ms_out1 = ms_out.resolve_neg()
        return ms_out1

    ms_out1 = neg_func(ms_tensor)
    assert np.allclose(torch_out1.resolve_neg().numpy(), ms_out1.numpy())
    assert ms_out1.is_neg() == torch_out1.is_neg()

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_i0_():
    np_array = np.random.rand(2, 3, 4, 5).astype(np.float32)
    np_array2 = (np.arange(12).reshape(3, 4) - 6).astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor = pytorch.tensor(np_array)
    ms_tensor2 = pytorch.tensor(np_array2)
    torch_tensor.i0_()
    torch_tensor2.i0_()
    ms_tensor.i0_()
    ms_tensor2.i0_()

    param_compare(torch_tensor, ms_tensor)
    param_compare(torch_tensor2, ms_tensor2)

@SKIP_ENV_GRAPH_MODE(reason="inpalce operation only support on pynative mode")
def test_logit_():
    np_array = np.random.randn(120).reshape(4, 6, 5) * 3 - 1
    np_array = np_array.astype(np.float32)

    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)

    torch_tensor.logit_(0.001)
    ms_tensor.logit_(0.001)
    param_compare(torch_tensor, ms_tensor, equal_nan=True)

    torch_tensor.logit_(0.4)
    ms_tensor.logit_(0.4)
    param_compare(torch_tensor, ms_tensor, equal_nan=True)

    torch_tensor.logit_()
    ms_tensor.logit_()
    param_compare(torch_tensor, ms_tensor, equal_nan=True)

    torch_tensor.logit_(-0.8)
    ms_tensor.logit_(-0.8)
    param_compare(torch_tensor, ms_tensor, equal_nan=True)

def test_nan_to_num():
    torch_x = torch.tensor([float('nan'), float('inf'), -float('inf'), 3.14])
    ms_x = pytorch.tensor([float('nan'), float('inf'), -float('inf'), 3.14])

    torch_out1 = torch_x.nan_to_num()
    torch_out2 = torch_x.nan_to_num(nan=2.0)
    torch_out3 = torch_x.nan_to_num(nan=2.0, posinf=1.0)

    ms_out1 = ms_x.nan_to_num()
    ms_out2 = ms_x.nan_to_num(nan=2.0)
    ms_out3 = ms_x.nan_to_num(nan=2.0, posinf=1.0)

    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out3.numpy().dtype == ms_out3.numpy().dtype
    assert np.allclose(torch_out3.numpy(), ms_out3.numpy())

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason='nan_to_num does not support float64 input on Ascend')
def test_nan_to_num_float64():
    torch_x = torch.tensor([float('nan'), float('inf'), -float('inf'), 3.14], dtype=torch.float64)
    ms_x = pytorch.tensor([float('nan'), float('inf'), -float('inf'), 3.14], dtype=pytorch.float64)

    torch_x.nan_to_num_()
    ms_x.nan_to_num_()
    assert torch_x.numpy().dtype == ms_x.numpy().dtype
    assert np.allclose(torch_x.numpy(), ms_x.numpy())

    torch_x.nan_to_num_(nan=-2.0)
    ms_x.nan_to_num_(nan=-2.0)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype
    assert np.allclose(torch_x.numpy(), ms_x.numpy())

    torch_x.nan_to_num_(nan=-2.0, posinf=1.0)
    ms_x.nan_to_num_(nan=-2.0, posinf=1.0)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype
    assert np.allclose(torch_x.numpy(), ms_x.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_nan_to_num_():
    torch_x = torch.tensor([float('nan'), float('inf'), -float('inf'), 3.14], dtype=torch.float16)
    ms_x = pytorch.tensor([float('nan'), float('inf'), -float('inf'), 3.14], dtype=pytorch.float16)

    torch_x.nan_to_num_(nan=-2.0, neginf=2.0, posinf=1.0)
    ms_x.nan_to_num_(nan=-2.0, neginf=2.0, posinf=1.0)
    assert torch_x.numpy().dtype == ms_x.numpy().dtype
    assert np.allclose(torch_x.numpy(), ms_x.numpy())

def test_index_put():
    x = np.arange(24).reshape(6, 4)
    index_x = np.random.randint(0, 6, (5))
    index_y = np.random.randint(0, 4, (5))
    values = np.arange(5)

    torch_x = torch.tensor(x)
    torch_index = (torch.tensor(index_x), torch.tensor(index_y))
    torch_values = torch.tensor(values)

    ms_x = pytorch.tensor(x)
    ms_index = (pytorch.tensor(index_x), pytorch.tensor(index_y))
    ms_values = pytorch.tensor(values)

    torch_out = torch_x.index_put(torch_index, torch_values, accumulate=True)
    ms_out = ms_x.index_put(ms_index, ms_values, accumulate=True)
    assert np.allclose(torch_out.numpy(), ms_out.numpy())
    assert torch_out.numpy().dtype == ms_out.numpy().dtype

    torch_out2 = torch_x.index_put(torch_index, torch_values, accumulate=False)
    ms_out2 = ms_x.index_put(ms_index, ms_values, accumulate=False)
    assert np.allclose(torch_out2.numpy(), ms_out2.numpy())
    assert torch_out2.numpy().dtype == ms_out2.numpy().dtype

def test_index_put_empty_indices():
    # indices contain only 1D emtpy tensor
    torch_input = torch.tensor([[1,2,3],[4,5,6]])
    torch_index = (torch.tensor([], dtype=torch.int64),)
    torch_values = torch.tensor([-100], dtype=torch.int64)
    torch_out = torch_input.index_put(torch_index, torch_values)

    ms_input = pytorch.tensor([[1,2,3],[4,5,6]])
    ms_index = (pytorch.tensor([], dtype=ms.int64),)
    ms_values = pytorch.tensor([-100], dtype=ms.int64)
    ms_out = ms_input.index_put(ms_index, ms_values)

    param_compare(torch_out, ms_out)

    torch_out2 = torch_input.index_put(torch_index, torch_values, accumulate=True)
    ms_out2 = ms_input.index_put(ms_index, ms_values, accumulate=True)

    param_compare(torch_out2, ms_out2)

    # TODO: uncomment the test below after CI updated
    # indices contain only non-empty tensor and higher-dim empty tensor
    # torch_index3 = (torch.tensor([[0]], dtype=torch.int64),torch.full((1,1,1,0),1, dtype=torch.int64))
    # ms_index3 = (pytorch.tensor([[1]], dtype=pytorch.int64),pytorch.full((1,1,1,0),1, dtype=pytorch.int64))
    # torch_out3 = torch_input.index_put(torch_index3, torch_values, accumulate=True)
    # ms_out3 = ms_input.index_put(ms_index3, ms_values, accumulate=True)
    # param_compare(torch_out3, ms_out3)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_index_put2():
    torch_x = torch.range(1, 12).long().reshape(2, 2, 3)
    torch_index = (torch.tensor([1, 1, 0]), torch.tensor([0, 0, 0]))
    torch_values = torch.tensor([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])

    ms_x = pytorch.range(1, 12).long().reshape(2, 2, 3)
    ms_index = (pytorch.tensor([1, 1, 0]), pytorch.tensor([0, 0, 0]))
    ms_values = pytorch.tensor([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])

    torch_x.index_put_(torch_index, torch_values, accumulate=True)
    ms_x.index_put_(ms_index, ms_values, accumulate=True)
    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="index_put(): ScatterNdAdd has bug on Ascend")
def test_index_put_():
    torch_x = torch.range(1., 12.).reshape(2, 2, 3)
    torch_index = (torch.tensor([1, 1, 0]), torch.tensor([0, 0, 0]), torch.tensor([2, 2, 1]))
    torch_values = torch.tensor([-1., -2., -3.])

    ms_x = pytorch.range(1., 12.).reshape(2, 2, 3)
    ms_index = (pytorch.tensor([1, 1, 0]), pytorch.tensor([0, 0, 0]), pytorch.tensor([2, 2, 1]))
    ms_values = pytorch.tensor([-1., -2., -3.])

    torch_x.index_put_(torch_index, torch_values, accumulate=True)
    ms_x.index_put_(ms_index, ms_values, accumulate=True)
    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

    torch_x.index_put_(torch_index, torch_values, accumulate=False)
    ms_x.index_put_(ms_index, ms_values, accumulate=False)
    assert np.allclose(torch_x.numpy(), ms_x.numpy())
    assert torch_x.numpy().dtype == ms_x.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_put_int_():
    # source and input type int64
    src = np.array([[4, 3, 5], [6, 7, 8]])
    torch_src = torch.tensor(src)
    ms_src = pytorch.tensor(src)

    torch_src.put_(torch.tensor([1, 3]), torch.tensor([9, 10]))
    ms_src.put_(pytorch.tensor([1, 3]), pytorch.tensor([9, 10]))
    assert np.allclose(torch_src.numpy(), ms_src.numpy())
    assert torch_src.numpy().dtype == ms_src.numpy().dtype

def test_put_float():
    # source and input type float32
    src = np.arange(24).reshape(2, 3, 4).astype(np.float32)
    torch_src = torch.tensor(src)
    ms_src = pytorch.tensor(src)

    torch_src.put_(torch.tensor([0, 10, 10]), torch.tensor([3., 4., 5.]), accumulate=True)
    ms_src.put_(pytorch.tensor([0, 10, 10]), pytorch.tensor([3., 4., 5.]), accumulate=True)
    assert np.allclose(torch_src.numpy(), ms_src.numpy())
    assert torch_src.numpy().dtype == ms_src.numpy().dtype

    # source and index of different shapes
    torch_src.put_(torch.tensor([[2], [5], [15]]), torch.tensor([-9., -10., -1.]), accumulate=True)
    ms_src.put_(pytorch.tensor([[2], [5], [15]]), pytorch.tensor([-9., -10., -1.]), accumulate=True)
    assert np.allclose(torch_src.numpy(), ms_src.numpy())
    assert torch_src.numpy().dtype == ms_src.numpy().dtype

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_nextafter_():
    #TODO: On CPU when dtype is float32, the result of inf, -inf, 0, -0 is different with pytorch
    np_array1 = np.array([np.nan, np.inf, -np.inf, 3, 0, -0]).astype(np.float64)
    np_other = np.array([1, 2, 3, 3, -5, 6]).astype(np.float64)

    torch_tensor1 = torch.tensor(np_array1)
    torch_other = torch.tensor(np_other)
    ms_tensor1 = pytorch.tensor(np_array1)
    ms_other = pytorch.tensor(np_other)

    torch_tensor1.nextafter_(torch_other)
    ms_tensor1.nextafter_(ms_other)

    param_compare(torch_tensor1, ms_tensor1, equal_nan=True)

def test_kthvalue():
    np_array1 = np.random.randn(8)
    np_array3 = np_array1.reshape(2, 2, 2)
    np_array4 = np.array([1, 2, 2, 2, 3, 4, 5, 6, 7]).reshape(3, 3)
    torch_tensor3 = torch.tensor(np_array3)
    torch_tensor4 = torch.tensor(np_array4)
    ms_tensor3 = pytorch.tensor(np_array3)
    ms_tensor4 = pytorch.tensor(np_array4)

    torch_val1, torch_indice1 = torch_tensor3.kthvalue(1)
    torch_val2, torch_indice2 = torch_tensor3.kthvalue(1, 0, True)
    torch_val3, torch_indice3 = torch_tensor3.kthvalue(2, 0)
    torch_val4, torch_indice4 = torch_tensor3.kthvalue(1, 1, True)
    torch_val5, torch_indice5 = torch_tensor3.kthvalue(1, 1)
    torch_val6, torch_indice6 = torch_tensor4.kthvalue(2)

    ms_val1, ms_indice1 = ms_tensor3.kthvalue(1)
    ms_val2, ms_indice2 = ms_tensor3.kthvalue(1, 0, True)
    ms_val3, ms_indice3 = ms_tensor3.kthvalue(2, 0)
    ms_val4, ms_indice4 = ms_tensor3.kthvalue(1, 1, True)
    ms_val5, ms_indice5 = ms_tensor3.kthvalue(1, 1)
    ms_val6, ms_indice6 = ms_tensor4.kthvalue(2)

    if not is_test_under_ascend_context():
        atol = 1e-5
    else:
        atol = 1e-3
    param_compare(torch_val1, ms_val1, atol=atol)
    param_compare(torch_val2, ms_val2, atol=atol)
    param_compare(torch_val3, ms_val3, atol=atol)
    param_compare(torch_val4, ms_val4, atol=atol)
    param_compare(torch_val5, ms_val5, atol=atol)
    param_compare(torch_val6, ms_val6, atol=atol)
    param_compare(torch_indice1, ms_indice1)
    param_compare(torch_indice2, ms_indice2)
    param_compare(torch_indice3, ms_indice3)
    param_compare(torch_indice4, ms_indice4)
    param_compare(torch_indice5, ms_indice5)
    param_compare(torch_indice6, ms_indice6)

@SKIP_ENV_GPU(reason="GPU has a bug with negative inf")
@SKIP_ENV_ASCEND(reason="Ascend has a bug with negative inf")
def test_scatter_reduce_amax():
    torch_input = torch.zeros(3, dtype=torch.float64)
    torch_src = torch.tensor([1, float('nan'), -float('inf'), -float('inf'), 2, float('inf')], dtype=torch.float64)
    torch_idx = torch.tensor([0, 0, 1, 1, 2, 2])
    torch_out = torch_input.scatter_reduce(0, torch_idx, torch_src, 'amax', include_self=False)

    ms_input = pytorch.zeros(3, dtype=pytorch.float64)
    ms_src = pytorch.tensor([1, float('nan'), -float('inf'), -float('inf'), 2, float('inf')], dtype=pytorch.float64)
    ms_idx = pytorch.tensor([0, 0, 1, 1, 2, 2])
    ms_out = ms_input.scatter_reduce(0, ms_idx, ms_src, 'amax', include_self=False)

    param_compare(ms_out, torch_out, equal_nan=True)

@SKIP_ENV_ASCEND(reason='scatter_reduce not support reduction=`prod` with dim>0 on Ascend')
def test_scatter_reduce_prod_nd():
    np_idx = np.random.randint(0, 4, (1, 3, 1))

    torch_input = torch.arange(12).reshape(1, 3, 4)
    torch_idx = torch.tensor(np_idx)
    torch_src = torch.arange(-13, -1).reshape(1, 3, 4).long()
    torch_out = torch.scatter_reduce(torch_input, 2, torch_idx, torch_src, 'prod')

    ms_input = pytorch.arange(12).reshape(1, 3, 4)
    ms_idx = pytorch.tensor(np_idx)
    ms_src = pytorch.arange(-13, -1).reshape(1, 3, 4).long()
    ms_out = pytorch.scatter_reduce(ms_input, 2, ms_idx, ms_src, 'prod')

    param_compare(ms_out, torch_out)

def test_scatter_reduce_amax_nd():
    torch_out = torch.arange(24).reshape(1, 2, 3, 4) \
        .scatter_reduce(3,
                        torch.tensor([[[[0, 1],[0, 2]],[[2, 3],[2, 3]]]]),
                        torch.arange(1000, 1024).reshape(1, 2, 3, 4).long(),
                        'amax')

    ms_out = pytorch.arange(24).reshape(1, 2, 3, 4) \
        .scatter_reduce(3,
                        pytorch.tensor([[[[0, 1],[0, 2]],[[2, 3],[2, 3]]]]),
                        pytorch.arange(1000, 1024).reshape(1, 2, 3, 4).long(),
                        'amax')

    param_compare(ms_out, torch_out)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_scatter_reduce_amin_nd():
    torch_in = torch.arange(1, 145).reshape(2, 3, 4, 3, 2)
    torch_in.scatter_reduce_(3,
                             torch.tensor([[[[0], [2], [2]]]]).expand(2, 3, 4, 3, 2),
                             torch.arange(-144, 0).flip(0).reshape(2, 3, 4, 3, 2).long(),
                             'amin')
    ms_in = pytorch.arange(1, 145).reshape(2, 3, 4, 3, 2)
    ms_in.scatter_reduce_(3,
                          pytorch.tensor([[[[0], [2], [2]]]]).expand(2, 3, 4, 3, 2),
                          pytorch.arange(-144, 0).flip(0).reshape(2, 3, 4, 3, 2).long(),
                          'amin')

    param_compare(ms_in, torch_in)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_scatter_reduce_sum_nd():
    torch_in = torch.arange(1, 145).reshape(2, 3, 4, 3, 2)
    torch_in.scatter_reduce_(3,
                             torch.tensor([[[[0], [2], [2]]]]).expand(2, 3, 4, 3, 2),
                             torch.arange(-144, 0).flip(0).reshape(2, 3, 4, 3, 2).long(),
                             'sum')
    ms_in = pytorch.arange(1, 145).reshape(2, 3, 4, 3, 2)
    ms_in.scatter_reduce_(3,
                          pytorch.tensor([[[[0], [2], [2]]]]).expand(2, 3, 4, 3, 2),
                          pytorch.arange(-144, 0).flip(0).reshape(2, 3, 4, 3, 2).long(),
                          'sum')

    param_compare(ms_in, torch_in)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_exponential_():
    for type1 in (np.float32, np.float16):
        np_array = np.random.rand(1, 3, 4).astype(type1) * 5
        torch_tensor = torch.tensor(np_array)
        ms_tensor = pytorch.tensor(np_array)
        torch_tensor.exponential_()
        ms_tensor.exponential_()
        assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
        assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
        torch_tensor.exponential_(1.5)
        ms_tensor.exponential_(1.5)
        assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
        assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
        np_array3 = np.random.rand(1, 3, 4, 6, 8).astype(type1) * 5
        ms_tensor = pytorch.tensor(np_array3)
        ms.set_seed(10)
        ms_tensor.exponential_()
        ms_tensor1 = ms_tensor
        ms_tensor.exponential_()
        ms_tensor2 = ms_tensor
        ms.set_seed(10)
        ms_tensor.exponential_()
        ms_tensor3 = ms_tensor
        ms_tensor.exponential_()
        ms_tensor4 = ms_tensor
        param_compare(ms_tensor1, ms_tensor3)
        param_compare(ms_tensor2, ms_tensor4)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason='exponential_ does not support float64 input on Ascend')
def test_exponential_fp64():
    np_array = np.random.rand(1, 3, 4).astype(np.float64) * 5
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)
    torch_tensor.exponential_()
    ms_tensor.exponential_()
    assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
    assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
    np_array3 = np.random.rand(1, 3, 4, 6, 8).astype(np.float64) * 5
    ms_tensor = pytorch.tensor(np_array3)
    ms.set_seed(10)
    ms_tensor.exponential_()
    ms_tensor1 = ms_tensor
    ms_tensor.exponential_()
    ms_tensor2 = ms_tensor
    ms.set_seed(10)
    ms_tensor.exponential_()
    ms_tensor3 = ms_tensor
    ms_tensor.exponential_()
    ms_tensor4 = ms_tensor
    param_compare(ms_tensor1, ms_tensor3)
    param_compare(ms_tensor2, ms_tensor4)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
def test_index_reduce_prod():
    torch_x = torch.empty(5, 3).fill_(2)
    torch_t = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=torch.float)
    torch_index = torch.tensor([0, 4, 2, 0])
    torch_x.index_reduce_(0, torch_index, torch_t, 'prod')

    ms_x = pytorch.empty(5, 3).fill_(2)
    ms_t = pytorch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=pytorch.float)
    ms_index = pytorch.tensor([0, 4, 2, 0])
    ms_x.index_reduce_(0, ms_index, ms_t, 'prod')

    param_compare(ms_x, torch_x)

    torch_x = torch.empty(5, 3).fill_(2)
    torch_x.index_reduce_(0, torch_index, torch_t, 'prod', include_self=False)
    ms_x = pytorch.empty(5, 3).fill_(2)
    ms_x.index_reduce_(0, ms_index, ms_t, 'prod', include_self=False)

    param_compare(ms_x, torch_x)

@SKIP_ENV_PYNATIVE_MODE(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_index_reduce_amax():
    torch_in = torch.full((5, 4, 3), 2.)
    ms_in = pytorch.full((5, 4, 3), 2.)

    torch_out = torch_in.index_reduce(1,
                                      torch.tensor([0, 3, 0, 3, 0]),
                                      torch.arange(100.,175.).reshape(5,5,3),
                                      'amax')
    ms_out = ms_in.index_reduce(1,
                                pytorch.tensor([0, 3, 0, 3, 0]),
                                pytorch.arange(100.,175.).reshape(5,5,3),
                                'amax')
    param_compare(ms_out, torch_out)

    torch_out2 = torch_in.index_reduce(1,
                                       torch.tensor([0, 3, 0, 3, 0]),
                                       torch.arange(100.,175.).reshape(5,5,3),
                                       'amax',
                                       include_self=False)
    ms_out2 = ms_in.index_reduce(1,
                                 pytorch.tensor([0, 3, 0, 3, 0]),
                                 pytorch.arange(100.,175.).reshape(5,5,3),
                                 'amax',
                                 include_self=False)
    param_compare(ms_out2, torch_out2)

@SKIP_ENV_PYNATIVE_MODE(reason="[CI] ms2.4.0 0920 still not pass, need to be fixed.")
def test_index_reduce_amin():
    torch_out = torch.full((5, 4, 3), 2.).index_reduce(2,
                                                       torch.tensor([0, 2]),
                                                       torch.arange(-40., 0.).reshape(5, 4, 2),
                                                       'amin')
    ms_out = pytorch.full((5, 4, 3), 2.).index_reduce(2,
                                                      pytorch.tensor([0, 2]),
                                                      pytorch.arange(-40., 0.).reshape(5, 4, 2),
                                                      'amin')

    param_compare(ms_out, torch_out)

    torch_out2 = torch.full((5, 4, 3), 2.).index_reduce(2,
                                                       torch.tensor([0, 2]),
                                                       torch.arange(-40., 0.).reshape(5, 4, 2),
                                                       'amin',
                                                       include_self=False)
    ms_out2 = pytorch.full((5, 4, 3), 2.).index_reduce(2,
                                                      pytorch.tensor([0, 2]),
                                                      pytorch.arange(-40., 0.).reshape(5, 4, 2),
                                                      'amin',
                                                      include_self=False)
    param_compare(ms_out2, torch_out2)

@SKIP_ENV_GPU(reason='masked_scatter is not supported on GPU')
@SKIP_ENV_ASCEND(reason="mindspore.tensor.masked_scatter has some problem.")
def test_masked_scatter():
    np_mask = np.random.randint(0, 2, (3, 4))

    torch_mask = torch.tensor(np_mask)
    torch_source = torch.range(-48, -1).reshape(4, 3, 4)
    torch_input = torch.ones(2, 3, 4)

    ms_mask = pytorch.tensor(np_mask)
    ms_source = pytorch.range(-48, -1).reshape(4, 3, 4)
    ms_input = pytorch.ones(2, 3, 4)

    torch_out = torch_input.masked_scatter(torch_mask, torch_source)
    ms_out = ms_input.masked_scatter(ms_mask, ms_source)

    assert torch_out.numpy().dtype == ms_out.numpy().dtype
    assert np.allclose(torch_out.numpy(), ms_out.numpy())

# TODO: ms.ops.masked_scatter does not support input to be broadcasted to the shape of mask
# @SKIP_ENV_GPU(reason='masked_scatter is not supported on GPU')
# def test_masked_scatter_input_broadcastedto_mask():
#     np_mask = np.random.randint(0, 2, (2, 3, 4))

#     torch_mask = torch.tensor(np_mask)
#     torch_source = torch.range(-48, -1).reshape(4, 3, 4)
#     torch_input = torch.ones(1, 1, 4)

#     ms_mask = pytorch.tensor(np_mask)
#     ms_source = pytorch.range(-48, -1).reshape(4, 3, 4)
#     ms_input = pytorch.ones(1, 1, 4)

#     torch_out = torch_input.masked_scatter(torch_mask, torch_source)
#     ms_out = ms_input.masked_scatter(ms_mask, ms_source)

#     assert torch_out.numpy().dtype == ms_out.numpy().dtype
#     assert np.allclose(torch_out.numpy(), ms_out.numpy())

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_GPU(reason='masked_scatter is not supported on GPU')
@SKIP_ENV_ASCEND(reason="mindspore.tensor.masked_scatter has some problem.")
def test_masked_scatter_():
    np_mask = np.random.randint(0, 2, (4))

    torch_mask = torch.tensor(np_mask)
    torch_source = torch.range(1, 24).reshape(4, 6)
    torch_input = torch.ones(3, 2, 4)

    ms_mask = pytorch.tensor(np_mask)
    ms_source = pytorch.range(1, 24).reshape(4, 6)
    ms_input = pytorch.ones(3, 2, 4)

    torch_input.masked_scatter_(torch_mask, torch_source)
    ms_input.masked_scatter_(ms_mask, ms_source)

    assert torch_input.numpy().dtype == ms_input.numpy().dtype
    assert np.allclose(torch_input.numpy(), ms_input.numpy())

def test_corrcoef():
    torch_out1 = torch.tensor([[0, 1, 2], [2, 1, 0]]).corrcoef()
    ms_out1 = pytorch.tensor([[0, 1, 2], [2, 1, 0]]).corrcoef()
    param_compare(torch_out1, ms_out1)

    x2 = np.random.randn(2, 4).astype(np.float32)

    torch_x2 = torch.tensor(x2)
    torch_out2 = torch_x2.corrcoef()
    torch_out3 = torch_x2[0].corrcoef()
    ms_x2 = pytorch.tensor(x2)
    ms_out2 = ms_x2.corrcoef()
    ms_out3 = ms_x2[0].corrcoef()

    param_compare(torch_out2, ms_out2)
    param_compare(torch_out3, ms_out3)

@SKIP_ENV_ASCEND(reason="corrcoef currently not support float64 on Ascend")
def test_corrcoef_fp64():
    x2 = np.random.randn(2, 4)

    torch_x2 = torch.tensor(x2)
    torch_out2 = torch_x2.corrcoef()
    ms_x2 = pytorch.tensor(x2)
    ms_out2 = ms_x2.corrcoef()

    param_compare(torch_out2, ms_out2)


@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_geometric_():
    for type1 in (np.float32, np.float16):
        np_array = np.random.rand(1, 3, 4).astype(type1) * 5
        torch_tensor = torch.tensor(np_array)
        ms_tensor = pytorch.tensor(np_array)
        torch_tensor.geometric_(0.5)
        ms_tensor.geometric_(0.5)
        assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
        assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
        torch_tensor.geometric_(0.75)
        ms_tensor.geometric_(0.75)
        assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
        assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
        np_array3 = np.random.rand(1, 3, 4, 6, 8).astype(type1) * 5
        ms_tensor = pytorch.tensor(np_array3)
        ms.set_seed(10)
        ms_tensor.geometric_(0.75)
        ms_tensor1 = ms_tensor
        ms_tensor.geometric_(0.75)
        ms_tensor2 = ms_tensor
        ms.set_seed(10)
        ms_tensor.geometric_(0.75)
        ms_tensor3 = ms_tensor
        ms_tensor.geometric_(0.75)
        ms_tensor4 = ms_tensor
        param_compare(ms_tensor1, ms_tensor3)
        param_compare(ms_tensor2, ms_tensor4)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
def test_log_normal_():
    for type1 in (np.float32, np.float16):
        np_array = np.random.rand(1, 3, 4).astype(type1) * 5
        torch_tensor = torch.tensor(np_array)
        ms_tensor = pytorch.tensor(np_array)
        torch_tensor.log_normal_(2.5, 1.5)
        ms_tensor.log_normal_(2.5, 1.5)
        assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
        assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
        torch_tensor.log_normal_(3.0, 2.0)
        ms_tensor.log_normal_(3.0, 2.0)
        assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
        assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
        np_array3 = np.random.rand(1, 3, 4, 6, 8).astype(type1) * 5
        ms_tensor = pytorch.tensor(np_array3)
        ms.set_seed(10)
        ms_tensor.log_normal_(2.5, 1.5)
        ms_tensor1 = ms_tensor
        ms_tensor.log_normal_(2.5, 1.5)
        ms_tensor2 = ms_tensor
        ms.set_seed(10)
        ms_tensor.log_normal_(2.5, 1.5)
        ms_tensor3 = ms_tensor
        ms_tensor.log_normal_(2.5, 1.5)
        ms_tensor4 = ms_tensor
        param_compare(ms_tensor1, ms_tensor3)
        param_compare(ms_tensor2, ms_tensor4)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason='geometric_ does not support float64 input on Ascend')
def test_geometric_fp64():
    np_array = np.random.rand(1, 3, 4).astype(np.float64)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)
    torch_tensor.geometric_(0.5)
    ms_tensor.geometric_(0.5)
    assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
    assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
    np_array3 = np.random.rand(1, 3, 4, 6, 8).astype(np.float64)
    ms_tensor = pytorch.tensor(np_array3)
    ms.set_seed(10)
    ms_tensor.geometric_(0.75)
    ms_tensor1 = ms_tensor
    ms_tensor.geometric_(0.75)
    ms_tensor2 = ms_tensor
    ms.set_seed(10)
    ms_tensor.geometric_(0.75)
    ms_tensor3 = ms_tensor
    ms_tensor.geometric_(0.75)
    ms_tensor4 = ms_tensor
    param_compare(ms_tensor1, ms_tensor3)
    param_compare(ms_tensor2, ms_tensor4)

@SKIP_ENV_GRAPH_MODE(reason="inplace testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason='log_normal_ does not support float64 input on Ascend')
def test_log_normal_fp64():
    np_array = np.random.rand(1, 3, 4).astype(np.float64) * 5
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)
    torch_tensor.log_normal_(2.5, 1.5)
    ms_tensor.log_normal_(2.5, 1.5)
    assert torch_tensor.numpy().dtype == ms_tensor.numpy().dtype
    assert torch_tensor.numpy().shape == ms_tensor.numpy().shape
    np_array3 = np.random.rand(1, 3, 4, 6, 8).astype(np.float64) * 5
    ms_tensor = pytorch.tensor(np_array3)
    ms.set_seed(10)
    ms_tensor.log_normal_(2.5, 1.5)
    ms_tensor1 = ms_tensor
    ms_tensor.log_normal_(2.5, 1.5)
    ms_tensor2 = ms_tensor
    ms.set_seed(10)
    ms_tensor.log_normal_(2.5, 1.5)
    ms_tensor3 = ms_tensor
    ms_tensor.log_normal_(2.5, 1.5)
    ms_tensor4 = ms_tensor
    param_compare(ms_tensor1, ms_tensor3)
    param_compare(ms_tensor2, ms_tensor4)

@SKIP_ENV_GRAPH_MODE(reason="testcase only for pynative mode")
@SKIP_ENV_ASCEND(reason="CANN_VERSION_ERR: ms.ops.Mul with int64 input result not correct on Ascend.")
def test_map_():
    def mul(x, y):
        return x * y
    np_array1 = np.array([1, 3, 4])
    np_array2 = np.array([2, 5, 8])
    torch_tensor1 = torch.tensor(np_array1)
    ms_tensor1 = pytorch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor2 = pytorch.tensor(np_array2)
    torch_tensor1.map_(torch_tensor2, mul)
    ms_tensor1.map_(ms_tensor2, mul)
    param_compare(torch_tensor1, ms_tensor1)

    torch_tensor1.map_(torch_tensor2, torch.mul)
    ms_tensor1.map_(ms_tensor2, pytorch.mul)
    param_compare(torch_tensor1, ms_tensor1)

    torch_tensor1.map_(torch_tensor2, torch.add)
    ms_tensor1.map_(ms_tensor2, pytorch.add)
    param_compare(torch_tensor1, ms_tensor1)

@SKIP_ENV_GPU(reason="nanmedian is not supported on GPU")
@SKIP_ENV_ASCEND(reason="nanmedian is not supported on Ascend")
def test_nanmedian1():
    torch_a = torch.tensor([1, float('nan'), 3, 2])
    torch_out1 = torch_a.nanmedian()
    ms_a = pytorch.tensor([1, float('nan'), 3, 2])
    ms_out1 = ms_a.nanmedian()
    assert np.allclose(torch_out1.numpy(), ms_out1.numpy(), equal_nan=True)
    assert torch_out1.numpy().dtype == ms_out1.numpy().dtype

@SKIP_ENV_GPU(reason="nanmedian is not supported on GPU")
@SKIP_ENV_ASCEND(reason="nanmedian is not supported on Ascend")
def test_nanmedian2():
    torch_a = torch.tensor([[2, 3, 1], [float('nan'), 1, float('nan')]])
    torch_out2 = torch_a.nanmedian(0)
    ms_a = pytorch.tensor([[2, 3, 1], [float('nan'), 1, float('nan')]])
    ms_out2 = ms_a.nanmedian(0)
    param_compare(torch_out2[0], ms_out2[0], equal_nan=True)
    param_compare(torch_out2[1], ms_out2[1])

def test_frexp():
    np_array = np.random.randn(2, 3, 4).astype(np.float16)
    torch_tensor = torch.tensor(np_array)
    ms_tensor = pytorch.tensor(np_array)

    torch_out1, torch_out2 = torch_tensor.frexp()
    ms_out1, ms_out2 = ms_tensor.frexp()
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason="ormqr currently not support on Ascend")
@SKIP_ENV_CPU(reason="ormqr currently not support on CPU")
def test_ormqr():
    a = np.random.randn(2, 3, 3)
    b = np.random.randn(2, 3)
    c = np.random.randn(2, 3, 3)
    A_t = torch.tensor(a)
    B_t = torch.tensor(b)
    C_t = torch.tensor(c)
    A_ms = pytorch.tensor(a)
    B_ms = pytorch.tensor(b)
    C_ms = pytorch.tensor(c)
    torch_out1 = torch.ormqr(A_t, B_t, C_t)
    torch_out2 = torch.ormqr(A_t, B_t, C_t, left=False, transpose=True)
    ms_out1 = A_ms.ormqr(B_ms, C_ms)
    ms_out2 = A_ms.ormqr(B_ms, C_ms, left=False, transpose=True)
    param_compare(torch_out1, ms_out1)
    param_compare(torch_out2, ms_out2)

@SKIP_ENV_ASCEND(reason="triangular_solve currently not support on Ascend")
def test_triangular_solve():
    np_array1 = np.random.randn(3, 3).astype(np.float32)
    np_array2 = np.random.randn(3, 4).astype(np.float32)

    torch_tensor1 = torch.tensor(np_array1)
    torch_tensor2 = torch.tensor(np_array2)
    ms_tensor1 = pytorch.tensor(np_array1)
    ms_tensor2 = pytorch.tensor(np_array2)

    A_t = torch_tensor1.triu()
    A_t1 = torch_tensor1.tril()
    X_t = torch_tensor2.triangular_solve(A_t, upper=True)
    X_t1 = torch_tensor2.triangular_solve(A_t1, upper=False, transpose=True, unitriangular=True)

    A_ms = ms_tensor1.triu()
    A_ms1 = ms_tensor1.tril()
    X_ms = ms_tensor2.triangular_solve(A_ms, upper=True)
    X_ms1 = ms_tensor2.triangular_solve(A_ms1, upper=False, transpose=True, unitriangular=True)

    param_compare(X_t, X_ms)
    param_compare(X_t1, X_ms1)

def test_relu():
    data = np.random.rand(2, 2, 3).astype(np.float32)

    torch_input = torch.tensor(data)
    torch_output = torch_input.relu()

    ms_input = pytorch.tensor(data)
    ms_output = ms_input.relu()
    param_compare(torch_output, ms_output)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_others_tensor()
    test_add_()
    test_mul()
    test_mul_()
    test_fill_()
    test_size_with_dim()
    test_size()
    test_zero_()
    test_normal_()
    test_uniform_()
    test_clamp_()
    test_permute1()
    test_permute2()
    test_copy_()
    test_copy_scalar()
    test_copy_adapter_scalar()
    test_expand()
    test_expand1()
    test_expand_list()
    test_sigmoid()
    test_sigmoid_()
    test_float()
    test_flip()
    test_sign()
    test_div()
    test_div2()
    test_div_()
    test_numel()
    test_sum()
    test_sum2()
    test_sum3()
    test_split()
    test_numpy()
    test_ndimension()
    test_pow()
    test_repeat()
    test_repeat_interleave()
    test_reshape()
    test_reshape_as()
    test_arcsinh()
    test_arctanh()
    test_det()
    test_negative()
    test_abs()
    test_ndim()
    test_amax()
    test_amin()
    test_as_strided()
    test_bmm()
    test_clamp()
    test_dim()
    test_expand_as()
    test_item()
    test_log()
    test_log2()
    test_matmul()
    test_squeeze()
    test_stride()
    test_sub()
    test_is_floating_point()
    test_unbind()
    test_unsqueeze()
    test_is_signed()
    test_transpose1()
    test_transpose2()
    test_floor()
    test_isfinite()
    test_isnan()
    test_expand()
    test_clone()
    test_detach()
    test_new_zeros()
    test_to()
    test_sort()
    test_msort()
    test_argsort()
    test_sqrt()
    test_rsqrt1()
    test_rsqrt2()
    test_rsqrt3()
    test_resize()
    test_resize_as()
    test_index_fill()
    test_index_fill_()
    test_data()
    test_new()
    test_cuda()
    test_t1()
    test_t2()
    test_mean1()
    test_mean2()
    test_prod1()
    test_prod_bool()
    test_index_select()
    test_index_select_scaler()
    test_std()
    test_exp()
    test_masked_fill()
    test_tolist()
    test_chunk()
    test_cumsum()
    test_absolute_()
    # test_acos_()
    test_addcdiv()
    test_addcdiv_fp64()
    # test_asinh_()
    # test_atanh_()
    test_gather()
    test_fmod()
    test_argmin()
    test_argmax()
    test_baddbmm()
    test_topk()
    test_slice()

    test_maximum()
    test_minimum()
    test_min()
    test_max()
    test_multiply()
    test_neg()
    test_ravel()
    test_select()
    test_square()
    test_broadcast_to()
    test_divide()
    test_mm()
    test_view()
    test_view_dtype()
    test_logsumexp()
    test_addmv()
    test_dot()
    test_inverse()
    # test_asin()
    # test_atan()
    # test_atan2()

    test_count_nonzero()
    test_scatter_1()
    test_scatter_2()
    test_addbmm()
    test_addr()
    test_cholesky()
    test_aminmax()
    test_any()
    test_bincount1()
    test_bincount2()
    test_bitwise_shift()
    test_cholesky_inverse()
    test_copysign()
    test_cos()
    test_cosh()
    test_cummax()
    test_cummin()
    test_cumprod()
    test_deg2rad()
    test_diag()
    test_diagflat()
    test_diagonal()
    test_isinf()
    test_isneginf()
    test_isposinf()
    test_isreal()
    test_diff()
    test_dist()
    test_erf()
    test_erfc()
    test_erfinv()
    test_expm1()
    test_fix()
    test_fix_()
    test_fliplr()
    test_addmm_()
    test_bitwise_()
    test_addmv_()
    test_float_power()
    test_trunc()
    test_trunc_()
    test_xlogy()
    test_xlogy_()
    test_vsplit()
    test_vdot_float()
    test_vdot_int()
    test_vdot_complex()
    test_where()
    test_where2()
    test_true_divide()
    test_true_divide_()
    test_triu()
    test_triu_()
    test_tril()
    test_tril_()
    test_heaviside()
    test_flipud()
    test_tile()
    test_unique_consecutive()
    test_tensor_split()
    test_tan()
    test_tan_()
    test_tanh()
    test_tanh_()
    # test_arctanh_()
    test_take()
    test_sinc()
    test_sinc_()
    test_sinh()
    test_sinh_()

    test_hardshrink()
    test_hsplit()
    test_hypot()
    test_log10()
    test_log1p()
    test_logaddexp()
    test_logdet()
    test_logical_not()
    test_logical_or()
    test_adjoint()
    test_lerp()
    test_masked_select()
    test_angle()
    test_element_size()
    test_positive()
    test_logical_and()
    test_igamma()
    test_lcm()
    test_lcm_()
    test_inner_int64()
    test_inner()
    test_igamma_()
    test_lgamma()
    test_roll()
    test_multinomial()
    test_cov()
    test_rot90()
    test_median_common1()
    test_median_common2()
    test_median()
    test_frac()
    test_frac_()
    test_gcd()
    test_gcd_()
    test_imag()
    test_ldexp()
    test_ldexp_()
    test_lerp_()
    test_mv()
    test_geqrf()
    test_logaddexp2()
    test_log1p_()
    test_log2_()
    test_lstsq()
    test_logical_not_()
    test_logical_and_()
    test_logical_or_()
    test_lu()
    test_lu_solve()
    test_floor_divide()
    test_floor_divide_()
    test_expm1_()
    test_float_power_()
    test_hypot_()
    test_square_()
    test_logical_xor_()
    test_lgamma_()
    test_renorm()
    test_renorm_()
    test_round()
    test_round_()
    test_floor_()
    test_mvlgamma()
    test_mvlgamma_()
    test_orgqr()
    test_qr()
    test_random_()
    test_bernoulli_()
    test_swapaxes2()
    test_transpose2()
    test_bernoulli()
    test_is_conj()
    test_resolve_conj()
    test_is_conj_jit()
    test_resolve_conj_jit()
    test_i0()
    test_matrix_power()
    test_index_add()
    test_index_add_()
    test_scatter_add()
    test_scatter_add_()
    test_index_copy()
    test_index_copy_()
    test_diag_embed()
    test_resolve_neg()
    test_resolve_neg_jit()
    test_i0_()
    test_logit_()
    test_symeig()
    test_symeig_namedtuple()
    test_nan_to_num()
    test_nan_to_num_float64()
    test_nan_to_num_()
    test_index_put()
    test_index_put2()
    test_index_put_()
    test_put_int_()
    test_put_float()
    test_nextafter_()
    test_kthvalue()
    test_scatter_reduce_amax()
    test_scatter_reduce_prod_nd()
    test_scatter_reduce_amax_nd()
    test_scatter_reduce_amin_nd()
    test_scatter_reduce_sum_nd()
    test_exponential_()
    test_exponential_fp64()
    test_index_reduce_prod()
    test_index_reduce_amax()
    test_index_reduce_amin()
    test_masked_scatter()
    test_masked_scatter_()
    test_to_device_index()
    test_corrcoef()
    test_geometric_()
    test_geometric_fp64()
    test_log_normal_()
    test_log_normal_fp64()
    test_map_()
    test_copysign_fp64()
    test_copysign_shape()
    test_abs_()
    test_igammac()
    test_igammac_()
    test_masked_fill_float64()
    test_vdot_float64()
    test_tile_int16()
    test_ascend_log1p_()
    test_nanmedian1()
    test_nanmedian2()
    test_cholesky_solve()
    test_erfinv_fp64()
    test_div3_fp64()
    test_div_fp64()
    test_amax_fp64()
    test_amin_fp64()
    test_baddbmm_fp64()
    test_addmm_fp64()
    test_cholesky_fp64()
    test_logaddexp_fp64()
    test_frac_fp64()
    test_lerp1_fp64()
    test_mv_fp64()
    test_floor_divide_fp64()
    test_renorm_fp64()
    test_floor_fp64()
    test_index_add_fp64()
    test_index_copy_fp64()
    test_corrcoef_fp64()
    test_frexp()
    test_ormqr()
    test_triangular_solve()
    test_uniform_range()
    test_random_range()
    test_max_int()
    test_min_int()
    test_max2()
    test_max2_fp64()
    test_min2()
    test_min2_fp64()
    test_relu()
    test_fill_tensor()
    test_tile_uint8()