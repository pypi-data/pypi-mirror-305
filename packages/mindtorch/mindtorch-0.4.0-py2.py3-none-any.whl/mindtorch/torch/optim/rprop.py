from mindspore.experimental.optim import Rprop as Rprop_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

class Rprop(_Optimizer, Rprop_MS):
    def __init__(self, params, lr=1e-2, etas=(0.5, 1.2), step_sizes=(1e-6, 50), *, foreach=None,
                 maximize=False, differentiable=False):
        unsupported_attr(foreach)
        _warn_differentiable(differentiable)
        Rprop_MS.__init__(self, params, lr, etas, step_sizes, maximize=maximize)
        _Optimizer.__init__(self)
        self._state_map = {'step_size':'step_size',
                           'prev':'prev',
                           }

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
