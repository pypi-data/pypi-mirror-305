import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def assert_finfo_attr(finfo, ms_finfo):
    assert finfo.bits == ms_finfo.bits
    assert abs(finfo.eps - ms_finfo.eps) <= 1e-6
    assert abs(finfo.max - ms_finfo.max) <= 1e-6
    assert abs(finfo.min - ms_finfo.min) <= 1e-6
    assert abs(finfo.tiny - ms_finfo.tiny) <= 1e-6
    if np.lib.NumpyVersion(np.__version__) >= '1.23.0':
        assert abs(finfo.smallest_normal - ms_finfo.smallest_normal) <= 1e-6
    assert abs(finfo.resolution - ms_finfo.resolution) <= 1e-6

def assert_iinfo_attr(iinfo, ms_iinfo):
    assert iinfo.bits == ms_iinfo.bits
    assert iinfo.min == ms_iinfo.min
    assert iinfo.max == ms_iinfo.max

def test_finfo():
    finfo = torch.finfo(torch.float16)
    ms_finfo = ms_torch.finfo(ms_torch.float16)
    assert_finfo_attr(finfo, ms_finfo)

    finfo = torch.finfo(torch.float32)
    ms_finfo = ms_torch.finfo(ms_torch.float32)
    assert_finfo_attr(finfo, ms_finfo)

    finfo = torch.finfo(torch.float64)
    ms_finfo = ms_torch.finfo(ms_torch.float64)
    assert_finfo_attr(finfo, ms_finfo)

def test_iinfo():
    iinfo = torch.iinfo(torch.uint8)
    ms_iinfo = ms_torch.iinfo(ms_torch.uint8)
    assert_iinfo_attr(iinfo, ms_iinfo)

    iinfo = torch.iinfo(torch.int8)
    ms_iinfo = ms_torch.iinfo(ms_torch.int8)
    assert_iinfo_attr(iinfo, ms_iinfo)

    iinfo = torch.iinfo(torch.int16)
    ms_iinfo = ms_torch.iinfo(ms_torch.int16)
    assert_iinfo_attr(iinfo, ms_iinfo)

    iinfo = torch.iinfo(torch.int32)
    ms_iinfo = ms_torch.iinfo(ms_torch.int32)
    assert_iinfo_attr(iinfo, ms_iinfo)

    iinfo = torch.iinfo(torch.int64)
    ms_iinfo = ms_torch.iinfo(ms_torch.int64)
    assert_iinfo_attr(iinfo, ms_iinfo)


if __name__ == '__main__':
    set_mode_by_env_config()
    test_finfo()
    test_iinfo()