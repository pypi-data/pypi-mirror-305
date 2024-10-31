from mindspore.experimental.optim import RMSprop as RMSprop_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

class RMSprop(_Optimizer, RMSprop_MS):
    def __init__(self, params, lr=1e-2, alpha=0.99, eps=1e-8, weight_decay=0, momentum=0,
                 centered=False, foreach=None, maximize=False, differentiable=False):
        unsupported_attr(foreach)
        _warn_differentiable(differentiable)
        RMSprop_MS.__init__(self, params, lr, alpha, eps, weight_decay, momentum, centered, maximize)
        _Optimizer.__init__(self)
        self._state_map = {'mean_grad':'grad_avg',
                           'mean_square':'square_avg',
                           'moment':'momentum_buffer',
                           }

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
