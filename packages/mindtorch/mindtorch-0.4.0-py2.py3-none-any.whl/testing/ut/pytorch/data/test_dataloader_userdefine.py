import mindtorch.torch as torch
from mindtorch.torch.utils.data import Dataset, DataLoader, Sampler, BatchSampler, SubsetRandomSampler
import numpy as np
import warnings

import mindspore as ms
ms.context.set_context(mode=ms.PYNATIVE_MODE)  #data only support pynative mode

class customsampler(Sampler):

    def __init__(self, data_source, replacement: bool = False,
                 num_samples: [int] = None, generator=None) -> None:
        super(customsampler, self).__init__(data_source)
        self.data_source = data_source
        self.replacement = replacement
        self._num_samples = num_samples
        self.generator = generator

        if generator is not None:
            warnings.warn("Don't support generator now.")

        if not isinstance(self.replacement, bool):
            raise TypeError("replacement should be a boolean value, but got "
                            "replacement={}".format(self.replacement))

        if not isinstance(self.num_samples, int) or self.num_samples <= 0:
            raise ValueError("num_samples should be a positive integer "
                             "value, but got num_samples={}".format(self.num_samples))

    @property
    def num_samples(self) -> int:
        # dataset size might change at runtime
        if self._num_samples is None:
            return len(self.data_source)
        return self._num_samples

    def __iter__(self):
        n = len(self.data_source)
        if self.replacement:
            for _ in range(self.num_samples // 32):
                yield from torch.from_numpy(np.random.choice(np.arange(n), 32, replace=True))
            yield from torch.from_numpy(np.random.choice(np.arange(n), self.num_samples % 32, replace=True))
        else:
            for _ in range(self.num_samples // n):
                yield from torch.from_numpy(np.random.choice(np.arange(n), n, replace=False))
            yield from torch.from_numpy(np.random.choice(np.arange(n), n, replace=False)[:self.num_samples % n])


    def __len__(self) -> int:
        return self.num_samples


class customdataset(Dataset):

    def __init__(self):
        self.data = []
        self.data1 = []
        self.label = []
        for i in range(1280):
            self.data.append(np.random.random((39,)).astype(np.float32))
            self.data1.append(np.random.random((39,)).astype(np.float32))
            self.label.append(np.random.randint(0, 10))


    def __getitem__(self, item):
        data = self.data[item]
        data1 = self.data1[item]
        label = self.label[item]
        return torch.from_numpy(data).unsqueeze(-1), torch.from_numpy(data1), label

    def __len__(self):

        return len(self.data)


def collate_fn(batch):

    targets = []
    imgs = []
    for sample in batch:
        imgs.append(sample[0])
        targets.append(sample[1])
    return np.stack(imgs, 0), targets

dataset = customdataset()
sampler = customsampler(dataset)

if __name__ == '__main__':
    loader1 = DataLoader(dataset, sampler=sampler, num_workers=2)
    loader2 = DataLoader(dataset, batch_size=4, sampler=sampler, num_workers=2)
    loader3 = DataLoader(dataset, sampler=sampler)

    x, y, z = next(loader1.__iter__())
    print(x[0][0][0])
    print(y[0][0])
    print(z)

    x, y, z = next(loader2.__iter__())
    print(x[0][0][0])
    print(y[0][0])
    print(z)

    x, y, z = next(loader3.__iter__())
    print(x[0][0][0])
    print(y[0][0])
    print(z)
