from mindspore.experimental.optim import AdamW as AdamW_MS
from mindspore.experimental.optim.adamw import prepare_func
from mindspore.ops import functional as F, composite as C, operations as P
from mindspore import ops, Parameter, ParameterTuple
import mindspore.common.dtype as mstype
from mindtorch.torch.optim.optimizer import _Optimizer, _warn_differentiable
from mindtorch.utils import unsupported_attr

op_mul = P.Mul()
op_pow = P.Pow()
op_sqrt = P.Sqrt()
op_maximum = P.Maximum()
hyper_map = C.HyperMap()

_adamw_opt = C.MultitypeFuncGraph("adamw_opt")

@_adamw_opt.register("Tensor", "Tensor", "Bool", "Float", "Tensor", "Float", "Float", "Tensor", "Tensor",
                     "Tensor", "Tensor", "Tensor")
def _run_adamw_opt(weight_decay_new, step_size, amsgrad, eps, bias_correction2_sqrt, beta1, beta2, param, grad,
                   exp_avg, exp_avg_sq, max_exp_avg_sq):
    """Apply adamw optimizer to the weight parameter."""
    success = True
    next_param = op_mul(param, weight_decay_new)
    F.assign(exp_avg, op_mul(exp_avg, beta1) + op_mul(grad, 1 - beta1))
    F.assign(exp_avg_sq, ops.addcmul(op_mul(exp_avg_sq, beta2), grad, grad, 1 - beta2))

    if amsgrad:
        next_max_exp_avg = op_maximum(max_exp_avg_sq, exp_avg_sq)
        denom = op_sqrt(next_max_exp_avg) / bias_correction2_sqrt + eps
        F.assign(max_exp_avg_sq, next_max_exp_avg)
    else:
        denom = op_sqrt(exp_avg_sq) / bias_correction2_sqrt + eps

    return_param = next_param - op_mul(exp_avg / denom, step_size)
    F.assign(param, return_param.astype(param.dtype))
    return success


# TODO: this is experimental, will be change in the future.
# This AdamW is for float32 params and grad.
# only can be run under pynative.
class Float32AdamW(_Optimizer, AdamW_MS):
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

        def cast_to_float32(xs):
            new = []
            for p in xs:
                new_ = Parameter(p.astype(mstype.float32))
                new_.name = p.name
                new.append(new_)
            return ParameterTuple(new)

        self.exp_avg = cast_to_float32(self.exp_avg)
        self.exp_avg_sq = cast_to_float32(self.exp_avg_sq)
        self.max_exp_avg_sq = cast_to_float32(self.max_exp_avg_sq)

    def state_dict(self):
        return _Optimizer._ms_state_dict(self, self._state_map)

    def load_state_dict(self, state_dict):
        return _Optimizer._ms_load_state_dict(self, state_dict, self._state_map)

    def implementation(self, lr, weight_decay, beta1, beta2, amsgrad, eps, params, grads, start_id, end_id):
        """Extract the common computing part for acceleration"""
        weight_decay_new, step_size, bias_correction2_sqrt = prepare_func(lr, weight_decay,
                                                                          self.state_step, beta1, beta2)
        self.hyper_map(F.partial(_adamw_opt, weight_decay_new, step_size, amsgrad,
                                 eps, bias_correction2_sqrt, beta1, beta2),
                       params, grads, self.exp_avg[start_id: end_id],
                       self.exp_avg_sq[start_id: end_id], self.max_exp_avg_sq[start_id: end_id])
        return True

    def construct(self, gradients):
        self.assignadd(self.state_step, self.increase_tensor)
        for group_id, group in enumerate(self.param_groups):
            beta1, beta2 = group['betas']
            start_id = self.group_start_id[group_id]
            end_id = self.group_start_id[group_id + 1]
            lr = self.lrs[group_id]
            if isinstance(group.get("lr"), float):
                lr = self.op_cast(group.get("lr"), mstype.float32)
            grads = (grad if not group.get("maximize") else F.neg(grad) for grad in gradients[start_id: end_id])

            params = self.param_groups[group_id]['params']
            self.implementation(lr, group.get("weight_decay"), beta1, beta2, group.get("amsgrad"), group.get("eps"),
                                params, grads, start_id, end_id)

        return True

    def step(self, grads=None, closure=None):
        loss = None
        if closure is not None:
            loss = closure()
        if grads is None:
            grads = []
            for param_group in self.param_groups:
                for param in param_group['params']:
                    _grad = param.grad if param.grad is not None else F.zeros_like(param)
                    grads.append(_grad)
            grads = tuple(grads)
        ret = self.construct(grads)
        if closure is not None:
            ret = loss
        return ret
