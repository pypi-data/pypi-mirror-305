import os
import re
import mindspore as ms
from mindtorch.utils import is_under_gpu_context, is_under_ascend_context

def _get_npu_device_info(device_id):
    try:
        str_command = "npu-smi info"
        out = os.popen(str_command)
        text_content = out.read()
        out.close()
        lines = text_content.split("\n")
        target_line = lines[7 + device_id * 3]
        mem_part = target_line.split("|")[3]
        use_mem = int(mem_part.split("/")[0].split()[-1]) * 1024 * 1024
        total_mem = int(mem_part.split("/")[1].split()[0]) * 1024 * 1024
        free_mem = total_mem - use_mem
    except Exception as e:
        raise RuntimeError("Some exceptions occurred and obtaining npu device_info failed.") from e
    return free_mem, total_mem

def _get_gpu_device_info(device_id):
    try:
        str_command = "nvidia-smi"
        out = os.popen(str_command)
        text_content = out.read()
        out.close()
        lines = text_content.split("\n")
        target_line = lines[9 + device_id * 4]
        mem_part = target_line.split("|")[2]
        use_mem = mem_part.split("/")[0].split()[-1]
        use_mem = int(re.findall(r'\d+', use_mem)[0]) * 1024 * 1024
        total_mem = mem_part.split("/")[1].split()[0]
        total_mem = int(re.findall(r'\d+', total_mem)[0]) * 1024 * 1024
        free_mem = total_mem - use_mem
    except Exception as e:
        raise RuntimeError("Some exceptions occurred and obtaining gpu device_info failed.") from e
    return free_mem, total_mem

def mem_get_info(device=None):
    if device is None:
        device = ms.context.get_context('device_id')

    if is_under_ascend_context():
        return _get_npu_device_info(device)

    if is_under_gpu_context():
        return _get_gpu_device_info(device)

    raise RuntimeError("Currently executing on CPU device, unable to obtain `cuda.mem_get_info`.")
