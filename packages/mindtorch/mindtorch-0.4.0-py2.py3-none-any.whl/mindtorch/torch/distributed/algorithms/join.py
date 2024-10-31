from abc import ABC, abstractmethod
from typing import NamedTuple
from mindtorch.utils import unsupported_attr

class JoinHook():
    def __init__(self):
        raise NotImplementedError("`JoinHook` is not currently supported.")


class Joinable(ABC):
    @abstractmethod
    def __init__(self):
        super(Joinable, self).__init__()
        raise NotImplementedError("`Joinable` is not currently supported.")

    @abstractmethod
    def join_hook(self, **kwargs):
        raise NotImplementedError("`Joinable.join_hook` is not currently supported.")

    @property
    @abstractmethod
    def join_device(self):
        raise NotImplementedError("`Joinable.join_device` is not currently supported.")

    @property
    @abstractmethod
    def join_process_group(self):
        raise NotImplementedError("`Joinable.join_process_group` is not currently supported.")


class _JoinConfig(NamedTuple):
    enable: bool
    throw_on_early_termination: bool
    is_first_joinable: bool

    @staticmethod
    def construct_disabled_join_config():
        return _JoinConfig(
            enable=False,
            throw_on_early_termination=False,
            is_first_joinable=False
        )



class Join():
    def __init__(
        self,
        joinables,
        enable=True,
        throw_on_early_termination=False,
        **kwargs,
    ):
        unsupported_attr(joinables)
        unsupported_attr(enable)
        unsupported_attr(throw_on_early_termination)
        unsupported_attr(kwargs)
        raise NotImplementedError("`Join` is not currently supported.")
