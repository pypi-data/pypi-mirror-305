import os
import mindtorch.torch as torch
import multiprocessing as mp


from ...utils import set_mode_by_env_config, SKIP_ENV_CPU, is_test_under_ascend_context, is_test_under_gpu_context

set_mode_by_env_config()

@SKIP_ENV_CPU(reason='not support on CPU.')
def test_simple_interface():
    print(torch.cuda.set_device(0))
    print(torch.cuda.get_arch_list())
    print(torch.cuda.current_device())
    print(torch.cuda.device_count())
    print(torch.cuda.is_initialized())
    print(torch.cuda.is_available())

@SKIP_ENV_CPU(reason='not support on CPU.')
def test_cuda_get_device_name():
    current_device = torch.cuda.current_device()
    current_device_name = torch.cuda.get_device_name(current_device)
    device_name_None = torch.cuda.get_device_name(None)
    assert current_device_name == device_name_None

    # Testing the behaviour for No argument
    device_name_no_argument = torch.cuda.get_device_name()
    assert current_device_name == device_name_no_argument

@SKIP_ENV_CPU(reason='not support on CPU.')
def test_cuda_get_device_capability():
    # Testing the behaviour with None as an argument
    current_device = torch.cuda.current_device()
    current_device_capability = torch.cuda.get_device_capability(current_device)
    device_capability_None = torch.cuda.get_device_capability(None)
    assert current_device_capability == device_capability_None

    # Testing the behaviour for No argument
    device_capability_no_argument = torch.cuda.get_device_capability()
    assert current_device_capability == device_capability_no_argument


if __name__ == '__main__':
    test_simple_interface()
    test_cuda_get_device_name()
    test_cuda_get_device_capability()
