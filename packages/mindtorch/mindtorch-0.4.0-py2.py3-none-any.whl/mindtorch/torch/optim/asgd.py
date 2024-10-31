from mindspore.experimental.optim import ASGD as ASGD_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

class ASGD(_Optimizer, ASGD_MS):
    def __init__(self, params, lr=1e-2, lambd=1e-4, alpha=0.75, t0=1e6, weight_decay=0,
                 foreach=None, maximize=False, differentiable=False):
        unsupported_attr(foreach)
        _warn_differentiable(differentiable)
        ASGD_MS.__init__(self, params, lr, lambd, alpha, t0, weight_decay, maximize)
        _Optimizer.__init__(self)
        self._state_map = {'eta':'eta',
                           'mu':'mu',
                           'ax':'ax',
                           'step_t':'step',
                           }

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
