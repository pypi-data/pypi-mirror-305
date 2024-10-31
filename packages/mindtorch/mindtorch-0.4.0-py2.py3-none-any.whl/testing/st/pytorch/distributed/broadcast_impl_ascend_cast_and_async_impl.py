import sys
import numpy as np

import mindtorch.torch as torch
import mindtorch.torch.distributed as dist

def func(backend):
    dist.init_process_group(backend)

    rank = dist.get_rank()

    if rank == 0:
        data = torch.tensor([1, 2.]).to(f'cuda:{rank}')
    else:
        data = torch.zeros(2).to(f'cuda:{rank}')

    _enum_dtype = {torch.bool, torch.int64}

    for dtype in _enum_dtype:
        _tmp = data.to(dtype)
        work = dist.broadcast(_tmp, 0, async_op=True)
        work.wait()
        assert _tmp.dtype == dtype
        if dtype == torch.bool:
            assert np.allclose(_tmp.cpu().numpy(), np.array([True, True]))
        else:
            assert np.allclose(_tmp.cpu().numpy(), np.array([1, 2.]))
        assert data.shape == (2,)

if __name__ == '__main__':
    backend = sys.argv[1]
    func(backend)