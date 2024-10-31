from typing import cast, List, Optional, Sequence, Tuple
import sys

import numpy as np
import mindtorch.torch as torch
import mindtorch.torch.nn.functional as F
from mindtorch.torch.distributed._tensor import DeviceMesh
import mindtorch.torch.distributed as dist
# from mindtorch.torch.distributed.tensor.parallel import PairwiseParallel, parallelize_module
import mindtorch.torch.nn as nn

TP_DEGREE = 2

class SimpleModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.net1 = torch.nn.Linear(5, 8)
        self.relu = torch.nn.ReLU()
        self.net2 = torch.nn.Linear(8, 4)
        self.net3 = torch.nn.Linear(4, 12)

    def forward(self, x):
        x = F.relu(self.net1(x))
        x = F.relu(self.net2(x))
        x = F.relu(self.net3(x))
        return x

class Placement:
    def is_shard(self, dim: Optional[int] = None) -> bool:
        if dim is not None and isinstance(self, Shard):
            return self.dim == dim
        else:
            return isinstance(self, Shard)

    def is_replicate(self) -> bool:
        return isinstance(self, Replicate)

    # def is_partial(self) -> bool:
    #     return isinstance(self, _Partial)

class Shard(Placement):
    # shard placement, shard on a dim
    def __init__(self, dim):
        self.dim = dim

    def _split_tensor(
        self,
        tensor: torch.Tensor,
        num_chunks: int,
        *,
        with_padding: bool = True,
        contiguous: bool = True,
    ) -> Tuple[List[torch.Tensor], int]:
        # NOTE: For with_padding option, we pad the tensor on each rank before calling
        # the collectives (i.e. scatter/all_gather, etc.). This is because for gloo
        # backend, it does not support uneven collectives, nccl supports some, but
        # it might be slow compared to even size collective, we need to pad tensor
        # before really calling the collective, and unpad/narrow it afterwards
        # TODO: consider if we should remove this logic once ProcessGroupGloo
        # support uneven list, and collective perfomance on par
        assert (
            self.dim <= tensor.ndim
        ), f"Sharding dim {self.dim} greater than tensor ndim {tensor.ndim}"
        assert (
            tensor.size(self.dim) >= num_chunks
        ), f"Tensors to be sharded on dim {self.dim} must be at least as large as "
        f"the number of devices in that dimension {num_chunks}"
        # split tensor over dimension `dim` into n slices with padding if necessary
        tensor_list = list(tensor.tensor_split(num_chunks, self.dim))
        idx_start_to_pad = tensor.size(self.dim) % num_chunks
        if with_padding or contiguous:
            shard_list = []
            for i, shard in enumerate(tensor_list):
                if with_padding and idx_start_to_pad != 0 and i >= idx_start_to_pad:
                    shard = self._pad_tensor(shard)
                # input tensors are expected to be congtiguous by the collective backend
                shard = shard.contiguous() if contiguous else shard
                shard_list.append(shard)
            return shard_list, idx_start_to_pad
        else:
            return tensor_list, idx_start_to_pad

    def _pad_tensor(self, tensor: torch.Tensor) -> torch.Tensor:
        # pad tensor by 1 on the shard dim
        pad = [0, 0] * (tensor.ndim - self.dim)
        pad[-1] = 1
        return torch.nn.functional.pad(tensor, pad)

    def _unpad_tensor(self, tensor: torch.Tensor) -> torch.Tensor:
        # unpad tensor by 1 on the shard dim
        return tensor.narrow(self.dim, start=0, length=tensor.size(self.dim) - 1)

    def _local_shard_size_on_dim(
        self,
        size_on_dim: int,
        num_chunks: int,
        rank: int,
        return_offset: bool = False,
    ) -> Tuple[int, int]:
        """
        returns the local shard size and offset on a given tensor dim
        """
        assert (
            size_on_dim >= num_chunks
        ), f"Size to be sharded on dim {self.dim} must be at least as large as the number of devices in that dimension {num_chunks}"
        split_size, pad_idx = divmod(size_on_dim, num_chunks)
        local_shard_size = (
            split_size + 1 if pad_idx != 0 and rank < pad_idx else split_size
        )
        local_offset_on_dim = -1
        if return_offset:
            local_offset_on_dim = (
                rank * split_size + pad_idx if rank >= pad_idx else rank
            )
        return (local_shard_size, local_offset_on_dim)

    def _shard_tensor(
        self, tensor: torch.Tensor, mesh: DeviceMesh, mesh_dim: int
    ) -> torch.Tensor:
        """
        shard and scatter a tensor on a mesh dimension (use coordinate
        0 on the mesh dimension as source of truth)
        """
        my_coordinate = mesh.get_coordinate()
        num_chunks = mesh.size(dim=mesh_dim)
        if my_coordinate is None:
            # if rank is not part of mesh, we simply return an empty tensor
            return tensor.new_empty(0, requires_grad=tensor.requires_grad)

        scatter_list, pad_idx = self._split_tensor(
            tensor, num_chunks, with_padding=True, contiguous=True
        )
        # TODO: MindSpore not support scatter yet
        # output = torch.empty_like(scatter_list[my_coordinate[mesh_dim]])
        # mesh.scatter(output, scatter_list, mesh_dim=mesh_dim)
        _global_rank = dist.get_rank()
        output = scatter_list[_global_rank]

        if pad_idx != 0 and my_coordinate[mesh_dim] >= pad_idx:
            output = self._unpad_tensor(output)
        return output

    def _reduce_shard_tensor(
        self,
        tensor: torch.Tensor,
        mesh: DeviceMesh,
        reduce_op,
        mesh_dim: int,
    ) -> torch.Tensor:
        """
        reduce and scatter a tensor on a mesh dimension
        """
        my_coordinate = mesh.get_coordinate()
        num_chunks = mesh.size(dim=mesh_dim)
        # TODO: what should happen if rank is not in the mesh?
        # see issue https://github.com/pytorch/tau/pull/492
        assert (
            my_coordinate is not None
        ), "Rank if not part of mesh"  # TODO: figure out behavior here
        scattered_list, pad_idx = self._split_tensor(
            tensor, num_chunks, with_padding=True, contiguous=True
        )
        # wrap with comm tensor
        scattered_list = [t for t in scattered_list]
        output = torch.empty_like(scattered_list[my_coordinate[mesh_dim]])
        mesh.reduce_scatter(
            output,
            scattered_list,  # pyre-ignore[6]
            op=reduce_op,
            mesh_dim=mesh_dim,
        )
        if pad_idx != 0 and my_coordinate[mesh_dim] >= pad_idx:
            output = self._unpad_tensor(output)
        return output

    def _to_replicate_tensor(
        self,
        local_tensor: torch.Tensor,
        size: torch.Size,
        mesh: DeviceMesh,
        mesh_dim: int,
    ) -> torch.Tensor:
        """
        This function all_gather all shards and return a tensor that
        is replicated on the previously sharded mesh dimension
        """
        my_coordinate = mesh.get_coordinate()
        num_chunks = mesh.size(dim=mesh_dim)
        # TODO: what should happen if rank is not in the mesh?
        # see issue https://github.com/pytorch/tau/pull/492
        assert (
            my_coordinate is not None
        ), "Rank if not part of mesh"  # TODO: figure out behavior here
        # check if it needs to pad input tensor before all_gather
        pad_idx = size[self.dim] % num_chunks
        if pad_idx != 0 and my_coordinate[mesh_dim] >= pad_idx:
            local_tensor = self._pad_tensor(local_tensor).contiguous()

        gathered_list = []
        # N.B. CommTensor does not change eager mode behavior. During tracing, it
        # makes sure communication result is properly waited before subsequent
        # read operations.
        for _ in range(num_chunks):
            gathered_list.append(
                torch.empty_like(
                    local_tensor,
                    memory_format=torch.contiguous_format,
                )
            )

        mesh.all_gather(gathered_list, local_tensor.contiguous(), mesh_dim=mesh_dim)  # type: ignore[arg-type]
        # unpad the tensor if the input tensor was padded
        if pad_idx != 0:
            gathered_list = [
                self._unpad_tensor(gathered_tensor)  # type: ignore[misc]
                if i >= pad_idx
                else gathered_tensor
                for i, gathered_tensor in enumerate(gathered_list)
            ]
        return torch.cat(gathered_list, dim=self.dim)  # type: ignore[arg-type]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Shard):
            return False
        return self.dim == other.dim

    def __hash__(self) -> int:
        return hash(self.dim)

    def __repr__(self) -> str:
        return f"Shard(dim={self.dim})"

class Replicate(Placement):
    # replicate placement
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Replicate):
            return False
        return True

    def __hash__(self) -> int:
        # every replicate placement is the same
        return -1

    def __repr__(self) -> str:
        return "Replicate()"

    def _replicate_tensor(
        self,
        tensor: torch.Tensor,
        mesh: DeviceMesh,
        mesh_dim: int
    ) -> torch.Tensor:
        """
        Replicate (broadcast) a torch.Tensor on a mesh dimension (use
        the first coordinate on the mesh dimension as source of truth)
        """
        my_coordinate = mesh.get_coordinate()
        if my_coordinate is None:
            # if rank is not part of mesh, we simply return an empty tensor
            return tensor.new_empty(0, requires_grad=tensor.requires_grad)

        tensor = tensor.contiguous()
        mesh.broadcast(tensor, mesh_dim=mesh_dim)
        return tensor

def distribute_tensor(
    tensor: torch.Tensor,
    device_mesh=None,
    placements=None,
):
    # if not tensor.is_meta:
    #     tensor = tensor.to(device_mesh.device_type)
    if placements is None:
        placements = [Replicate() for _ in range(device_mesh.ndim)]

    if len(placements) != device_mesh.ndim:
        raise ValueError(
            f"`placements` must have the same length as `device_mesh.ndim`! "
            f"Found placements length: {len(placements)}, and device_mesh.ndim: {device_mesh.ndim}."
        )

    local_tensor = tensor

    # distribute the tensor according to the placements.
    for idx, placement in enumerate(placements):
        if placement.is_shard():
            output = placement._shard_tensor(local_tensor, device_mesh, idx)  # split and scatter from rank0
            # scatter call could not return a tensor with correct requires_grad
            # field, as ProcessGroupNCCL refuse to take a tensor with requires_grad
            # to do inplace update! So we manually set it here
            output.requires_grad_(tensor.requires_grad)
            local_tensor = output
        elif placement.is_replicate():
            local_tensor = placement._replicate_tensor(local_tensor, device_mesh, idx) # broadcast from zero rank.
        else:
            raise RuntimeError(
                f"Trying to distribute tensor with unsupported placements {placement} on device mesh dimension {idx}!"
            )

    assert local_tensor is not None, "distributing a tensor should not be None"
    # return DTensor(
    #     local_tensor,
    #     device_mesh,
    #     placements,
    #     shape=tensor.size(),
    #     dtype=tensor.dtype,
    #     requires_grad=tensor.requires_grad,
    #     stride=tensor.stride(),
    # )
    return local_tensor

# distribute mlp
def distribute_module(
    module: nn.Module,
    device_mesh=None,
    partition_fn=None,
    input_fn=None,
    output_fn=None,
):
    # if device_mesh is None:
    #     device_mesh = get_global_device_mesh()

    def replicate_module_params_buffers(m: nn.Module, mesh: DeviceMesh) -> None:
        # This function loop over the immediate module parameters and
        # buffers, replicate all non DTensor params/buffers to DTensor
        # parameters/buffers, if they have not been partitioned in the
        # partition_fn, we can't easily use `module._apply` here
        # because we don't know what happened inside partition_fn as
        # user could do anything, i.e. install hooks, and we want to
        # preserve those.
        full_replicate = [Replicate()] * mesh.ndim
        for key, param in m._parameters.items():
            if param is not None:
                m.register_parameter(
                    key,
                    nn.Parameter(distribute_tensor(param.data, mesh, full_replicate)),
                )
        for key, buffer in m._buffers.items():
            if buffer is not None:
                m._buffers[key] = distribute_tensor(buffer, mesh, full_replicate)

    if partition_fn is None:
        # if partition_fn not specified, we by default replicate
        # all module params/buffers
        for name, submod in module.named_modules():
            replicate_module_params_buffers(submod, device_mesh)
    else:
        # apply partition_fun to submodules
        for name, submod in module.named_modules():
            partition_fn(name, submod, device_mesh)
            # replicate_module_params_buffers(submod, device_mesh)

    # register input_fn as module forward pre hook
    if input_fn is not None:
        module.register_forward_pre_hook(lambda _, inputs: input_fn(inputs[0]))  # type: ignore[misc]
    # register input_fn as module forward hook
    if output_fn is not None:
        module.register_forward_hook(
            lambda mod, inputs, outputs: output_fn(outputs, device_mesh)  # type: ignore[misc]
        )

    return module


def _rowwise_parallelize_linear_fn(
    name: str,
    module: nn.Module,
    device_mesh: DeviceMesh,
):
    for name, param in module.named_parameters():
        dist_spec = (
            [Shard(1)] if name == "weight" else [Replicate()]  # type: ignore[list-item]
        )
        dist_param = torch.nn.Parameter(
            distribute_tensor(param, device_mesh, dist_spec)
        )
        module.register_parameter(name, dist_param)


def _colwise_parallelize_linear_fn(
    name: str,
    module: nn.Module,
    device_mesh: DeviceMesh,
):
    for name, param in module.named_parameters():
        dist_param = torch.nn.Parameter(
            distribute_tensor(param, device_mesh, [Shard(0)])
        )
        module.register_parameter(name, dist_param)

def make_input_replicate_1d(inputs):
    dist.broadcast(inputs, 0)
    

def make_output_tensor():
    ...


def _create_1d_device_mesh(device_mesh: DeviceMesh, tp_mesh_dim: int = 0) -> DeviceMesh:
    assert tp_mesh_dim < device_mesh.ndim and tp_mesh_dim >= -device_mesh.ndim, (
        f"Expect tp_mesh_dim within range [{-device_mesh.ndim},"
        f" {device_mesh.ndim}), but found {tp_mesh_dim}."
    )

    if device_mesh.ndim == 1:
        return device_mesh

    # swap the current dim to the last dim then reshape to flatten out other
    # dims, so we can just extract the list of ranks which contains cur_rank.
    cur_rank = device_mesh.get_rank()
    pg_ranks_by_dim = device_mesh.mesh.swapdims(-1, tp_mesh_dim).reshape(
        -1, device_mesh.mesh.size(tp_mesh_dim)
    )
    dim_mesh_1d = pg_ranks_by_dim[torch.any(pg_ranks_by_dim == cur_rank, 1), :]

    sub_pg = device_mesh.get_dim_groups()[tp_mesh_dim]
    mesh_1d = DeviceMesh(device_mesh.device_type, dim_mesh_1d.squeeze(), _init_process_groups=False)
    mesh_1d._dim_groups = [sub_pg]
    return mesh_1d

def _parallelize_mlp(
    module,
    device_mesh,
    parallel_style,
    tp_mesh_dim=0,
):
    # if not isinstance(parallel_style, PairwiseParallel):
    #     raise NotImplementedError(
    #         "Only support PairwiseParallel for MLP parallelization."
    #     )
    # directly create 1D mesh.
    if device_mesh.ndim > 1:
        device_mesh = _create_1d_device_mesh(device_mesh, tp_mesh_dim)

    linear_submodules = list(
        filter(lambda x: isinstance(x, nn.Linear), module.children())
    )
    mlp_last_even_layer = (len(linear_submodules) // 2) * 2
    for i in range(mlp_last_even_layer):
        m = linear_submodules[i]
        if i % 2 == 0:
            # Col-wise Parallelize the linear layer
            distribute_module(
                m,
                device_mesh,
                _colwise_parallelize_linear_fn,
                # input_fn=parallel_style._prepare_input  # type: ignore[arg-type, misc] # pyre-ignore[6]
                input_fn = make_input_replicate_1d
                if i == 0
                else None,
            )
        else:
            # Row-wise Parallelize the linear layer
            distribute_module(
                m,
                device_mesh,
                _rowwise_parallelize_linear_fn,
                # output_fn=parallel_style._prepare_output  # type: ignore[arg-type, misc] # pyre-ignore[6]
                # output_fn = make_output_tensor
                # if i == (mlp_last_even_layer - 1)
                # else None,
                output_fn = None
            )
    return module

def init_model(model_parallel_size=TP_DEGREE, use_orig_params=False, fsdp_nested=False):
    rank = dist.get_rank()
    torch.cuda.set_device(rank)
    world_size = dist.get_world_size()

    torch.manual_seed(0)
    model = SimpleModel().cuda(rank)

    # 2-D mesh is [dp, tp]
    twod_mesh = DeviceMesh(
        device_type="cuda",
        mesh=torch.arange(0, world_size).view(model_parallel_size, -1),
    )

    # Create Input
    tp_model = _parallelize_mlp(model, twod_mesh, None)
    return tp_model, model

if __name__ == '__main__':
    backend = sys.argv[1]
    dist.init_process_group(backend)
    rank = dist.get_rank()
    model_tp, model = init_model()
    input = torch.rand(4, 5).cuda()
    out1 = model_tp(input)
    out2 = model(input)
    assert np.allclose(out1.numpy(), out2.numpy())
