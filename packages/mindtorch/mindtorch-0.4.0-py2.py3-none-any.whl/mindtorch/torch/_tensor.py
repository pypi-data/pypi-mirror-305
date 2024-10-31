from ._utils import _set_obj_state
def _rebuild_from_type(func, type, args, dict):
    from mindtorch.torch.tensor import Tensor # pylint: disable=R0401, C0415
    if type is Tensor:
        return func(*args)

    ret = func(*args).as_subclass(type)
    ret.__dict__ = dict
    return ret

def _rebuild_from_type_v2(func, new_type, args, state):
    from mindtorch.torch.tensor import Tensor # pylint: disable=R0401, C0415
    ret = func(*args)
    if not isinstance(ret, new_type):
        ret = ret.as_subclass(new_type)
    if getattr(ret.__class__, "__setstate__", Tensor.__setstate__) is not Tensor.__setstate__:
        ret.__setstate__(state)
    else:
        ret = _set_obj_state(ret, state)
    return ret
