# Owner(s): ["module: dataloader"]

import math
import sys
import errno
import os
import ctypes
import faulthandler
import gc
import time
import signal
import unittest
import warnings
import mindtorch.torch.multiprocessing as mp
from mindtorch.torch.utils.data import (
    ChainDataset,
    ConcatDataset,
    DataLoader,
    # DataLoader2,
    Dataset,
    IterableDataset,
    # IterDataPipe,
    Subset,
    TensorDataset,
    # communication,
    _utils
)
import mindtorch.torch as torch
from mindtorch.torch._utils import ExceptionWrapper
from mindtorch.torch.utils.data.dataset import random_split

import mindspore as ms
ms.context.set_context(mode=ms.PYNATIVE_MODE)  #data only support pynative mode

IS_WINDOWS = sys.platform == "win32"
NO_MULTIPROCESSING_SPAWN = os.environ.get('NO_MULTIPROCESSING_SPAWN', '0') == '1'

IS_CI = bool(os.getenv('CI'))
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False
    err_msg = ("psutil not found. Some critical data loader tests relying on it "
               "(e.g., TestDataLoader.test_proper_exit) will not run.")
    if IS_CI:
        raise ImportError(err_msg) from None
    else:
        warnings.warn(err_msg)

try:
    import dill
    # XXX: By default, dill writes the Pickler dispatch table to inject its
    # own logic there. This globally affects the behavior of the standard library
    # pickler for any user who transitively depends on this module!
    # Undo this extension to avoid altering the behavior of the pickler globally.
    dill.extend(use_dill=False)
    HAS_DILL = True
except ImportError:
    HAS_DILL = False
skipIfNoDill = unittest.skipIf(not HAS_DILL, "no dill")


try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
skipIfNoNumpy = unittest.skipIf(not HAS_NUMPY, "no NumPy")

JOIN_TIMEOUT = 60.0  # seconds
supported_multiprocessing_contexts = [None] + list(mp.get_all_start_methods())
np.random.seed(42)
ms.set_seed(42)

def test_splits_have_correct_size():
    splits = random_split([1, 2, 3, 4, 5, 6], [2, 4])
    assert np.allclose(len(splits), 2)
    assert np.allclose(len(splits[0]), 2)
    assert np.allclose(len(splits[1]), 4)

    splits = random_split([1, 2, 3, 4, 5, 6], [0.5, 0.5])
    assert np.allclose(len(splits), 2)
    assert np.allclose(len(splits[0]), 3)
    assert np.allclose(len(splits[1]), 3)

    # Odd size splits
    assert np.allclose(
        len(random_split(range(3), [0.5, 0.5])),
        2
    )

    # Odd sized round-robin splits
    splits = random_split(range(106), [0.1, 0.2, 0.3, 0.4],)
    assert np.allclose(len(splits[0]), 11)
    assert np.allclose(len(splits[1]), 22)
    assert np.allclose(len(splits[2]), 31)
    assert np.allclose(len(splits[3]), 42)


def test_splits_are_mutually_exclusive():
    data = [5, 2, 3, 4, 1, 6]
    splits = random_split(data, [2, 4])
    all_values = []
    all_values.extend(list(splits[0]))
    all_values.extend(list(splits[1]))
    data.sort()
    all_values.sort()
    assert np.allclose(data, all_values)

    splits = random_split(data, [0.33, 0.67])
    all_values = []
    all_values.extend(list(splits[0]))
    all_values.extend(list(splits[1]))
    data.sort()
    all_values.sort()
    assert np.allclose(data, all_values)

    data = [1, 2, 3, 4]
    splits = random_split(data, [0.25, 0.75])
    all_values = []
    all_values.extend(list(splits[0]))
    all_values.extend(list(splits[1]))
    data.sort()
    all_values.sort()
    assert np.allclose(data, all_values)

class CustomDataset():
    def __init__(self, custom_list):
        self.data = custom_list

    def __getitem__(self, key):
        if type(key) == type(0):
            return self.data[key]
        else:
            raise TypeError("Type do not match.")

    def __len__(self):
        return len(self.data)

def test_splits_indexing_type():

    x = [1, 2, 3, 4, 5]
    dataset = CustomDataset(x)
    dataset = random_split(dataset, [5])[0]
    data_loader = DataLoader(dataset)
    for batch in data_loader:
        pass

    # fractional splitting
    dataset = CustomDataset(x)
    dataset = random_split(dataset, [1.0])[0]
    data_loader = DataLoader(dataset)
    for batch in data_loader:
        pass


def test_slicing_of_subset_of_dataset():
    # Testing slicing a subset initialized with a dataset
    dataset = TensorDataset(torch.tensor([1, 2, 3, 4, 5]))
    subset_of_dataset = Subset(dataset, [0, 1, 2, 3, 4])
    assert np.allclose(subset_of_dataset[:][0], dataset[:][0])
    assert np.allclose(subset_of_dataset[1:2][0], dataset[1:2][0])
    assert np.allclose(subset_of_dataset[0:-1:2][0], dataset[0:-1:2][0])
    # Testing slicing of subset from random split
    subset1, subset2 = random_split(dataset, [3, 2])
    assert np.allclose(subset1[:][0], dataset[subset1.indices[:]][0])
    assert np.allclose(subset1[0:2][0], dataset[subset1.indices[0:2]][0])
    assert np.allclose(subset1[0:-1:2][0], dataset[subset1.indices[0:-1:2]][0])

def test_slicing_of_subset_of_subset():
    # Testing slicing a subset initialized with a subset
    dataset = TensorDataset(torch.tensor([1, 2, 3, 4, 5]))
    subset_of_dataset = Subset(dataset, [0, 1, 2, 3, 4])
    subset_of_subset = Subset(subset_of_dataset, [0, 1, 2, 3, 4])
    assert np.allclose(subset_of_subset[:][0], dataset[:][0])
    assert np.allclose(subset_of_subset[0:2][0], dataset[0:2][0])
    assert np.allclose(subset_of_subset[0:-1:2][0], dataset[0:-1:2][0])
    # Testing slicing of subset of subset from random split
    subset1, subset2 = random_split(dataset, [4, 1])
    subset_of_subset1, subset_of_subset2 = random_split(subset1, [3, 1])
    idx = [subset1.indices[i] for i in subset_of_subset1.indices]
    assert np.allclose(subset_of_subset1[:][0], dataset[idx[:]][0])
    assert np.allclose(subset_of_subset1[0:2][0], dataset[idx[0:2]][0])
    assert np.allclose(subset_of_subset1[0:-1:2][0], dataset[idx[0:-1:2]][0])

class CountingDataset(Dataset):
    def __init__(self, n):
        super(CountingDataset, self).__init__()
        self.n = n

    def __getitem__(self, i):
        return i

    def __len__(self):
        return self.n


class CountingIterableDataset(IterableDataset):
    def __init__(self, n):
        super(CountingIterableDataset, self).__init__()
        self.n = n

    def __iter__(self):
        return iter(range(self.n))

    def __len__(self):
        return self.n



def test_len():
    source = TensorDataset(torch.randn(15, 10, 2, 3, 4, 5), torch.randperm(15))
    assert np.allclose(len(source), 15)

def test_getitem():
    t = torch.randn(15, 10, 2, 3, 4, 5)
    l = torch.randn(15, 10)
    source = TensorDataset(t, l)
    for i in range(15):
        assert np.allclose(t[i].asnumpy(), source[i][0])
        assert np.allclose(l[i].asnumpy(), source[i][1])

def test_getitem_1d():
    t = torch.randn(15)
    l = torch.randn(15)
    source = TensorDataset(t, l)
    for i in range(15):
        assert np.allclose(t[i].asnumpy(), source[i][0])
        assert np.allclose(l[i].asnumpy(), source[i][1])

def test_single_tensor():
    t = torch.randn(5, 10)
    source = TensorDataset(t)
    assert np.allclose(len(source), 5)
    for i in range(5):
        assert np.allclose(t[i].asnumpy(), source[i][0])

def test_many_tensors():
    t0 = torch.randn(5, 10, 2, 3, 4, 5)
    t1 = torch.randn(5, 10)
    t2 = torch.randn(5, 10, 2, 5)
    t3 = torch.randn(5, 10, 3, 7)
    source = TensorDataset(t0, t1, t2, t3)
    assert np.allclose(len(source), 5)
    for i in range(5):
        assert np.allclose(t0[i].asnumpy(), source[i][0])
        assert np.allclose(t1[i].asnumpy(), source[i][1])
        assert np.allclose(t2[i].asnumpy(), source[i][2])
        assert np.allclose(t3[i].asnumpy(), source[i][3])

def test_concat_two_singletons():
    result = ConcatDataset([[0], [1]])
    assert np.allclose(2, len(result))
    assert np.allclose(0, result[0])
    assert np.allclose(1, result[1])

def test_concat_two_non_singletons():
    result = ConcatDataset([[0, 1, 2, 3, 4],
                            [5, 6, 7, 8, 9]])
    assert np.allclose(10, len(result))
    assert np.allclose(0, result[0])
    assert np.allclose(5, result[5])

def test_concat_two_non_singletons_with_empty():
    # Adding an empty dataset somewhere is correctly handled
    result = ConcatDataset([[0, 1, 2, 3, 4],
                            [],
                            [5, 6, 7, 8, 9]])
    assert np.allclose(10, len(result))
    assert np.allclose(0, result[0])
    assert np.allclose(5, result[5])

def test_add_dataset():
    d1 = TensorDataset(torch.randn(7, 3, 28, 28), torch.randn(7))
    d2 = TensorDataset(torch.randn(7, 3, 28, 28), torch.randn(7))
    d3 = TensorDataset(torch.randn(7, 3, 28, 28), torch.randn(7))
    result = d1 + d2 + d3
    assert np.allclose(21, len(result))
    assert np.allclose(0, (torch.tensor(d1[0][0]) - torch.tensor(result[0][0])).abs().sum().asnumpy())
    assert np.allclose(0, (torch.tensor(d2[0][0]) - torch.tensor(result[7][0])).abs().sum().asnumpy())
    assert np.allclose(0, (torch.tensor(d3[0][0]) - torch.tensor(result[14][0])).abs().sum().asnumpy())


# takes in dummy var so this can also be used as a `worker_init_fn`
def set_faulthander_if_available(_=None):
    faulthandler.enable(sys.__stderr__)
    if not IS_WINDOWS:
        # windows does not have faulthandler.register
        # chain=False prevents the default behavior of killing the process
        faulthandler.register(signal.SIGUSR1, file=sys.__stderr__, chain=False)


set_faulthander_if_available()

# Process `pid` must have called `set_faulthander_if_available`
def print_traces_of_all_threads(pid):
    if not IS_WINDOWS:
        # use the custom signal if available
        os.kill(pid, signal.SIGUSR1)
    else:
        # otherwise we can still use the handler given by faulthandler.enable()
        # at the cost of killing the process.
        os.kill(pid, signal.SIGSEGV)

    # wait in parent process to give subprocess some time to print
    time.sleep(5)


class ErrorTrackingProcess(mp.Process):

    # Why no *args?
    #   py2 doesn't support def fn(x, *args, key=val, **kwargs)
    # Setting disable_stderr=True may generate a lot of unrelated error outputs
    # but could be helpful for debugging.
    def __init__(self, disable_stderr=True, **kwargs):
        super(ErrorTrackingProcess, self).__init__(**kwargs)
        self._pconn, self._cconn = mp.Pipe()
        self._exception = None
        self.disable_stderr = disable_stderr

    def run(self):
        set_faulthander_if_available()
        if self.disable_stderr:
            # Disable polluting stderr with errors that are supposed to happen.
            with open(os.devnull, 'w') as devnull:
                os.dup2(devnull.fileno(), sys.stderr.fileno())
        try:
            super(ErrorTrackingProcess, self).run()
            self._cconn.send(None)
        except Exception:
            self._cconn.send(ExceptionWrapper(sys.exc_info()))
            raise

    def print_traces_of_all_threads(self):
        assert self.is_alive(), "can only use print_traces_of_all_threads if the process is alive"
        assert not self.disable_stderr, "do not disable stderr if you use print_traces_of_all_threads"
        # On platforms without `SIGUSR1`, `set_faulthander_if_available` sets
        # `faulthandler.enable()`, and `print_traces_of_all_threads` may kill
        # the process. So let's poll the exception first
        _ = self.exception
        print_traces_of_all_threads(self.pid)

    @property
    def exception(self):
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        if self._exception is None:
            return None
        else:
            return self._exception.exc_type(self._exception.exc_msg)

    # ESRCH means that os.kill can't finds alive proc
    def send_signal(self, signum, ignore_ESRCH=False):
        try:
            os.kill(self.pid, signum)
        except OSError as e:
            if not ignore_ESRCH or e.errno != errno.ESRCH:
                raise


class ErrorDataset(Dataset):

    def __init__(self, size):
        self.size = size

    def __len__(self):
        return self.size


class SegfaultDataset(Dataset):

    def __init__(self, size):
        self.size = size

    def __getitem__(self, idx):
        return ctypes.string_at(0)

    def __len__(self):
        return self.size


class SleepDataset(Dataset):

    def __init__(self, size, sleep_sec):
        self.size = size
        self.sleep_sec = sleep_sec
        self.sleeped = False

    def __getitem__(self, idx):
        if not self.sleeped:
            time.sleep(self.sleep_sec)
            self.sleeped = True
        return idx

    def __len__(self):
        return self.size


class SeedDataset(Dataset):

    def __init__(self, size):
        self.size = size

    def __getitem__(self, idx):
        return ms.get_seed()

    def __len__(self):
        return self.size


class WorkerSpecificIterableDataset(IterableDataset):
    def __init__(self, sizes_for_all_workers):
        self.sizes_for_all_workers = sizes_for_all_workers

    def __iter__(self):
        worker_info = torch.utils.data.get_worker_info()
        assert worker_info is not None
        return iter(range(self.sizes_for_all_workers[worker_info.id]))

    def __len__(self):
        return sum(self.sizes_for_all_workers)



class SynchronizedDataset(Dataset):

    def __init__(self, size, batch_size, num_workers):
        assert size >= num_workers * batch_size
        self.count = mp.Value('i', 0, lock=True)
        self.barrier = mp.Semaphore(0)
        self.num_workers = num_workers
        self.size = size

    def sync_once(self):
        with self.count.get_lock():
            self.count.value += 1
            if self.count.value == self.num_workers:
                self.barrier.release()
        self.barrier.acquire()
        self.barrier.release()

    def __getitem__(self, idx):
        raise NotImplementedError

    def __len__(self):
        return self.size


class EmptyTensorDataset(torch.utils.data.Dataset):
    def __init__(self, len):
        self.len = len

    def __len__(self):
        return self.len

    def __getitem__(self, any):
        return torch.empty(0)


class SynchronizedSeedDataset(SynchronizedDataset):
    def __getitem__(self, idx):
        self.sync_once()
        return ms.get_seed()


def _test_timeout(persistent_workers):
    dataset = SleepDataset(10, 3)
    dataloader = DataLoader(dataset, batch_size=2, num_workers=1, timeout=1,
                            persistent_workers=persistent_workers)
    _ = next(iter(dataloader))


def _test_timeout_pin_memory(persistent_workers):
    dataset = SleepDataset(10, 3)
    dataloader = DataLoader(dataset, batch_size=2, num_workers=1, timeout=1, pin_memory=True,
                            persistent_workers=persistent_workers)
    _ = next(iter(dataloader))


def _test_large_sampler_indices(persistent_workers):

    dataloader = torch.utils.data.DataLoader(
        EmptyTensorDataset(10000000),
        batch_size=40960,
        persistent_workers=persistent_workers,
        num_workers=1)

    it = iter(dataloader)

    for x in it:
        assert x.numel() == 0
        raise RuntimeError('My Error')


def disable_stderr(worker_id):
    r"""
    Avoids printing "ERROR: Unexpected segmentation fault encountered in worker."
    from workers. Since worker signal handler prints with low-level write(),
    this has to be done on OS level via dup.
    This is used as worker_init_fn for test_segfault.
    """
    sys.stderr.flush()  # flush library buffers that dup2 knows nothing about
    # Can't use a with-block because otherwise the fd will be closed when this
    # function ends.
    with open(os.devnull, 'w') as devnull:
        os.dup2(devnull.fileno(), sys.stderr.fileno())


def _test_segfault():
    dataset = SegfaultDataset(10)
    dataloader = DataLoader(dataset, batch_size=2, num_workers=1, worker_init_fn=disable_stderr)
    _ = next(iter(dataloader))

def _test_no_segfault():
    dataset = [1, 2, 3]
    num_threads = torch.get_num_threads()
    if num_threads < 4:
        torch.set_num_threads(4)
    else:
        torch.set_num_threads(num_threads)
    mp_ctx = torch.multiprocessing.get_context(method='fork')
    dataloader = DataLoader(dataset, num_workers=1, worker_init_fn=disable_stderr,
                            multiprocessing_context=mp_ctx)
    _ = next(iter(dataloader))

class TestProperExitDataset(Dataset):
    def __init__(self, size, error_event):
        self.size = size
        self.error_event = error_event

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        worker_info = torch.utils.data.get_worker_info()
        if self.error_event is not None and self.error_event.is_set() and \
                worker_info.id == worker_info.num_workers - 1:
            # only error in the last worker
            raise RuntimeError('Worker error')
        return torch.tensor([idx])


class TestProperExitIterableDataset(IterableDataset):
    def __init__(self, size, error_event):
        self.error_event = error_event
        self.size = size
        self.remaining = size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self

    def __next__(self):
        worker_info = torch.utils.data.get_worker_info()
        if self.error_event is not None and self.error_event.is_set() and \
                worker_info.id == worker_info.num_workers - 1:
            # only error in the last worker
            raise RuntimeError('Worker error')
        self.remaining -= 1
        if self.remaining < 0:
            raise StopIteration
        return torch.tensor(-1000)


# See TestDataLoader.test_proper_exit for usage
def _test_proper_exit(is_iterable_dataset, use_workers, pin_memory, exit_method,
                      hold_iter_reference, loader_setup_event, tester_setup_event,
                      persistent_workers):
    num_workers = 2 if use_workers else 0

    if exit_method == 'worker_error' or exit_method == 'worker_kill':
        assert use_workers is True

    if exit_method == 'worker_error':
        worker_error_event = mp.Event()
    else:
        worker_error_event = None

    if is_iterable_dataset:
        ds = TestProperExitIterableDataset(7, worker_error_event)
    else:
        ds = TestProperExitDataset(12, worker_error_event)

    loader = DataLoader(ds, batch_size=1, shuffle=False,
                        num_workers=num_workers, pin_memory=pin_memory,
                        worker_init_fn=set_faulthander_if_available,
                        persistent_workers=persistent_workers)

    error_it = 2

    if use_workers:
        # 2 is the magical per-worker prefetch number...
        # FIXME: change this after the number becomes configurable.
        if is_iterable_dataset:
            assert len(ds) * num_workers > (error_it + 2 + 1)
        else:
            assert len(loader) > (error_it + 2 + 1) * num_workers
    else:
        if is_iterable_dataset:
            assert len(ds) > error_it + 1
        else:
            assert len(loader) > error_it + 1

    it = iter(loader)
    if use_workers:
        workers = it._workers

    def kill_pid(pid):
        psutil_p = psutil.Process(pid)
        psutil_p.kill()
        psutil_p.wait(JOIN_TIMEOUT)
        assert not psutil_p.is_running()

    for i, _ in enumerate(it):
        if i == 0:
            if not hold_iter_reference:
                del it
                del loader
            loader_setup_event.set()
            tester_setup_event.wait()
            # ensure that the workers are still alive
            if use_workers:
                for w in workers:
                    assert w.is_alive()
            if worker_error_event is not None:
                worker_error_event.set()

        if i == error_it:
            if exit_method == 'loader_error':
                raise RuntimeError('Loader error')
            elif exit_method == 'loader_kill':
                kill_pid(os.getpid())
            elif exit_method == 'worker_kill':
                kill_pid(workers[-1].pid)  # kill last worker

    if not hold_iter_reference:
        # Tries to trigger the __del__ clean-up rather than the automatic
        # exiting of daemonic children. Technically it should be automatically
        # triggered, but I don't want to rely on the implementation detail of
        # Python gc.
        gc.collect()


class TestWorkerInfoDataset(SynchronizedDataset):
    def __getitem__(self, idx):
        self.sync_once()
        return torch.tensor(self.value)


# Should be used as worker_init_fn with TestWorkerInfoDataset.
# See _test_get_worker_info below for usage.
def _test_worker_info_init_fn(worker_id):
    worker_info = torch.utils.data.get_worker_info()
    assert worker_id == worker_info.id, "worker_init_fn and worker_info should have consistent id"
    assert worker_id < worker_info.num_workers, "worker_init_fn and worker_info should have valid id"
    assert worker_info.seed == ms.get_seed(), "worker_init_fn and worker_info should have consistent seed"
    dataset = worker_info.dataset
    assert isinstance(dataset, TestWorkerInfoDataset), "worker_info should have correct dataset copy"
    assert not hasattr(dataset, 'value'), "worker_info should have correct dataset copy"
    # test that WorkerInfo attributes are read-only
    try:
        worker_info.id = 3999
    except RuntimeError as e:
        assert str(e) == "Cannot assign attributes to WorkerInfo objects"
    try:
        worker_info.a = 3
    except RuntimeError as e:
        assert str(e) == "Cannot assign attributes to WorkerInfo objects"
    for k in ['id', 'num_workers', 'seed', 'dataset']:
        assert "{}=".format(k) in repr(worker_info)
    dataset.value = [worker_id, os.getpid()]


def _test_get_worker_info():
    # get_worker_info returns None in main proc
    assert torch.utils.data.get_worker_info() is None
    num_workers = 2
    batch_size = 2
    dataset = TestWorkerInfoDataset(6, batch_size, num_workers)
    dataloader = DataLoader(dataset, batch_size=batch_size,
                            num_workers=num_workers,
                            worker_init_fn=_test_worker_info_init_fn)
    it = iter(dataloader)
    data = []
    for d in it:
        data.append(d)
    worker_pids = [w.pid for w in it._workers]
    data = torch.cat(data, 0)
    for d in data:
        # each `d` is a [worker_id, worker_pid] pair, which is set in
        # _test_worker_info_init_fn
        assert d[1] == worker_pids[d[0]]
    # get_worker_info returns None in main proc after data loading
    assert torch.utils.data.get_worker_info() is None
    # main proc dataset was never assigned this attribute
    assert not hasattr(dataset, 'value')
    try:
        _ = dataset[0]
    except AttributeError:
        return
    raise RuntimeError('Expected AttributeError')


# test custom init function
def init_fn(worker_id):
    ms.set_seed(12345)


# used with test_error_in_init
class ErrorIterableDataset(IterableDataset):
    def __iter__(self):
        raise RuntimeError("Error in __iter__")


# used with test_error_in_init
def error_worker_init_fn(_):
    raise RuntimeError("Error in worker_init_fn")


class BulkLoadingDataset(Dataset):
    def __init__(self, length):
        self.length = length

    def __getitem__(self, indices):
        assert isinstance(indices, (list, tuple))
        return torch.tensor(indices)

    def __len__(self):
        return self.length


class BulkLoadingSampler(torch.utils.data.Sampler):
    def __init__(self, dataset, batch_size):
        self.dataset = dataset
        self.batch_size = batch_size

    def __iter__(self):
        for x in torch.randperm(len(self.dataset)).split(self.batch_size):
            yield x.asnumpy().tolist()

    def __len__(self):
        return int(math.ceil(len(self.dataset) / float(self.batch_size)))


class TestMultiEpochDataset(IterableDataset):
    def __init__(self, length):
        self.length = length

    def __iter__(self):
        worker_info = torch.utils.data.get_worker_info()
        assert worker_info is not None
        worker_id = worker_info.id
        for idx in range(self.length // worker_info.num_workers):
            yield worker_id

    def __len__(self):
        return self.length


class CustomList(list):
    pass


class CustomDict(dict):
    pass


def row_processor(row):
    return np.add(row, 1)


def filter_len(row):
    return len(row) == 4

from ...utils import is_test_under_ascend_context
if is_test_under_ascend_context():
    data = np.random.randn(100, 2, 3, 5).astype(np.float32)
else:
    data = np.random.randn(100, 2, 3, 5)
labels = np.random.permutation(50).repeat(2)
dataset = TensorDataset(data, labels)
persistent_workers = False


def _get_data_loader(dataset, **kwargs):
    persistent_workers = kwargs.get('persistent_workers', False)
    if persistent_workers and kwargs.get('num_workers', 0) == 0:
        persistent_workers = False
    kwargs['persistent_workers'] = persistent_workers
    return DataLoader(dataset, **kwargs)

def _test_sequential(loader):
    batch_size = loader.batch_size
    if batch_size is None:
        for idx, (sample, target) in enumerate(loader):
            assert np.allclose(sample.asnumpy(), data[idx])
            assert np.allclose(target.asnumpy(), labels[idx])
        assert np.allclose(idx, len(dataset) - 1)
    else:
        for i, (sample, target) in enumerate(loader):
            idx = i * batch_size
            assert np.allclose(sample.asnumpy(), data[idx:idx + batch_size])
            assert np.allclose(target.asnumpy(), labels[idx:idx + batch_size])
        assert np.allclose(i, math.floor((len(dataset) - 1) / batch_size))

def _test_shuffle(loader):
    found_data = {i: 0 for i in range(data.shape[0])}
    found_labels = {i: 0 for i in range(labels.shape[0])}
    batch_size = loader.batch_size
    if batch_size is None:
        for i, (batch_samples, batch_targets) in enumerate(loader):
            sample, target = (batch_samples, batch_targets)
            target = torch.tensor(target)
            for data_point_idx, data_point in enumerate(data):
                data_point = torch.tensor(data_point)
                sample = torch.tensor(sample)
                res = ms.ops.equal(data_point, sample)
                res = res.all()
                if res:
                    found_data[data_point_idx] += 1
                    break
            assert np.allclose(target.asnumpy(), labels[data_point_idx])
            found_labels[data_point_idx] += 1
            assert np.allclose(sum(found_data.values()), (i + 1))
            assert np.allclose(sum(found_labels.values()), (i + 1))
        assert np.allclose(i, (len(dataset) - 1))
    else:
        for i, (batch_samples, batch_targets) in enumerate(loader):
            for sample, target in zip(batch_samples, batch_targets):
                target = torch.tensor(target)
                for data_point_idx, data_point in enumerate(data):
                    data_point = torch.tensor(data_point)
                    sample = torch.tensor(sample)
                    res = ms.ops.equal(data_point, sample)
                    res = res.all()
                    if res:
                        found_data[data_point_idx] += 1
                        break
                assert np.allclose(target.asnumpy(), labels[data_point_idx])
                found_labels[data_point_idx] += 1
            assert np.allclose(sum(found_data.values()), (i + 1) * batch_size)
            assert np.allclose(sum(found_labels.values()), (i + 1) * batch_size)
        assert np.allclose(i, math.floor((len(dataset) - 1) / batch_size))

def _test_error(loader):
    it = iter(loader)
    errors = 0
    while True:
        try:
            next(it)
        except NotImplementedError:
            errors += 1
        except StopIteration:
            assert np.allclose(errors,
                             math.ceil(float(len(loader.dataset)) / loader.batch_size))
            return


def test_sequential_nonbatch():
    _test_sequential(_get_data_loader(dataset, batch_size=None))

def test_sequential_batch():
    _test_sequential(_get_data_loader(dataset))
    _test_sequential(_get_data_loader(dataset, batch_size=2))

def test_growing_dataset():
    dataset = [torch.ones(4) for _ in range(4)]
    dataloader_seq = _get_data_loader(dataset, shuffle=False)
    dataloader_shuffle = _get_data_loader(dataset, shuffle=True)
    dataset.append(torch.ones(4))
    assert np.allclose(len(dataloader_seq), 5)
    assert np.allclose(len(dataloader_shuffle), 5)


# def test_multiple_dataloaders():
#     for multiprocessing_context in supported_multiprocessing_contexts:
#         loader1_it = iter(_get_data_loader(dataset, num_workers=0))
#         loader2_it = iter(_get_data_loader(dataset, num_workers=0, multiprocessing_context=multiprocessing_context))
#         next(loader1_it)
#         next(loader1_it)
#         next(loader2_it)
#         next(loader2_it)
#         next(loader1_it)
#         next(loader2_it)
#         del loader1_it
#         del loader2_it


def test_builtin_collection_conversion():
    for coll_ty in (list, tuple):
            # map-style dataset
        dataset = CountingDataset(20)
        # no auto-batching
        fetched = coll_ty(_get_data_loader(dataset, batch_size=None, num_workers=0))
        assert np.allclose(fetched, coll_ty(range(20)))
        # auto-batching
        fetched = coll_ty(_get_data_loader(dataset, batch_size=2, num_workers=0))
        sample = coll_ty(torch.tensor([i, i + 1]) for i in range(0, 20, 2))
        for i in range(len(fetched)):
            assert np.allclose(fetched[i].asnumpy(), sample[i].asnumpy())

        # iterable-style dataset
        dataset = CountingIterableDataset(20)
        # no auto-batching
        fetched = coll_ty(_get_data_loader(dataset, batch_size=None, num_workers=0))
        assert np.allclose(fetched, coll_ty(range(20)))

        fetched = coll_ty(_get_data_loader(dataset, batch_size=2, num_workers=0))
        sample = coll_ty(torch.tensor([i, i + 1]) for i in range(0, 20, 2))
        for i in range(len(fetched)):
            assert np.allclose(fetched[i].asnumpy(), sample[i].asnumpy())

def test_iterable_style_dataset():
    # [no auto-batching] single process loading
    dataset = CountingIterableDataset(20)
    dataloader = _get_data_loader(dataset, batch_size=None)
    fetched = list(dataloader)
    assert np.allclose(len(fetched), 20)
    for i, d in enumerate(fetched):
        # non-batched should not convert ints into tensors
        assert np.allclose(d, i)
    # DataLoader should match len of the iterable-style dataset (if implemented)
    assert np.allclose(len(dataloader), len(dataset))

    # [no auto-batching] multiprocessing loading
    # num_workers = 3
    # sizes_for_all_workers = [0, 4, 20]
    # expected = sorted(sum((list(range(s)) for s in sizes_for_all_workers), []))
    # assert len(sizes_for_all_workers) == num_workers, 'invalid test case'
    # for prefetch_factor in [2, 3, 4]:
    #     dataset = WorkerSpecificIterableDataset(sizes_for_all_workers)
    #     dataloader = _get_data_loader(dataset, num_workers=num_workers, batch_size=None,
    #                                        worker_init_fn=set_faulthander_if_available,
    #                                        prefetch_factor=prefetch_factor)
    #     dataloader_iter = iter(dataloader)
    #     fetched = sorted(dataloader_iter)
    #     for a, b in zip(fetched, expected):
    #         # non-batched should not convert ints into tensors
    #         assert np.allclose(a, b)
    #     # DataLoader should match len of the iterable-style dataset (if implemented)
    #     assert np.allclose(len(dataloader), len(dataset))
    #     # When loading more than len(dataset) data, after accessing len(dataloader),
    #     # we should get a warning. See NOTE [ IterableDataset and __len__ ].
    #     dataset = CountingIterableDataset(20)
    #     dataloader = _get_data_loader(dataset, num_workers=num_workers,
    #                                        worker_init_fn=set_faulthander_if_available,
    #                                        prefetch_factor=prefetch_factor)
    #     it = iter(dataloader)
    #     assert np.allclose(len(dataloader), len(dataset))
    #     assert np.allclose(len(dataloader), 20)
    #     it = iter(dataloader)
    # # [no auto-batching] test that workers exit gracefully
    # workers = dataloader_iter._workers
    # del dataloader_iter
    # del dataloader
    # try:
    #     for w in workers:
    #         w.join(JOIN_TIMEOUT)
    #         assert np.allclose(w.exitcode, 0)
    # finally:
    #     for w in workers:
    #         w.terminate()
    #
    # # [auto-batching] single process loading
    # dataset = CountingIterableDataset(20)
    # fetched = list(_get_data_loader(dataset, batch_size=7))
    # assert np.allclose(len(fetched), 3)
    # assert np.allclose(fetched[0].asnumpy().tolist(), list(range(7)))
    # assert np.allclose(fetched[1].asnumpy().tolist(), list(range(7, 14)))
    # assert np.allclose(fetched[2].asnumpy().tolist(), list(range(14, 20)))
    #
    # # [auto-batching] multiprocessing loading
    # num_workers = 3
    # sizes_for_all_workers = [0, 4, 20]
    # expected = sorted(sum((list(range(s)) for s in sizes_for_all_workers), []))
    # assert len(sizes_for_all_workers) == num_workers, 'invalid test case'
    # for prefetch_factor in [2, 3, 4]:
    #     dataset = WorkerSpecificIterableDataset(sizes_for_all_workers)
    #     # worker 0 should return 0 batches
    #     # worker 1 should return 1 batches
    #     # worker 2 should return 3 batches
    #     dataloader = _get_data_loader(dataset, num_workers=num_workers, batch_size=7, prefetch_factor=prefetch_factor)
    #     dataloader_iter = iter(dataloader)
    #     fetched = list(dataloader_iter)
    #     assert np.allclose(len(fetched), 4)
    #     fetched = set(tuple(t.tolist()) for t in fetched)
    #     assert np.allclose(fetched, tuple(range(4)))
    #     assert np.allclose(fetched, tuple(range(7)))
    #     assert np.allclose(fetched, tuple(range(7, 14)))
    #     assert np.allclose(fetched, tuple(range(14, 20)))
    #
    #     # [auto-batching] test that workers exit gracefully
    #     workers = dataloader_iter._workers
    #     del dataloader_iter
    #     del dataloader
    #     try:
    #         for w in workers:
    #             w.join(JOIN_TIMEOUT)
    #             assert np.allclose(w.exitcode, 0)
    #     finally:
    #         for w in workers:
    #             w.terminate()
    # # [auto-batching & drop_last] single process loading
    # dataset = CountingIterableDataset(20)
    # fetched = list(_get_data_loader(dataset, batch_size=7, drop_last=True))
    # assert np.allclose(len(fetched), 2)
    # assert np.allclose(fetched[0].tolist(), list(range(7)))
    # assert np.allclose(fetched[1].tolist(), list(range(7, 14)))
    #
    # # [auto-batching & drop_last] multiprocessing loading
    # num_workers = 3
    # sizes_for_all_workers = [0, 4, 20]
    # expected = sorted(sum((list(range(s)) for s in sizes_for_all_workers), []))
    # assert len(sizes_for_all_workers) == num_workers, 'invalid test case'
    # for prefetch_factor in [2, 3, 4]:
    #     dataset = WorkerSpecificIterableDataset(sizes_for_all_workers)
    #     # worker 0 should return 0 batches
    #     # worker 1 should return 1 batches
    #     # worker 2 should return 3 batches
    #     dataloader = _get_data_loader(dataset, num_workers=num_workers, batch_size=7, drop_last=True,
    #                                        worker_init_fn=set_faulthander_if_available,
    #                                        prefetch_factor=prefetch_factor)
    #     dataloader_iter = iter(dataloader)
    #     fetched = list(dataloader_iter)
    #     assert np.allclose(len(fetched), 2)
    #     fetched = set(tuple(t.tolist()) for t in fetched)
    #     assert np.allclose(fetched, {tuple(range(7)), tuple(range(7, 14))})
    #
    #     # [auto-batching & drop_last] test that workers exit gracefully
    #     workers = dataloader_iter._workers
    #     del dataloader_iter
    #     del dataloader
    #     try:
    #         for w in workers:
    #             w.join(JOIN_TIMEOUT)
    #             assert np.allclose(w.exitcode, 0)
    #     finally:
    #         for w in workers:
    #             w.terminate()

def test_chain_iterable_style_dataset():
    dataset1 = CountingIterableDataset(20)
    dataset2 = CountingIterableDataset(15)
    expected = list(range(20)) + list(range(15))
    for num_workers in [0]: #TODO test num_workers > 0
        for chained_dataset in [dataset1 + dataset2, ChainDataset([dataset1, dataset2])]:
            fetched = list(_get_data_loader(chained_dataset, num_workers=num_workers))
            assert np.allclose(len(fetched), len(expected))
            for e, d in zip(expected, fetched):
                assert np.allclose(e, d.asnumpy())


# def test_multiprocessing_contexts():
#     reference = [
#         torch.arange(0, 3),
#         torch.arange(3, 6),
#         torch.arange(6, 9),
#         torch.arange(9, 11),
#     ]
#     counting_ds_n = 11
#     dl_common_args = dict(num_workers=1, batch_size=3)
#     for ctx in supported_multiprocessing_contexts:
#         ds_cls = CountingDataset
#         sample = list(_get_data_loader(ds_cls(counting_ds_n), multiprocessing_context=ctx, **dl_common_args))
#         for i in range(4):
#             assert np.allclose(reference[i].asnumpy(), sample[i].asnumpy())
#         if ctx is not None:
#             # test ctx object
#             ctx = mp.get_context(ctx)
#             sample = list(_get_data_loader(ds_cls(counting_ds_n), multiprocessing_context=ctx, **dl_common_args))
#             for i in range(4):
#                 assert np.allclose(reference[i].asnumpy(), sample[i].asnumpy())


# def test_worker_seed():
#     num_workers = 6
#     batch_size = 1
#     dataset = SynchronizedSeedDataset(num_workers, batch_size, num_workers)
#     dataloader = _get_data_loader(dataset, batch_size=batch_size, num_workers=num_workers)
#     seeds = set()
#     for batch in dataloader:
#         seeds.add(batch[0])
#     assert np.allclose(len(seeds), num_workers)
#
def test_worker_seed_reproducibility():
    np.random.seed(42)
    ms.set_seed(42)
    def get_dataloader():
        return DataLoader(dataset, batch_size=batch_size, num_workers=num_workers)

    num_workers = 0 # TODO test num_workers > 0
    batch_size = 1
    dataset = SynchronizedSeedDataset(num_workers, batch_size, num_workers)
    first = list(int(batch) for batch in get_dataloader())
    second = list(int(batch) for batch in get_dataloader())
    for i in range(len(first)):
        assert np.allclose(first[i], second[i])

def test_multi_epochs_reproducibility():
    num_workers = 3 # TODO test num_workers > 0
    batch_size = 10
    num_epochs = 3

    dataset = TestMultiEpochDataset(batch_size * num_workers)
    dataloader = _get_data_loader(dataset, batch_size=batch_size,
                                       shuffle=False, num_workers=num_workers)

    for ind in range(num_epochs):
        for batch_idx, sample in enumerate(dataloader):
            np.allclose(sample.asnumpy().tolist(), [batch_idx % num_workers] * batch_size)


# def test_get_worker_info():
#     p = ErrorTrackingProcess(target=_test_get_worker_info)
#     p.start()
#     p.join(JOIN_TIMEOUT)
#     try:
#         assert p.is_alive() is not False
#         np.allclose(p.exitcode, 0)
#     finally:
#         p.terminate()

def test_shuffle():
    _test_shuffle(_get_data_loader(dataset, shuffle=True))

def test_shuffle_batch_none():
    _test_shuffle(DataLoader(dataset, batch_size=None))

def test_shuffle_batch():
    _test_shuffle(_get_data_loader(dataset, batch_size=2, shuffle=True))

def test_shuffle_reproducibility():
    np.random.seed(42)
    ms.set_seed(42)
    first = list(DataLoader(dataset, shuffle=True, num_workers=0))
    np.random.seed(42)
    second = list(DataLoader(dataset, shuffle=True, num_workers=0))
    length = len(first)
    for i in range(length):
        for j in range(len(first[i])):
            assert np.allclose(first[i][j].asnumpy(), second[i][j].asnumpy())


def test_sequential_workers():
    _test_sequential(_get_data_loader(dataset, num_workers=4))

def test_seqential_batch_workers():
    _test_sequential(_get_data_loader(dataset, batch_size=2, num_workers=4))

def test_seqential_batch_workers_prefetch():
    _test_sequential(DataLoader(dataset, batch_size=2, num_workers=4, prefetch_factor=3))

def test_shuffle_workers():
    _test_shuffle(_get_data_loader(dataset, shuffle=True, num_workers=4))

def test_shuffle_batch_workers():
    _test_shuffle(_get_data_loader(dataset, batch_size=2, shuffle=True, num_workers=4))

def test_shuffle_batch_workers_prefetch():
    _test_shuffle(DataLoader(dataset, batch_size=2, shuffle=True, num_workers=4, prefetch_factor=3))

def test_random_sampler():

    from collections import Counter
    from mindtorch.torch.utils.data import RandomSampler

    def sample_stat(sampler, num_samples):
        counts = Counter(sampler)
        count_repeated = sum(val > 1 for val in counts.values())
        return (count_repeated, min(counts.keys()), max(counts.keys()), sum(counts.values()))

    # test sample with replacement
    n = len(dataset) + 1  # ensure at least one sample is drawn more than once
    sampler_with_replacement = RandomSampler(dataset, replacement=True, num_samples=n)
    count_repeated, minval, maxval, count_total = sample_stat(sampler_with_replacement, n)
    assert np.allclose(count_total, n)

    # test sample without replacement and without specified num_samples
    sampler_without_replacement = RandomSampler(dataset)
    count_repeated, minval, maxval, count_total = sample_stat(sampler_without_replacement, len(dataset))
    assert np.allclose(count_repeated, 0)
    assert np.allclose(minval , 0)
    assert np.allclose(maxval , len(dataset) - 1)
    assert np.allclose(count_total , len(dataset))

    # test sample without replacement and with specified num_samples
    n = len(dataset) * 2
    sampler_without_replacement = RandomSampler(dataset, num_samples=n)
    count_repeated, minval, maxval, count_total = sample_stat(sampler_without_replacement, len(dataset))
    assert np.allclose(count_repeated, len(dataset))
    assert np.allclose(minval, 0)
    assert np.allclose(maxval, len(dataset) - 1)
    assert np.allclose(count_total, n)

    n = len(dataset) - 1
    sampler_without_replacement = RandomSampler(dataset, num_samples=n)
    count_repeated, minval, maxval, count_total = sample_stat(sampler_without_replacement, len(dataset))
    assert np.allclose(count_total, n)

    n = len(dataset) + 1
    sampler_without_replacement = RandomSampler(dataset, num_samples=n)
    count_repeated, minval, maxval, count_total = sample_stat(sampler_without_replacement, len(dataset))
    assert np.allclose(count_repeated , 1)
    assert np.allclose(minval,0)
    assert np.allclose(maxval, len(dataset) - 1)
    assert np.allclose(count_total, n)



def test_random_sampler_len_with_replacement():
    from mindtorch.torch.utils.data import RandomSampler
    # add 5 extra samples
    num_samples = len(dataset) + 5
    sampler = RandomSampler(dataset,
                            replacement=True,
                            num_samples=num_samples)
    # test len method
    assert np.allclose(num_samples, len(sampler))

    # test with iteration
    count_num_samples = sum(1 for _ in sampler)
    assert np.allclose(num_samples, count_num_samples)

    # test with dataloader, batch_size = 1
    batch_size = 1
    count_num_samples_in_data_loader = len(_get_data_loader(
        dataset, batch_size=batch_size, sampler=sampler))
    assert np.allclose(num_samples, count_num_samples_in_data_loader)

    # test with dataloader, batch_size = 6
    batch_size = 6
    count_num_samples_in_data_loader = len(_get_data_loader(
        dataset, batch_size=batch_size, sampler=sampler))
    assert np.allclose(int(math.ceil(float(num_samples) / batch_size)),
                     count_num_samples_in_data_loader)

def test_random_sampler_len_without_replacement():
    from mindtorch.torch.utils.data import RandomSampler
    # add 5 extra samples
    num_samples = len(dataset) + 5
    sampler = RandomSampler(dataset,
                            replacement=False,
                            num_samples=num_samples)
    # test len method
    assert np.allclose(num_samples, len(sampler))

    # test with iteration
    count_num_samples = sum(1 for _ in sampler)
    assert np.allclose(num_samples, count_num_samples)

    # test with dataloader, batch_size = 1
    batch_size = 1
    count_num_samples_in_data_loader = len(_get_data_loader(
        dataset, batch_size=batch_size, sampler=sampler))
    assert np.allclose(num_samples, count_num_samples_in_data_loader)

    # test with dataloader, batch_size = 6
    batch_size = 6
    count_num_samples_in_data_loader = len(_get_data_loader(
        dataset, batch_size=batch_size, sampler=sampler))
    assert np.allclose(num_samples // batch_size + (num_samples % batch_size > 0),
                     count_num_samples_in_data_loader)


def test_duplicating_data_with_drop_last():
    # TODO: Ascend not support concat empty tensor
    if ms.get_context('device_target') == 'Ascend':
        warnings.warn("test_dataloder.py: test_duplicating_data_with_drop_last not run on Ascend.")
        return
    from mindtorch.torch.utils.data.distributed import DistributedSampler

    num_processes = 4
    num_batches = 9
    data_set = np.asarray(list(range(num_batches))).astype(np.int64)
    scanned_data =np.asarray([]).astype(np.int64)
    for i in range(num_processes):
        s = DistributedSampler(data_set, num_processes, i)
        d_loader = _get_data_loader(data_set, batch_size=int(num_batches / num_processes), drop_last=True, sampler=s)
        for data in d_loader:
            scanned_data = np.concatenate((scanned_data, data), 0)
    unique_data = np.unique(scanned_data)
    assert np.allclose(scanned_data.shape, unique_data.shape)

def test_sampler_reproducibility():
    from mindtorch.torch.utils.data import RandomSampler, WeightedRandomSampler, SubsetRandomSampler
    weights = [0.1, 0.9, 0.4, 0.7, 3.0, 0.6]
    np.random.seed(42)
    ms.set_seed(42)
    first = list(RandomSampler(dataset, num_samples=5, replacement=True))
    np.random.seed(42)
    ms.set_seed(42)
    second = list(RandomSampler(dataset, num_samples=5, replacement=True))
    assert np.allclose(first, second)

    np.random.seed(42)
    ms.set_seed(42)
    first =list(RandomSampler(dataset, replacement=False))
    np.random.seed(42)
    ms.set_seed(42)
    second =list(RandomSampler(dataset, replacement=False))
    assert np.allclose(first, second)

    np.random.seed(42)
    ms.set_seed(42)
    first = list(WeightedRandomSampler(weights, num_samples=5, replacement=True))
    np.random.seed(42)
    ms.set_seed(42)
    second = list(WeightedRandomSampler(weights, num_samples=5, replacement=True))
    np.allclose(first, second)

    np.random.seed(42)
    ms.set_seed(42)
    first = list(WeightedRandomSampler(weights, num_samples=5, replacement=False))
    np.random.seed(42)
    ms.set_seed(42)
    second = list(WeightedRandomSampler(weights, num_samples=5, replacement=False))
    np.allclose(first, second)

    np.random.seed(42)
    ms.set_seed(42)
    first = list(SubsetRandomSampler(range(10)))
    np.random.seed(42)
    ms.set_seed(42)
    second = list(SubsetRandomSampler(range(10)))
    assert np.allclose(first, second)

def _test_sampler(**kwargs):
    indices = range(2, 12)  # using a regular iterable
    dl = _get_data_loader(dataset, sampler=indices, batch_size=2, **kwargs)
    assert np.allclose(len(dl), 5)
    for i, (input, _target) in enumerate(dl):
        assert np.allclose(len(input), 2)
        assert np.allclose(input.asnumpy(), data[i * 2 + 2:i * 2 + 4].asnumpy())

# def test_sampler():
#     _test_sampler()
#     _test_sampler(num_workers=4)
#     if not NO_MULTIPROCESSING_SPAWN:
#        _test_batch_sampler(num_workers=4, multiprocessing_context='spawn')

def _test_batch_sampler( **kwargs):
    # [(0, 1), (2, 3, 4), (5, 6), (7, 8, 9), ...]
    batches = []  # using a regular iterable
    for i in range(0, 20, 5):
        batches.append(tuple(range(i, i + 2)))
        batches.append(tuple(range(i + 2, i + 5)))

    dl = _get_data_loader(dataset, batch_sampler=batches, **kwargs)
    assert np.allclose(len(dl), 8)
    for i, (input, _target) in enumerate(dl):
        if i % 2 == 0:
            offset = i * 5 // 2
            assert np.allclose(len(input), 2)
            assert np.allclose(input.asnumpy(), data[offset:offset + 2].asnumpy())
        else:
            offset = i * 5 // 2
            assert np.allclose(len(input), 3)
            assert np.allclose(input.asnumpy(), data[offset:offset + 3].asnumpy())

# def test_batch_sampler():
#     _test_batch_sampler()
#     _test_batch_sampler(num_workers=4)
#     if not NO_MULTIPROCESSING_SPAWN:
#         _test_batch_sampler(num_workers=4, multiprocessing_context='spawn')

def test_error():
    _test_error(_get_data_loader(ErrorDataset(100), batch_size=2, shuffle=True))

def test_error_workers():
    _test_error(_get_data_loader(ErrorDataset(41), batch_size=2, shuffle=True, num_workers=4))


def test_len_1():
    def check_len(dl, expected):
        assert np.allclose(len(dl), expected)
        n = 0
        for _ in dl:
            n += 1
        assert np.allclose(n, expected)
    check_len(dataset, 100)
    check_len(_get_data_loader(dataset, batch_size=2), 50)
    check_len(_get_data_loader(dataset, batch_size=3), 34)

class IterableDataset_custom(torch.utils.data.IterableDataset):
    def __len__(self):
        return 10

    def __iter__(self):
        return iter(range(10))

def test_iterabledataset_len():

    iterable_loader = DataLoader(IterableDataset_custom(), batch_size=1)
    assert np.allclose(len(iterable_loader), 10)
    iterable_loader = DataLoader(IterableDataset_custom(), batch_size=1, drop_last=True)
    assert np.allclose(len(iterable_loader), 10)

    iterable_loader = DataLoader(IterableDataset_custom(), batch_size=2)
    assert np.allclose(len(iterable_loader), 5)
    iterable_loader = DataLoader(IterableDataset_custom(), batch_size=2, drop_last=True)
    assert np.allclose(len(iterable_loader), 5)

    iterable_loader = DataLoader(IterableDataset_custom(), batch_size=3)
    assert np.allclose(len(iterable_loader), 4)
    iterable_loader = DataLoader(IterableDataset_custom(), batch_size=3, drop_last=True)
    assert np.allclose(len(iterable_loader), 3)


def test_default_convert_mapping_keep_type():
    data = CustomDict({"a": 1, "b": 2})
    converted = _utils.collate.default_convert(data)

    assert converted == data

def test_default_convert_sequence_keep_type():
    data = CustomList([1, 2, 3])
    converted = _utils.collate.default_convert(data)

    assert np.allclose(converted, data)

def test_default_convert_sequence_dont_keep_type():
    data = range(2)
    converted = _utils.collate.default_convert(data)

    assert np.allclose(converted, [0, 1])

def test_default_collate_dtype():
    arr = [1, 2, -1]
    collated = _utils.collate.default_collate(arr)
    assert np.allclose(collated, torch.tensor(arr).asnumpy())
    assert collated.dtype == np.int64

    arr = [1.1, 2.3, -0.9]
    collated = _utils.collate.default_collate(arr)
    assert np.allclose(collated, torch.tensor(arr).asnumpy())
    assert collated.dtype == np.float64

    arr = [True, False]
    collated = _utils.collate.default_collate(arr)
    assert np.allclose(collated, torch.tensor(arr).asnumpy())
    assert collated.dtype == np.bool_

    # Should be a no-op
    arr = ['a', 'b', 'c']
    assert arr == _utils.collate.default_collate(arr)

def test_default_collate_mapping_keep_type():
    batch = [CustomDict({"a": 1, "b": 2}), CustomDict({"a": 3, "b": 4})]
    collated = _utils.collate.default_collate(batch)

    expected = CustomDict({"a": torch.tensor([1, 3]), "b": torch.tensor([2, 4])})
    for i in expected.keys():
        assert np.allclose(collated[i], expected[i].asnumpy())

def test_default_collate_sequence_keep_type():
    batch = [CustomList([1, 2, 3]), CustomList([4, 5, 6])]
    collated = _utils.collate.default_collate(batch)

    expected = CustomList([
        torch.tensor([1, 4]),
        torch.tensor([2, 5]),
        torch.tensor([3, 6]),
    ])
    for i in range(len(expected)):
        assert np.allclose(collated[i], expected[i].asnumpy())

def test_enable_fork_utils_default():
    if not IS_WINDOWS:
        assert mp.get_start_method() == 'fork'
