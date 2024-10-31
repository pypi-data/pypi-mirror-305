import mindspore as ms
from mindspore.ops import ReduceOp as ReduceOp_MS
from mindspore.ops._primitive_cache import _get_cache_prim
from mindspore.communication.management import GlobalComm
from mindspore.communication._comm_helper import _get_group_ranks

from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor, Tensor
from mindtorch.utils import unsupported_attr

__all__ = ['ReduceOp', 'ProcessGroup', 'ProcessGroupNCCL', 'BroadcastOptions', 'AllreduceOptions',
           'AllreduceCoalescedOptions', 'ReduceOptions', 'AllGatherOptions', 'GatherOptions',
           'GatherOptions', 'ScatterOptions', 'ReduceScatterOptions', 'BarrierOptions', 'AllToAllOptions',
           'Work']

class ReduceOp(str):
    SUM = None
    PRODUCT = None
    MIN = None
    MAX = None

    # TODO: mindspore not support the ReduceOp below.
    # BAND = ...
    # BOR = ...
    # BXOR = ...
    # PREMUL_SUM = ...
    # UNUSED = ...

    int_2_op = {0: SUM,
                2: PRODUCT,
                3: MIN,
                4: MAX}

    def __new__(cls, reduce_op):
        if not isinstance(reduce_op, (int, str, ReduceOp)):
            raise TypeError(f'distributed.ReduceOp only support int or str, but got {type(reduce_op)}.')
        if isinstance(reduce_op, int):
            if reduce_op not in ReduceOp.int_2_op:
                raise NotImplementedError(f'reduce op: {reduce_op} not support yet.')
            value = ReduceOp.int_2_op[reduce_op]
        else:
            value = str(reduce_op)
        object = str.__new__(cls, value)
        return object

    def __eq__(self, other):
        return str(self) == str(other)

ReduceOp.SUM = ReduceOp(ReduceOp_MS.SUM)
ReduceOp.PRODUCT = ReduceOp(ReduceOp_MS.PROD)
ReduceOp.MIN = ReduceOp(ReduceOp_MS.MIN)
ReduceOp.MAX = ReduceOp(ReduceOp_MS.MAX)

def _get_str_from_reduceop(reduce_op):
    return str(reduce_op)

_pg_map={}  # pg_map has no 'Store', because it not support yet.  Dict[ProcessGroup, Tuple[str, Optional[Store]]]
_pg_names={} # Dict[ProcessGroup, str]
_group_count = 0

def _get_pg_name(group=None):
    if group is None:
        return GlobalComm.WORLD_COMM_GROUP
    if isinstance(group, ProcessGroup):
        if group in _pg_map:
            return _pg_names[group]
        raise ValueError(f"Group {group} is not existed.")
    raise TypeError('The dtype of `group` must be `ProcessGroup`, but got {}'.format(type(group)))

@ms.jit_class
class Work:
    def __init__(self, handle=None):
        # Do nothings here for now. After mindspore stream support, use stream to create work.
        self._handle = handle

    def start(self):
        # Do nothings here for now. After mindspore stream support, use stream to create work.
        ...
    def wait(self):
        # Do nothings here for now. After mindspore stream support, use stream to create work.
        if self._handle:
            self._handle.wait()

    def result(self):
        return self._result

def _create_work():
    return Work()


class BroadcastOptions:
    rootRank=None
    rootTensor=None
    timeout=None

class AllreduceOptions:
    reduceOp=None
    timeout=None

class AllreduceCoalescedOptions(AllreduceOptions):
    ...

class ReduceOptions:
    reduceOp=None
    rootRank=None
    rootTensor=None
    timeout=None

class AllGatherOptions:
    timeout=None

class GatherOptions:
    rootRank=None
    timeout=None

class ScatterOptions:
    rootRank=None
    timeout=None

class ReduceScatterOptions:
    reduceOp=None
    timeout=None

class BarrierOptions:
    device_ids=None
    timeout=None

class AllToAllOptions:
    timeout=None


def _check_nest_list(obj):
    if not isinstance(obj, (list, tuple)):
        return False
    for elem in obj:
        if isinstance(elem, (list, tuple)):
            return True
    return False

# inherit from str to support graph mode
class ProcessGroup(str):
    def __new__(cls, *args, **kwargs):
        args_index = 0
        def get_args(name):
            nonlocal args_index
            if name in kwargs:
                value = kwargs[name]
            elif len(args) > args_index:
                value = args[args_index]
                args_index += 1
            else:
                value = None
            return value

        rank = get_args('rank')
        world_size = get_args('world_size')

        if kwargs.get('name', None) is not None:
            value = kwargs['name']
        else:
            value = f'{cls.__name__}_{rank}_{world_size}'
        object = str.__new__(cls, value)
        object.rank = rank
        object.world_size = world_size
        return object

    # TODO: implemented the following methods after the operators supported.
    def broadcast(
        self,
        tensor,
        root=None,
    ):
        if not isinstance(tensor, list):
            raise TypeError(f"ProcessGroup.broadcast: `tensor` must be type of list, but got {type(tensor)}.")
        if len(tensor) != 1:
            raise NotImplementedError("ProcessGroup.broadcast: mutilple `tensor` broadcast not support yet."
                                      f"`tensor` length can only be 1, but got {len(tensor)}.")
        if isinstance(root, BroadcastOptions):
            root = root.rootRank
        _group_name = _get_pg_name(self)
        if root is None:
            root = ms.communication.get_rank(_group_name)
        _bc_op = _get_cache_prim(ms.ops.Broadcast)(root, _group_name)
        tensor = tuple(tensor)
        work = _create_work()
        work.start()
        output = _bc_op(tensor)
        tensor[0].data = output[0]
        output = cast_to_adapter_tensor(output)
        work._result = output
        return work

    def allreduce(
        self,
        tensors,
        op=ReduceOp.SUM,
    ):
        if len(tensors) > 1:
            raise NotImplementedError('ProcessGroup.allreduce not support list of tensors yet.')

        if isinstance(op, AllreduceOptions):
            op = op.reduceOp
            if op is None:
                op = ReduceOp.SUM
        _group_name = _pg_names[self]
        op = _get_str_from_reduceop(op)
        _reduce_op = _get_cache_prim(ms.ops.AllReduce)(op, _group_name)
        tensor = tensors[0]
        result, handle = _reduce_op(tensor)
        tensor.data = result
        return Work(handle)

    def reduce(
        self,
        tensors,
        root,
        op=ReduceOp.SUM,
    ):
        if len(tensors) > 1:
            raise NotImplementedError('ProcessGroup.reduce not support list of tensors yet.')

        if isinstance(root, ReduceOptions):
            op = root.reduceOp
            root = root.rootRank
        _group_name = _get_pg_name(self)
        _reduce_op = _get_cache_prim(ms.ops.Reduce)(root, op, _group_name)
        tensor = tensors[0]
        out, handle = _reduce_op(tensor)
        _comm_inplace_assign(tensor, out)
        return Work(handle)

    def _allgather_base(
        self,
        output,
        input,
        opts=AllGatherOptions()
    ):
        # TODO: timeout not support yet
        unsupported_attr(opts)
        _group_name = _get_pg_name(self)
        _ag_op = _get_cache_prim(ms.ops.AllGather)(_group_name)
        result, handle = _ag_op(input)
        _comm_inplace_assign(output, result)
        return Work(handle)

    def allgather(
        self,
        output_tensors,
        input_tensor,
        opts=None,
    ):
        unsupported_attr(opts)
        _group_name = _get_pg_name(self)
        _group_size = ms.communication.get_group_size(_group_name)
        _ag_op = _get_cache_prim(ms.ops.AllGather)(_group_name)
        _split_op = _get_cache_prim(ms.ops.Split)(0, _group_size)
        input_tensor = input_tensor[0]
        result, handle = _ag_op(input_tensor)
        result = _split_op(result)
        _comm_inplace_assign(output_tensors, result)
        return Work(handle)

    def gather(
        self,
        output_tensors,
        input_tensor,
        root,
    ):
        if isinstance(input_tensor, list) or _check_nest_list(output_tensors):
            raise NotImplementedError("ProcessGroup.gather not support list input_tensor yet.")
        if isinstance(root, GatherOptions):
            root = root.rootRank
        _group_name = _get_pg_name(self)
        _op = _get_cache_prim(ms.ops.CollectiveGather)(root, _group_name)
        work = _create_work()
        work.start()
        out = _op(input_tensor)

        my_rank = ms.communication.get_rank(_group_name)
        if root == my_rank:
            _split_count = len(output_tensors)
            _spilit_size = out.shape[0] // _split_count
            out = ms.ops.split(out, _spilit_size)
            for i, output in enumerate(output_tensors):
                output.data = out[i]
        return work

    def scatter(
        self,
        output_tensor,
        input_tensors,
        root,
    ):
        if isinstance(output_tensor, list) or _check_nest_list(input_tensors):
            raise NotImplementedError("ProcessGroup.scatter not support list input_tensors yet.")
        if isinstance(root, ScatterOptions):
            root = root.rootRank
        _group_name = _get_pg_name(self)
        _op = _get_cache_prim(ms.ops.CollectiveScatter)(root, _group_name)
        work = _create_work()
        work.start()

        my_rank = ms.communication.get_rank(_group_name)
        if root == my_rank:
            input_list = cast_to_ms_tensor(input_tensors)
            input_ms = ms.ops.stack(input_list)
            out = _op(input_ms)[0]
        else:
            group_size = len(_get_group_ranks(_group_name))
            input_ms = ms.ops.zeros((group_size,) + output_tensor.shape, dtype=output_tensor.dtype)
            out = _op(input_ms)[0]
        output_tensor.data = out
        return work

    def reduce_scatter(
        self,
        output_tensors,
        input_tensor,
        opts=None,
    ):
        if isinstance(output_tensors, (list, tuple)) and len(output_tensors) > 1:
            raise NotImplementedError('ProcessGroup.reduce_scatter not support list of output_tensors yet.')
        if isinstance(opts, ReduceOptions):
            op = opts.reduceOp
        elif opts is not None:
            if opts not in (ReduceOp.SUM, ReduceOp.MAX):
                raise ValueError("ProcessGroup.reduce_scatter: reduce op only support ReduceOp.SUM, ReduceOp.MAX now.")
            op = opts
        else:
            op = ReduceOp.SUM
        op = _get_str_from_reduceop(op)
        _group_name = _get_pg_name(self)
        _reduce_scatter_op = _get_cache_prim(ms.ops.ReduceScatter)(op, _group_name)
        input_tensor = cast_to_ms_tensor(input_tensor)
        for i, tensor in enumerate(input_tensor):
            if tensor.ndim == 0:
                _zero_ndim = 1
                input_tensor[i] = tensor.expand_dims(0)
        input_ms = ms.ops.concat(input_tensor)
        out, handle = _reduce_scatter_op(input_ms)
        if not _zero_ndim:
            output_tensors.data = out
        else:
            output_tensors.data = out[0]
        return Work(handle)

    def _reduce_scatter_base(
        self,
        output,
        input
    ):
        _group_name = _get_pg_name(self)
        op = _get_str_from_reduceop(ReduceOp.SUM)
        _reduce_scatter_op = _get_cache_prim(ms.ops.ReduceScatter)(op, _group_name)
        input_ms = cast_to_ms_tensor(input)
        if input_ms.ndim <= 1:
            input_ms.expand_dims(-1)
        out, handle = _reduce_scatter_op(input_ms)
        _comm_inplace_assign(output, out)
        return Work(handle)


    def alltoall_base(
        self,
        output_tensor,
        input_tensor,
        output_split_sizes,
        input_split_sizes,
        opts=None,
    ):
        raise NotImplementedError

    def alltoall(
        self,
        output_tensor,
        input_tensor,
        opts=None,
    ):
        raise NotImplementedError

    def send(
        self,
        tensors,
        dstRank,
        tag,
    ):
        if len(tensors) > 1:
            raise NotImplementedError('ProcessGroup.send not support list of tensors yet.')
        _group_name = _get_pg_name(self)
        _send_op = _get_cache_prim(ms.ops.Send)(tag, dstRank, _group_name)
        _, handle = _send_op(tensors[0])
        return Work(handle)

    def recv(
        self,
        tensors,
        srcRank,
        tag,
    ):
        _group_name = _get_pg_name(self)
        if len(tensors) > 1:
            raise NotImplementedError('ProcessGroup.recv not support list of tensors yet.')
        tensor = tensors[0]
        _recv_op = _get_cache_prim(ms.ops.Receive)(tag,
                                                   srcRank,
                                                   list(tensor.shape),
                                                   tensor.dtype,
                                                   _group_name)
        out, handle = _recv_op(tensor)
        _comm_inplace_assign(tensor, out)
        return Work(handle)

    def barrier(self,
                opts=BarrierOptions(),
    ):
        if opts.device_ids is not None or opts.timeout is not None:
            raise NotImplementedError("ProcessGroup.barrier not support device_id and timeout yet.")
        work = _create_work()
        work.start()
        _group_name = _get_pg_name(self)
        _barrier_op = _get_cache_prim(ms.ops.Barrier)(_group_name)
        _barrier_op()
        return work

class ProcessGroupNCCL(ProcessGroup):
    class Options:
        # TODO：MindSpore to support ProcessGroup options in the future.
        ...

    def __new__(
        cls,
        store,
        rank,
        size,
        timeout=None,
    ):
        obj = ProcessGroup.__new__(cls, rank, size)
        obj.store = store
        obj.timeout = timeout
        return obj

    @staticmethod
    def _group_start():
        ...
    @staticmethod
    def _group_end():
        ...

def _comm_inplace_assign(output, result):
    if isinstance(output, Tensor):
        output.assign_value(result)
    else:
        for out, res in zip(output, result):
            out.assign_value(res)

def _comm_process_handle(handle, async_op):
    if async_op:
        return Work(handle)
    return None
