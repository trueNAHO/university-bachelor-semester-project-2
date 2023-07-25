from ....base.state import State
from ..commands.move_right import CommandPlayerMoveRight


class StatePlayerMoveRight(State):

    _COMMAND = CommandPlayerMoveRight
