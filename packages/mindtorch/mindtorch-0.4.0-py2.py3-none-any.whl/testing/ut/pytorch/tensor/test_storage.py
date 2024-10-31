#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pickle
import numpy as np
import torch
import mindtorch.torch as ms_torch
# import mindspore as ms

from ...utils import set_mode_by_env_config, SKIP_ENV_GRAPH_MODE, param_compare, SKIP_ENV_ASCEND
set_mode_by_env_config()

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_bytestorage():
    a = pickle.dumps((1, 2, 3))

    storage = torch.ByteStorage.from_buffer(a)
    torch_out = torch.ByteTensor(storage)

    storage = ms_torch.ByteStorage.from_buffer(a)
    ms_out = ms_torch.ByteTensor(storage)

    assert np.allclose(ms_out.numpy(), torch_out.numpy())
    assert ms_out.numpy().dtype == torch_out.numpy().dtype
    assert ms_out.storage().type() == "mindtorch.ByteStorage"

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
@SKIP_ENV_ASCEND(reason="mindspore stridedslice not support float64 on Ascend")
def test_storage_float():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage()
    storage_msa = msa_tensor.storage()
    assert storage_msa.size() == storage_torch.size()
    assert storage_msa.nbytes() == storage_torch.nbytes()
    assert len(storage_msa) == len(storage_torch)
    assert storage_msa[2] == storage_torch[2]
    assert storage_msa.element_size() == storage_torch.element_size()
    assert storage_msa.tolist() == storage_torch.tolist()
    assert storage_msa.type() == "mindtorch.DoubleStorage"
    storage_msa[2] = 7
    storage_torch[2] = 7
    param_compare(torch_tensor, msa_tensor)

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
@SKIP_ENV_ASCEND(reason="mindspore stridedslice not support float64 on Ascend")
def test_storage_untyped():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    untyped_storage_torch = torch_tensor.storage()._untyped()
    untyped_storage_msa = msa_tensor.storage()._untyped()
    assert untyped_storage_msa.size() == untyped_storage_torch.size()
    assert untyped_storage_msa.nbytes() == untyped_storage_torch.nbytes()
    assert len(untyped_storage_msa) == len(untyped_storage_torch)
    assert untyped_storage_msa[2] == untyped_storage_torch[2]
    assert untyped_storage_msa.element_size() == untyped_storage_torch.element_size()
    assert untyped_storage_msa.tolist() == untyped_storage_torch.tolist()

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
@SKIP_ENV_ASCEND(reason="mindspore stridedslice not support int8 on Ascend")
def test_storage_int8():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).astype(np.int8)
    storage_torch = torch.tensor(data).storage()
    storage_msa = ms_torch.tensor(data).storage()
    assert storage_msa.size() == storage_torch.size()
    assert storage_msa.nbytes() == storage_torch.nbytes()
    assert len(storage_msa) == len(storage_torch)
    assert storage_msa[-2] == storage_torch[-2]
    assert storage_msa.element_size() == storage_torch.element_size()
    assert storage_msa.tolist() == storage_torch.tolist()
    assert storage_msa.type() == "mindtorch.CharStorage"

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_storage_to():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    storage_float = ms_torch.tensor(data).to(ms_torch.float32).storage()
    assert storage_float.type() == "mindtorch.FloatStorage"
    storage_int = storage_float.int()
    assert storage_int.type() == "mindtorch.IntStorage"

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
@SKIP_ENV_ASCEND(reason="mindspore stridedslice not support float64 on Ascend")
def test_storage_half():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage().half()
    storage_msa = msa_tensor.storage().half()
    assert storage_msa.size() == storage_torch.size()
    assert storage_msa.nbytes() == storage_torch.nbytes()
    assert len(storage_msa) == len(storage_torch)
    assert storage_msa[2] == storage_torch[2]
    assert storage_msa.element_size() == storage_torch.element_size()
    assert storage_msa.tolist() == storage_torch.tolist()
    assert storage_msa.type() == "mindtorch.HalfStorage"
    storage_msa[2] = 7
    storage_torch[2] = 7
    # Consistent with [[1., 2., 3.], [4., 5., 6.]].
    param_compare(torch_tensor, msa_tensor)

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_storage_type():
    tensor = ms_torch.tensor([1, 2])
    assert str(tensor.storage_type()) == "<class 'mindtorch.torch.storage.LongStorage'>"

# TODO:Do not support tensor.storage() in graph mode.
# def test_storage_graph_mode():
#     @ms.jit
#     def storage_attrs(x):
#         storage_msa = x.storage()
#         return storage_msa.size(), storage_msa.nbytes(), len(storage_msa), storage_msa[-2], \
#                storage_msa.element_size(), storage_msa.tolist(), storage_msa.type()
#
#     data = np.array([[1., 2., 3.], [4., 5., 6.]])
#     storage_torch = torch.tensor(data).storage()
#     storage_msa_attrs = storage_attrs(ms_torch.tensor(data))
#     assert storage_msa_attrs[0] == storage_torch.size()
#     assert storage_msa_attrs[1] == storage_torch.nbytes()
#     assert storage_msa_attrs[2] == len(storage_torch)
#     assert storage_msa_attrs[3] == storage_torch[2]
#     assert storage_msa_attrs[4] == storage_torch.element_size()
#     assert storage_msa_attrs[5] == storage_torch.tolist()
#     assert storage_msa_attrs[6] == "mindtorch.DoubleStorage"

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_is_storage():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    storage_float = ms_torch.tensor(data).to(ms_torch.float32).storage()
    res_ms = ms_torch.is_storage(storage_float)
    assert storage_float.type() == "mindtorch.FloatStorage"
    assert res_ms == True

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_storage_inplace():
    data = np.array([1., 2., 3.])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage()
    storage_msa = msa_tensor.storage()
    assert storage_msa[2] == storage_torch[2] == 3.
    torch_tensor[2] = 0
    msa_tensor[2] = 0
    # Mindtorch needs to synchronize data first.
    msa_tensor.numpy()
    assert storage_msa[2] == storage_torch[2] == 0

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_storage_file():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage()
    storage_msa = msa_tensor.storage()

    with open('torch_storage_file.pth', 'wb') as f:
        storage_torch._write_file(f, True, True, torch._utils._element_size(storage_torch.dtype))
        f.close()

    with open('mindtorch_storage_file.pth', 'wb') as f:
        storage_msa._write_file(f, True, True, ms_torch._utils._element_size(storage_msa.dtype))
        f.close()

    data = np.array([[7., 8., 9.], [10., 11., 12.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage()
    storage_msa = msa_tensor.storage()

    with open('torch_storage_file.pth', 'rb') as f:
        storage_torch._set_from_file(f, 0, True, torch._utils._element_size(storage_torch.dtype))
        f.close()

    with open('mindtorch_storage_file.pth', 'rb') as f:
        storage_msa._set_from_file(f, 0, True, ms_torch._utils._element_size(storage_msa.dtype))
        f.close()

    param_compare(torch_tensor, msa_tensor)

    # test set_
    data = np.array([[0., 0., 0.], [0., 0., 0.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage()
    storage_msa = msa_tensor.storage()

    t_torch = torch.tensor([], dtype=storage_torch.dtype, device=storage_torch._untyped().device)
    t_torch.set_(storage_torch._untyped())

    t_msa = ms_torch.tensor([], dtype=storage_msa.dtype, device=storage_msa._untyped().device)
    t_msa.set_(storage_msa._untyped())

    param_compare(t_torch, t_msa)

    with open('torch_storage_file.pth', 'rb') as f:
        storage_torch._set_from_file(f, 0, True, torch._utils._element_size(storage_torch.dtype))
        f.close()

    with open('mindtorch_storage_file.pth', 'rb') as f:
        storage_msa._set_from_file(f, 0, True, ms_torch._utils._element_size(storage_msa.dtype))
        f.close()

    param_compare(t_torch, t_msa)

    os.remove("mindtorch_storage_file.pth")
    os.remove("torch_storage_file.pth")

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_storage_clone():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage()
    storage_msa = msa_tensor.storage()

    storage_clone_torch = storage_torch.clone()
    storage_clone_msa = storage_msa.clone()
    storage_clone_torch[0] = 2
    storage_clone_msa[0] = 2
    assert storage_torch[0] == storage_msa[0] == 1
    assert storage_clone_torch[0] == storage_clone_msa[0] == 2

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_storage_fill():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage()
    storage_msa = msa_tensor.storage()

    storage_torch.fill_(2)
    storage_msa.fill_(2)
    param_compare(torch_tensor, msa_tensor)

@SKIP_ENV_GRAPH_MODE(reason="Do not support Storage in graph mode.")
def test_storage_resize():
    data = np.array([[1., 2., 3.], [4., 5., 6.]])
    torch_tensor = torch.tensor(data)
    msa_tensor = ms_torch.tensor(data)
    storage_torch = torch_tensor.storage()
    storage_msa = msa_tensor.storage()

    assert storage_torch.size() == storage_msa.size() == 6
    storage_torch.resize_(8)
    storage_msa.resize_(8)
    assert storage_torch.size() == storage_msa.size() == 8
    storage_torch.resize_(4)
    storage_msa.resize_(4)
    assert storage_torch.size() == storage_msa.size() == 4

if __name__ == '__main__':
    set_mode_by_env_config()
    test_bytestorage()
    test_storage_float()
    test_storage_untyped()
    test_storage_int8()
    test_storage_to()
    test_storage_half()
    test_storage_type()
    # test_storage_graph_mode()
    test_is_storage()
    test_storage_inplace()
    test_storage_file()
    test_storage_clone()
    test_storage_fill()
    test_storage_resize()
