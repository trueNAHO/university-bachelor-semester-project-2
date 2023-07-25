from typing import Any, Callable, Dict, List, Optional


class EventManager:
    _EVENT_SUBSCRIBERS: Dict[Any, List[Callable[..., None]]] = {}

    @classmethod
    def emit(cls, event: object, target: Optional[Any] = None) -> None:
        for callback in cls._EVENT_SUBSCRIBERS.get(type(event), []):
            if target is None or callback.__self__ == target:
                callback(event)

    @classmethod
    def subscribe(cls, event: object, callback: Callable[..., None]) -> None:
        if event not in cls._EVENT_SUBSCRIBERS:
            cls._EVENT_SUBSCRIBERS[event] = []

        cls._EVENT_SUBSCRIBERS[event].append(callback)

    @classmethod
    def unsubscribe(cls, event: object, callback: Callable[..., None]) -> None:
        if event not in cls._EVENT_SUBSCRIBERS:
            return

        cls._EVENT_SUBSCRIBERS[event] = [
            subscriber for subscriber in cls._EVENT_SUBSCRIBERS[event]
            if subscriber != callback
        ]
