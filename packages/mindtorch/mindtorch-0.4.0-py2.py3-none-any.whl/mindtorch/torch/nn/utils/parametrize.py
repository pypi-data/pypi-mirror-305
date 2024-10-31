#The main code of this file stems from PyTorch open-source code, only necessary adaptation modifications are made.

import collections
from contextlib import contextmanager
from mindspore import _no_grad as torch_no_grad
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.torch.tensor import Tensor
from mindtorch.torch.jit._jit_internal import unused as torch_jit_unused
from ..modules.container import ModuleList, ModuleDict

_cache_enabled = 0
_cache = {}


@contextmanager
def cached():
    global _cache
    global _cache_enabled
    _cache_enabled += 1
    try:
        yield
    finally:
        _cache_enabled -= 1
        if not _cache_enabled:
            _cache = {}


def _register_parameter_or_buffer(module, name, X):
    if isinstance(X, Parameter):
        module.register_parameter(name, X)
    else:
        module.register_buffer(name, X)


class ParametrizationList(ModuleList):
    def __init__(
        self, modules, original, unsafe=False):
        if len(modules) == 0:
            raise ValueError("ParametrizationList requires one or more modules.")

        super().__init__(modules)
        self.unsafe = unsafe

        original_shape = original.shape
        original_dtype = original.dtype

        with torch_no_grad():
            new = original
            for module in reversed(self):
                if hasattr(module, "right_inverse"):
                    try:
                        new = module.right_inverse(new)
                    except NotImplementedError:
                        pass

        if not isinstance(new, Tensor) and not isinstance(new, collections.abc.Sequence):
            raise ValueError("'right_inverse' must return a Tensor or a Sequence of tensors (list, tuple...). "
                             f"Got {type(new).__name__}")

        self.is_tensor = isinstance(new, Tensor)
        self.ntensors = 1 if self.is_tensor else len(new)

        if self.is_tensor:
            if original.dtype != new.dtype:
                raise ValueError(
                    "When `right_inverse` outputs one tensor, it may not change the dtype.\n"
                    f"original.dtype: {original.dtype}\n"
                    f"right_inverse(original).dtype: {new.dtype}"
                )
            with torch_no_grad():
                original.set_(new)
            _register_parameter_or_buffer(self, "original", original)
        else:
            for i, originali in enumerate(new):
                if not isinstance(originali, Tensor):
                    raise ValueError("'right_inverse' must return a Tensor or a Sequence of tensors "
                                     "(list, tuple...). "
                                     f"Got element {i} of the sequence with type {type(originali).__name__}.")

                if isinstance(original, Parameter):
                    originali = Parameter(originali)
                originali.requires_grad_(original.requires_grad)
                _register_parameter_or_buffer(self, f"original{i}", originali)

        if not self.unsafe:
            Z = self()
            if not isinstance(Z, Tensor):
                raise ValueError(
                    f"A parametrization must return a tensor. Got {type(Z).__name__}."
                )
            if Z.dtype != original_dtype:
                raise ValueError(
                    "Registering a parametrization may not change the dtype of the tensor, "
                    "unless `unsafe` flag is enabled.\n"
                    f"unparametrized dtype: {original_dtype}\n"
                    f"parametrized dtype: {Z.dtype}"
                )
            if Z.shape != original_shape:
                raise ValueError(
                    "Registering a parametrization may not change the shape of the tensor, "
                    "unless `unsafe` flag is enabled.\n"
                    f"unparametrized shape: {original_shape}\n"
                    f"parametrized shape: {Z.shape}"
                )

    def right_inverse(self, value):
        with torch_no_grad():
            for module in reversed(self):
                if hasattr(module, "right_inverse"):
                    value = module.right_inverse(value)
                else:
                    raise RuntimeError(f"parametrization {type(module).__name__} does not implement "
                                       "right_inverse.")
            if self.is_tensor:
                if not isinstance(value, Tensor):
                    raise ValueError(
                        f"`right_inverse` should return a tensor. Got {type(value).__name__}"
                    )
                if value.dtype != self.original.dtype:
                    raise ValueError(
                        f"The tensor returned by `right_inverse` has dtype {value.dtype} "
                        f"while `original` has dtype {self.original.dtype}"
                    )
                self.original.set_(value)
            else:
                if not isinstance(value, collections.abc.Sequence):
                    raise ValueError(
                        "'right_inverse' must return a sequence of tensors. "
                        f"Got {type(value).__name__}."
                    )
                if len(value) != self.ntensors:
                    raise ValueError(
                        "'right_inverse' must return a sequence of tensors of length "
                        f"{self.ntensors}. Got a sequence of lenght {len(value)}."
                    )
                for i, tensor in enumerate(value):
                    original_i = getattr(self, f"original{i}")
                    if not isinstance(tensor, Tensor):
                        raise ValueError(
                            f"`right_inverse` must return a sequence of tensors. "
                            f"Got element {i} of type {type(tensor).__name__}"
                        )
                    if original_i.dtype != tensor.dtype:
                        raise ValueError(
                            f"Tensor {i} returned by `right_inverse` has dtype {tensor.dtype} "
                            f"while `original{i}` has dtype {original_i.dtype}"
                        )
                    original_i.set_(tensor)

    def forward(self):
        if self.is_tensor:
            x = self[0](self.original)
        else:
            originals = (getattr(self, f"original{i}") for i in range(self.ntensors))
            x = self[0](*originals)
        curr_idx = 1
        while hasattr(self, str(curr_idx)):
            x = self[curr_idx](x)
            curr_idx += 1
        return x


def _inject_new_class(module):
    cls = module.__class__

    def getstate(self):
        raise RuntimeError(
            "Serialization of parametrized modules is only "
            "supported through state_dict()."
        )

    param_cls = type(
        f"Parametrized{cls.__name__}",
        (cls,),
        {
            "__getstate__": getstate,
        },
    )

    module.__class__ = param_cls


def _inject_property(module, tensor_name):
    assert not hasattr(module, tensor_name)

    @torch_jit_unused
    def get_cached_parametrization(parametrization):
        global _cache
        key = (id(module), tensor_name)
        tensor = _cache.get(key)
        if tensor is None:
            tensor = parametrization()
            _cache[key] = tensor
        return tensor

    def get_parametrized(self):
        parametrization = self.parametrizations[tensor_name]
        if _cache_enabled:
            # TODO: torch.jit.is_scripting and torch._C._get_tracing_state are not supported currently.
            # if torch.jit.is_scripting():
            #     # Scripting
            #     raise RuntimeError('Caching is not implemented for scripting. '
            #                        'Either disable caching or avoid scripting.')
            # elif torch._C._get_tracing_state() is not None:
            #     # Tracing
            #     raise RuntimeError('Cannot trace a model while caching parametrizations.')
            # else:
            #     return get_cached_parametrization(parametrization)
            return get_cached_parametrization(parametrization)
        else:
            return parametrization()

    def set_original(self, value):
        self.parametrizations[tensor_name].right_inverse(value)

    setattr(module.__class__, tensor_name, property(get_parametrized, set_original))

def register_parametrization(module, tensor_name, parametrization, *, unsafe=False):
    parametrization.train(module.training)
    if is_parametrized(module, tensor_name):
        if not unsafe:
            Y = getattr(module, tensor_name)
            X = parametrization(Y)
            if not isinstance(X, Tensor):
                raise ValueError(
                    f"A parametrization must return a tensor. Got {type(X).__name__}."
                )
            if X.dtype != Y.dtype:
                raise ValueError(
                    "Registering a parametrization may not change the dtype of the tensor, "
                    "unless the `unsafe` flag is enabled.\n"
                    f"module.{tensor_name}.dtype: {Y.dtype}\n"
                    f"parametrization(module.{tensor_name}).dtype: {X.dtype}"
                )
            if X.shape != Y.shape:
                raise ValueError(
                    "Registering a parametrization may not change the shape of the tensor, "
                    "unless the `unsafe` flag is enabled.\n"
                    f"module.{tensor_name}.shape: {Y.shape}\n"
                    f"parametrization(module.{tensor_name}).shape: {X.shape}"
                )
            if hasattr(parametrization, "right_inverse"):
                try:
                    Z = parametrization.right_inverse(X)  # type: ignore[operator]
                except NotImplementedError:
                    pass
                else:
                    if not isinstance(Z, Tensor):
                        raise ValueError(
                            f"parametrization.right_inverse must return a tensor. Got: {type(Z).__name__}"
                        )
                    if Z.dtype != Y.dtype:
                        raise ValueError(
                            "The tensor returned by parametrization.right_inverse must have the same dtype "
                            f"as module.{tensor_name}, unless the `unsafe` flag is enabled.\n"
                            f"module.{tensor_name}.dtype: {Y.dtype}\n"
                            f"returned dtype: {Z.dtype}"
                        )
                    if Z.shape != Y.shape:
                        raise ValueError(
                            "The tensor returned by parametrization.right_inverse must have the same shape "
                            f"as module.{tensor_name}, unless the `unsafe` flag is enabled.\n"
                            f"module.{tensor_name}.shape: {Y.shape}\n"
                            f"returned shape: {Z.shape}"
                        )

        assert isinstance(module.parametrizations, ModuleDict)
        module.parametrizations[tensor_name].append(parametrization)
        module.parametrizations[tensor_name].unsafe |= unsafe
    elif tensor_name in module._buffers or tensor_name in module._parameters:
        original = getattr(module, tensor_name)
        parametrizations = ParametrizationList([parametrization], original, unsafe=unsafe)
        delattr(module, tensor_name)
        if not is_parametrized(module):
            _inject_new_class(module)
            module.parametrizations = ModuleDict()
        _inject_property(module, tensor_name)
        assert isinstance(module.parametrizations, ModuleDict)
        module.parametrizations[tensor_name] = parametrizations
    else:
        raise ValueError(
            f"Module '{module}' does not have a parameter, a buffer, or a "
            f"parametrized element with name '{tensor_name}'"
        )
    return module


def is_parametrized(module, tensor_name=None):
    parametrizations = getattr(module, "parametrizations", None)
    if parametrizations is None or not isinstance(parametrizations, ModuleDict):
        return False
    if tensor_name is None:
        return len(parametrizations) > 0
    else:
        return tensor_name in parametrizations

def remove_parametrizations(module, tensor_name, leave_parametrized=True):
    if not is_parametrized(module, tensor_name):
        raise ValueError(f"Module {module} does not have a parametrization on {tensor_name}")

    assert isinstance(module.parametrizations, ModuleDict)
    parametrizations = module.parametrizations[tensor_name]
    if parametrizations.is_tensor:
        original = parametrizations.original
        if leave_parametrized:
            with torch_no_grad():
                t = getattr(module, tensor_name)
            with torch_no_grad():
                if isinstance(original, Tensor):
                    original.set_(t)
                else:
                    try:
                        original.set_(t)
                    except RuntimeError as e:
                        # TODO: Fix this for tensor subclasses that are parameters:
                        # RuntimeError: set_storage is not allowed on a Tensor created from .data or .detach().
                        raise RuntimeError("Calling remove_parametrizations() with leave_parametrized=True "
                                           "for a parameter that is an instance of a tensor subclass requires "
                                           "set_() to be implemented correctly for the tensor subclass. Either "
                                           "set leave_parametrized=False or provide a working implementation for "
                                           "set_() in the tensor subclass.") from e
    else:
        if leave_parametrized:
            t = getattr(module, tensor_name)
            original = Parameter(t) if t.requires_grad else t
        else:
            raise ValueError("Cannot leave unparametrized (`leave_parametrized=False`) a tensor "
                             "that is parametrized in terms of a sequence of tensors.")

    delattr(module.__class__, tensor_name)
    del module.parametrizations[tensor_name]

    _register_parameter_or_buffer(module, tensor_name, original)

    if not is_parametrized(module):
        delattr(module, "parametrizations")
        orig_cls = module.__class__.__bases__[0]
        module.__class__ = orig_cls
    return module

def type_before_parametrizations(module):
    if is_parametrized(module):
        return module.__class__.__bases__[0]
    else:
        return type(module)

def transfer_parametrizations_and_params(from_module, to_module, tensor_name=None):
    if is_parametrized(from_module):
        assert isinstance(from_module.parametrizations, ModuleDict)

        parameters_to_transfer = (
            from_module.parametrizations if tensor_name is None else [tensor_name]
        )

        assert hasattr(parameters_to_transfer, "__iter__")
        for parameter_name in parameters_to_transfer:

            if not hasattr(to_module, parameter_name):
                setattr(
                    to_module,
                    parameter_name,
                    Parameter(getattr(from_module, parameter_name)),
                )

            for param_func in from_module.parametrizations[parameter_name]:
                register_parametrization(to_module, parameter_name, param_func)
            assert isinstance(to_module.parametrizations, ModuleDict)

            if hasattr(from_module.parametrizations[parameter_name], "original"):
                to_module.parametrizations[parameter_name].original = \
                    from_module.parametrizations[parameter_name].original
            else:
                num = 0
                orig_num = "original" + str(num)
                while hasattr(from_module.parametrizations[parameter_name], orig_num):
                    setattr(
                        to_module.parametrizations[parameter_name],
                        orig_num,
                        getattr(from_module.parametrizations[parameter_name], orig_num),
                    )
                    num = num + 1
                    orig_num = "original" + str(num)

    return to_module
