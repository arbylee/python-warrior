import mock
import unittest
from pythonwarrior.level import Level
from pythonwarrior.level_loader import LevelLoader
from pythonwarrior.profile import Profile


class TestLevelLoader(unittest.TestCase):
    def setUp(self):
        self.profile = Profile()
        self.level = Level(self.profile, 1)
        self.loader = LevelLoader(self.level)

    def test_should_be_able_to_add_description_tip_and_clue(self):
        self.loader.description('foo')
        self.loader.tip('bar')
        self.loader.clue('clue')
        self.assertEqual(self.level.description, 'foo')
        self.assertEqual(self.level.tip, 'bar')
        self.assertEqual(self.level.clue, 'clue')

    def test_should_be_able_to_set_size(self):
        self.loader.size(5, 3)
        self.assertEqual(self.level.floor.width, 5)

    def test_should_be_able_to_add_stairs(self):
        with mock.patch.object(self.level.floor, 'place_stairs') as mock_ps:
            self.loader.stairs(1, 2)
            mock_ps.assert_called_once_with(1, 2)

    def test_should_accept_a_function_to_apply_to_new_unit(self):
        def some_function(unit):
            unit._health = 20
            unit.take_damage(15)

        unit = self.loader.unit('unit_base', 1, 2, "north", func=some_function)
        self.assertEqual(unit.__class__.__name__, "UnitBase")
        self.assertTrue(unit.position.at(1, 2))
        self.assertEqual(unit.health, 5)

    @unittest.skip
    def test_should_be_able_to_add_multi_word_units(self):
        self.loader.unit('thick_sludge')

    def test_should_build_warrior_from_profile(self):
        def some_function(unit):
            unit.take_damage(1)
        self.loader.warrior(1, 2, func=some_function)

    def test_should_be_able_to_set_time_bonus(self):
        self.loader.time_bonus(100)
        self.assertEqual(self.level.time_bonus, 100)

    def test_should_be_able_to_set_ace_score(self):
        self.loader.ace_score(100)
        self.assertEqual(self.level.ace_score, 100)
