from mindspore.experimental.optim import Adamax as Adamax_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

class Adamax(_Optimizer, Adamax_MS):
    def __init__(self, params, lr=2e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0, foreach=None,
                 *, maximize=False, differentiable=False):
        unsupported_attr(foreach)
        _warn_differentiable(differentiable)
        Adamax_MS.__init__(self, params, lr, betas, eps, weight_decay, maximize=maximize)
        _Optimizer.__init__(self)
        self._state_map = {'exp_avg': 'exp_avg',
                           'exp_inf': 'exp_inf',
                           'step_t': 'step',
                           }

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
