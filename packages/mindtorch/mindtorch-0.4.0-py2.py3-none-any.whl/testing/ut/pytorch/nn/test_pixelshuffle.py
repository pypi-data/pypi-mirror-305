import mindtorch.torch as ms_torch
import numpy as np
import torch


from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_pixelshuffle():
    data = np.random.randn(1, 9 ,4, 4).astype(np.float32)

    pixel_shuffle = torch.nn.PixelShuffle(3)
    input = torch.tensor(data)
    torch_output = pixel_shuffle(input)

    pixel_shuffle = ms_torch.nn.PixelShuffle(3)
    input = ms_torch.tensor(data)
    ms_output = pixel_shuffle(input)

    assert np.allclose(torch_output.numpy(), ms_output.numpy())

def test_pixelunshuffle():
    data = np.random.randn(1, 1 ,12, 12).astype(np.float32)

    pixel_unshuffle = torch.nn.PixelUnshuffle(3)
    input = torch.tensor(data)
    torch_output = pixel_unshuffle(input)

    pixel_unshuffle = ms_torch.nn.PixelUnshuffle(3)
    input = ms_torch.tensor(data)
    ms_output = pixel_unshuffle(input)

    assert np.allclose(torch_output.numpy(), ms_output.numpy())


if __name__ == '__main__':
    set_mode_by_env_config()
    test_pixelshuffle()
    test_pixelunshuffle()