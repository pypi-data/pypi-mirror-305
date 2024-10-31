from mindspore.experimental.optim import SGD as SGD_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

_default_lr = 0.01
class SGD(_Optimizer, SGD_MS):
    def __init__(self, params, lr=None, momentum=0, dampening=0,
                 weight_decay=0, nesterov=False, *, maximize=False, foreach=None,
                 differentiable=False):
        unsupported_attr(foreach)
        _warn_differentiable(differentiable)
        if lr is None:
            for p_dict in params:
                if not isinstance(p_dict, dict) or 'lr' not in p_dict:
                    raise ValueError("parameter group didn't specify a value of required optimization parameter lr.")
            # Fake lr. The above code guarantees that every param_group has its own 'lr' setting.
            # So the following _default_lr won't take effect, just for the input args of mindspore SGD.
            lr = _default_lr
        SGD_MS.__init__(self, params, lr, momentum, dampening, weight_decay, nesterov, maximize=maximize)
        _Optimizer.__init__(self)
        self._state_map = {'accum': 'momentum_buffer'}

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        for group in state_dict['param_groups']:
            group['momentum'] = float(group['momentum'])
            group['dampening'] = float(group['dampening'])
            group['weight_decay'] = float(group['weight_decay'])
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
