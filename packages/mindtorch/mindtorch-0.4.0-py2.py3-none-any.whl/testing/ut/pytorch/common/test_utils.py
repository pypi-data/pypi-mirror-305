import os
import mindtorch.torch as torch
from torch.utils import _pytree as pytree
from mindtorch.torch.utils import _pytree as msa_pytree
from mindtorch.torch.logging import debug, info, warning, error, critical, _setup_logger
from ...utils import set_mode_by_env_config

set_mode_by_env_config()

def test_logging():
    # The following three contents are not expected to be displayed on the terminal.
    debug('This is a debug message.')
    info('This is an info message.')
    warning('This is a warning message.')
    # The following seven contents are expected to be displayed on the terminal.
    error('This is an error message.')
    critical('This is a critical message.')
    os.environ['MSA_LOG'] = '0'
    _setup_logger()
    torch.debug('This is a debug message.')
    torch.info('This is an info message.')
    torch.warning('This is a warning message.')
    torch.error('This is an error message.')
    torch.critical('This is a critical message.')

    try:
        os.environ['MSA_LOG'] = '6'
        _setup_logger()
    except ValueError as e:
        assert "Incorrect log level, please check the configuration of 'MSA_LOG', desire integer log level: " \
               "4-CRITICAL, 3-ERROR, 2-WARNING, 1-INFO, 0-DEBUG. but got 6." in str(e)
    os.environ['MSA_LOG'] = '2'
    _setup_logger()

def test_tree_flatten_unflatten():
    input = [1, {"k1": 2, "k2": (3, 4)}, 5]
    flatten_torch = pytree.tree_flatten(input)
    flatten_msa = msa_pytree.tree_flatten(input)
    assert flatten_torch == flatten_msa

    unflatten_torch = pytree.tree_unflatten(*flatten_torch)
    unflatten_msa = msa_pytree.tree_unflatten(*flatten_msa)
    assert unflatten_torch == unflatten_msa


if __name__ == '__main__':
    test_logging()
    test_tree_flatten_unflatten()
