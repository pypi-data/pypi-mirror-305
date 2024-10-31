from typing import List, Optional, Sequence, TypeVar, Union
import mindtorch.torch as torch
from mindtorch.torch.distributed.distributed_c10d import ( # pylint: disable=W0611
    _get_default_group,
    all_gather,
    all_to_all,
    broadcast,
    get_global_rank,
    get_rank,
    get_world_size,
    GroupMember,
    init_process_group,
    is_initialized,
    new_group,
    ProcessGroup,
    reduce_scatter,
    ReduceOp,
    # scatter,
    Work,
    all_reduce,
)

from mindtorch.utils import unsupported_attr


_global_device_mesh=None

def get_global_device_mesh():
    global _global_device_mesh
    assert _global_device_mesh is not None, "Could not get a default device mesh!"
    return _global_device_mesh

def set_global_device_mesh(mesh):
    global _global_device_mesh
    _global_device_mesh = mesh

T = TypeVar("T")
_L = Union[T, Sequence[T]]
NDIntList = _L[_L[_L[_L[_L[_L[_L[int]]]]]]]

MeshExprT = Union[
    torch.Tensor,
    NDIntList,
]


class DeviceMesh:
    def __init__(
        self,
        device_type,
        mesh,
        *,
        _init_process_groups=True,
    ):
        self.device_type = device_type
        self.mesh = (
            mesh.detach()
            if isinstance(mesh, torch.Tensor)
            else torch.tensor(mesh, dtype=torch.int)
        )
        self._get_or_create_default_group()
        if _init_process_groups:
            self._dim_groups = self._init_process_groups()

    def _get_or_create_default_group(self):
        self._backend = "nccl" if self.device_type == "gpu" else "hccl"
        if not is_initialized():
            init_process_group(backend=self._backend)
        else:
            world_size = get_world_size()
            if self.mesh.numel() > world_size:
                raise RuntimeError(
                    f"Mesh should not be bigger than default world size, but found {self.mesh.numel()} ranks!"
                )
        # calculate the coordinates of the current global rank on the mesh
        rank_coords = (self.mesh == get_rank()).nonzero()
        if rank_coords.size(0) not in (0, 1):
            raise ValueError(f"rank_coords.size(0) is not in (0, 1), got {rank_coords.size(0)}.")
        self._coordinate_on_dim: Optional[List[int]] = (
            rank_coords[0].tolist() if rank_coords.size(0) > 0 else None
        )
        return _get_default_group()

    def _init_process_groups(self):
        default_pg = _get_default_group()
        unique_mesh_values = self.mesh.unique(sorted=True)
        if unique_mesh_values.numel() != self.mesh.numel():
            raise RuntimeError(
                f"DeviceMesh cannot have duplicate values, but found {self.mesh.tolist()}"
            )

        # groups created by dimension, each dimension should have exact
        # one valid process group per rank
        dim_groups=[]

        if self.mesh.ndim == 1 and len(unique_mesh_values) == get_world_size() - 1:
            # if the mesh is the same as world_pg, we just append the default
            # pg to the first dim goups, as new_group cannot have the exact
            # same ranks as world
            dim_groups.append(default_pg)
        else:
            # create sub pgs base on the mesh argument specified
            # handle multi-dim mesh, create subgroups by
            # looping over the pg_ranks_by_dim for each dim
            for dim in range(self.mesh.ndim):
                # swap the current dim to the last dim
                # then reshape to flatten out other dims
                pg_ranks_by_dim = self.mesh.swapdims(-1, dim).reshape(
                    -1, self.mesh.size(dim)
                )
                # multi-dim mesh, create subgroups by
                # looping over the pg_ranks for each dim
                # and append the groups
                for dim_mesh in pg_ranks_by_dim:
                    subgroup_ranks = dim_mesh.tolist()
                    # call new_group regardless of the current rank in the
                    # pg or not, it's required that all ranks participate
                    # in subgroup construction
                    new_subgroup = new_group(ranks=subgroup_ranks)
                    # only add to dim_groups if the current rank in the subgroup
                    if self.get_rank() in subgroup_ranks:
                        if len(dim_groups) > dim:
                            raise RuntimeError(
                                "Each device mesh dimension should get only one process group, "
                                f"but got {self.get_rank} in {subgroup_ranks}!"
                            )
                        dim_groups.append(new_subgroup)
        return dim_groups

    def __enter__(self):
        # set global device_mesh to this instance
        set_global_device_mesh(self)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # unset global device mesh
        set_global_device_mesh(None)

    def __repr__(self):
        return f"DeviceMesh:({self.mesh.tolist()})"

    def __hash__(self):
        return hash((self.mesh, id(self)))

    def __eq__(self, other):
        if not isinstance(other, DeviceMesh):
            return False
        if id(self) == id(other):
            return True
        return self.mesh.equal(other.mesh)

    def get_dim_groups(self):
        if not hasattr(self, "_dim_groups"):
            raise RuntimeError("DeviceMesh process groups not initialized!")
        return self._dim_groups

    def size(self, dim=0):
        return self.mesh.size(dim)

    @property
    def ndim(self):
        return self.mesh.ndim

    def get_rank(self):
        return get_rank()

    def get_coordinate(self):
        """
        Return the relative indices of this rank relative to all
        dimensions of the mesh. If this rank is not part of the mesh, return None.
        """
        return self._coordinate_on_dim if self._coordinate_on_dim else None

    def scatter(
        self,
        output,
        scatter_list,
        mesh_dim=0,
        async_op=False,
    ):
        raise NotImplementedError('DeviceMesh.scatter is not supported yet.')

    def broadcast(
        self,
        tensor,
        mesh_dim=0,
        async_op=False,
    ):
        # if tensor.is_meta:
        #     return None
        dim_group = self._dim_groups[mesh_dim]
        # src need to be global rank
        src_for_dim = 0
        if dim_group is not GroupMember.WORLD:
            src_for_dim = get_global_rank(dim_group, 0)

        return broadcast(tensor, src=src_for_dim, group=dim_group, async_op=async_op)

    def all_gather(
        self,
        tensor_list,
        tensor,
        mesh_dim=0,
        async_op=False,
    ):
        raise NotImplementedError('DeviceMesh.all_gather is not supported yet.')

    def all_reduce(
        self,
        tensor,
        op=ReduceOp.SUM,
        mesh_dim=0,
        async_op=False,
    ):
        unsupported_attr(async_op)
        dim_group = self._dim_groups[mesh_dim]
        return all_reduce(tensor, reduceOp=op, group=dim_group)

    def reduce_scatter(
        self,
        output,
        input_list,
        op=ReduceOp.SUM,
        mesh_dim=0,
        async_op=False,
    ):
        if self._backend == "nccl":
            dim_group = self._dim_groups[mesh_dim]
            # TODO: reduce_scatter not support async_op yet, so it has no return value.
            reduce_scatter(
                output, input_list, op=op, group=dim_group, async_op=async_op
            )
            fut = None
        # TODO: MindSpore not support "gloo" backend.
        elif self._backend == "gloo":
            raise NotImplementedError("'gloo' backend is not support yet.")
        else:
            raise RuntimeError(
                f"backend {self._backend} does not support reduce_scatter!"
            )
        return fut

    # TODO: MindSpore not support scatter yet.
    def all_to_all(
        self,
        output_tensor_list,
        input_tensor_list,
        mesh_dim=0,
        async_op=False,
    ):
        raise NotImplementedError("DeviceMesh.all_to_all is not supported yet.")
