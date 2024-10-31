from mindspore.nn.wrap.grad_reducer import DistributedGradReducer
from mindspore.communication.management import GlobalComm
from mindspore import ops
import mindspore as ms

from mindtorch.torch import distributed as dist
from mindtorch.torch.distributed.distributed_c10d import _get_pg_name, all_reduce, _get_default_group
from mindtorch.torch.distributed.utils import _sync_module_states
from mindtorch.torch.nn.modules.module import Module
from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning

class DistributedDataParallel(Module):
    def __init__(
            self,
            module,
            device_ids=None,
            output_device=None,
            dim=0,
            broadcast_buffers=True,
            process_group=None,
            bucket_cap_mb=25,
            find_unused_parameters=False,
            check_reduction=False,
            gradient_as_bucket_view=False,
            static_graph=False,
    ):
        super(DistributedDataParallel, self).__init__()
        ms.set_auto_parallel_context(comm_fusion={"allreduce": {"mode": "size", "config": bucket_cap_mb}})
        if ms.get_context('mode') == ms.PYNATIVE_MODE:
            warning("`bucket_cap_mb` takes effect only in graph mode.")
        device_num = dist.get_world_size(process_group)
        pg_name = GlobalComm.WORLD_COMM_GROUP if process_group is None else _get_pg_name(process_group)
        self.grad_reducer = DistributedGradReducer(module.trainable_params(), degree=device_num, group=pg_name)
        self.broadcast = ops.Broadcast(0, pg_name)

        self.module = module
        if process_group is None:
            self.process_group = _get_default_group()
        else:
            self.process_group = process_group

        self.modules_buffers = list()
        self.broadcast_buffers = broadcast_buffers
        if broadcast_buffers:
            for buffer in module.buffers():
                self.modules_buffers.append(buffer)

        self.broadcast_bucket_size = int(250 * 1024 * 1024)
        # TODO: not support 'parameters_to_ignore' now, because it is used by 'delay_all_reduce_named_params',
        # but 'delay_all_reduce_named_params' relies on Parameter's hook, which is not support yet.
        self.parameters_to_ignore = set()
        _sync_module_states(
            module=self.module,
            process_group=self.process_group,
            broadcast_bucket_size=self.broadcast_bucket_size,
            src=0,
            params_and_buffers_to_ignore=self.parameters_to_ignore,
        )

        unsupported_attr(device_ids)
        unsupported_attr(output_device)
        unsupported_attr(dim)
        unsupported_attr(find_unused_parameters)
        unsupported_attr(check_reduction)
        unsupported_attr(gradient_as_bucket_view)
        unsupported_attr(static_graph)

    def will_sync_module_buffers(self):
        return self.broadcast_buffers and len(self.modules_buffers) > 0

    def _sync_buffers(self):
        for buffer in self.modules_buffers:
            _buffer = buffer.detach()
            _buffer_dtype = _buffer.dtype
            remote_buffer = self.broadcast((_buffer.float(),))[0]
            buffer.assign_value(remote_buffer.astype(_buffer_dtype))

    def forward(self, *inputs, **kwargs):
        if self.will_sync_module_buffers():
            self._sync_buffers()
        return self.module(*inputs, **kwargs)

    def all_reduce(self, grads=None):
        if grads is None:
            for p in self.module.parameters():
                if p.grad is not None:
                    all_reduce(p.grad, group=self.process_group)
        else:
            grads = self.grad_reducer(grads)
        return grads

    def gather(self, outputs, output_device):
        # TODO: implemented the method after the operators supported.
        unsupported_attr(outputs)
        unsupported_attr(output_device)

    def scatter(self, inputs, kwargs, device_ids):
        # TODO: implemented the method after the operators supported.
        unsupported_attr(inputs)
        unsupported_attr(kwargs)
        unsupported_attr(device_ids)

def _find_tensors(obj):
    unsupported_attr(obj)
    raise NotImplementedError("`_find_tensors` is not implemented now.")
