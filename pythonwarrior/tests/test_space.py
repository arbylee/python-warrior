import unittest
from pythonwarrior.floor import Floor
from pythonwarrior.units.warrior import Warrior
from pythonwarrior.units.sludge import Sludge
from pythonwarrior.units.captive import Captive
from pythonwarrior.units.golem import Golem


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


class TestWithWarrior(TestSpace):
    def setUp(self):
        super(TestWithWarrior, self).setUp()
        warrior = Warrior()
        self.floor.add(warrior, 0, 0)
        self.space = self.floor.space(0, 0)

    def test_should_be_warrior(self):
        self.assertTrue(self.space.is_warrior())

    def test_should_be_player(self):
        self.assertTrue(self.space.is_player())

    def test_should_not_be_enemy(self):
        self.assertFalse(self.space.is_enemy())

    def test_should_not_be_empty(self):
        self.assertFalse(self.space.is_empty())

    def test_should_know_what_unit_is_on_that_space(self):
        self.assertEqual(self.space.unit.__class__.__name__, "Warrior")


class TestWithEnemy(TestSpace):
    def setUp(self):
        super(TestWithEnemy, self).setUp()
        sludge = Sludge()
        self.floor.add(sludge, 0, 0)
        self.space = self.floor.space(0, 0)

    def test_should_be_enemy(self):
        self.assertTrue(self.space.is_enemy())

    def test_should_not_be_warrior(self):
        self.assertFalse(self.space.is_warrior())

    def test_should_not_be_empty(self):
        self.assertFalse(self.space.is_empty())

    def test_should_have_name_of_unit(self):
        self.assertEqual(str(self.space), 'Sludge')

    def test_bound_enemy_should_be_captive(self):
        self.space.unit.bind()
        self.assertTrue(self.space.is_captive)

    def test_bound_enemy_should_not_look_like_enemy(self):
        self.space.unit.bind()
        self.assertFalse(self.space.is_enemy())


class TestWithCaptive(TestSpace):
    def setUp(self):
        super(TestWithCaptive, self).setUp()
        self.captive = Captive()
        self.floor.add(self.captive, 0, 0)
        self.space = self.floor.space(0, 0)

    def test_should_be_captive(self):
        self.assertTrue(self.space.is_captive())

    def test_should_not_be_enemy(self):
        self.assertFalse(self.space.is_enemy())

    def test_should_be_ticking_if_captive_has_time_bomb(self):
        self.captive.add_abilities('explode_')
        self.assertTrue(self.space.is_ticking())

    def test_should_not_be_ticking_if_captive_does_not_have_time_bomb(self):
        self.assertFalse(self.space.is_ticking())


class TestWithGolem(TestSpace):
    def setUp(self):
        super(TestWithGolem, self).setUp()
        self.golem = Golem()
        self.floor.add(self.golem, 0, 0)
        self.space = self.floor.space(0, 0)

    def test_should_be_golem(self):
        self.assertTrue(self.space.is_golem())

    def test_should_not_be_enemy(self):
        self.assertFalse(self.space.is_enemy())

    def test_should_be_player(self):
        self.assertTrue(self.space.is_player())


class TestAtStairs(TestSpace):
    def setUp(self):
        super(TestAtStairs, self).setUp()
        self.floor.place_stairs(0, 0)
        self.space = self.floor.space(0, 0)

    def test_should_be_empty(self):
        self.assertTrue(self.space.is_empty())

    def test_should_be_stairs(self):
        self.assertTrue(self.space.is_stairs())


if __name__ == '__main__':
    unittest.main()
