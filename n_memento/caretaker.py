from n_memento.originator import Originator

from .memento import Memento


class Caretaker:
    def __init__(self, originator: Originator):
        self._mementos: list[Memento, ...] = []
        self._originator = originator

    def backup(self):
        concrete_memento = self._originator.save()
        self._mementos.append(concrete_memento)
        print(f'Backed up {concrete_memento.get_name()}')

    def undo(self):
        if not len(self._mementos):
            print('No more memento to undo.')
            return
        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
            print(f'Undone and restored {memento.get_name()}')
        except Exception:
            self.undo()

    def show_history(self):
        print(f'\nShow history...')
        for n, memento in enumerate(self._mementos):
            print(n, memento.get_name())
        print()

    @property
    def history(self) -> dict:
        return dict(zip(range(len(self._mementos)), tuple(m.get_name() for m in self._mementos)))
