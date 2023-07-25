from ....base.command import Command


class CommandPlayerMoveRight(Command):

    def do(self) -> None:
        self._target.x += self._target.speed * self._elapsed_time_seconds

    def undo(self) -> None:
        self._target.x -= self._target.speed * self._elapsed_time_seconds
