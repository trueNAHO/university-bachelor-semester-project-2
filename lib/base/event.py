import abc


class Event(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __init__(self) -> None:
        pass
