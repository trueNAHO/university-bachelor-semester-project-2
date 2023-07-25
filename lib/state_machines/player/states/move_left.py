from ....base.state import State
from ..commands.move_left import CommandPlayerMoveLeft


class StatePlayerMoveLeft(State):

    _COMMAND = CommandPlayerMoveLeft
