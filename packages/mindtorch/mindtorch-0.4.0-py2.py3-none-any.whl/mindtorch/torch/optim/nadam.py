from mindspore.experimental.optim import NAdam as NAdam_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

class NAdam(_Optimizer, NAdam_MS):
    def __init__(self, params, lr=2e-3, betas=(0.9, 0.999), eps=1e-8,
                 weight_decay=0, momentum_decay=4e-3, *, foreach=None, differentiable=False):
        unsupported_attr(foreach)
        _warn_differentiable(differentiable)
        NAdam_MS.__init__(self, params, lr, betas, eps, weight_decay, momentum_decay)
        _Optimizer.__init__(self)
        self._state_map = {
            'exp_avg':'exp_avg',
            'exp_avg_sq':'exp_avg_sq',
            'mu_product':'mu_product',
            'step_t':'step',
        }

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
