from mindspore.experimental.optim import Adagrad as Adagrad_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

class Adagrad(_Optimizer, Adagrad_MS):
    def __init__(self, params, lr=1e-2, lr_decay=0, weight_decay=0, initial_accumulator_value=0,
                 eps=1e-10, foreach=None, *, maximize=False, differentiable=False):
        unsupported_attr(foreach)
        _warn_differentiable(differentiable)
        Adagrad_MS.__init__(self, params, lr, lr_decay, weight_decay, initial_accumulator_value,
                            eps, maximize=maximize)
        _Optimizer.__init__(self)
        self._state_map = {'accum': 'sum', 'step_t': 'step'}

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
