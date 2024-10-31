#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import torch
import random

import mindspore as ms

from mindtorch.utils import is_under_gpu_context
import mindtorch.torch as ms_torch
import torch
import numpy as np

from ...utils import set_mode_by_env_config
set_mode_by_env_config()

def test_pad_sequence1():
    torch_a = torch.ones(2, 5)
    torch_b = torch.ones(3, 5)
    torch_c = torch.ones(1, 5)
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_a, torch_b, torch_c], batch_first=True)

    ms_a = ms_torch.ones(2, 5)
    ms_b = ms_torch.ones(3, 5)
    ms_c = ms_torch.ones(1, 5)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_a, ms_b, ms_c], batch_first=True)

    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.asnumpy().dtype
    assert np.allclose(torch_out.numpy(), ms_out.asnumpy())

def test_pad_sequence1_withvalue():
    torch_a = torch.ones(2, 5)
    torch_b = torch.ones(3, 5)
    torch_c = torch.ones(1, 5)
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_a, torch_b, torch_c], padding_value=-1)

    ms_a = ms_torch.ones(2, 5)
    ms_b = ms_torch.ones(3, 5)
    ms_c = ms_torch.ones(1, 5)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_a, ms_b, ms_c], padding_value=-1)

    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.asnumpy().dtype
    assert np.allclose(torch_out.numpy(), ms_out.asnumpy())

def test_pad_sequence1_numpy():
    torch_a = torch.ones(25, 300)
    torch_b = torch.ones(22, 300)
    torch_c = torch.ones(15, 300)
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_a, torch_b, torch_c], batch_first=True)

    ms_a = np.ones((25, 300)).astype(np.float32)
    ms_b = np.ones((22, 300)).astype(np.float32)
    ms_c = np.ones((15, 300)).astype(np.float32)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_a, ms_b, ms_c], batch_first=True)

    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.dtype
    assert np.allclose(torch_out.numpy(), ms_out)

    torch_out = torch.nn.utils.rnn.pad_sequence([torch_a, torch_b, torch_c], padding_value=-1)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_a, ms_b, ms_c], padding_value=-1)

    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.dtype
    assert np.allclose(torch_out.numpy(), ms_out)

def test_pad_sequence2():
    # single dimensional
    torch_a = torch.tensor([1, 2, 3])
    torch_b = torch.tensor([4, 5])
    torch_c = torch.tensor([6])

    ms_a = ms_torch.tensor([1, 2, 3])
    ms_b = ms_torch.tensor([4, 5])
    ms_c = ms_torch.tensor([6])

    # batch_first = true
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_b, torch_a, torch_c], True)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_b, ms_a, ms_c], True)
    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.asnumpy().dtype
    assert np.allclose(torch_out.numpy(), ms_out.asnumpy())

    # batch_first = false
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_b, torch_a, torch_c])
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_b, ms_a, ms_c])
    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.asnumpy().dtype
    assert np.allclose(torch_out.numpy(), ms_out.asnumpy())

    # pad with non-zero value
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_b, torch_a, torch_c], True, 1)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_b, ms_a, ms_c], True, 1)
    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.asnumpy().dtype
    assert np.allclose(torch_out.numpy(), ms_out.asnumpy())

    # Test pad sorted sequence
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_a, torch_b, torch_c], True)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_a, ms_b, ms_c], True)
    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.asnumpy().dtype
    assert np.allclose(torch_out.numpy(), ms_out.asnumpy())

def test_pad_sequence2_ndims():
    # more dimensions
    for num_dim in (0, 2):
        torch_sequences = []
        ms_sequences = []
        trailing_dims = [4] * num_dim
        for i in (1, 2):
            seq_len = i * i
            np_arr = np.random.rand(seq_len, 5, *trailing_dims)
            if ms.get_context('device_target') == 'Ascend':
                np_arr = np_arr.astype(np.float32)
            torch_sequences.append(torch.tensor(np_arr))
            ms_sequences.append(ms_torch.tensor(np_arr))
        random.seed(4)
        random.shuffle(torch_sequences)
        random.seed(4)
        random.shuffle(ms_sequences)

        # batch first = true
        torch_out = torch.nn.utils.rnn.pad_sequence(torch_sequences, True)
        ms_out = ms_torch.nn.utils.rnn.pad_sequence(ms_sequences, True)
        assert torch_out.shape == ms_out.shape
        assert torch_out.numpy().dtype == ms_out.asnumpy().dtype
        assert np.allclose(torch_out.numpy(), ms_out.asnumpy())

        # batch first = false
        torch_out = torch.nn.utils.rnn.pad_sequence(torch_sequences)
        ms_out = ms_torch.nn.utils.rnn.pad_sequence(ms_sequences)
        assert torch_out.shape == ms_out.shape
        assert torch_out.numpy().dtype == ms_out.asnumpy().dtype
        assert np.allclose(torch_out.numpy(), ms_out.asnumpy())

def test_pad_sequence2_numpy1():
    # single dimensional
    torch_a = torch.tensor([1, 2, 3])
    torch_b = torch.tensor([4, 5])
    torch_c = torch.tensor([6])

    ms_a = np.array([1, 2, 3]).astype(np.int64)
    ms_b = np.array([4, 5]).astype(np.int64)
    ms_c = np.array([6]).astype(np.int64)

    # batch_first = true
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_b, torch_a, torch_c], True)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_b, ms_a, ms_c], True)
    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.dtype
    assert np.allclose(torch_out.numpy(), ms_out)

    # batch_first = false
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_b, torch_a, torch_c])
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_b, ms_a, ms_c])
    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.dtype
    assert np.allclose(torch_out.numpy(), ms_out)

    # pad with non-zero value
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_b, torch_a, torch_c], True, 1)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_b, ms_a, ms_c], True, 1)
    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.dtype
    assert np.allclose(torch_out.numpy(), ms_out)

    # Test pad sorted sequence
    torch_out = torch.nn.utils.rnn.pad_sequence([torch_a, torch_b, torch_c], True)
    ms_out = ms_torch.nn.utils.rnn.pad_sequence([ms_a, ms_b, ms_c], True)
    assert torch_out.shape == ms_out.shape
    assert torch_out.numpy().dtype == ms_out.dtype
    assert np.allclose(torch_out.numpy(), ms_out)

def test_pad_sequence2_numpy2():
    maxlen = 9
    for num_dim in (0, 1, 2, 3):
        torch_sequences = []
        ms_sequences = []
        trailing_dims = [4] * num_dim
        for i in range(1, maxlen + 1):
            seq_len = i * i
            np_arr = np.random.rand(seq_len, 5, *trailing_dims)
            if ms.get_context('device_target') == 'Ascend':
                np_arr = np_arr.astype(np.float32)
            torch_sequences.append(torch.tensor(np_arr))
            ms_sequences.append(np_arr)
        random.seed(4)
        random.shuffle(torch_sequences)
        random.seed(4)
        random.shuffle(ms_sequences)

        # batch first = true
        torch_out = torch.nn.utils.rnn.pad_sequence(torch_sequences, True)
        ms_out = ms_torch.nn.utils.rnn.pad_sequence(ms_sequences, True)
        assert torch_out.shape == ms_out.shape
        assert torch_out.numpy().dtype == ms_out.dtype
        assert np.allclose(torch_out.numpy(), ms_out)

        # batch first = false
        torch_out = torch.nn.utils.rnn.pad_sequence(torch_sequences)
        ms_out = ms_torch.nn.utils.rnn.pad_sequence(ms_sequences)
        assert torch_out.shape == ms_out.shape
        assert torch_out.numpy().dtype == ms_out.dtype
        assert np.allclose(torch_out.numpy(), ms_out)

def test_simple_pack_padded_sequence():
    # single dimensional
    torch_a = torch.tensor([1, 2, 3])
    torch_b = torch.tensor([4, 5])
    torch_c = torch.tensor([6])

    ms_a = ms_torch.tensor([1, 2, 3])
    ms_b = ms_torch.tensor([4, 5])
    ms_c = ms_torch.tensor([6])

    # batch_first = true
    torch_padded = torch.nn.utils.rnn.pad_sequence([torch_b, torch_a, torch_c], True)
    ms_padded = ms_torch.nn.utils.rnn.pad_sequence([ms_b, ms_a, ms_c], True)
    torch_out1 = torch.nn.utils.rnn.pack_padded_sequence(torch_padded, [3, 2, 1], batch_first=True)
    ms_out1 = ms_torch.nn.utils.rnn.pack_padded_sequence(ms_padded, [3, 2, 1], batch_first=True)

    assert np.allclose(torch_out1.data.numpy(), ms_out1.data.numpy())
    assert np.allclose(torch_out1.batch_sizes.numpy(), ms_out1.batch_sizes.numpy())
    assert torch_out1.sorted_indices == ms_out1.sorted_indices
    assert torch_out1.unsorted_indices == ms_out1.unsorted_indices

    torch_out2 = torch.nn.utils.rnn.pack_padded_sequence(torch_padded, [1, 1, 3], batch_first=True,
                                                         enforce_sorted=False)
    ms_out2 = ms_torch.nn.utils.rnn.pack_padded_sequence(ms_padded, [1, 1, 3], batch_first=True,
                                                         enforce_sorted=False)

    assert np.allclose(torch_out2.data.numpy(), ms_out2.data.numpy())
    assert np.allclose(torch_out2.batch_sizes.numpy(), ms_out2.batch_sizes.numpy())
    assert np.allclose(torch_out2.sorted_indices.numpy(), ms_out2.sorted_indices.numpy())
    assert np.allclose(torch_out2.unsorted_indices.numpy(), ms_out2.unsorted_indices.numpy())

    # testcases for class PackedSequence
    torch_out_fp16 = torch_out2.to(torch.float16)
    ms_out_fp16 = ms_out2.to(ms.float16)
    assert torch_out_fp16.data.numpy().dtype == ms_out_fp16.data.numpy().dtype
    assert torch_out_fp16.batch_sizes.numpy().dtype == ms_out_fp16.batch_sizes.numpy().dtype
    assert torch_out_fp16.sorted_indices.numpy().dtype == ms_out_fp16.sorted_indices.numpy().dtype
    assert torch_out_fp16.unsorted_indices.numpy().dtype == ms_out_fp16.unsorted_indices.numpy().dtype

    assert torch_out2.double().data.numpy().dtype == ms_out2.double().data.numpy().dtype
    assert torch_out2.float().data.numpy().dtype == ms_out2.float().data.numpy().dtype
    assert torch_out2.half().data.numpy().dtype == ms_out2.half().data.numpy().dtype
    assert torch_out2.long().data.numpy().dtype == ms_out2.long().data.numpy().dtype
    assert torch_out2.int().data.numpy().dtype == ms_out2.int().data.numpy().dtype
    assert torch_out2.short().data.numpy().dtype == ms_out2.short().data.numpy().dtype
    assert torch_out2.byte().data.numpy().dtype == ms_out2.byte().data.numpy().dtype

    assert ms_out2.is_cuda == is_under_gpu_context()

def test_simple_pack_padded_sequence2():
    torch_padded = torch.arange(0, 24).reshape(4,3,2)
    ms_padded = ms_torch.arange(0, 24).reshape(4,3,2)
    torch_out = torch.nn.utils.rnn.pack_padded_sequence(torch_padded, [3, 1, 1, 1], batch_first=True)
    ms_out = ms_torch.nn.utils.rnn.pack_padded_sequence(ms_padded, [3, 1, 1, 1], batch_first=True)

    assert np.allclose(torch_out.data.numpy(), ms_out.data.numpy())
    assert np.allclose(torch_out.batch_sizes.numpy(), ms_out.batch_sizes.numpy())
    assert torch_out.sorted_indices == ms_out.sorted_indices
    assert torch_out.unsorted_indices == ms_out.unsorted_indices

def test_simple_pack_sequence():
    torch_a = torch.tensor([1, 2, 3])
    torch_b = torch.tensor([4, 5])
    torch_c = torch.tensor([6])

    ms_a = ms_torch.tensor([1, 2, 3])
    ms_b = ms_torch.tensor([4, 5])
    ms_c = ms_torch.tensor([6])

    # enforce_sorted = false
    torch_out1 = torch.nn.utils.rnn.pack_sequence([torch_b, torch_a, torch_c], enforce_sorted=False)
    ms_out1 = ms_torch.nn.utils.rnn.pack_sequence([ms_b, ms_a, ms_c], enforce_sorted=False)
    assert np.allclose(torch_out1.data.numpy(), ms_out1.data.numpy())
    assert np.allclose(torch_out1.batch_sizes.numpy(), ms_out1.batch_sizes.numpy())

    # enforce_sorted = true
    torch_out2 = torch.nn.utils.rnn.pack_sequence([torch_a, torch_b, torch_c], enforce_sorted=True)
    ms_out2 = ms_torch.nn.utils.rnn.pack_sequence([ms_a, ms_b, ms_c], enforce_sorted=True)
    assert np.allclose(torch_out2.data.numpy(), ms_out2.data.numpy())
    assert np.allclose(torch_out2.batch_sizes.numpy(), ms_out2.batch_sizes.numpy())

def test_simple_pad_packed_sequence():
    torch_seq = torch.tensor([[1,2,0], [3,0,0], [4,5,6]])
    ms_seq = ms_torch.tensor([[1,2,0], [3,0,0], [4,5,6]])
    lens = [2, 1, 3]

    torch_packed = torch.nn.utils.rnn.pack_padded_sequence(torch_seq, lens, batch_first=True, enforce_sorted=False)
    ms_packed = ms_torch.nn.utils.rnn.pack_padded_sequence(ms_seq, lens, batch_first=True, enforce_sorted=False)

    assert np.allclose(torch_packed.data.numpy(), ms_packed.data.numpy())
    assert torch_packed.data.numpy().dtype == ms_packed.data.numpy().dtype
    assert np.allclose(torch_packed.batch_sizes.numpy(), ms_packed.batch_sizes.numpy())
    assert torch_packed.batch_sizes.numpy().dtype == ms_packed.batch_sizes.numpy().dtype
    assert np.allclose(torch_packed.sorted_indices.numpy(), ms_packed.sorted_indices.numpy())
    assert torch_packed.sorted_indices.numpy().dtype == ms_packed.sorted_indices.numpy().dtype
    assert np.allclose(torch_packed.unsorted_indices.numpy(), ms_packed.unsorted_indices.numpy())
    assert torch_packed.unsorted_indices.numpy().dtype == ms_packed.unsorted_indices.numpy().dtype

    torch_seq_unpacked, torch_lens_unpacked = torch.nn.utils.rnn.pad_packed_sequence(torch_packed, batch_first=True)
    ms_seq_unpacked, ms_lens_unpacked = ms_torch.nn.utils.rnn.pad_packed_sequence(ms_packed, batch_first=True)

    assert np.allclose(torch_seq_unpacked.numpy(), ms_seq_unpacked.numpy())
    assert torch_seq_unpacked.numpy().dtype == ms_seq_unpacked.numpy().dtype
    assert np.allclose(torch_lens_unpacked.numpy(), ms_lens_unpacked.numpy())
    assert torch_lens_unpacked.numpy().dtype == ms_lens_unpacked.numpy().dtype

def test_simple_pad_packed_sequence_sorted():
    torch_seq = torch.tensor([[1,2,0], [3,0,0], [4,5,6]])
    ms_seq = ms_torch.tensor([[1,2,0], [3,0,0], [4,5,6]])

    torch_packed = torch.nn.utils.rnn.pack_padded_sequence(torch_seq, [3, 2, 1], batch_first=True, enforce_sorted=True)
    ms_packed = ms_torch.nn.utils.rnn.pack_padded_sequence(ms_seq, [3, 2, 1], batch_first=True, enforce_sorted=True)

    assert np.allclose(torch_packed.data.numpy(), ms_packed.data.numpy())
    assert torch_packed.data.numpy().dtype == ms_packed.data.numpy().dtype
    assert np.allclose(torch_packed.batch_sizes.numpy(), ms_packed.batch_sizes.numpy())
    assert torch_packed.batch_sizes.numpy().dtype == ms_packed.batch_sizes.numpy().dtype

if __name__ == '__main__':
    set_mode_by_env_config()
    test_pad_sequence1()
    test_pad_sequence1_withvalue()
    test_pad_sequence2()
    test_pad_sequence2_ndims()
    test_simple_pack_padded_sequence()
    test_simple_pack_padded_sequence2()
    test_simple_pack_sequence()
    test_simple_pad_packed_sequence()
    test_simple_pad_packed_sequence_sorted()
    test_pad_sequence1_numpy()
    test_pad_sequence2_numpy1()
    test_pad_sequence2_numpy2()
