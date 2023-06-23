from n_memento.interface import Memento
from n_memento.memento import ConcreteMemento


class Originator:
    def __init__(self, state: dict = None):
        self._state = state if state is not None else {}

    def set(self, key: str, value):
        self._state[key] = value

    def get(self, key):
        return self._state.get(key)

    def save(self) -> Memento:
        return ConcreteMemento(dict(self._state))

    def restore(self, memento: Memento):
        self._state = memento.get_state()

    @property
    def state(self) -> dict:
        return dict(self._state)
