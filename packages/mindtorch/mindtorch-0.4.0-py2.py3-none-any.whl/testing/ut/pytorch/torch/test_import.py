from mindtorch.module_hooker import torch_enable, torch_pop
from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_import():
    torch_enable()
    import torch
    import torchvision
    import torchaudio
    torch_pop()

if __name__ == '__main__':
    set_mode_by_env_config()
    test_import()