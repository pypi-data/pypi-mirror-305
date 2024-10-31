import os
import subprocess

from ....ut.utils import SKIP_ENV_CPU, set_mode_by_env_config, SKIP_ENV_ASCEND, is_test_under_ascend_context,\
                         SKIP_ENV_GPU, SKIP_ENV_PYNATIVE_MODE, SKIP_ENV_GRAPH_MODE
set_mode_by_env_config()

if is_test_under_ascend_context():
    backend = 'hccl'
else:
    backend = 'nccl'

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_all_reduce():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/allreduce_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_all_reduce_2_group():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 4 '
    cmd += 'python {}/allreduce_2_group_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_send_recv():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/send_recv_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_send_recv_2_group():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 4 '
    cmd += 'python {}/send_recv_2_group_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_send_recv_2_tag():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/send_recv_2_tag_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
@SKIP_ENV_GPU(reason='mindspore not support barrier on GPU')
def test_barrier():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/barrier_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_broadcast():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/broadcast_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_broadcast_2_group():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 4 '
    cmd += 'python {}/broadcast_2_group_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_PYNATIVE_MODE(reason='mindspore has some bug on backward when use TupleGetItem')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_broadcast_grad():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/broadcast_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
@SKIP_ENV_ASCEND(reason='destroy_process_group has some problem on Ascend.')
def test_destroy_process_group():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/destroy_process_group_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_get_global_rank():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/get_global_rank_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_all_gather_into_tensor():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/all_gather_into_tensor_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_all_gather_into_tensor_2_group():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 4 '
    cmd += 'python {}/all_gather_into_tensor_2_group_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_all_gather():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/all_gather_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_all_gather_2_group():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 4 '
    cmd += 'python {}/all_gather_2_group_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
@SKIP_ENV_GPU(reason='MindSpore not support Reduce on GPU')
def test_reduce():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/reduce_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_simple_interface():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/simple_interface_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_reduce_scatter():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/reduce_scatter_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_reduce_scatter_2_group():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 4 '
    cmd += 'python {}/reduce_scatter_2_group_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_reduce_scatter_grad():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/reduce_scatter_grad_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
@SKIP_ENV_GPU(reason='MindSpore not support alltoall on GPU')
def test_all_to_all():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/all_to_all_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_from_torch_common():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/from_torch_common_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_from_torch_c10d_nccl():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/from_torch_c10d_nccl_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
@SKIP_ENV_GPU(reason='mindspore gather not support gpu')
def test_gather():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/gather_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
@SKIP_ENV_GPU(reason='mindspore gather not support gpu')
def test_gather_2_group():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 4 '
    cmd += 'python {}/gather_2_group_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_PYNATIVE_MODE(reason='MindSpore not support gather bprop yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
@SKIP_ENV_GPU(reason='mindspore gather not support gpu')
def test_gather_grad():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/gather_grad_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
@SKIP_ENV_GPU(reason='mindspore scatter not support gpu')
def test_scatter():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/scatter_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_allreduce_grad():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/allreduce_grad_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_allgather_grad():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/all_gather_grad_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_reduce_scatter_tensor():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/reduce_scatter_tensor_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_broadcast_cast_async():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/broadcast_impl_ascend_cast_and_async_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_allreduce_dtype():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/all_reduce_dtype_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())

@SKIP_ENV_GRAPH_MODE(reason='mindtorch distirbute not support graph mode yet.')
@SKIP_ENV_CPU(reason='distribute op not supported on CPU')
def test_batch_isend_irecv():
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    cmd = 'mpirun --allow-run-as-root -n 2 '
    cmd += 'python {}/batch_isend_irecv_impl.py {}'.format(cur_dir, backend)
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode())
