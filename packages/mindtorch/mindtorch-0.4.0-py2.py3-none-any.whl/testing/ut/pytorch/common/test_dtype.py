import mindtorch.torch as ms_torch
from ...utils import set_mode_by_env_config

set_mode_by_env_config()

def test_torch_dtype():
    assert isinstance(ms_torch.float32, ms_torch.dtype)
    assert isinstance(ms_torch.int8, ms_torch.dtype)

if __name__ == '__main__':
    test_torch_dtype()
