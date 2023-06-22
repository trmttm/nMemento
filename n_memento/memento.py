import datetime

from n_memento.interface import Memento


class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._datetime = datetime.datetime.now()

    def get_name(self) -> str:
        return f'{self.get_date_time()} / {self.get_state()}'

    def get_state(self):
        return self._state

    def get_date_time(self) -> datetime.date:
        return self._datetime