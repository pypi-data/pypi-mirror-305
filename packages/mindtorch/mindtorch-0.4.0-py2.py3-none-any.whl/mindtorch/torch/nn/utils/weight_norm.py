import mindspore as ms
from mindtorch.torch.nn.parameter import Parameter, UninitializedParameter
from mindtorch.torch.tensor import cast_to_adapter_tensor, cast_to_ms_tensor


def _norm(p, dim):
    """Computes the norm over all dimensions except dim"""
    if dim is None:
        return p.norm()
    elif dim == 0:
        output_size = (p.size(0),) + (1,) * (p.dim() - 1)
        ms_p = cast_to_ms_tensor(p)
        out = ms.ops.norm(ms_p.view(p.size(0), -1), ord=None, dim=1, keepdim=False)
        out = out.view(*output_size)
        return cast_to_adapter_tensor(out)
    elif dim == p.dim() - 1:
        output_size = (1,) * (p.dim() - 1) + (p.size(-1),)
        ms_p = cast_to_ms_tensor(p)
        out = ms.ops.norm(ms_p.view(-1, p.size(-1)), ord=None, dim=0, keepdim=False)
        out = out.view(*output_size)
        return cast_to_adapter_tensor(out)
    else:
        return _norm(p.transpose(0, dim), 0).transpose(0, dim)


class WeightNorm():
    name: str
    dim: int

    def __init__(self, name, dim):
        if dim is None:
            dim = -1
        self.name = name
        self.dim = dim

    # TODO Make return type more specific
    def compute_weight(self, module):
        g = getattr(module, self.name + '_g')
        v = getattr(module, self.name + '_v')
        return v * (g / _norm(v, self.dim))

    @staticmethod
    def apply(module, name, dim):
        for _, hook in module._forward_pre_hooks.items():
            if isinstance(hook, WeightNorm) and hook.name == name:
                raise RuntimeError("Cannot register two weight_norm hooks on "
                                   "the same parameter {}".format(name))

        if dim is None:
            dim = -1

        fn = WeightNorm(name, dim)

        weight = getattr(module, name)

        if isinstance(weight, UninitializedParameter):
            raise ValueError(
                'The module passed to `WeightNorm` can\'t have uninitialized parameters. '
                'Make sure to run the dummy forward before applying weight normalization')

        # remove w from parameter list
        del module._parameters[name]

        # add g and v as new parameters and express w as g/||v|| * v
        module.register_parameter(name + '_g', Parameter(_norm(weight, dim).data))
        module.register_parameter(name + '_v', Parameter(weight.data))
        setattr(module, name, fn.compute_weight(module))

        # recompute weight before every forward()
        module.register_forward_pre_hook(fn)

        return fn

    def remove(self, module):
        weight = self.compute_weight(module)
        delattr(module, self.name)
        del module._parameters[self.name + '_g']
        del module._parameters[self.name + '_v']
        setattr(module, self.name, Parameter(weight.data))

    def __call__(self, module, inputs):
        setattr(module, self.name, self.compute_weight(module))


def weight_norm(module, name='weight', dim=0):
    WeightNorm.apply(module, name, dim)
    return module


def remove_weight_norm(module, name='weight'):
    for k, hook in module._forward_pre_hooks.items():
        if isinstance(hook, WeightNorm) and hook.name == name:
            hook.remove(module)
            del module._forward_pre_hooks[k]
            return module

    raise ValueError("weight_norm of '{}' not found in {}"
                     .format(name, module))
