#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
ms.context.set_context(mode=ms.PYNATIVE_MODE)  #data only support pynative mode

from mindtorch.torch.utils.data.sampler import (
    BatchSampler,
    RandomSampler,
    Sampler,
    SequentialSampler,
    SubsetRandomSampler,
    WeightedRandomSampler,
)


def test_BatchSampler():
     index_1 = list(BatchSampler(SequentialSampler(range(10)), batch_size=3, drop_last=False))
     index_2 = list(BatchSampler(SequentialSampler(range(10)), batch_size=3, drop_last=True))
     len_1 = len(BatchSampler(SequentialSampler(range(10)), batch_size=3, drop_last=False))
     len_2 = len(BatchSampler(SequentialSampler(range(10)), batch_size=3, drop_last=True))
     print(index_1)
     print(index_2)
     print(len_1)
     print(len_2)


def test_SequentialSampler():
    index_1 = list(SequentialSampler(range(10)))
    len_1 = len(SequentialSampler(range(10)))
    print(index_1)
    print(len_1)


def test_WeightedRandomSampler():
    index_1 = list(WeightedRandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6], 5, replacement=True))
    index_2 = list(WeightedRandomSampler([0.9, 0.4, 0.05, 0.2, 0.3, 0.1], 5, replacement=False))
    len_1 = len(WeightedRandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6], 5, replacement=True))
    len_2 = len(WeightedRandomSampler([0.9, 0.4, 0.05, 0.2, 0.3, 0.1], 5, replacement=False))
    print(index_1)
    print(index_2)
    print(len_1)
    print(len_2)

def test_RandomSampler():
    index_1 = list(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6],  replacement=True))
    len_1 = len(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6],  replacement=True))
    print(index_1)
    print(len_1)

    index_2 = list(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6], replacement=True, num_samples=3))
    len_2 = len(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6],  replacement=True, num_samples=3))
    print(index_2)
    print(len_2)

    index_3 = list(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6],  replacement=False))
    len_3 = len(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6],  replacement=False))
    print(index_3)
    print(len_3)

    index_4 = list(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6], replacement=False, num_samples=3))
    len_4 = len(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6],  replacement=False, num_samples=3))
    print(index_4)
    print(len_4)

    index_5 = list(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6], replacement=True, num_samples=9))
    len_5 = len(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6],  replacement=True, num_samples=9))
    print(index_5)
    print(len_5)

    index_6 = list(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6], replacement=False, num_samples=9))
    len_6 = len(RandomSampler([0.1, 0.9, 0.4, 0.7, 3.0, 0.6],  replacement=False, num_samples=9))
    print(index_6)
    print(len_6)

def test_SubsetRandomSampler():
    index_1 = list(SubsetRandomSampler([1, 9, 4, 7, 3, 6]))
    len_1 = len(SubsetRandomSampler([1, 9, 4, 7, 3, 6]))
    print(index_1)
    print(len_1)