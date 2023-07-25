from ....base.state import State
from ..commands.move_up import CommandPlayerMoveUp


class StatePlayerMoveUp(State):

    _COMMAND = CommandPlayerMoveUp
