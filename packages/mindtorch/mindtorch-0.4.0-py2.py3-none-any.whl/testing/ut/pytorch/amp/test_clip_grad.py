import mindspore as ms
import torch

from ...utils import param_compare, SKIP_ENV_GRAPH_MODE, enable_backward
import mindtorch.torch as ms_torch

    
@SKIP_ENV_GRAPH_MODE(reason="clip_grad_norm_ not support graph mode.")
def test_clip_grad_norm_():
    max_norm = 2
    norm_type = 2.0

    l = ms_torch.nn.Linear(2, 2)
    ms_grads = ms.ops.arange(1., 5).view(2, 2), ms.ops.ones(2).div(1000)
    ms_total_norm = ms_torch.nn.utils.clip_grad_norm_(l.parameters(), max_norm, grads=ms_grads,
                                                      norm_type=norm_type)

    l = torch.nn.Linear(2, 2)
    grads = torch.arange(1., 5).view(2, 2), torch.ones(2).div(1000)
    for p, g in zip(l.parameters(), grads):
        p._grad = g.clone().view_as(p.data)
    pt_total_norm = torch.nn.utils.clip_grad_norm_(l.parameters(), max_norm,
                                                   norm_type=norm_type)

    ms_grad_norm1 = ms_torch.norm(ms_torch.cast_to_adapter_tensor(ms_grads[0]))
    ms_grad_norm2 = ms_torch.norm(ms_torch.cast_to_adapter_tensor(ms_grads[1]))
    _param = list(l.parameters())
    pt_grad_norm1 = torch.norm(_param[0]._grad)
    pt_grad_norm2 = torch.norm(_param[1]._grad)
    param_compare(ms_total_norm, pt_total_norm)
    param_compare(ms_grad_norm1, pt_grad_norm1)
    param_compare(ms_grad_norm2, pt_grad_norm2)
    param_compare(ms_grads[0], _param[0]._grad)
    param_compare(ms_grads[1], _param[1]._grad)

@SKIP_ENV_GRAPH_MODE(reason="clip_grad_norm_ not support graph mode.")
def test_clip_grad_value_():
    def test_case(value):
        l = ms_torch.nn.Linear(10, 10)
        ms_grads = ms.ops.arange(-50., 50).view(10, 10).div(5), ms.ops.ones(10).mul(2)
        ms_torch.nn.utils.clip_grad_value_(l.parameters(), value, grads=ms_grads)

        l = torch.nn.Linear(10, 10)
        grads = torch.arange(-50., 50).view(10, 10).div_(5), torch.ones(10).mul_(2)
        for p, g in zip(l.parameters(), grads):
            p._grad = g.clone().view_as(p.data)
        torch.nn.utils.clip_grad_value_(l.parameters(), value)

        _param = list(l.parameters())
        param_compare(ms_grads[0], _param[0]._grad)
        param_compare(ms_grads[1], _param[1]._grad)

    for value in [2.5, -2.5]:
        test_case(value)

@SKIP_ENV_GRAPH_MODE(reason="clip_grad_norm_ not support graph mode.")
def test_clip_grad_norm_autograd():
    with enable_backward():
        max_norm = 2
        norm_type = 2.0

        l = ms_torch.nn.Linear(2, 2)
        ms_grads = ms.ops.arange(1., 5).view(2, 2), ms.ops.ones(2).div(1000)
        for p, g in zip(l.parameters(), ms_grads):
            p.grad = g
        ms_total_norm = ms_torch.nn.utils.clip_grad_norm_(l.parameters(), max_norm,
                                                          norm_type=norm_type)
        _ms_param = list(l.parameters())
        ms_grad_norm1 = ms_torch.norm(ms_torch.cast_to_adapter_tensor(_ms_param[0].grad))
        ms_grad_norm2 = ms_torch.norm(ms_torch.cast_to_adapter_tensor(_ms_param[1].grad))

        l = torch.nn.Linear(2, 2)
        grads = torch.arange(1., 5).view(2, 2), torch.ones(2).div(1000)
        for p, g in zip(l.parameters(), grads):
            p.grad = g.clone().view_as(p.data)
        pt_total_norm = torch.nn.utils.clip_grad_norm_(l.parameters(), max_norm,
                                                    norm_type=norm_type)
        _param = list(l.parameters())
        pt_grad_norm1 = torch.norm(_param[0].grad)
        pt_grad_norm2 = torch.norm(_param[1].grad)

        param_compare(ms_total_norm, pt_total_norm)
        param_compare(ms_grad_norm1, pt_grad_norm1)
        param_compare(ms_grad_norm2, pt_grad_norm2)
        param_compare(_ms_param[0].grad, _param[0].grad)
        param_compare(_ms_param[1].grad, _param[1].grad)

@SKIP_ENV_GRAPH_MODE(reason="clip_grad_norm_ not support graph mode.")
def test_clip_grad_value_autograd():
    def test_case(value):
        l = ms_torch.nn.Linear(10, 10)
        ms_grads = ms.ops.arange(-50., 50).view(10, 10).div(5), ms.ops.ones(10).mul(2)
        for p, g in zip(l.parameters(), ms_grads):
            p.grad = g
        ms_torch.nn.utils.clip_grad_value_(l.parameters(), value)
        ms_param = list(l.parameters())

        l = torch.nn.Linear(10, 10)
        grads = torch.arange(-50., 50).view(10, 10).div_(5), torch.ones(10).mul_(2)
        for p, g in zip(l.parameters(), grads):
            p.grad = g.clone().view_as(p.data)
        torch.nn.utils.clip_grad_value_(l.parameters(), value)
        _param = list(l.parameters())

        param_compare(ms_param[0].grad, _param[0].grad)
        param_compare(ms_param[1].grad, _param[1].grad)

    with enable_backward():
        for value in [2.5, -2.5]:
            test_case(value)

if __name__ == '__main__':
    test_clip_grad_norm_()
    test_clip_grad_value_()
    test_clip_grad_norm_autograd()
    test_clip_grad_value_autograd()
