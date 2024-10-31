#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindspore.ops.primitive import _primexpr
from mindtorch.torch.tensor import cast_to_adapter_tensor, Tensor
from mindtorch.torch.logging import info
from mindtorch.utils import pynative_mode_condition, graph_mode_condition


def _out_limit_pynative(out, op_name):
    if out is not None and graph_mode_condition():  # TODO: ms_function
        raise ValueError(
            'In MindSpore static graph mode, `out` in `{}` should be None, ' \
            'please set out=None and use return value instead of `out`.'.format(op_name)
        )
    elif out is not None:
        info(
            'If you want to convert to the MindSpore static graph mode, `out` in `{}` should be None, ' \
            'please set out=None and use return value instead of `out`.'.format(op_name)
        )

def _out_assign_with_output(out, output, op_name, requires_grad=None):
    if pynative_mode_condition():  # TODO: ms_function
        info(
            'If you want to convert to the MindSpore static graph mode, `out` in `{}` should be None, ' \
            'please set out=None and use return value instead of `out`.'.format(op_name)
        )

        if requires_grad is not None:
            if out.is_leaf:
                if output.requires_grad and requires_grad is False:
                    raise RuntimeError("a leaf Variable that requires grad is being used in an in-place operation.")
                out.requires_grad = requires_grad
                output.requires_grad = requires_grad
            else:
                if out.requires_grad:
                    output.requires_grad = out.requires_grad
                else:
                    out.requires_grad = requires_grad
                    output.requires_grad = requires_grad

        def _assign(out, output):
            if isinstance(out, Tensor):
                # Pass `cast_to_ms_tensor(output)` for performance, add it back when needed.
                out.assign_value(output.astype(out.dtype))
            elif isinstance(out, (tuple, list)):
                for item in zip(out, output):
                    _assign(item[0], item[1])

        _assign(out, output)
        return out

    raise ValueError(
        'In MindSpore static graph mode, `out` in `{}` should be None, ' \
        'please set out=None and use return value instead of `out`.'.format(op_name)
    )

def _out_inplace_assign_with_adapter_tensor(out, output, op_name, requires_grad=None):
    r'''
    Use for assign `out` with `output` when `output` is(are) Adapter Tensor(s).
    '''
    if out is None:
        if requires_grad is not None:
            output.requires_grad = requires_grad
        return output

    return _out_assign_with_output(out, output, op_name, requires_grad)


def _out_inplace_assign(out, output, op_name, requires_grad=None):
    r'''
    Use for assign `out` with `output` when `output` is(are) MindSpore Tensor(s)
    '''

    if out is None:
        if requires_grad is not None:
            output.requires_grad = requires_grad
        return cast_to_adapter_tensor(output)

    return _out_assign_with_output(out, output, op_name, requires_grad)


def _inplace_assign_pynative(input, inplace, output, op_name):
    if inplace is True:
        if pynative_mode_condition():  # TODO: ms_function
            info(
                'If you want to convert to the MindSpore static graph mode, `inplace` in `{}` should not be True, ' \
                'please set inplace=False and use return value instead of `input`.'.format(op_name)
            )
            input.assign_value(output)
            return input

        raise ValueError(
            'In MindSpore static graph mode, `inplace` in `{}` should not be True, ' \
            'please set inplace=False and use return value instead of `input`.'.format(op_name)
        )

    return cast_to_adapter_tensor(output)


def _nn_functional_inplace_assign(input, output, op_name, replace_op):

    if pynative_mode_condition():  # TODO: ms_function
        info(
            '`nn.functional.{a}` is an in-place operation and "nn.functional.{a}(x)" is not supported ' \
            'to use in MindSpore static graph mode. If you want to convert to the MindSpore static graph mode,' \
            'please use "x = nn.functional.{b}(x)" or other API instead.'.format(a=op_name, b=replace_op)
        )
        input.assign_value(output)
        return input

    raise RuntimeError(
        '`nn.functional.{a}` is an in-place operation and "nn.functional.{a}(x)" is not supported ' \
        'to use in MindSpore static graph mode. Please use "x = nn.functional.{b}(x)" or other API ' \
        'instead.'.format(a=op_name, b=replace_op)
    )

def _functional_inplace_assign(input, output, op_name, replace_op):
    if pynative_mode_condition():  # TODO: ms_function
        info(
            '`functional.{a}` is an in-place operation and "functional.{a}(x)" is not supported ' \
            'to use in MindSpore static graph mode. If you want to covert to the MindSpore static graph mode,' \
            'please use "x = functional.{b}(x)" or other API instead.'.format(a=op_name, b=replace_op)
        )
        input.assign_value(output)
        return input

    raise RuntimeError(
        '`functional.{a}` is an in-place operation and "functional.{a}(x)" is not supported ' \
        'to use in MindSpore static graph mode. Please use "x = functional.{b}(x)" or other API ' \
        'instead.'.format(a=op_name, b=replace_op)
    )

@_primexpr
def _inplace_limit_pynative(inplace, op_name):
    if inplace is True and graph_mode_condition(): # TODO: ms_function
        raise ValueError(
            'In MindSpore static graph mode, `inplace` in `{}` should not be True, ' \
            'please set inplace=False and use return value instead of `input`.'.format(op_name)
        )
    elif inplace is True:
        info(
            'If you want to convert to the MindSpore static graph mode, `inplace` in `{}` should not be True, ' \
            'please set inplace=False and use return value instead of `input`.'.format(op_name)
        )

def _inplace_assign(input, inplace, output):
    if inplace is True:
        input.assign_value(output)
        return input
    return cast_to_adapter_tensor(output)
