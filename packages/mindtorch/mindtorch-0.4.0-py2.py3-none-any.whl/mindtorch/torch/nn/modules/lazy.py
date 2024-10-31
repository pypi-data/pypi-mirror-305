import itertools
from typing_extensions import Protocol

from mindspore import _no_grad as torch_no_grad
from mindtorch.torch.logging import warning
from mindtorch.utils import unsupported_attr
from ..parameter import is_lazy


class _LazyProtocol(Protocol):
    def _register_load_state_dict_pre_hook(self, hook):
        ...

    def register_forward_pre_hook(self, hook):
        ...

    def _lazy_load_hook(
            self, state_dict, prefix, local_metadata, strict,
            missing_keys, unexpected_keys, error_msgs):
        ...

    def _get_name(self):
        ...

    def _infer_parameters(self, module, input):
        ...

    @property
    def _parameters(self):
        ...

    @property
    def _buffers(self):
        ...

    @property
    def _non_persistent_buffers_set(self):
        ...

    @property
    def _load_hook(self):
        ...

    @property
    def _initialize_hook(self):
        ...


class LazyModuleMixin:

    cls_to_become = None

    def __init__(self: _LazyProtocol, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._load_hook = self._register_load_state_dict_pre_hook(self._lazy_load_hook)
        self._initialize_hook = self.register_forward_pre_hook(self._infer_parameters)
        warning('Lazy modules are a new feature under heavy development '
                'so changes to the API or functionality can happen at any moment.')

    def _save_to_state_dict(self: _LazyProtocol, destination, prefix, keep_vars):
        for name, param in self._parameters.items():
            if param is not None:
                if not (is_lazy(param) or keep_vars):
                    param = param.detach()
                destination[prefix + name] = param
        for name, buf in self._buffers.items():
            if buf is not None and name not in self._non_persistent_buffers_set:
                if not (is_lazy(buf) or keep_vars):
                    buf = buf.detach()
                destination[prefix + name] = buf

    def _lazy_load_hook(
            self: _LazyProtocol, state_dict, prefix, local_metadata, strict,
            missing_keys, unexpected_keys, error_msgs):
        unsupported_attr(local_metadata)
        unsupported_attr(strict)
        unsupported_attr(missing_keys)
        unsupported_attr(unexpected_keys)
        unsupported_attr(error_msgs)
        for name, param in itertools.chain(self._parameters.items(), self._buffers.items()):
            key = prefix + name
            if key in state_dict and param is not None:
                input_param = state_dict[key]
                if is_lazy(param):
                    if not is_lazy(input_param):
                        with torch_no_grad():
                            param.materialize(input_param.shape)

    def initialize_parameters(self: _LazyProtocol, *args, **kwargs):
        raise NotImplementedError('initialize_parameters is not implemented for {}'.format(self.__class__.__name__))

    def has_uninitialized_params(self: _LazyProtocol):
        params = self._parameters.values()
        buffers = self._buffers.values()
        for param in itertools.chain(params, buffers):
            if is_lazy(param):
                return True
        return False

    def _infer_parameters(self: _LazyProtocol, module, input):
        module.initialize_parameters(*input)
        if module.has_uninitialized_params():
            raise RuntimeError('module {} has not been fully initialized'.format(self._get_name()))
        module._initialize_hook.remove()
        module._load_hook.remove()
        delattr(module, '_initialize_hook')
        delattr(module, '_load_hook')
        if module.cls_to_become is not None:
            module.__class__ = module.cls_to_become


    def _replicate_for_data_parallel(self: _LazyProtocol):
        raise RuntimeError('Modules with uninitialized parameters can\'t be used with `DataParallel`. '
                           'Run a dummy forward pass to correctly initialize the modules')
