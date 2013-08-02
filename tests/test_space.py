import unittest
from pythonwarrior.space import Space
from pythonwarrior.floor import Floor

class TestSpace(unittest.TestCase):
    def setUp(self):
        self.floor = Floor()
        self.floor.width = 2
        self.floor.height = 3

class TestEmptySpace(TestSpace):
    def setUp(self):
        super(TestEmptySpace, self).setUp()
        self.space = self.floor.space(0, 0)

    def test_should_not_be_enemy(self):
        self.assertFalse(self.space.is_enemy())

    def test_should_not_be_warrior(self):
        self.assertFalse(self.space.is_warrior())

    def test_should_be_empty(self):
        self.assertTrue(self.space.is_empty())

    def test_should_not_be_stairs(self):
        self.assertFalse(self.space.is_stairs())

    def test_should_not_be_captive(self):
        self.assertFalse(self.space.is_captive())

    def test_should_say_nothing_as_name(self):
        self.assertEqual(str(self.space), 'nothing')

class TestOutOfBounds(TestSpace):
    def setUp(self):
        super(TestOutOfBounds, self).setUp()
        self.space = self.floor.space(-1, 1)

    def test_should_be_wall(self):
        self.assertTrue(self.space.is_wall())

    def test_should_not_be_empty(self):
        self.assertFalse(self.space.is_empty())

    def test_should_have_name_of_wall(self):
        self.assertEqual(str(self.space), 'wall')


if __name__ == '__main__':
    unittest.main()
