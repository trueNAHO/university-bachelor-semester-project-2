from ....base.command import Command


class CommandPlayerMoveDown(Command):

    def do(self) -> None:
        self._target.y += self._target.speed * self._elapsed_time_seconds

    def undo(self) -> None:
        self._target.y -= self._target.speed * self._elapsed_time_seconds
