import os
import mindspore as ms
import mindtorch.torch as ms_torch
import torch
import numpy as np
from mindspore import context

from ...utils import set_mode_by_env_config, param_compare, SKIP_ENV_GRAPH_MODE, \
                     is_test_under_ascend_context
set_mode_by_env_config()

def test_avg_pool1d():
    data = np.random.randn(2, 3, 4).astype(np.float32)

    ms_tensor = ms_torch.tensor(data)
    ms_result = ms_torch.avg_pool1d(ms_tensor, 3)

    pt_tensor = torch.tensor(data)
    pt_result = torch.avg_pool1d(pt_tensor, 3)

    if is_test_under_ascend_context():
        param_compare(ms_result, pt_result, atol=2e-3)
    else:
        param_compare(ms_result, pt_result)

if __name__ == '__main__':
    test_avg_pool1d()