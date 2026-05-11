from collections.abc import Callable


class Observable:
    def __init__(self) -> None:
        self._observers: list[Callable[[], None]] = []

    def attach(self, observer: Callable[[], None]) -> None:
        self._observers.append(observer)

    def detach(self, observer: Callable[[], None]) -> None:
        self._observers.remove(observer)

    def _notify(self) -> None:
        for observer in self._observers:
            observer()
