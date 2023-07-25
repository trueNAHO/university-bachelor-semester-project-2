from ....base.state_machine import StateMachine
from ....settings.settings import Settings
from ..events.move_down import EventPlayerMoveDown
from ..events.move_down_stop import EventPlayerMoveDownStop
from ..events.move_left import EventPlayerMoveLeft
from ..events.move_left_stop import EventPlayerMoveLeftStop
from ..events.move_right import EventPlayerMoveRight
from ..events.move_right_stop import EventPlayerMoveRightStop
from ..events.move_up import EventPlayerMoveUp
from ..events.move_up_stop import EventPlayerMoveUpStop
from ..states.idle import StatePlayerIdle
from ..states.move_down import StatePlayerMoveDown
from ..states.move_left import StatePlayerMoveLeft
from ..states.move_right import StatePlayerMoveRight
from ..states.move_up import StatePlayerMoveUp

StatePlayerIdle._EVENT_STATE_TRANSITIONS = {
    EventPlayerMoveDown: StatePlayerMoveDown,
    EventPlayerMoveLeft: StatePlayerMoveLeft,
    EventPlayerMoveRight: StatePlayerMoveRight,
    EventPlayerMoveUp: StatePlayerMoveUp,
}
StatePlayerIdle._EVENTS = list(StatePlayerIdle._EVENT_STATE_TRANSITIONS.keys())

StatePlayerMoveDown._EVENT_STATE_TRANSITIONS = {
    EventPlayerMoveDownStop: StatePlayerIdle,
}
StatePlayerMoveDown._EVENTS = list(
    StatePlayerMoveDown._EVENT_STATE_TRANSITIONS.keys())

StatePlayerMoveLeft._EVENT_STATE_TRANSITIONS = {
    EventPlayerMoveLeftStop: StatePlayerIdle,
}
StatePlayerMoveLeft._EVENTS = list(
    StatePlayerMoveLeft._EVENT_STATE_TRANSITIONS.keys())

StatePlayerMoveRight._EVENT_STATE_TRANSITIONS = {
    EventPlayerMoveRightStop: StatePlayerIdle,
}
StatePlayerMoveRight._EVENTS = list(
    StatePlayerMoveRight._EVENT_STATE_TRANSITIONS.keys())

StatePlayerMoveUp._EVENT_STATE_TRANSITIONS = {
    EventPlayerMoveUpStop: StatePlayerIdle,
}
StatePlayerMoveUp._EVENTS = list(
    StatePlayerMoveUp._EVENT_STATE_TRANSITIONS.keys())

class StateMachinePlayer(StateMachine):

    _FINAL_STATES = set()

    _INITIAL_STATE = StatePlayerIdle

    _STATES = {
        StatePlayerIdle,
        StatePlayerMoveDown,
        StatePlayerMoveLeft,
        StatePlayerMoveRight,
        StatePlayerMoveUp,
    }

    def __init__(self,
                 speed: float = Settings.PLAYER_SPEED,
                 x: float = Settings.PLAYER_SPAWN_X,
                 y: float = Settings.PLAYER_SPAWN_Y) -> None:
        super().__init__()
        self.speed: float = speed
        self.x: float = x
        self.y: float = y
