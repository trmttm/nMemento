from n_memento.interface import Memento
from n_memento.interface import Memento
from n_memento.memento import ConcreteMemento


class Originator:
    def __init__(self, state):
        self._state = state

    def do(self):
        # changes state
        self._state += 1

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.get_state()