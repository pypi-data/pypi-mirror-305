from mindtorch.torch.distributed.distributed_c10d import _get_pg_name
from mindtorch.torch import distributed as dist


def dist_basic():
    dist.init_process_group(backend='hccl', world_size=2)
    pg0 = dist.new_group([0, 1])
    print('rank:', dist.get_rank())
    print('world_size:', dist.get_world_size())
    print('pg0:', _get_pg_name(pg0))
    print('pg0 rank:', dist.get_rank(pg0))
    print('is_available:', dist.is_available())
    print('is_initialized:', dist.is_initialized())
    print('is_mpi_available:', dist.is_mpi_available())
    print('is_nccl_available:', dist.is_nccl_available())
    print('is_hccl_available:', dist.is_hccl_available())
    print('get_backend:', dist.get_backend())
    print('pg0 get_process_group_ranks:', dist.get_process_group_ranks(pg0))
    dist.destroy_process_group(pg0)

    # pg1 = dist.new_group([1, 2])
    # print('rank:', dist.get_rank())
    # print('world_size:', dist.get_world_size())
    # print('pg1:', _get_pg_name(pg1))
    # print('pg1 rank:', dist.get_rank(pg1))
    # print('pg1 get_process_group_ranks:', dist.get_process_group_ranks(pg1))
    # dist.destroy_process_group(pg1)

    # pg2 = dist.new_group([0, 1, 2])
    # print('rank:', dist.get_rank())
    # print('world_size:', dist.get_world_size())
    # print('pg2 rank:', dist.get_rank(pg2))
    # print('pg2 get_process_group_ranks:', dist.get_process_group_ranks(pg2))
    # dist.destroy_process_group(pg2)


if __name__ == '__main__':
    dist_basic()
