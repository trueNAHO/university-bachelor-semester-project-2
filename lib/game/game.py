import pygame

from ..command_manager.command_manager import CommandManager
from ..event_manager.event_manager import EventManager
from ..settings.settings import Settings
from ..state_machines.player.events.move_down import EventPlayerMoveDown
from ..state_machines.player.events.move_down_stop import EventPlayerMoveDownStop
from ..state_machines.player.events.move_left import EventPlayerMoveLeft
from ..state_machines.player.events.move_left_stop import EventPlayerMoveLeftStop
from ..state_machines.player.events.move_right import EventPlayerMoveRight
from ..state_machines.player.events.move_right_stop import EventPlayerMoveRightStop
from ..state_machines.player.events.move_up import EventPlayerMoveUp
from ..state_machines.player.events.move_up_stop import EventPlayerMoveUpStop
from ..state_machines.player.state_machine.state_machine import StateMachinePlayer


class Game:

    def __init__(self) -> None:
        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._player: StateMachinePlayer = StateMachinePlayer()
        self._running: bool = True
        self._screen: pygame.Surface = pygame.display.set_mode(
            (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))

        pygame.init()
        pygame.display.set_caption(Settings.WINDOW_CAPTION)

    def run(self) -> None:
        while self._running:
            self._handle_events()

            elapsed_time_seconds: float = self._clock.get_time() / 1000.0

            self._update(elapsed_time_seconds)
            self._check_collision()
            self._render()
            self._cap_fps()

        self._cleanup()

    def _cap_fps(self) -> None:
        self._clock.tick(Settings.FPS)

    def _check_collision(self) -> None:
        if self._player.x > Settings.SCREEN_WIDTH:
            self._player.x = Settings.SCREEN_WIDTH
        elif self._player.x < 0:
            self._player.x = 0
        elif self._player.y > Settings.SCREEN_HEIGHT:
            self._player.y = Settings.SCREEN_HEIGHT
        elif self._player.y < 0:
            self._player.y = 0

    def _cleanup(self) -> None:
        pygame.quit()

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self._running = False

                case pygame.KEYDOWN:
                    match event.key:
                        case Settings.KEY_QUIT:
                            self._running = False

                        case Settings.KEY_MOVE_DOWN:
                            EventManager.emit(EventPlayerMoveDown())

                        case Settings.KEY_MOVE_LEFT:
                            EventManager.emit(EventPlayerMoveLeft())

                        case Settings.KEY_MOVE_RIGHT:
                            EventManager.emit(EventPlayerMoveRight())

                        case Settings.KEY_MOVE_UP:
                            EventManager.emit(EventPlayerMoveUp())

                        case Settings.KEY_UNDO:
                            CommandManager.undo()

                        case _:
                            pass

                case pygame.KEYUP:
                    match event.key:
                        case Settings.KEY_MOVE_DOWN:
                            EventManager.emit(EventPlayerMoveDownStop())

                        case Settings.KEY_MOVE_LEFT:
                            EventManager.emit(EventPlayerMoveLeftStop())

                        case Settings.KEY_MOVE_RIGHT:
                            EventManager.emit(EventPlayerMoveRightStop())

                        case Settings.KEY_MOVE_UP:
                            EventManager.emit(EventPlayerMoveUpStop())

                        case _:
                            pass

    def _render(self) -> None:
        self._screen.fill((0, 0, 255))
        pygame.draw.circle(self._screen, (255, 0, 0), (self._player.x,
                                                       self._player.y), 10)
        pygame.display.flip()

    def _update(self, elapsed_time_seconds: float) -> None:
        self._player.update(elapsed_time_seconds)
        CommandManager.do()
        print(self._player.x, self._player.y, len(EventManager._EVENT_SUBSCRIBERS))
