from mindtorch.torch.distributed.distributed_c10d import broadcast
from mindtorch.utils import unsupported_attr

def _sync_module_states(
    module,
    process_group,
    broadcast_bucket_size,
    src,
    params_and_buffers_to_ignore,
):
    module_states = []
    for name, param in module.named_parameters():
        if name not in params_and_buffers_to_ignore:
            module_states.append(param)

    for name, buffer in module.named_buffers():
        if name not in params_and_buffers_to_ignore:
            module_states.append(buffer)

    _sync_params_and_buffers(
        process_group,
        module_states,
        broadcast_bucket_size,
        src
    )

def _sync_params_and_buffers(
    process_group,
    module_states,
    broadcast_bucket_size,
    src,
):
    unsupported_attr(broadcast_bucket_size)
    if len(module_states) > 0:
        for state in module_states:
            _state = state.detach()
            _state_dtype = state.dtype
            broadcast(_state.float(), src, process_group)
            state.assign_value(_state.astype(_state_dtype))
