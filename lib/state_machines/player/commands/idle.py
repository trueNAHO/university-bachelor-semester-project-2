from ....base.command import Command


class CommandPlayerIdle(Command):

    def do(self) -> None:
        print(f"{self}: do()")

    def undo(self) -> None:
        print(f"{self}: undo()")
