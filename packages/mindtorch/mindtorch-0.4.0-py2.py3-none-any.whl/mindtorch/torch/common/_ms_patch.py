#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindspore import ops
from mindspore.common import dtype as mstype
from mindspore.ops._primitive_cache import _get_cache_prim

# patch of ms.ops.nansum
def _ms_nansum(input, axis=None, keepdims=False, *, dtype=None):
    if input.is_complex():
        raise TypeError(f'For nansum, input are not supported complex type, but got {input.dtype}.')
    if dtype is not None and dtype in mstype.complex_type:
        raise TypeError(f'For nansum, dtype not supported complex type, but got {dtype}.')
    if axis is None:
        axis = ()
    if input.dtype == mstype.bool_:
        input = input.astype(mstype.int64)
    is_nan = ops.isnan(input)
    # ops.masked_fill() has bug when input contains nan on 910A
    # input = ops.masked_fill(input, is_nan, ops.cast(0, input.dtype))
    input = ops.select(is_nan, 0, input)
    input = _get_cache_prim(ops.ReduceSum)(keepdims)(input, axis)
    if dtype is not None and input.dtype != dtype:
        input = input.astype(dtype)
    return input


# patch of ms.ops.nanmean
def _ms_nanmean(input, axis=None, keepdims=False, *, dtype=None):
    if input.dtype not in mstype.float_type:
        raise TypeError(f"For 'nanmean', input should be floating point dtype, but got {type(input)}.")
    nan_sum = _ms_nansum(input, axis, keepdims)
    is_num = ops.isnan(input).logical_not()
    is_num = is_num.sum(axis=axis, keepdims=keepdims)
    out = nan_sum / is_num
    if dtype is not None:
        return out.astype(dtype)
    return out
