#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import mindtorch.torch as ms_torch
import mindspore as ms
import numpy as np
from mindspore import jit, grad

user_stream1 = ms_torch.cuda.Stream()
user_stream2 = ms_torch.cuda.Stream()

from ...utils import set_mode_by_env_config, SKIP_ENV_CPU
set_mode_by_env_config()

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_args():
    stream1 = ms_torch.cuda.Stream()
    assert stream1 is not None
    stream2 = ms_torch.cuda.Stream(priority=0)
    assert stream2 is not None
    curr_stream = ms_torch.cuda.current_stream()
    stream3 = ms_torch.cuda.Stream(stream=curr_stream)
    assert stream3 is not None

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_repr():
    stream = ms_torch.cuda.current_stream()
    stream_str = repr(stream)
    assert "Stream(device_name=" in stream_str

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_eq():
    default_stream = ms_torch.cuda.current_stream()
    user_stream = user_stream1
    assert ms_torch.cuda.current_stream() == default_stream
    assert default_stream != user_stream
    with ms_torch.cuda.stream(user_stream):
        assert ms_torch.cuda.current_stream() == user_stream
    assert ms_torch.cuda.current_stream() == default_stream

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_hash():
    stream1 = user_stream1
    stream2 = user_stream2
    stream3 = ms_torch.cuda.Stream(stream=stream2)

    assert stream1 != stream2
    assert hash(stream1) != hash(stream2)
    assert stream2 == stream3
    assert hash(stream2) == hash(stream3)

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_query():
    a = ms_torch.ones(1024, 2048, dtype=ms_torch.float32, device="cuda")
    b = ms_torch.ones(2048, 4096, dtype=ms_torch.float32, device="cuda")
    stream1 = user_stream1

    with ms_torch.cuda.stream(stream1):
        ms_torch.mm(a, b).to('cuda')

    stream1.synchronize()
    assert stream1.query() is True

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_record_event():
    stream1 = user_stream1
    curr_stream = ms_torch.cuda.current_stream()
    event = ms_torch.cuda.Event()

    # A with large shape to ensure it run for a long time and stream1 will be synchronized by current stream.
    A = ms_torch.rand(5000, 5000, device="cuda")
    with ms_torch.cuda.stream(stream1):
        ms_torch.mm(A, A).to("cuda")
        stream1.record_event(event)

    curr_stream.wait_event(event)
    curr_stream.synchronize()
    assert event.query() is True

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_synchronize():
    stream1 = user_stream1

    # A with large shape to ensure it run for a long time and will be synchronized by stream1.
    A = ms_torch.rand(5000, 5000, device="cuda")
    with ms_torch.cuda.stream(stream1):
        ms_torch.mm(A, A).to("cuda")

    stream1.synchronize()
    assert stream1.query() is True

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_wait_event():
    stream1 = user_stream1
    stream2 = user_stream2
    event = ms_torch.cuda.Event()

    # A with large shape to ensure it run for a long time and will be synchronized by stream2.
    A = ms_torch.rand(5000, 5000, device="cuda")
    with ms_torch.cuda.stream(stream1):
        B = ms_torch.mm(A, A).to("cuda")
        event.record(stream1)

    with ms_torch.cuda.stream(stream2):
        stream2.wait_event(event)
        C = ms_torch.mm(B, B).to("cuda")

    ms_torch.cuda.synchronize()
    assert event.query() is True
    assert np.allclose(ms_torch.mm(A, A).numpy(), B.numpy())
    assert np.allclose(ms_torch.mm(B, B).numpy(), C.numpy())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_Stream_wait_stream():
    stream1 = user_stream1
    stream2 = user_stream2

    A = ms_torch.rand(5000, 5000, device="cuda")
    with ms_torch.cuda.stream(stream1):
        B = ms_torch.mm(A, A).to("cuda")

    with ms_torch.cuda.stream(stream2):
        stream2.wait_stream(stream1)
        C = ms_torch.mm(B, B).to("cuda")

    ms_torch.cuda.synchronize()
    assert np.allclose(ms_torch.mm(A, A).numpy(), B.numpy())
    assert np.allclose(ms_torch.mm(B, B).numpy(), C.numpy())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_jit_stream():
    stream1 = user_stream1
    event = ms_torch.cuda.Event()
    a = ms_torch.ones([1, 2], dtype=ms_torch.float32, device="cuda")
    b = ms_torch.ones([2], dtype=ms_torch.float32, device="cuda")
    a *= 4
    event.record()
    with ms_torch.cuda.stream(stream1):
        stream1.wait_event(event)
        @jit
        def jit_func():
            return a + 2
        c = jit_func()
        d = ms_torch.mm(c, b)

    ms_torch.cuda.synchronize()
    assert np.allclose(d.numpy(), ms_torch.mm((a + 2), b).numpy())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_grad_stream():
    def func(x):
        return ms_torch.sin(x)
    grad_fn = grad(func)

    a = ms_torch.tensor([0.62, 0.29, 0.45, 0.38], dtype=ms_torch.float32, device="cuda")
    stream1 = user_stream1
    event = ms_torch.cuda.Event()
    a *= 4
    event.record()
    with ms_torch.cuda.stream(stream1):
        stream1.wait_event(event)
        grad_a = grad_fn(a)

    ms_torch.cuda.synchronize()
    assert np.allclose(grad_fn(a).numpy(), grad_a.numpy())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_data_dependency_between_streams():
    prev_curr_stream = ms_torch.cuda.current_stream()
    stream1 = user_stream1
    stream2 = user_stream2
    event = ms_torch.cuda.Event(False, False, False)

    A = ms_torch.rand(500, 500, device="cuda")
    with ms_torch.cuda.stream(stream1):
        is_stream_stream1 = (ms_torch.cuda.current_stream() == stream1)
        B = ms_torch.mm(A, A).to("cuda")
    stream1.record_event(event)
    is_stream_prev_curr_stream_1 = (ms_torch.cuda.current_stream() == prev_curr_stream)
    stream2.wait_event(event)
    with ms_torch.cuda.stream(stream2):
        is_stream_stream2 = (ms_torch.cuda.current_stream() == stream2)
        C = ms_torch.mm(B, B).to("cuda")
    stream2.synchronize()
    is_stream_prev_curr_stream_2 = (ms_torch.cuda.current_stream() == prev_curr_stream)

    assert is_stream_stream1 is True
    assert is_stream_prev_curr_stream_1 is True
    assert is_stream_stream2 is True
    assert is_stream_prev_curr_stream_2 is True
    assert np.allclose(ms_torch.mm(A, A).numpy(), B.numpy())
    assert np.allclose(ms_torch.mm(B, B).numpy(), C.numpy())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Stream is not supported on cpu.")
def test_cuda_multi_streams():
    prev_curr_stream = ms_torch.cuda.current_stream()
    stream1 = user_stream1
    stream2 = user_stream2

    A = ms_torch.rand(5000, 5000, device="cuda")
    B = ms_torch.rand(5000, 5000, device="cuda")
    with ms_torch.cuda.stream(stream1):
        C = ms_torch.mm(A, A).to("cuda")
        is_stream1 = (ms_torch.cuda.current_stream() == stream1)
        with ms_torch.cuda.stream(stream2):
            is_stream2 = (ms_torch.cuda.current_stream() == stream2)
            D = ms_torch.mm(B, B).to("cuda")
        is_stream1_after = (ms_torch.cuda.current_stream() == stream1)
        stream2.synchronize()
    stream1.synchronize()

    is_prev_curr_stream = (ms_torch.cuda.current_stream() == prev_curr_stream)
    assert is_stream1 is True
    assert is_stream2 is True
    assert is_stream1_after is True
    assert is_prev_curr_stream is True
    assert np.allclose(ms_torch.mm(A, A).numpy(), C.numpy())
    assert np.allclose(ms_torch.mm(B, B).numpy(), D.numpy())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.set_stream is not supported on cpu.")
def test_cuda_set_stream():
    curr_stream = ms_torch.cuda.current_stream()
    assert curr_stream == ms_torch.cuda.default_stream()
    stream1 = user_stream1
    ms_torch.cuda.set_stream(stream1)
    assert stream1 == ms_torch.cuda.current_stream()
    ms_torch.cuda.set_stream(ms_torch.cuda.default_stream())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.synchronize is not supported on cpu.")
def test_cuda_synchronize():
    stream1 = user_stream1
    stream2 = user_stream2

    A = ms_torch.rand(500, 500, device="cuda")
    B = ms_torch.rand(500, 500, device="cuda")
    with ms_torch.cuda.stream(stream1):
        C = ms_torch.mm(A, A).to("cuda")
    with ms_torch.cuda.stream(stream2):
        D = ms_torch.mm(B, B).to("cuda")

    ms_torch.cuda.synchronize()
    assert np.allclose(ms_torch.mm(A, A).numpy(), C.numpy())
    assert np.allclose(ms_torch.mm(B, B).numpy(), D.numpy())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.stream is not supported on cpu.")
def test_cuda_stream():
    curr_stream = ms_torch.cuda.current_stream()
    default_stream = ms_torch.cuda.default_stream()
    user_stream = user_stream1
    is_curr_and_default_stream_same = (curr_stream == default_stream)
    is_user_and_default_stream_not_same = (user_stream != default_stream)
    with ms_torch.cuda.stream(user_stream):
        is_stream_set = (ms_torch.cuda.current_stream() == user_stream)
    is_stream_reset = (ms_torch.cuda.current_stream() == curr_stream)

    assert is_curr_and_default_stream_same is True
    assert is_user_and_default_stream_not_same is True
    assert is_stream_set is True
    assert is_stream_reset is True

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.stream is not supported on cpu.")
def test_cuda_set_none_stream():
    curr_stream = ms_torch.cuda.current_stream()
    default_stream = ms_torch.cuda.default_stream()

    with ms_torch.cuda.stream(None):
        is_curr_stream_same = (ms_torch.cuda.current_stream() == curr_stream)
        is_default_stream_same = (ms_torch.cuda.default_stream() == default_stream)
    assert is_curr_stream_same is True
    assert is_default_stream_same is True


if __name__ == '__main__':
    test_cuda_Stream_args()
    test_cuda_Stream_repr()
    test_cuda_Stream_eq()
    test_cuda_Stream_hash()
    test_cuda_Stream_query()
    test_cuda_Stream_record_event()
    test_cuda_Stream_synchronize()
    test_cuda_Stream_wait_event()
    test_cuda_Stream_wait_stream()
    test_cuda_jit_stream()
    test_cuda_grad_stream()
    test_cuda_data_dependency_between_streams()
    test_cuda_multi_streams()
    test_cuda_set_stream()
    test_cuda_synchronize()
    test_cuda_stream()
    test_cuda_set_none_stream()
