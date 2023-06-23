from .caretaker import Caretaker
from .originator import Originator


class Entity:
    def __init__(self, state: dict = None):
        self._originator = Originator(state)
        self._caretaker = Caretaker(self._originator)

    def set(self, key: str, value):
        self._originator.set(key, value)

    def backup(self):
        self._caretaker.backup()

    def show_history(self):
        self._caretaker.show_history()

    def get(self, key: str):
        return self._originator.get(key)

    def undo(self):
        self._caretaker.undo()

    @property
    def state(self) -> dict:
        return self._originator.state
