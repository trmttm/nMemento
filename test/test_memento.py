import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from n_memento import Caretaker
        from n_memento import Originator

        original_state = {'x': 0}
        originator = Originator(original_state)
        caretaker = Caretaker(originator)

        caretaker.backup()
        originator.set('x', 1)
        self.assertEqual(originator.get('x'), 1)
        self.assertEqual(originator.get('y'), None)

        caretaker.backup()
        originator.set('x', 2)
        self.assertEqual(originator.get('x'), 2)
        self.assertEqual(originator.get('y'), None)

        caretaker.backup()
        originator.set('y', 0)
        self.assertEqual(originator.get('x'), 2)
        self.assertEqual(originator.get('y'), 0)

        caretaker.show_history()
        caretaker.undo()
        caretaker.undo()


if __name__ == '__main__':
    unittest.main()
