import mindspore as ms
from mindtorch.torch._C.Generator import *
from mindtorch.torch._C.Size import *
from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning

def _jit_set_profiling_mode(profiling_flag):
    unsupported_attr(profiling_flag)
    warning("Currently, _jit_set_profiling_mode is not effectived.")
    return False

def _jit_set_profiling_executor(profiling_flag):
    unsupported_attr(profiling_flag)
    warning("Currently, _jit_set_profiling_executor is not effectived.")
    return False

@ms.jit_class
class memory_format():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "mindtorch." + self.name

contiguous_format = memory_format("contiguous_format")
channels_last = memory_format("channels_last")
channels_last_3d = memory_format("channels_last_3d")
preserve_format = memory_format("preserve_format")

def get_num_thread():
    return ms.get_context('runtime_num_threads')

def set_num_threads(nthreads):
    warning("Currently, `set_num_threads` only supports being called before the program executes operations, and does "
            "not support modifications during execution. Additionally, due to differences in the multi-threaded "
            "mechanism of the framework, this function is equivalent to `set_num_interop_threads`.")
    ms.set_context(runtime_num_threads=nthreads)

def get_num_interop_threads():
    return ms.get_context('runtime_num_threads')

def set_num_interop_threads(nthreads):
    warning("Currently, `set_num_interop_threads` only supports being called before the program executes operations, "
            "and does not support modifications during execution.")
    ms.set_context(runtime_num_threads=nthreads)
