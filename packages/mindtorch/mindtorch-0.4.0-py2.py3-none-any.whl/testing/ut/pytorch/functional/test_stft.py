#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from ...utils import set_mode_by_env_config, param_compare
set_mode_by_env_config()

def test_stft1():
    x = np.sin(2 * np.pi * 50 * np.linspace(0, 10, 2048)) + np.sin(
        2 * np.pi * 20 * np.linspace(0, 10, 2048)) + np.random.normal(scale=1, size=2048)

    ms_tensor = ms_torch.tensor(x)
    spec_ms_torch = ms_torch.stft(ms_tensor, n_fft=512, hop_length=128, center=False, pad_mode="reflect",
                                window=ms_torch.hann_window(window_length=512, periodic=True))
    rea_ms_torch = spec_ms_torch[:, :, 0]  # 实部
    imag_ms_torch = spec_ms_torch[:, :, 1]  # 虚部
    mag_ms_torch = ms_torch.abs(ms_torch.sqrt(ms_torch.pow(rea_ms_torch, 2) + ms_torch.pow(imag_ms_torch, 2)))
    # pha_ms_torch = ms_torch.atan2(imag_ms_torch.data, rea_ms_torch.data)

    torch_tensor = torch.tensor(x)
    spec_torch = torch.stft(torch_tensor, n_fft=512, hop_length=128, center=False, pad_mode="reflect",
                            window=torch.hann_window(window_length=512, periodic=True))
    rea_torch = spec_torch[:, :, 0]  # 实部
    imag_torch = spec_torch[:, :, 1]  # 虚部
    mag_torch = torch.abs(torch.sqrt(torch.pow(rea_torch, 2) + torch.pow(imag_torch, 2)))
    # pha_torch = torch.atan2(imag_torch.data, rea_torch.data)

    assert np.allclose(rea_ms_torch.asnumpy(), rea_torch.numpy(), 1e-2)

def test_stft2():
    x = np.sin(2 * np.pi * 50 * np.linspace(0, 10, 2048)) + np.sin(
        2 * np.pi * 20 * np.linspace(0, 10, 2048)) + np.random.normal(scale=1, size=2048)
    x = [x, x, x] # (B?, length)
    ms_tensor = ms_torch.tensor(x)
    spec_ms_torch = ms_torch.stft(ms_tensor, n_fft=512, hop_length=128, center=False, pad_mode="reflect",
                                window=ms_torch.hann_window(window_length=512, periodic=True))
    rea_ms_torch = spec_ms_torch[:, :, 0]  # 实部
    imag_ms_torch = spec_ms_torch[:, :, 1]  # 虚部
    mag_ms_torch = ms_torch.abs(ms_torch.sqrt(ms_torch.pow(rea_ms_torch, 2) + ms_torch.pow(imag_ms_torch, 2)))
    # pha_ms_torch = ms_torch.atan2(imag_ms_torch.data, rea_ms_torch.data)

    torch_tensor = torch.tensor(x)
    spec_torch = torch.stft(torch_tensor, n_fft=512, hop_length=128, center=False, pad_mode="reflect",
                            window=torch.hann_window(window_length=512, periodic=True))
    rea_torch = spec_torch[:, :, 0]  # 实部
    imag_torch = spec_torch[:, :, 1]  # 虚部
    mag_torch = torch.abs(torch.sqrt(torch.pow(rea_torch, 2) + torch.pow(imag_torch, 2)))
    # pha_torch = torch.atan2(imag_torch.data, rea_torch.data)

    assert np.allclose(rea_ms_torch.asnumpy(), rea_torch.numpy(), 1e-2)

def test_istft1():
    x = np.sin(2 * np.pi * 50 * np.linspace(0, 10, 2048)) + np.sin(
        2 * np.pi * 20 * np.linspace(0, 10, 2048)) + np.random.normal(scale=1, size=2048)
    spec_torch = torch.stft(torch.tensor(x), n_fft=512, hop_length=160, return_complex=True, onesided=True)
    istft_torch = torch.istft(spec_torch, n_fft=512, hop_length=160)

    spec_mstorch = ms_torch.stft(ms_torch.tensor(x), n_fft = 512, hop_length = 160, return_complex=True, onesided=True)
    istft_mstorch = ms_torch.istft(spec_mstorch, n_fft = 512, hop_length = 160)

    assert np.allclose(istft_torch.numpy(), istft_mstorch.asnumpy(), 1e-2)

def test_istft2():
    x = np.sin(2 * np.pi * 50 * np.linspace(0, 10, 2048)) + np.sin(
        2 * np.pi * 20 * np.linspace(0, 10, 2048)) + np.random.normal(scale=1, size=2048)
    x = [x, x, x]

    spec_torch = torch.stft(torch.tensor(x), n_fft=512, hop_length=160, return_complex=True, onesided=True)
    istft_torch = torch.istft(spec_torch, n_fft=512, hop_length=160)

    spec_mstorch = ms_torch.stft(ms_torch.tensor(x), n_fft=512, hop_length=160, return_complex=True, onesided=True)
    istft_mstorch = ms_torch.istft(spec_mstorch, n_fft=512, hop_length=160)

    assert np.allclose(istft_torch.numpy(), istft_mstorch.asnumpy(), 1e-2)

if __name__ == '__main__':
    set_mode_by_env_config()
    test_stft1()
    test_stft2()
    test_istft1()
    test_istft2()
