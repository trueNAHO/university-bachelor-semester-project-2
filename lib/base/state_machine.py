import abc

from typing import Set, Type

from .event_null import EventNull
from .state import State


class StateMachine(metaclass=abc.ABCMeta):

    _FINAL_STATES: Set[Type[State]]
    _INITIAL_STATE: Type[State]
    _STATES: Set[Type[State]]

    def __init__(self) -> None:
        self._current_state: State = self._INITIAL_STATE(self, EventNull())

    def get_current_state(self) -> object:
        return self._current_state

    def set_current_state(self, state: State) -> None:
        self._current_state.exit()
        self._current_state = state
        self._current_state.enter()

    def update(self, elapsed_time_seconds: float) -> None:
        self._current_state.update(elapsed_time_seconds)
