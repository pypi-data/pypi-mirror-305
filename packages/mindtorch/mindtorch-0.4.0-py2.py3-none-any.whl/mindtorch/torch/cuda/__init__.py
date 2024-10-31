#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import threading
import traceback
import mindspore as ms

from mindtorch.utils import get_backend, unsupported_attr, is_under_ascend_context
from mindtorch.torch.tensor import BoolTensor, ByteTensor, CharTensor, ShortTensor, IntTensor, HalfTensor, \
                                     FloatTensor, DoubleTensor, LongTensor, BFloat16Tensor, tensor
import mindtorch.torch.cuda.amp as amp
from mindtorch.torch.cuda.random import manual_seed_all, manual_seed
from mindtorch.torch.logging import warning
from mindtorch.torch.cuda.streams import *
from mindtorch.torch.cuda.memory import *
from ._utils import _get_device_index

_tls = threading.local()
_initialization_lock = threading.Lock()
_queued_calls = []


class device:
    def __init__(self, device):
        self.idx = _get_device_index(device, optional=True)
        self.prev_idx = -1

    def __enter__(self):
        # TODO: to support exchange device here.
        current_idx = current_device()
        if self.idx != current_idx:
            # TODO: Mindspore not support exchange device in a single process.
            raise NotImplementedError(f"Trying to exchange device from {current_idx} to {self.idx} "
                                      "using 'cuda.device', which is not supported yet. For now, only one device "
                                      "can be used in a single process.")

    def __exit__(self, type, value, traceback):
        # TODO: to support exchange device here.
        return False

class _LazySeedTracker:
    # Since seeding is memory-less, only track the latest seed.
    # Note: `manual_seed_all` followed by `manual_seed` overwrites
    # the seed on current device. We track the order of **latest**
    # calls between these two API.
    def __init__(self):
        self.manual_seed_all_cb = None
        self.manual_seed_cb = None
        self.call_order = []

    def queue_seed_all(self, cb, traceback):
        self.manual_seed_all_cb = (cb, traceback)
        # update seed_all to be latest
        self.call_order = [self.manual_seed_cb, self.manual_seed_all_cb]

    def queue_seed(self, cb, traceback):
        self.manual_seed_cb = (cb, traceback)
        # update seed to be latest
        self.call_order = [self.manual_seed_all_cb, self.manual_seed_cb]

    def get_calls(self):
        return self.call_order


_lazy_seed_tracker = _LazySeedTracker()

def init():
    _lazy_init()

def _cuda_init():
    a = tensor(1)
    a = a + 1
    ms.hal.synchronize()

def _lazy_init():
    # TODO: for now, _lazy_call is not supported yet.
    # global _queued_calls
    if is_initialized() or hasattr(_tls, 'is_initializing'):
        return
    with _initialization_lock:
        if is_initialized():
            return
        _cuda_init()
        _tls.is_initializing = True

        # TODO: for now, _lazy_call is not supported yet.
        # after _lazy_call support, should call the 'queued_call' in the following.
        delattr(_tls, 'is_initializing')

def _lazy_call(callable, **kwargs):
    unsupported_attr(kwargs)
    if not is_initialized():
        init()
    # TODO: _lazy_call is not supported yet on MindSpore.
    # _lazy_call mainly is for setting seed/state for random number generator,
    # however in mindspore, 'set_seed' can be call before backend init. So here directly call it.
    callable()

def is_available():
    backend = get_backend()
    return ms.hal.is_available(backend) and ms.hal.device_count(backend) > 0

def is_initialized():
    backend = get_backend()
    return ms.hal.is_initialized(backend)

def is_bf16_supported():
    return True

def empty_cache():
    # TODO: MindSpore not support device empty_cache
    warning("cuda.empty_cache can not actually take effect.")

def current_device():
    return ms.context.get_context('device_id')

def device_count():
    return ms.hal.device_count()

def set_device(device):
    unsupported_attr(device)
    warning("cuda.set_device can not actually take effect. "
            "Please try use mindspore.set_context('device_id') to exchange device.")

def get_device_capability(device=None):
    if device is None:
        device = current_device()
    else:
        device = _get_device_index(device)
    cap = ms.hal.get_device_capability(device)
    if cap is None:
        # TODO: MindSpore not support get_device_capability on CPU and Ascend.
        # When capability >= (7, 0), it means device support bf16, which MindSpore has supported.
        # But capability >=(8, 0) means device support triton, which MindSpore not support yet."
        # Therefore, set default capability=(7, 0)
        cap = (7, 0)
    return cap

def get_device_properties(device):
    device = _get_device_index(device)
    # TODO: Property only support 'name', 'total memory' and 'free_memory' on Ascend.
    return ms.hal.get_device_properties(device)

def get_device_name(device=None):
    if device is None:
        device = current_device()
    else:
        device = _get_device_index(device)
    return ms.hal.get_device_name(device)

def get_arch_list():
    arch_list = ms.hal.get_arch_list()
    if arch_list is None:
        arch_list = []
        warning(f"cuda.get_arch_list not support on {get_backend()} yet.")
    return arch_list

def set_stream(stream):
    return ms.hal.set_cur_stream(stream)

def stream(stream):
    return ms.hal.StreamCtx(stream)

def current_stream(device=None):
    if device is not None:
        raise NotImplementedError("'cuda.current_stream' can not support parameter 'device'.")
    stream = ms._c_expression.current_stream() # pylint: disable=I1101
    return Stream(stream=stream)

def default_stream(device=None):
    if device is not None:
        raise NotImplementedError("cuda.default_stream' can not support parameter 'device'.")
    stream = ms._c_expression.default_stream() # pylint: disable=I1101
    return Stream(stream=stream)

def synchronize(device=None):
    if device is not None:
        raise NotImplementedError("'cuda.synchronize' can not support parameter 'device'.")
    return ms.hal.synchronize()
