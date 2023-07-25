import time

from collections import deque
from typing import Any, Deque, Tuple


class CommandManager:

    _COMMANDS: Deque[Tuple[float, Any]] = deque()
    _COMMAND_EXPIRATION_TIME_SECONDS: float = 5
    _LAST_PROCESSED_INDEX: int = -1

    @classmethod
    def add(cls, command: Any) -> None:
        current_time: float = time.time()
        cls._COMMANDS.append((current_time, command))

    @classmethod
    def do(cls) -> None:
        current_time: float = time.time()

        if not cls._COMMANDS:
            return

        cls._remove_expired_commands(current_time)

        commands_length = len(cls._COMMANDS)

        for i in range(cls._LAST_PROCESSED_INDEX + 1, commands_length):
            cls._COMMANDS[i][1].do()

        cls._LAST_PROCESSED_INDEX = commands_length - 1

    @classmethod
    def undo(cls, seconds_to_undo: float = float("inf")) -> None:
        current_time: float = time.time()

        if not cls._COMMANDS:
            return

        cls._remove_expired_commands(current_time)

        for _ in range(len(cls._COMMANDS) - cls._LAST_PROCESSED_INDEX - 1):
            cls._COMMANDS.pop()

        while (cls._LAST_PROCESSED_INDEX != -1
               and current_time - cls._COMMANDS[cls._LAST_PROCESSED_INDEX][0]
               <= seconds_to_undo):
            command = cls._COMMANDS.pop()
            command[1].undo()
            cls._LAST_PROCESSED_INDEX -= 1

    @classmethod
    def _remove_expired_commands(cls, current_time: float) -> None:
        while (cls._COMMANDS and current_time - cls._COMMANDS[0][0] >
               cls._COMMAND_EXPIRATION_TIME_SECONDS):
            cls._COMMANDS.popleft()

            if cls._LAST_PROCESSED_INDEX > 0:
                cls._LAST_PROCESSED_INDEX -= 1

            elif cls._LAST_PROCESSED_INDEX == 0:
                if cls._COMMANDS:
                    cls._COMMANDS[0][1].do()
                else:
                    cls._LAST_PROCESSED_INDEX = -1

            else:
                pass
