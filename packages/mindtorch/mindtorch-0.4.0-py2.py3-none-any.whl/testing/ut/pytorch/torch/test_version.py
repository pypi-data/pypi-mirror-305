import mindtorch.torch as ms_torch
import torch
import numpy as np
from packaging.version import Version
import mindspore as ms

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_version_compare():
    # ms_torch.__version__ : '1.12.1'
    assert ms_torch.__version__ > '1.2.0'
    assert ms_torch.__version__ > (1,2,0)
    assert ms_torch.__version__ > Version('1.10.0a')
    assert ms_torch.__version__ < "2"
    assert ms_torch.__version__ < "2.0.0"

def test_version_other_feature():
    assert ms_torch.__version__.split('.')[1] == "12"
    assert "Hello " + ms_torch.__version__ + ".123" == "Hello 1.12.1.123"
    assert ms_torch.__version__.startswith("1.12")

def test_version_jit():
    @ms.jit
    def test_version():
         return ms_torch.__version__ > '1.2.0'
    test_version()

if __name__ == '__main__':
    test_version_compare()
    test_version_other_feature()
    test_version_jit()
