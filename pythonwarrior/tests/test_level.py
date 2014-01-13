import mock
import os
import unittest

from pythonwarrior.floor import Floor
from pythonwarrior.level import Level
from pythonwarrior.profile import Profile
from pythonwarrior.units.warrior import Warrior


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.profile = Profile()
        self.floor = Floor()
        self.level = Level(self.profile, 1)
        self.level.floor = self.floor

    def test_should_consider_passed_When_warrior_is_on_stairs(self):
        self.level.warrior = Warrior()
        self.floor.add(self.level.warrior, 0, 0, 'north')
        self.floor.place_stairs(0, 0)
        self.assertTrue(self.level.is_passed())

    def test_should_default_time_bonus_to_zero(self):
        self.assertEqual(self.level.time_bonus, 0)

    def test_should_have_a_grade_relative_to_ace_score(self):
        self.level.ace_score = 100
        self.assertEqual(self.level.grade_for(110), "S")
        self.assertEqual(self.level.grade_for(100), "S")
        self.assertEqual(self.level.grade_for(99), "A")
        self.assertEqual(self.level.grade_for(89), "B")
        self.assertEqual(self.level.grade_for(79), "C")
        self.assertEqual(self.level.grade_for(69), "D")
        self.assertEqual(self.level.grade_for(59), "F")

    def test_should_have_no_grade_if_there_is_no_ace_score(self):
        self.assertIsNone(self.level.ace_score)
        self.assertIsNone(self.level.grade_for(100))

    def test_should_load_file_contents_into_level(self):
        with mock.patch.object(self.level, 'load_path',
                               return_value='path/to/level.py'):
            mock_file = mock.Mock(
                read=mock.Mock(return_value="level.description('foo')"))
            with mock.patch('__builtin__.open',
                            return_value=mock_file):
                self.level.load_level()
                self.assertEqual(self.level.description, 'foo')

    def test_should_have_a_player_path_from_profile(self):
        with mock.patch.object(self.profile, '_player_path', 'path/to/player'):
            self.assertEqual(self.level.player_path(), 'path/to/player')

    def test_should_have_load_path_from_profile_tower_with_level_number(self):
        with mock.patch.object(self.profile, 'tower_path', 'path/to/tower'):
            self.assertEqual(self.level.load_path(),
                             os.path.abspath(
                                 'pythonwarrior/towers/tower/level_001.py'))

    @mock.patch('pythonwarrior.level.os.path.exists')
    def test_should_exist_if_file_exists(self, mock_exists):
        self.level.load_path = mock.Mock(return_value='/foo/bar')
        mock_exists.return_value = True
        self.assertTrue(self.level.exists())
        mock_exists.assert_called_once_with('/foo/bar')

    @mock.patch('pythonwarrior.level.PlayerGenerator')
    def test_should_generate_player_files(self, mock_pg):
        generator = mock.Mock()
        mock_pg.return_value = generator
        self.level.load_level = mock.Mock()
        self.level.generate_player_files()
        generator.generate.assert_called_once_with()
        self.level.load_level.assert_called_once_with()

    def test_should_setup_warrior_with_profile_abilities(self):
        self.profile.abilities = ['foo', 'bar']
        warrior = mock.Mock()
        self.level.setup_warrior(warrior)
        warrior.add_abilities.assert_called_once_with('foo', 'bar')

    def test_should_setup_warrior_with_profile_name(self):
        self.profile.warrior_name = "Joe"
        warrior = mock.Mock()
        self.level.setup_warrior(warrior)
        self.assertEqual(warrior.name_attr, "Joe")


class TestPlaying(unittest.TestCase):
    def setUp(self):
        self.profile = Profile()
        self.floor = Floor()
        self.level = Level(self.profile, 1)
        self.level.floor = self.floor
        self.level.load_level = mock.Mock()
        self.level.is_failed = mock.Mock(return_value=False)

    def test_load_level_once_when_playing_multiple_turns(self):
        self.level.play(2)
        self.level.load_level.assert_called_once_with()

    def test_prepare_turn_and_play_turn_each_object_specified_amount(self):
        unit = Warrior()
        unit.prepare_turn = mock.Mock()
        unit.perform_turn = mock.Mock()
        self.floor.add(unit, 0, 0, 'north')
        self.level.play(2)
        unit.prepare_turn.assert_called_with()
        unit.perform_turn.assert_called_with()
        self.assertEqual(2, unit.prepare_turn.call_count)
        self.assertEqual(2, unit.perform_turn.call_count)

    def test_should_return_immediately_when_passed(self):
        unit = Warrior()
        unit.turn = mock.Mock()
        self.floor.add(unit, 0, 0, 'north')
        self.level.is_passed = mock.Mock(return_value=True)
        self.level.play(2)

    def test_call_fxn_in_play_for_each_turn(self):
        self.i = 0

        def foo():
            self.i += 1

        self.level.play(2, foo)
        self.assertEqual(self.i, 2)

    def test_should_count_down_time_bonus_once_each_turn(self):
        self.level.time_bonus = 10
        self.level.play(3)
        self.assertEqual(self.level.time_bonus, 7)

    def test_should_count_down_time_bonus_to_zero(self):
        self.level.time_bonus = 2
        self.level.play(5)
        self.assertEqual(self.level.time_bonus, 0)

    def test_should_have_a_pretty_score_calculation(self):
        self.assertEqual(self.level.score_calculation(123, 45),
                         "123 + 45 = 168")

    def test_should_not_have_score_calc_when_starting_score_is_zero(self):
        self.assertEqual(self.level.score_calculation(0, 45), "45")


class TestTallying(unittest.TestCase):
    def setUp(self):
        self.profile = Profile()
        self.floor = Floor()
        self.level = Level(self.profile, 1)
        self.level.floor = self.floor
        self.level.load_level = mock.Mock()
        self.level.is_failed = mock.Mock(return_value=False)
        self.level.floor.other_units = mock.Mock(return_value=[mock.Mock()])
        self.warrior = mock.Mock(score=0, abilities={})
        self.level.warrior = self.warrior

    def test_should_add_warrior_score_to_profile(self):
        self.warrior.score = 30
        self.profile.score = 0
        self.level.tally_points()
        self.assertEqual(self.profile.score, 30)

    def test_should_apply_warrior_abilities_to_profile(self):
        self.warrior.abilities = {'foo': None, 'bar': None}
        self.level.tally_points()
        self.assertEqual(['foo', 'bar'], self.profile.abilities)

    def test_should_apply_time_bonus_to_profile_score(self):
        self.level.time_bonus = 20
        self.level.tally_points()
        self.assertEqual(20, self.profile.score)

    def test_should_give_20_percent_bonus_when_no_other_units_left(self):
        self.level.floor.other_units = mock.Mock(return_value=[])
        self.warrior.score = 10
        self.level.time_bonus = 10
        self.level.tally_points()
        self.assertEqual(24, self.profile.score)
