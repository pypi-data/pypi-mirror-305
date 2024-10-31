import contextlib
from mindtorch.utils import unsupported_attr

__all__ = ["functional_call"]


def _change_class(module, params_and_buffers):
    cls = module.__class__
    attr_to_path = module._attr_to_path

    def _getattribute(self, name):
        if name in attr_to_path:
            return params_and_buffers[attr_to_path[name]]
        return cls.__getattribute__(self, name)

    def _setattr(self, name, value):
        if name in attr_to_path:
            params_and_buffers[attr_to_path[name]] = value
            return params_and_buffers[attr_to_path[name]]
        return cls.__setattr__(self, name, value)

    param_cls = type(
        f"StatelessReplacer{cls.__name__}",
        (cls,),
        {
            "__getattribute__": _getattribute,
            "__setattr__": _setattr,
        },
    )

    module.__class__ = param_cls
    module._orig_class = cls

def _create_swap_params(params_and_buffers):
    def _swap_parameters(module, tensor_name, full_path, tensor):
        unsupported_attr(tensor)
        if hasattr(module, "_attr_to_path"):
            module._attr_to_path[tensor_name] = full_path
        else:
            module._attr_to_path = {}
            module._attr_to_path[tensor_name] = full_path
            _change_class(module, params_and_buffers)
    return _swap_parameters


def _remove_swap(module, name, full_path):
    if hasattr(module, "_orig_class"):
        module.__class__ = module._orig_class
        delattr(module, "_orig_class")
        delattr(module, "_attr_to_path")
    unsupported_attr(name)
    unsupported_attr(full_path)


@contextlib.contextmanager
def _reparametrize_module(module, parameters_and_buffers):
    for name, tensor in parameters_and_buffers.items():
        _apply_func_submodules(
            _create_swap_params(parameters_and_buffers),
            module, name.split("."), name, (tensor,))
    try:
        yield
    finally:
        for name in parameters_and_buffers:
            _apply_func_submodules(
                _remove_swap,
                module, name.split("."), name, ())


def _apply_func_submodules(func, module, path, full_path, args):
    if len(path) == 1:
        func(module, path[0], full_path, *args)
    else:
        _apply_func_submodules(func, getattr(module, path[0]), path[1:], full_path, args)


def functional_call(module, parameters_and_buffers, args, kwargs=None):
    # TODO allow kwargs such as unsafe and others for parametrization
    # TODO: Currently, jit function is not supported.
    # if (
    #         torch.jit.is_tracing()
    #         or torch.jit.is_scripting()
    #         or isinstance(module, (
    #             torch.jit.RecursiveScriptModule,
    #             torch.jit.ScriptModule,
    #             torch.jit.ScriptFunction)
    #         )
    # ):
    #     raise RuntimeError("The stateless API can't be used with Jitted modules")
    if kwargs is None:
        kwargs = {}
    with _reparametrize_module(module, parameters_and_buffers):
        if isinstance(args, tuple):
            out = module(*args, **kwargs)
        else:
            out = module(args, **kwargs)
    return out
