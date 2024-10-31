from typing import cast
import mindtorch.torch.distributed.distributed_c10d as c10d

import mindtorch.torch as torch

class Placement:
    # base class Placement type

    # convenient utils to check for placement types
    def is_shard(self, dim=None):
        if dim is not None and isinstance(self, Shard):
            return self.dim == dim
        else:
            return isinstance(self, Shard)

    def is_replicate(self):
        return isinstance(self, Replicate)

    def is_partial(self):
        return isinstance(self, _Partial)


class Shard(Placement):
    # shard placement, shard on a dim
    def __init__(self, dim):
        self.dim = dim

    def _split_tensor(
        self,
        tensor,
        num_chunks,
        *,
        with_padding=True,
        contiguous=True,
    ):
        # NOTE: For with_padding option, we pad the tensor on each rank before calling
        # the collectives (i.e. scatter/all_gather, etc.). This is because for gloo
        # backend, it does not support uneven collectives, nccl supports some, but
        # it might be slow compared to even size collective, we need to pad tensor
        # before really calling the collective, and unpad/narrow it afterwards
        # TODO: consider if we should remove this logic once ProcessGroupGloo
        # support uneven list, and collective perfomance on par
        if self.dim > tensor.ndim:
            raise ValueError(f"Sharding dim {self.dim} greater than tensor ndim {tensor.ndim}")
        if tensor.size(self.dim) < num_chunks:
            raise ValueError(f"Tensors to be sharded on dim {self.dim} must be at least as large as "
                             f"the number of devices in that dimension {num_chunks}")
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

    def _pad_tensor(self, tensor):
        # pad tensor by 1 on the shard dim
        pad = [0, 0] * (tensor.ndim - self.dim)
        pad[-1] = 1
        return torch.nn.functional.pad(tensor, pad)

    def _unpad_tensor(self, tensor):
        # unpad tensor by 1 on the shard dim
        return tensor.narrow(self.dim, start=0, length=tensor.size(self.dim) - 1)

    def _local_shard_size_on_dim(
        self,
        size_on_dim,
        num_chunks,
        rank,
        return_offset=False,
    ):
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

    def _shard_tensor(self, tensor, mesh, mesh_dim):
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
        output = torch.empty_like(scatter_list[my_coordinate[mesh_dim]])
        mesh.scatter(output, scatter_list, mesh_dim=mesh_dim)

        if pad_idx != 0 and my_coordinate[mesh_dim] >= pad_idx:
            output = self._unpad_tensor(output)
        return output

    def _reduce_shard_tensor(
        self,
        tensor,
        mesh,
        reduce_op,
        mesh_dim,
    ):
        """
        reduce and scatter a tensor on a mesh dimension
        """
        my_coordinate = mesh.get_coordinate()
        num_chunks = mesh.size(dim=mesh_dim)
        # TODO: what should happen if rank is not in the mesh?
        # see issue https://github.com/pytorch/tau/pull/492
        if my_coordinate is None:
            raise RuntimeError("Rank if not part of mesh")  # TODO: figure out behavior here
        scattered_list, pad_idx = self._split_tensor(
            tensor, num_chunks, with_padding=True, contiguous=True
        )
        # TODO: mindtorch do not support DTensor. so not use CommTensor below.
        # wrap with comm tensor
        # scattered_list = [CommTensor(t) for t in scattered_list]
        output = torch.empty_like(scattered_list[my_coordinate[mesh_dim]])
        mesh.reduce_scatter(
            # CommTensor(output),
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
        local_tensor,
        size,
        mesh,
        mesh_dim,
    ):
        """
        This function all_gather all shards and return a tensor that
        is replicated on the previously sharded mesh dimension
        """
        my_coordinate = mesh.get_coordinate()
        num_chunks = mesh.size(dim=mesh_dim)
        # TODO: what should happen if rank is not in the mesh?
        # see issue https://github.com/pytorch/tau/pull/492
        if my_coordinate is None:
            raise RuntimeError("Rank if not part of mesh")  # TODO: figure out behavior here
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
                # CommTensor(
                #     torch.empty_like(
                #         local_tensor,
                #         memory_format=torch.contiguous_format,
                #     )
                # )
                torch.empty_like(
                    local_tensor,
                    memory_format=torch.contiguous_format,
                )
            )

        mesh.all_gather(gathered_list, local_tensor.contiguous(), mesh_dim=mesh_dim)
        # unpad the tensor if the input tensor was padded
        if pad_idx != 0:
            gathered_list = [
                self._unpad_tensor(gathered_tensor)  # type: ignore[misc]
                if i >= pad_idx
                else gathered_tensor
                for i, gathered_tensor in enumerate(gathered_list)
            ]
        return torch.cat(gathered_list, dim=self.dim)  # type: ignore[arg-type]

    def __eq__(self, other):
        if not isinstance(other, Shard):
            return False
        return self.dim == other.dim

    def __hash__(self):
        return hash(self.dim)

    def __repr__(self):
        return f"Shard(dim={self.dim})"


class Replicate(Placement):
    # replicate placement
    def __eq__(self, other):
        if not isinstance(other, Replicate):
            return False
        return True

    def __hash__(self):
        # every replicate placement is the same
        return -1

    def __repr__(self):
        return "Replicate()"

    def _replicate_tensor(
        self,
        tensor,
        mesh,
        mesh_dim
    ):
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

class _Partial(Placement):
    # This is a default partial placement with element-wise reduce op
    # when doing reduction it follows the contract of `_to_replicate`
    # and `_to_shard` to do the reduction and convert the local tensor
    # to the corresponding state (replicate or shard)
    #
    # We can implement custom reductions as needed by subclassing this
    # class and override those contracts.

    def __init__(self, reduce_op=c10d.ReduceOp.SUM):  # type: ignore[assignment]
        self.reduce_op=reduce_op

    def _to_replicate(self, tensor, mesh, mesh_dim):
        return mesh.all_reduce(
            tensor, self.reduce_op, mesh_dim=mesh_dim  # type: ignore[call-arg]
        )

    def _to_shard(
        self,
        tensor,
        mesh,
        mesh_dim,
        shard_spec,
    ):
        # by default call reduce_shard_tensor of the shard_spec.
        shard_spec = cast(Shard, shard_spec)
        return shard_spec._reduce_shard_tensor(
            tensor, mesh, self.reduce_op, mesh_dim  # type: ignore[call-arg]
        )

    def __eq__(self, other):
        if not isinstance(other, _Partial):
            return False
        return self.reduce_op == other.reduce_op

    def __hash__(self):
        return hash(self.reduce_op)

    def __repr__(self):
        return f"_Partial(reduce_op={self.reduce_op})"
