import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from n_memento import Caretaker
        from n_memento import Originator

        original_state = 0
        originator = Originator(original_state)
        caretaker = Caretaker(originator)

        caretaker.backup()
        originator.do()

        caretaker.backup()
        originator.do()

        caretaker.backup()
        originator.do()

        caretaker.show_history()
        caretaker.undo()
        caretaker.undo()


if __name__ == '__main__':
    unittest.main()
