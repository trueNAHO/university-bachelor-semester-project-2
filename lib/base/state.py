from __future__ import annotations

import abc

from typing import Any, Dict, List, Type

from ..command_manager.command_manager import CommandManager
from ..event_manager.event_manager import EventManager
from .command import Command
from .event import Event


class State(metaclass=abc.ABCMeta):

    _COMMAND: Type[Command]
    _EVENTS: List[Type[Event]]
    _EVENT_STATE_TRANSITIONS: Dict[Type[Event], Type[State]]

    def __init__(self, state_machine: Any, event: Event) -> None:
        self._event: Event = event
        self._state_machine: Any = state_machine
        self.enter()

    def enter(self) -> None:
        for event in self._EVENTS:
            EventManager.subscribe(event, self._handle_event)

    def exit(self) -> None:
        for event in self._EVENTS:
            EventManager.unsubscribe(event, self._handle_event)

    def update(self, elapsed_time_seconds: float) -> None:
        CommandManager.add(
            self._COMMAND(self._state_machine, self._event,
                          elapsed_time_seconds))

    def _handle_event(self, event: Event) -> None:
        state = self._EVENT_STATE_TRANSITIONS.get(type(event))

        if not state:
            return

        self._state_machine.set_current_state(state(self._state_machine,
                                                    event))
