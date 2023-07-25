import abc

from typing import Any


class Command(metaclass=abc.ABCMeta):

    def __init__(self, target: Any, event: Any,
                 elapsed_time_seconds: float) -> None:
        self._elapsed_time_seconds: float = elapsed_time_seconds
        self._event: Any = event
        self._target: Any = target

    @abc.abstractmethod
    def do(self) -> None:
        pass

    @abc.abstractmethod
    def undo(self) -> None:
        pass
