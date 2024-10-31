from mindspore.experimental.optim import AdamW as AdamW_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

class AdamW(_Optimizer, AdamW_MS):
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=1e-2, amsgrad=False,
                 *, maximize=False, foreach=None, capturable=False, differentiable=False, fused=None):
        unsupported_attr(foreach)
        unsupported_attr(capturable)
        unsupported_attr(fused)
        _warn_differentiable(differentiable)
        AdamW_MS.__init__(self, params, lr, betas, eps, weight_decay, amsgrad, maximize=maximize)
        _Optimizer.__init__(self)
        self._state_map = {
            'exp_avg':'exp_avg',
            'exp_avg_sq':'exp_avg_sq',
            'max_exp_avg_sq':'max_exp_avg_sq',
            'state_step':'step',
        }

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)
