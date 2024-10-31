import os
import subprocess

from ...utils import SKIP_ENV_CPU, SKIP_ENV_ASCEND, SKIP_ENV_GPU, set_mode_by_env_config
set_mode_by_env_config()


@SKIP_ENV_ASCEND(reason='Ascend not support 3 cards.')
@SKIP_ENV_CPU(reason='`distributed` is not supported on CPU')
def test_dist_basic_gpu():
    os.environ.unsetenv('CUDA_VISIBLE_DEVICES') # only for this process

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd1 = 'mpirun -n 3  python {}/dist_impl_gpu.py'.format(cur_dir)
    cmd2 = 'mpirun --allow-run-as-root -n 3  python {}/dist_impl_gpu.py'.format(cur_dir)
    try:
        subprocess.check_output(cmd1, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        subprocess.check_output(cmd2, stderr=subprocess.STDOUT, shell=True)


@SKIP_ENV_GPU(reason='GPU need run-as-root.')
@SKIP_ENV_CPU(reason='`distributed` is not supported on CPU')
def test_dist_basic_ascend():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    # TODO: Ascend unsupport 4 when new_group([0,1])
    cmd = 'msrun --worker_num=2 --local_worker_num=2 {}/dist_impl_ascend.py'.format(cur_dir)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

if __name__ == '__main__':
    test_dist_basic_gpu()
    test_dist_basic_ascend()