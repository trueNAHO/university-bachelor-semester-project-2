from ....base.state import State
from ..commands.move_down import CommandPlayerMoveDown


class StatePlayerMoveDown(State):

    _COMMAND = CommandPlayerMoveDown
