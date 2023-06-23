import unittest


class MyTestCase(unittest.TestCase):
    def test_each_object(self):
        from n_memento.caretaker import Caretaker
        from n_memento.originator import Originator

        original_state = {'x': 0}
        originator = Originator(original_state)
        caretaker = Caretaker(originator)
        self.assertEqual(originator.state, original_state)

        caretaker.backup()
        originator.set('x', 1)
        self.assertEqual(originator.get('x'), 1)
        self.assertEqual(originator.get('y'), None)
        self.assertEqual(originator.state, {'x': 1})

        caretaker.backup()
        originator.set('x', 2)
        self.assertEqual(originator.get('x'), 2)
        self.assertEqual(originator.get('y'), None)
        self.assertEqual(originator.state, {'x': 2})

        caretaker.backup()
        originator.set('y', 0)
        self.assertEqual(originator.get('x'), 2)
        self.assertEqual(originator.get('y'), 0)
        self.assertEqual(originator.state, {'x': 2, 'y': 0})

        caretaker.show_history()
        caretaker.undo()
        self.assertEqual(originator.state, {'x': 2, })
        caretaker.undo()
        self.assertEqual(originator.state, {'x': 1, })

    def test_encapsulation(self):
        from n_memento.entity import Entity
        entity = Entity()
        self.assertEqual(entity.state, {})

        entity.backup()
        entity.set('x', 0)
        self.assertEqual(entity.state, {'x': 0})

        entity.backup()
        entity.set('x', 2)
        self.assertEqual(entity.state, {'x': 2})

        entity.backup()
        entity.set('y', 0)
        self.assertEqual(entity.state, {'x': 2, 'y': 0})

        entity.backup()
        entity.show_history()

        entity.undo()
        self.assertEqual(entity.state, {'x': 2, 'y': 0})
        entity.undo()
        self.assertEqual(entity.state, {'x': 2,})
        entity.undo()
        self.assertEqual(entity.state, {'x': 0})
        entity.undo()
        self.assertEqual(entity.state, {})
        entity.undo()
        self.assertEqual(entity.state, {})


if __name__ == '__main__':
    unittest.main()
