from mindspore.experimental.optim import Adadelta as Adadelta_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

class Adadelta(_Optimizer, Adadelta_MS):
    def __init__(self, params, lr=1.0, rho=0.9, eps=1e-6, weight_decay=0, foreach=None, *,
                 maximize=False, differentiable=False):
        unsupported_attr(foreach)
        _warn_differentiable(differentiable)
        Adadelta_MS.__init__(self, params, lr, rho, eps, weight_decay, maximize=maximize)
        _Optimizer.__init__(self)
        self._state_map = {'accum': 'square_avg', 'accum_update': 'acc_delta'}

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
