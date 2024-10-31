import sys
from mindtorch.utils import get_backend

this_module = sys.modules['mindtorch.torch']

try:
    from mindspore import hal  # pylint: disable=W0611
    # A tag used to identify if mindspore has hal
    has_hal = True
except ImportError:
    has_hal = False

def cuda_is_available():
    """
    func to replace "mindtorch.torch.cuda.is_available" on mindspore 2.2 and earlier version.
    """
    backend = get_backend()
    if backend in ('GPU', 'Ascend') :
        return True
    return False

def cuda_device_count():
    """
    func to replace "mindtorch.torch.cuda.device_count" on mindspore 2.2 and earlier version.
    """
    return 1

def _patch_func_ms():
    """
    Function to replace MindTorch's func to adapt to earlier version of mindspore.
    """
    if not has_hal:
        # When there is no 'mindspore.hal', replace 'mindtorch.torch.cuda.is_available' with 'cuda_is_available',
        # so it can run without 'mindspore.hal' on earlier mindspore version.
        this_module.cuda.is_available = cuda_is_available
        this_module.cuda.device_count = cuda_device_count
