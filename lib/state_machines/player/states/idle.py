from ....base.state import State
from ..commands.idle import CommandPlayerIdle


class StatePlayerIdle(State):

    _COMMAND = CommandPlayerIdle
