#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import mindtorch.torch as ms_torch
import mindspore as ms
import numpy as np
from mindspore import jit, grad


from ...utils import set_mode_by_env_config, SKIP_ENV_CPU
set_mode_by_env_config()

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Event is not supported on cpu.")
def test_cuda_Event_args():
    event1 = ms_torch.cuda.Event()
    assert event1 is not None
    event2 = ms_torch.cuda.Event(enable_timing=True, blocking=True)
    assert event2 is not None

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Event is not supported on cpu.")
def test_cuda_Event_repr():
    stream = ms_torch.cuda.current_stream()
    event = ms_torch.cuda.Event()
    event_str = repr(event)
    assert "is_created:0" in event_str
    stream.record_event(event)
    event_str = repr(event)
    assert "is_created:1" in event_str

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Event is not supported on cpu.")
def test_cuda_Event_elapsed_time():
    start = ms_torch.cuda.Event(enable_timing=True)
    end = ms_torch.cuda.Event(enable_timing=True)
    start.record()
    tensor1 = ms_torch.rand(5000, 5000, device="cuda")
    ms_torch.mm(tensor1, tensor1).to("cuda")
    end.record()

    start.synchronize()
    end.synchronize()
    elapsed_time = start.elapsed_time(end)
    assert elapsed_time > 0

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Event is not supported on cpu.")
def test_cuda_Event_wait():
    stream1 = ms_torch.cuda.Stream()
    stream2 = ms_torch.cuda.Stream()
    event1 = ms_torch.cuda.Event()
    event2 = ms_torch.cuda.Event()

    A = ms_torch.rand(5000, 5000, device="cuda")
    with ms_torch.cuda.stream(stream1):
        B = ms_torch.mm(A, A).to("cuda")
        event1.record()
    with ms_torch.cuda.stream(stream2):
        event1.wait()
        C = ms_torch.mm(B, B).to("cuda")
        event2.record()

    event2.synchronize()
    assert event1.query() is True
    assert event2.query() is True
    assert np.allclose(ms_torch.mm(A, A).numpy(), B.numpy())
    assert np.allclose(ms_torch.mm(B, B).numpy(), C.numpy())

@SKIP_ENV_CPU(reason="mindtorch.torch.cuda.Event is not supported on cpu.")
def test_cuda_Event_synchronize():
    stream = ms_torch.cuda.Stream()
    start_event = ms_torch.cuda.Event(True, False, False)
    end_event = ms_torch.cuda.Event(True, False, False)

    start_event.record(stream)
    tensor1 = ms_torch.rand(5000, 5000, device="cuda")
    with ms_torch.cuda.stream(stream):
        ms_torch.mm(tensor1, tensor1).to("cuda")
        stream.record_event(end_event)

    start_event.synchronize()
    end_event.synchronize()
    assert end_event.query() is True
    assert stream.query() is True
    elapsed_time = start_event.elapsed_time(end_event)
    assert elapsed_time > 0

if __name__ == '__main__':
    test_cuda_Event_args()
    test_cuda_Event_repr()
    test_cuda_Event_elapsed_time()
    test_cuda_Event_wait()
    test_cuda_Event_synchronize()
