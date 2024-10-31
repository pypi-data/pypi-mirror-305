# pylint: disable=unused-variable
# pylint: disable=unused-argument
# pylint: disable=eval-used
# pylint: disable=broad-except
import difflib
import os
import io
import struct
import sys
import pickle
import pathlib
import shutil
import zipfile
import tarfile
import tempfile
import inspect
from enum import Enum
from contextlib import closing, contextmanager
from typing import Any, BinaryIO, Union, IO, Optional, Type, Dict, Tuple
from typing_extensions import TypeAlias
import numpy as np
from mindtorch.module_hooker import torch_disable, torch_pop
from mindtorch.torch import _utils
from mindtorch.torch.storage import _UntypedStorage, _TypedStorage
from mindtorch.torch.tensor import tensor, Tensor
from mindtorch.torch.nn.modules.module import Module
from mindtorch.torch.logging import warning
import mindtorch.torch.common.dtype as _dtype
from mindtorch.torch.storage import _get_dtype_from_pickle_storage_type

DEFAULT_PROTOCOL = 2
LONG_SIZE = struct.Struct('=l').size
INT_SIZE = struct.Struct('=i').size
SHORT_SIZE = struct.Struct('=h').size

MAGIC_NUMBER = 0x1950a86a20f9469cfc6c
PROTOCOL_VERSION = 1001

string_classes = (str, bytes)

FILE_LIKE: TypeAlias = Union[str, os.PathLike, BinaryIO, IO[bytes]]

__all__ = [
    'save',
    'load',
]


def typename(o):
    if isinstance(o, Tensor):
        return o.type()

    module = ''
    class_name = ''
    if hasattr(o, '__module__') and o.__module__ != 'builtins' \
            and o.__module__ != '__builtin__' and o.__module__ is not None:
        module = o.__module__ + '.'

    if hasattr(o, '__qualname__'):
        class_name = o.__qualname__
    elif hasattr(o, '__name__'):
        class_name = o.__name__
    else:
        class_name = o.__class__.__name__

    return module + class_name


class SourceChangeWarning(Warning):
    pass

def get_source_lines_and_file(obj, error_msg = None) :
    try:
        filename = inspect.getsourcefile(obj)
        sourcelines, file_lineno = inspect.getsourcelines(obj)
    except OSError as e:
        msg = (
            f"Can't get source for {obj}. TorchScript requires source access in "
            "order to carry out compilation, make sure original .py files are "
            "available."
        )
        if error_msg:
            msg += "\n" + error_msg
        raise OSError(msg) from e

    return sourcelines, file_lineno, filename

@contextmanager
def mkdtemp():
    path = tempfile.mkdtemp()
    try:
        yield path
    finally:
        shutil.rmtree(path)

class _HasStorage:
    def __init__(self, storage):
        self._storage = storage

    def storage(self):
        return self._storage

class PyTorchFileReader:

    def __init__(self, file):
        self.file = zipfile.ZipFile(file)
        self.directory = self.file.namelist()[0].split('/')[0]

    def open_record(self, name):
        filename = f"{self.directory}/{name}"
        if filename in self.file.namelist():
            return self.file.open(filename)
        return None

    def read_record(self, name):
        filename = f"{self.directory}/{name}"
        if filename in self.file.namelist():
            return self.file.read(filename)
        return None

    def has_record(self, name):
        filename = f"{self.directory}/{name}"
        return filename in self.file.namelist()

    def get_all_records(
            self,
    ):
        files = [name.replace(self.directory + '/', '') for name in self.file.namelist()]
        return files

    def get_record_offset(self, name):
        filename = f"{self.directory}/{name}"
        if filename in self.file.namelist():
            return self.file.getinfo(filename).header_offset
        return None

    def get_storage_from_record(self, name, numel, dtype):
        filename = f"{self.directory}/{name}"
        storage = _UntypedStorage
        return _HasStorage(storage.from_buffer(self.read_record(name)))


class PyTorchFileWriter:
    def __init__(self, file):
        self.zipfile = zipfile.ZipFile(file, mode='w')
        self.written_records = set()

    def write_record(self, name, data, offset=0):
        if name in self.written_records:
            raise RuntimeError(f"Record {name} already written")
        self.written_records.add(name)
        self.zipfile.writestr(name, data)

    def write_end_of_file(self):
        pass

    def get_all_written_records(self):
        return self.written_records


class LoadEndianness(Enum):
    NATIVE = 1
    LITTLE = 2
    BIG = 3

_default_load_endian = None

def get_default_load_endianness():
    return _default_load_endian


def set_default_load_endianness(endianness):
    global _default_load_endian
    if not isinstance(endianness, LoadEndianness) and endianness is not None:
        raise TypeError("Invalid argument type in function set_default_load_endianness")
    _default_load_endian = endianness


def _is_zipfile(f):
    read_bytes = []
    start = f.tell()

    byte = f.read(1)
    while byte != b"":
        read_bytes.append(byte)
        if len(read_bytes) == 4:
            break
        byte = f.read(1)
    f.seek(start)

    local_header_magic_number = [b'P', b'K', b'\x03', b'\x04']
    return read_bytes == local_header_magic_number


def _check_seekable(f):
    def raise_err_msg(patterns, e):
        for p in patterns:
            if p in str(e):
                msg = (str(e) + ". You can only torch.load from a file that is seekable."
                       + " Please pre-load the data into a buffer like io.BytesIO and"
                       + " try to load from it instead.")
                raise type(e)(msg)
        raise e

    try:
        f.seek(f.tell())
        return True
    except (io.UnsupportedOperation, AttributeError) as e:
        raise_err_msg(["seek", "tell"], e)
    return False

def check_module_version_greater_or_equal(module, req_version_tuple, error_if_malformed=True):
    version_strs = module.__version__.split('.')
    module_version = tuple(
        type(req_field)(version_strs[idx]) for idx, req_field in enumerate(req_version_tuple)
    )
    try:
        requirement_is_met = module_version >= req_version_tuple

    except RuntimeError as e:
        message = (
                      "'%s' module version string is malformed '%s' and cannot be compared"
                      " with tuple %s"
                  ) % (
                      module.__name__, module.__version__, str(req_version_tuple)
                  )
        if error_if_malformed:
            raise RuntimeError(message) from e
        else:
            warning(message + ', but continuing assuming that requirement is met')
            requirement_is_met = True

    return requirement_is_met

def _is_path(name_or_buffer):
    return isinstance(name_or_buffer, (str, pathlib.Path))

def _is_torchscript_zip(zip_file):
    return 'constants.pkl' in zip_file.get_all_records()

class _opener():
    def __init__(self, file_like):
        self.file_like = file_like

    def __enter__(self):
        return self.file_like

    def __exit__(self, *args):
        pass

class _open_file(_opener):
    def __init__(self, name, mode):
        super(_open_file, self).__init__(open(name, mode))

    def __exit__(self, *args):
        self.file_like.close()

class _open_buffer_reader(_opener):
    def __init__(self, buffer):
        super(_open_buffer_reader, self).__init__(buffer)
        _check_seekable(buffer)

class _open_buffer_writer(_opener):
    def __exit__(self, *args):
        self.file_like.flush()

def _open_file_like(name_or_buffer, mode):
    if _is_path(name_or_buffer):
        return _open_file(name_or_buffer, mode)
    else:
        if 'w' in mode:
            return _open_buffer_writer(name_or_buffer)
        elif 'r' in mode:
            return _open_buffer_reader(name_or_buffer)
        else:
            raise RuntimeError(f"Expected 'r' or 'w' in mode but got {mode}")

class _open_zipfile_reader(_opener):
    def __init__(self, name_or_buffer):
        super().__init__(PyTorchFileReader(name_or_buffer))

class _open_zipfile_writer_file(_opener):
    def __init__(self, name):
        self.file_stream = None
        self.name = str(name)
        try:
            self.name.encode('ascii')
        except UnicodeEncodeError:
            self.file_stream = io.FileIO(self.name, mode='w')
            super().__init__(PyTorchFileWriter(self.file_stream))
        else:
            super().__init__(PyTorchFileWriter(self.name))

    def __exit__(self, *args):
        self.file_like.write_end_of_file()
        if self.file_stream is not None:
            self.file_stream.close()

class _open_zipfile_writer_buffer(_opener):
    def __init__(self, buffer):
        if not callable(getattr(buffer, "write", None)):
            msg = f"Buffer of {str(type(buffer)).strip('<>')} has no callable attribute 'write'"
            if not hasattr(buffer, "write"):
                raise AttributeError(msg)
            raise TypeError(msg)
        self.buffer = buffer
        super().__init__(PyTorchFileWriter(buffer))

    def __exit__(self, *args):
        self.file_like.write_end_of_file()
        self.buffer.flush()

def _open_zipfile_writer(name_or_buffer):
    container: Type[_opener]
    if _is_path(name_or_buffer):
        container = _open_zipfile_writer_file
    else:
        container = _open_zipfile_writer_buffer
    return container(name_or_buffer)


def _is_compressed_file(f):
    compress_modules = ['gzip']
    try:
        return f.__module__ in compress_modules
    except AttributeError:
        return False

def _should_read_directly(f):
    if _is_compressed_file(f):
        return False
    try:
        return f.fileno() >= 0
    except io.UnsupportedOperation:
        return False
    except AttributeError:
        return False

def normalize_storage_type(storage_type):
    import mindtorch.torch as ms_torch # pylint: disable=R0401, C0415
    return getattr(ms_torch, storage_type.__name__)

def _maybe_decode_ascii(bytes_str: Union[bytes, str]):
    if isinstance(bytes_str, bytes):
        return bytes_str.decode('ascii')
    return bytes_str

def _check_dill_version(pickle_module):
    if pickle_module is not None and pickle_module.__name__ == 'dill':
        required_dill_version = (0, 3, 1)
        if not check_module_version_greater_or_equal(pickle_module, required_dill_version, False):
            raise ValueError((
                                 "'mindtorch' supports dill >= %s, but you have dill %s."
                                 " Please upgrade dill or switch to 'pickle'"
                             ) % (
                                 '.'.join([str(num) for num in required_dill_version]),
                                 pickle_module.__version__
                             ))

def _check_save_filelike(f):
    if not isinstance(f, (str, os.PathLike)) and not hasattr(f, 'write'):
        raise AttributeError(
            "expected 'f' to be string, path, or a file-like object with "
            "a 'write' attribute")


def save(obj, f, pickle_module = pickle, pickle_protocol = DEFAULT_PROTOCOL, _use_new_zipfile_serialization = True):

    _check_dill_version(pickle_module)
    _check_save_filelike(f)

    if _use_new_zipfile_serialization:
        with _open_zipfile_writer(f) as opened_zipfile:
            _save(obj, opened_zipfile, pickle_module, pickle_protocol)
            return

    with _open_file_like(f, 'wb') as opened_file:
        _legacy_save(obj, opened_file, pickle_module, pickle_protocol)


def _legacy_save(obj, f, pickle_module, pickle_protocol):
    serialized_container_types = {}
    serialized_storages = {}
    id_map: Dict[int, str] = {}
    storage_dtypes = {}
    def persistent_id(obj):
        if isinstance(obj, type) and issubclass(obj, Module):
            if obj in serialized_container_types:
                return None
            serialized_container_types[obj] = True
            source_file = source = None
            try:
                source_lines, _, source_file = get_source_lines_and_file(obj)
                source = ''.join(source_lines)
            except Exception:
                warning("Couldn't retrieve source code for container of "
                              "type " + obj.__name__ + ". It won't be checked "
                                                       "for correctness upon loading.")
            return ('module', obj, source_file, source)
        from mindtorch.torch import is_storage # pylint: disable=R0401, C0415
        if isinstance(obj, _TypedStorage) or is_storage(obj):
            storage = None
            if isinstance(obj, _TypedStorage):
                import mindtorch.torch as ms_torch # pylint: disable=R0401, C0415
                storage = obj._storage
                storage_dtype = obj.dtype
                storage_type_str = obj.pickle_storage_type()
                storage_type = getattr(ms_torch, storage_type_str)
                dtype = obj.dtype
                storage_numel = obj.size()
            elif isinstance(obj, _UntypedStorage):
                storage = obj
                storage_dtype = _dtype.uint8
                storage_type = normalize_storage_type(type(obj))
                dtype = _dtype.uint8
                storage_numel = storage.nbytes()
            else:
                raise TypeError(f'type not recognized: {type(obj)}')

            storage_dataptr = storage.data_ptr()
            if storage_dataptr != 0:
                if storage_dataptr in storage_dtypes:
                    if storage_dtype != storage_dtypes[storage_dataptr]:
                        raise RuntimeError(
                            'Cannot save multiple tensors or storages that '
                            'view the same data as different types')
                else:
                    storage_dtypes[storage_dataptr] = storage_dtype

            view_metadata: Optional[Tuple[str, int, int]]
            offset = 0
            storage_key = str(id(storage))
            location = 'cpu'
            if storage_key not in serialized_storages:
                serialized_storages[storage_key] = (storage, dtype)
            view_metadata = None

            res = ('storage',
                   storage_type,
                   storage_key,
                   location,
                   storage_numel,
                   view_metadata)
            return res
        return None

    sys_info = dict(
        protocol_version=PROTOCOL_VERSION,
        little_endian=sys.byteorder == 'little',
        type_sizes=dict(
            short=SHORT_SIZE,
            int=INT_SIZE,
            long=LONG_SIZE,
        ),
    )

    pickle_module.dump(MAGIC_NUMBER, f, protocol=pickle_protocol)
    pickle_module.dump(PROTOCOL_VERSION, f, protocol=pickle_protocol)
    pickle_module.dump(sys_info, f, protocol=pickle_protocol)
    pickler = pickle_module.Pickler(f, protocol=pickle_protocol)
    pickler.persistent_id = persistent_id
    pickler.dump(obj)

    serialized_storage_keys = sorted(serialized_storages.keys())
    pickle_module.dump(serialized_storage_keys, f, protocol=pickle_protocol)
    f.flush()
    for key in serialized_storage_keys:
        storage, dtype = serialized_storages[key]
        storage._write_file(f, _should_read_directly(f), True, _utils._element_size(dtype))

def _save(obj, zip_file, pickle_module, pickle_protocol):
    serialized_storages = {}
    id_map: Dict[int, str] = {}
    storage_dtypes = {}

    def persistent_id(obj):
        from mindtorch.torch import is_storage  # pylint: disable=R0401, C0415
        if isinstance(obj, _TypedStorage) or is_storage(obj):

            if isinstance(obj, _TypedStorage):
                import mindtorch.torch as ms_torch  # pylint: disable=R0401, C0415
                storage = obj._storage
                storage_dtype = obj.dtype
                storage_type_str = obj.pickle_storage_type()
                storage_type = getattr(ms_torch, storage_type_str)
                storage_numel = obj.size()

            else:
                storage = obj
                storage_dtype = _dtype.uint8
                storage_type = normalize_storage_type(type(obj))
                storage_numel = storage.nbytes()

            storage_dataptr = storage.data_ptr()
            if storage_dataptr != 0:
                if storage_dataptr in storage_dtypes:
                    if storage_dtype != storage_dtypes[storage_dataptr]:
                        raise RuntimeError(
                            'Cannot save multiple tensors or storages that '
                            'view the same data as different types')
                else:
                    storage_dtypes[storage_dataptr] = storage_dtype

            storage_key = id_map.setdefault(id(storage), str(len(id_map)))
            location = 'cpu'
            serialized_storages[storage_key] = storage

            return ('storage',
                    storage_type,
                    storage_key,
                    location,
                    storage_numel)

        return None

    data_buf = io.BytesIO()
    pickler = pickle_module.Pickler(data_buf, protocol=pickle_protocol)
    pickler.persistent_id = persistent_id
    pickler.dump(obj)
    data_value = data_buf.getvalue()
    zip_file.write_record('archive/data.pkl', data_value, len(data_value))

    for key in sorted(serialized_storages.keys()):
        name = f'archive/data/{key}'
        storage = serialized_storages[key]
        storage_data = storage.inner_data
        zip_file.write_record(name, storage_data)

class StorageType():
    def __init__(self, name):
        self.dtype = _get_dtype_from_pickle_storage_type(name)

    def __str__(self):
        return f'StorageType(dtype={self.dtype})'


def load(f: FILE_LIKE,
         map_location=None,
         pickle_module = pickle,
         **pickle_load_args
         ):

    if pickle_module is None:
        pickle_module = pickle

    if 'encoding' not in pickle_load_args:
        pickle_load_args['encoding'] = 'utf-8'

    with _open_file_like(f, 'rb') as opened_file:
        if _is_zipfile(opened_file):
            overall_storage = None
            with _open_zipfile_reader(opened_file, ) as opened_zipfile:
                if _is_torchscript_zip(opened_zipfile):
                    raise ValueError('do not support torchscript now')
                torch_disable()
                result = _load(opened_zipfile,
                             pickle_module,
                             overall_storage=overall_storage,
                             **pickle_load_args)
                torch_pop()
                return result
        torch_disable()
        result = _legacy_load(opened_file, pickle_module, **pickle_load_args)
        torch_pop()
        return result

def _legacy_load(f, pickle_module, **pickle_load_args):
    deserialized_objects: Dict[int, Any] = {}
    class UnpicklerWrapper(pickle_module.Unpickler):
        def find_class(self, mod_name, name):
            if isinstance(name, str) and 'Storage' in name:
                try:
                    return StorageType(name)
                except KeyError:
                    pass
            return super().find_class(mod_name, name)

    def _check_container_source(container_type, source_file, original_source):
        try:
            current_source = ''.join(get_source_lines_and_file(container_type)[0])
        except Exception:
            warning("Couldn't retrieve source code for container of "
                          "type " + container_type.__name__ + ". It won't be checked "
                                                              "for correctness upon loading.")
            return
        if original_source != current_source:
            if container_type.dump_patches:
                file_name = container_type.__name__ + '.patch'
                diff = difflib.unified_diff(current_source.split('\n'),
                                            original_source.split('\n'),
                                            source_file,
                                            source_file, lineterm="")
                lines = '\n'.join(diff)
                try:
                    with open(file_name, 'a+') as f:
                        file_size = f.seek(0, 2)
                        f.seek(0)
                        if file_size == 0:
                            f.write(lines)
                        elif file_size != len(lines) or f.read() != lines:
                            raise OSError
                    msg = ("Saved a reverse patch to " + file_name + ". "
                            "Run `patch -p0 < " + file_name + "` to revert your changes.")
                except OSError:
                    msg = ("Tried to save a patch, but couldn't create a "
                           "writable file " + file_name + ". Make sure it "
                                                          "doesn't exist and your working directory is "
                                                          "writable.")
            else:
                msg = ("you can retrieve the original source code by "
                       "accessing the object's source attribute or set "
                       "`torch.nn.Module.dump_patches = True` and use the "
                       "patch tool to revert the changes.")
            msg = f"source code of class '{typename(container_type)}' has changed. {msg}"
            warning(msg, SourceChangeWarning)


    def legacy_load(file):
        deserialized_objects: Dict[int, Any] = {}
        def persistent_load(saved_id):
            if isinstance(saved_id, tuple):
                if all(saved_id[1:]):
                    _check_container_source(*saved_id) #TODO
                return saved_id[0]
            return deserialized_objects[int(saved_id)]

        with closing(tarfile.open(fileobj=file, mode='r:', format=tarfile.PAX_FORMAT)) as tar, \
                mkdtemp() as tmpdir:

            tar.extract('storages', path=tmpdir)
            with open(os.path.join(tmpdir, 'storages'), 'rb', 0) as _file:
                num_storages = pickle_module.load(_file, **pickle_load_args)
                for i in range(num_storages):
                    args = pickle_module.load(_file, **pickle_load_args)
                    key, location, storage_type = args
                    dtype = storage_type.dtype
                    element_size = _utils._element_size(dtype)
                    nbytes = np.frombuffer(_file.read(8), np.int64).item() * element_size
                    data = np.fromfile(_file, dtype=np.uint8, count=nbytes, offset=0)
                    obj = _UntypedStorage.from_buffer(data)

                    deserialized_objects[key] = _TypedStorage(
                        wrap_storage=obj,
                        dtype=dtype,
                        _internal=True)

                storage_views = pickle_module.load(_file, **pickle_load_args)
                for target_cdata, root_cdata, offset, numel in storage_views:
                    root = deserialized_objects[root_cdata]
                    element_size = _utils._element_size(root.dtype)
                    offset_bytes = offset * element_size
                    deserialized_objects[target_cdata] = _TypedStorage(
                        wrap_storage=root._untyped()[offset_bytes:offset_bytes + numel * element_size],
                        dtype=root.dtype,
                        _internal=True)

            tar.extract('tensors', path=tmpdir)
            with open(os.path.join(tmpdir, 'tensors'), 'rb', 0) as _file:
                num_tensors = pickle_module.load(_file, **pickle_load_args)
                for _ in range(num_tensors):
                    args = pickle_module.load(_file, **pickle_load_args)
                    key, storage_id, original_tensor_type = args
                    storage = deserialized_objects[storage_id]
                    ndim, = struct.unpack('<i', _file.read(4))
                    _file.read(4)
                    numel = struct.unpack(f'<{ndim}q', _file.read(8 * ndim))
                    stride = struct.unpack(f'<{ndim}q', _file.read(8 * ndim))
                    storage_offset, = struct.unpack('<q', _file.read(8))
                    tmp_tensor = tensor([], dtype=storage.dtype).set_(
                        storage._untyped(), storage_offset, numel, stride)
                    deserialized_objects[key] = tmp_tensor

            pickle_file = tar.extractfile('pickle')
            unpickler = UnpicklerWrapper(pickle_file, **pickle_load_args)
            unpickler.persistent_load = persistent_load
            result = unpickler.load()
            return result

    deserialized_objects = {}

    def persistent_load(saved_id):
        assert isinstance(saved_id, tuple)
        typename = _maybe_decode_ascii(saved_id[0])
        data = saved_id[1:]
        mindtorch_info = None
        if typename == 'module':
            return data[0]
        if typename == 'storage':
            storage_type, root_key, location, numel, view_metadata = data
            location = _maybe_decode_ascii(location)
            dtype = storage_type.dtype

            nbytes = numel * _utils._element_size(dtype)

            if root_key not in deserialized_objects:
                obj = _UntypedStorage(nbytes)
                deserialized_objects[root_key] = _TypedStorage(
                    wrap_storage=obj, dtype=dtype)

            typed_storage = deserialized_objects[root_key]
            if view_metadata is not None:
                view_key, offset, view_size = view_metadata
                offset_bytes = offset * _utils._element_size(dtype)
                view_size_bytes = view_size * _utils._element_size(dtype)
                if view_key not in deserialized_objects:
                    deserialized_objects[view_key] = _TypedStorage(
                        wrap_storage=typed_storage._storage[offset_bytes:offset_bytes + view_size_bytes],
                        dtype=dtype)
                res = deserialized_objects[view_key]
            else:
                res = typed_storage
            return res
        raise RuntimeError(f"Unknown saved id type: {saved_id[0]}")

    _check_seekable(f)
    f_should_read_directly = _should_read_directly(f)

    if f_should_read_directly and f.tell() == 0:
        try:
            return legacy_load(f)
        except tarfile.TarError:
            if _is_zipfile(f):
                raise RuntimeError(
                    f"{f.name} is a zip archive (did you mean to use jit.load()?)") from None
            f.seek(0)

    if not hasattr(f, 'readinto') and (3, 8, 0) <= sys.version_info < (3, 8, 2):
        raise RuntimeError(
            "'load' does not work with file-like objects that do not implement readinto on Python 3.8.0 and 3.8.1. "
            f"Received object of type \"{type(f)}\". Please update to Python 3.8.2 or newer to restore this "
            "functionality.")

    magic_number = pickle_module.load(f, **pickle_load_args)
    if magic_number != MAGIC_NUMBER:
        raise RuntimeError("Invalid magic number; corrupt file?")
    protocol_version = pickle_module.load(f, **pickle_load_args)
    if protocol_version != PROTOCOL_VERSION:
        raise RuntimeError(f"Invalid protocol version: {protocol_version}")

    _sys_info = pickle_module.load(f, **pickle_load_args)
    unpickler = UnpicklerWrapper(f, **pickle_load_args)
    unpickler.persistent_load = persistent_load
    result = unpickler.load()

    deserialized_storage_keys = pickle_module.load(f, **pickle_load_args)

    offset = f.tell() if f_should_read_directly else None
    for key in deserialized_storage_keys:
        assert key in deserialized_objects
        typed_storage = deserialized_objects[key]
        typed_storage._storage._set_from_file(
            f, 0, f_should_read_directly,
            _utils._element_size(typed_storage.dtype))
        if offset is not None:
            offset = f.tell()
    return result


def _load(zip_file, pickle_module, overall_storage=None, pickle_file='data.pkl', **pickle_load_args):
    loaded_storages = {}
    byteordername = 'byteorder'
    byteorderdata = None
    if zip_file.has_record(byteordername):
        byteorderdata = zip_file.read_record(byteordername)
        if byteorderdata not in [b'little', b'big']:
            raise ValueError('Unknown endianness type: ' + byteorderdata.decode())
    elif get_default_load_endianness() == LoadEndianness.LITTLE or \
            get_default_load_endianness() is None:
        byteorderdata = b'little'
    elif get_default_load_endianness() == LoadEndianness.BIG:
        byteorderdata = b'big'
    elif get_default_load_endianness() == LoadEndianness.NATIVE:
        pass
    else:
        raise ValueError('Invalid load endianness type')

    if not zip_file.has_record(byteordername) and \
            get_default_load_endianness() is None and \
            sys.byteorder == 'big':
        warning("The default load endianness for checkpoints without a byteorder mark "
                      "on big endian machines was changed from 'native' to 'little' endian, "
                      "to avoid this behavior please use "
                      "torch.serialization.set_default_load_endianness to set "
                      "the desired default load endianness",
                      UserWarning)

    def load_tensor(dtype, numel, key, location):
        name = f'data/{key}'

        tmp_storage = zip_file.get_storage_from_record(name, numel, _UntypedStorage).storage()._untyped()
        loaded_storages[key] = _TypedStorage(
            wrap_storage=tmp_storage,dtype=dtype)

    def persistent_load(saved_id):
        assert isinstance(saved_id, tuple)
        typename = _maybe_decode_ascii(saved_id[0])
        data = saved_id[1:]

        assert typename == 'storage', \
            f"Unknown typename for persistent_load, expected 'storage' but got '{typename}'"
        storage_type, key, location, numel = data
        if storage_type is _UntypedStorage:
            dtype = _dtype.uint8
        else:
            dtype = storage_type.dtype

        if key not in loaded_storages:
            nbytes = numel * _utils._element_size(dtype)
            load_tensor(dtype, nbytes, key, _maybe_decode_ascii(location))

        return loaded_storages[key]

    load_module_mapping: Dict[str, str] = {
        'torch.tensor': 'torch._tensor'
    }
    class UnpicklerWrapper(pickle_module.Unpickler):  # type: ignore[name-defined]
        def find_class(self, mod_name, name):
            if isinstance(name, str) and 'Storage' in name:
                try:
                    return StorageType(name)
                except KeyError:
                    pass
            mod_name = load_module_mapping.get(mod_name, mod_name)
            return super().find_class(mod_name, name)

    data_file = zip_file.open_record(pickle_file)

    unpickler = UnpicklerWrapper(data_file, **pickle_load_args)
    unpickler.persistent_load = persistent_load
    result = unpickler.load()

    return result
