import abc
import datetime


class Memento(abc.ABC):
    @abc.abstractmethod
    def get_name(self) -> str:
        pass

    @abc.abstractmethod
    def get_state(self):
        pass

    @abc.abstractmethod
    def get_date_time(self) -> datetime.date:
        pass