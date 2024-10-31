#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0301
from mindspore import dtype as mstype
from mindspore._extends.parse import trope as T
from mindspore._extends.parse.resources import convert_object_map
from mindtorch.torch.tensor import Tensor as adapter_Tensor
from mindtorch.torch._register.register_utils import convert_to_ms_tensor, convert_to_adapter_tensor


matmul_fn = convert_object_map.get(T.matmul)
invert_fn = convert_object_map.get(T.invert)
abs_fn = convert_object_map.get(T.abs)
round_fn = convert_object_map.get(T.round)
max_fn = convert_object_map.get(T.max)
min_fn = convert_object_map.get(T.min)
sum_fn = convert_object_map.get(T.sum)


def adapter_matmul(x, y):
    if isinstance(x, adapter_Tensor) and isinstance(y, adapter_Tensor):
        x = convert_to_ms_tensor(x)
        y = convert_to_ms_tensor(y)
        out = matmul_fn(x, y)
        out = convert_to_adapter_tensor(out)
    else:
        out = matmul_fn(x, y)
    return out


def adapter_invert(x):
    if isinstance(x, adapter_Tensor):
        x = convert_to_ms_tensor(x)
        if x.dtype != mstype.bool_:
            out = - 1 - x
        else:
            out = invert_fn(x)
        out = convert_to_adapter_tensor(out)
    else:
        out = invert_fn(x)
    return out


def adapter_abs(x):
    if isinstance(x, adapter_Tensor):
        x = convert_to_ms_tensor(x)
        out = abs_fn(x)
        out = convert_to_adapter_tensor(out)
    else:
        out = abs_fn(x)
    return out


def adapter_round(*data):
    if (len(data) == 1 and isinstance(data[0], adapter_Tensor)) or \
      (len(data) == 2 and isinstance(data[0], adapter_Tensor) and data[1] is None):
        x = data[0]
        x = convert_to_ms_tensor(x)
        out = round_fn(x)
        out = convert_to_adapter_tensor(out)
    else:
        out = round_fn(*data)
    return out


def _has_adapter_tensor(*data):
    if len(data) == 1 and isinstance(data[0], adapter_Tensor):
        return True
    for elem in data:
        if isinstance(elem, adapter_Tensor):
            return True
    return False


def adapter_max(*data):
    if _has_adapter_tensor(*data):
        out = max_fn(*data)
        out = convert_to_adapter_tensor(out)
    else:
        out = max_fn(*data)
    return out


def adapter_min(*data):
    if _has_adapter_tensor(*data):
        out = min_fn(*data)
        out = convert_to_adapter_tensor(out)
    else:
        out = min_fn(*data)
    return out


def adapter_sum(*data):
    if _has_adapter_tensor(*data):
        out = sum_fn(*data)
        out = convert_to_adapter_tensor(out)
    else:
        out = sum_fn(*data)
    return out


# Please note that the comments at the end of the sentence, such as `@jit.typing: () -> tensor_type[float32]`,
# are intended to guide type derivation and should not be deleted.
def create_adapter_tensor(*data, requires_grad=False, dtype=None, inner=False, cast_tensor=False):
    if dtype is None and isinstance(data[0], adapter_Tensor):
        dtype = data[0].dtype
    if dtype is None:
        return adapter_Tensor(
            *data, requires_grad=requires_grad, dtype=dtype, inner=inner, cast_tensor=cast_tensor)  # @jit.typing: () -> tensor_type[float32]
    return adapter_Tensor(
        *data, requires_grad=requires_grad, dtype=dtype, inner=inner, cast_tensor=cast_tensor) # @jit.typing: () -> tensor_type[{dtype}]

def create_adapter_bool_tensor(*data):
    return adapter_Tensor(*data, dtype='bool', inner=False) # @jit.typing: () -> tensor_type[bool_]

def create_adapter_byte_tensor(*data):
    return adapter_Tensor(*data, dtype='uint8', inner=False) # @jit.typing: () -> tensor_type[uint8]

def create_adapter_char_tensor(*data):
    return adapter_Tensor(*data, dtype='int8', inner=False) # @jit.typing: () -> tensor_type[int8]

def create_adapter_short_tensor(*data):
    return adapter_Tensor(*data, dtype='int16', inner=False) # @jit.typing: () -> tensor_type[int16]

def create_adapter_int_tensor(*data):
    return adapter_Tensor(*data, dtype='int32', inner=False) # @jit.typing: () -> tensor_type[int32]

def create_adapter_half_tensor(*data):
    return adapter_Tensor(*data, dtype='float16', inner=False) # @jit.typing: () -> tensor_type[float16]

def create_adapter_float_tensor(*data):
    return adapter_Tensor(*data, dtype='float32', inner=False) # @jit.typing: () -> tensor_type[float32]

def create_adapter_double_tensor(*data):
    return adapter_Tensor(*data, dtype='float64', inner=False) # @jit.typing: () -> tensor_type[float64]

def create_adapter_long_tensor(*data):
    return adapter_Tensor(*data, dtype='int64', inner=False) # @jit.typing: () -> tensor_type[int64]

def create_adapter_bfloat16_tensor(*data):
    return adapter_Tensor(*data, dtype='bfloat16', inner=False) # @jit.typing: () -> tensor_type[bfloat16]
