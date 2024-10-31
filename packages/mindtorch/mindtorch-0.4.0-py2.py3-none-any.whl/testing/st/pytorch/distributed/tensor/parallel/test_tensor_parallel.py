import os
import subprocess

from ......ut.utils import SKIP_ENV_CPU, set_mode_by_env_config, SKIP_ENV_ASCEND, is_test_under_ascend_context,\
                         SKIP_ENV_GPU, SKIP_ENV_PYNATIVE_MODE
set_mode_by_env_config()

if is_test_under_ascend_context():
    backend = 'hccl'
else:
    backend = 'nccl'

@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_2d_parallel():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/2d_parallel_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())
