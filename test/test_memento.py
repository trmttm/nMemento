import unittest


class MyTestCase(unittest.TestCase):
    def test_each_object(self):
        from n_memento.caretaker import Caretaker
        from n_memento.originator import Originator

        state_0 = {'x': 0}
        state_1 = {'x': 1}
        state_2 = {'x': 2}
        state_3 = {'x': 2, 'y': 0}

        originator = Originator(state_0)
        caretaker = Caretaker(originator)
        self.assertEqual(originator.state, state_0)

        caretaker.backup()
        originator.set('x', 1)
        self.assertEqual(originator.get('x'), 1)
        self.assertEqual(originator.get('y'), None)
        self.assertEqual(originator.state, state_1)

        caretaker.backup()
        originator.set('x', 2)
        self.assertEqual(originator.get('x'), 2)
        self.assertEqual(originator.get('y'), None)
        self.assertEqual(originator.state, state_2)

        caretaker.backup()
        originator.set('y', 0)
        self.assertEqual(originator.get('x'), 2)
        self.assertEqual(originator.get('y'), 0)
        self.assertEqual(originator.state, state_3)

        caretaker.show_history()
        caretaker.undo()
        self.assertEqual(originator.state, state_2)
        caretaker.undo()
        self.assertEqual(originator.state, state_1)

    def test_encapsulation(self):
        from n_memento.entity import Entity
        entity = Entity()
        self.assertEqual(entity.state, {})

        state_0 = {'x': 0}
        state_1 = {'x': 2}
        state_2 = {'x': 2, 'y': 0}

        entity.backup()
        entity.set('x', 0)
        self.assertEqual(entity.state, state_0)

        entity.backup()
        entity.set('x', 2)
        self.assertEqual(entity.state, state_1)

        entity.backup()
        entity.set('y', 0)
        self.assertEqual(entity.state, state_2)

        entity.backup()
        entity.show_history()

        entity.undo()
        self.assertEqual(entity.state, state_2)
        entity.undo()
        self.assertEqual(entity.state, state_1)
        entity.undo()
        self.assertEqual(entity.state, state_0)
        entity.undo()
        self.assertEqual(entity.state, {})
        entity.undo()
        self.assertEqual(entity.state, {})


if __name__ == '__main__':
    unittest.main()
