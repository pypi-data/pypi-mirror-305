import os
import subprocess

from ....ut.utils import SKIP_ENV_CPU, SKIP_ENV_GPU, SKIP_ENV_ASCEND, set_mode_by_env_config
set_mode_by_env_config()


@SKIP_ENV_ASCEND(reason='Ascend not support 3 cards.')
@SKIP_ENV_CPU(reason='`DistributedDataParallel` is not supported on CPU')
def test_ddp_basic_gpu():
    os.environ.unsetenv('CUDA_VISIBLE_DEVICES') # only for this process

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd1 = 'mpirun -n 3  python {}/ddp_impl_gpu.py'.format(cur_dir)
    cmd2 = 'mpirun --allow-run-as-root -n 3  python {}/ddp_impl_gpu.py'.format(cur_dir)
    try:
        subprocess.check_output(cmd1, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        subprocess.check_output(cmd2, stderr=subprocess.STDOUT, shell=True)


@SKIP_ENV_GPU(reason='GPU need run-as-root.')
@SKIP_ENV_CPU(reason='`DistributedDataParallel` is not supported on CPU')
def test_ddp_basic_ascend():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun -n 2 python {}/ddp_impl_ascend.py'.format(cur_dir)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())


if __name__ == '__main__':
    test_ddp_basic_gpu()
    test_ddp_basic_ascend()