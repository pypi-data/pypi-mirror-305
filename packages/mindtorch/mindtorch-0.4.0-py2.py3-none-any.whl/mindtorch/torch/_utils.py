import sys
import traceback
import copyreg
import mindtorch.torch.common.dtype as _dtype
from mindtorch.torch.common.dtype import finfo, iinfo
from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning

# class KeyErrorMessage(str):
#     r"""str subclass that returns itself in repr"""
#     def __repr__(self):
#         return self

def _type(self, dtype=None, non_blocking=False, **kwargs):
    non_blocking = _get_async_or_non_blocking('type', non_blocking, kwargs)
    if dtype is None:
        return self.__module__ + '.' + self.__class__.__name__

    if isinstance(dtype, str):
        dtype = _import_dotted_name(dtype)
    if dtype == type(self):
        return self
    if self.is_sparse:
        if not dtype.is_sparse:
            raise RuntimeError("Cannot cast sparse tensor to dense tensor")
        raise NotImplementedError("Sparse feature not fully supported at the moment.")
        # TODO: Sparse feature not fully supported at the moment
        # new_module_name = dtype.__module__.replace('.sparse', '')
        # new_values_type_name = new_module_name + '.' + dtype.__name__
        # new_values = Tensor._values(self).type(new_values_type_name, non_blocking)
        # new_indices_type_name = new_module_name + '.LongTensor'
        # new_indices = Tensor._indices(self).type(new_indices_type_name, non_blocking)
        # return dtype(new_indices, new_values, self.size())
    if dtype.is_sparse:
        raise RuntimeError("Cannot cast dense tensor to sparse tensor")
    return dtype(self.size()).copy_(self, non_blocking)

def _cuda(self, device=None, non_blocking=False, **kwargs):
    # Currently, no copy is performed and the original object is returned.
    unsupported_attr(device)
    unsupported_attr(non_blocking)
    unsupported_attr(kwargs)
    return self

def _get_async_or_non_blocking(function_name, non_blocking, kwargs):
    if not kwargs:
        return non_blocking
    if len(kwargs) != 1 or 'async' not in kwargs:
        message = "{}() got an unexpected keyword argument '{}'"
        argument = list(kwargs.keys()).pop()
        raise TypeError(message.format(function_name, argument))
    warning("'async' is deprecated; use 'non_blocking'")
    return kwargs['async']

def _rebuild_tensor(storage, storage_offset, size, stride):
    unsupported_attr(stride)
    from mindtorch.torch.tensor import tensor # pylint: disable=R0401, C0415
    t = tensor([], dtype=storage.dtype, device=storage._untyped().device)
    return t._set_storage(storage._untyped(), storage_offset, size)


def _rebuild_tensor_v2(storage, storage_offset, size, stride, requires_grad, backward_hooks, metadata=None):
    unsupported_attr(backward_hooks)
    unsupported_attr(metadata)
    tensor = _rebuild_tensor(storage, storage_offset, size, stride)
    tensor.requires_grad = requires_grad
    return tensor

def _rebuild_mindtorch_tensor(data, dtype):
    from mindtorch.torch.tensor import tensor  # pylint: disable=R0401, C0415
    t = tensor(data, dtype=dtype)
    return t

def _rebuild_device_tensor_from_numpy(data, dtype, device, requires_grad):
    from mindtorch.torch.functional import from_numpy # pylint: disable=R0401, C0415
    tensor = from_numpy(data).to(dtype=dtype, device=device)
    tensor.requires_grad = requires_grad
    return tensor


def _rebuild_parameter(data, requires_grad, backward_hooks):
    unsupported_attr(backward_hooks)
    from mindtorch.torch.nn import Parameter # pylint: disable=R0401, C0415
    param = Parameter(data, requires_grad)
    param._set_storage(data.storage()._untyped(), 0, data.size())
    return param

def _rebuild_parameter_with_state(data, requires_grad, backward_hooks, state):
    unsupported_attr(backward_hooks)
    from mindtorch.torch.nn import Parameter # pylint: disable=R0401, C0415
    param = Parameter(data, requires_grad)
    param._backward_hooks = backward_hooks
    param = _set_obj_state(param, state)
    return param

def _rebuild_mindtorch_parameter(data, requires_grad, name, layerwise_parallel):
    from mindtorch.torch.nn import Parameter # pylint: disable=R0401, C0415
    param = Parameter(data, requires_grad, name, layerwise_parallel)
    return param

def _rebuild_mindtorch_parameter_with_state(data, requires_grad, name, layerwise_parallel, state):
    from mindtorch.torch.nn import Parameter # pylint: disable=R0401, C0415
    param = Parameter(data, requires_grad, name, layerwise_parallel)
    param = _set_obj_state(param, state)
    return param

def _import_dotted_name(name):
    components = name.split('.')
    obj = __import__(components[0])
    for component in components[1:]:
        obj = getattr(obj, component)
    return obj

def _element_size(dtype):
    """
    Returns the element size for a dtype, in bytes
    """
    if not isinstance(dtype, _dtype.ms_dtype):
        raise RuntimeError(f'expected torch.dtype, but got {type(dtype)}')

    if dtype.is_complex:
        return finfo(dtype).bits >> 2
    elif dtype.is_floating_point:
        return finfo(dtype).bits >> 3
    elif dtype == _dtype.bool:
        # NOTE: torch.bool is not supported in torch.iinfo()
        return 1
    else:
        return iinfo(dtype).bits >> 3

class ExceptionWrapper:
    r"""Wraps an exception plus traceback to communicate across threads"""
    def __init__(self, exc_info=None, where="in background"):
        if exc_info is None:
            exc_info = sys.exc_info()
        self.exc_type = exc_info[0]
        self.exc_msg = "".join(traceback.format_exception(*exc_info))
        self.where = where

    def reraise(self):
        r"""Reraises the wrapped exception in the current thread"""
        msg = "Caught {} {}.\nOriginal {}".format(
            self.exc_type.__name__, self.where, self.exc_msg)
        if self.exc_type == KeyError:
            # msg = KeyErrorMessage(msg)
            msg = str(msg)
        elif getattr(self.exc_type, "message", None):
            raise self.exc_type(message=msg)
        try:
            exception = self.exc_type(msg)
        except TypeError:
            raise RuntimeError(msg) from None
        raise exception

class _ClassPropertyDescriptor:
    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner=None):
        if owner is None:
            owner = type(instance)
        return self.fget.__get__(instance, owner)()

def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)
    return _ClassPropertyDescriptor(func)

def _flatten_dense_tensors(tensors):
    unsupported_attr(tensors)
    raise NotImplementedError("`_flatten_dense_tensors` is not implemented now.")

def _take_tensors(tensors, size_limit):
    unsupported_attr(tensors)
    unsupported_attr(size_limit)
    raise NotImplementedError("`_take_tensors` is not implemented now.")

def _unflatten_dense_tensors(flat, tensors):
    unsupported_attr(flat)
    unsupported_attr(tensors)
    raise NotImplementedError("`_unflatten_dense_tensors` is not implemented now.")

def _set_obj_state(obj, state):
    if isinstance(state, tuple):
        if not len(state) == 2:
            raise RuntimeError(f"Invalid serialized state: {state}")
        dict_state = state[0]
        slots_state = state[1]
    else:
        dict_state = state
        slots_state = None

    if dict_state:
        for k, v in dict_state.items():
            setattr(obj, k, v)

    if slots_state:
        for k, v in slots_state.items():
            setattr(obj, k, v)
    return obj

def _get_obj_state(obj):
    getstate_fn = getattr(obj, "__getstate__", None)
    if getstate_fn is not None:
        state = getstate_fn()
    else:
        slots_to_save = copyreg._slotnames(obj.__class__)  # type: ignore[attr-defined]
        if slots_to_save:
            state = (
                obj.__dict__,
                {
                    name: getattr(obj, name)
                    for name in slots_to_save
                    if hasattr(obj, name)
                },
            )
        else:
            state = obj.__dict__.copy()

    return state
