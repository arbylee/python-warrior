import mock
import os
import unittest
from pythonwarrior.level import Level
from pythonwarrior.profile import Profile
from pythonwarrior.floor import Floor
from pythonwarrior.units.warrior import Warrior

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.profile = Profile()
        self.floor = Floor()
        self.level = Level(self.profile, 1)
        self.level.floor = self.floor
        #stub failed

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
        with mock.patch.object(self.level, 'load_path', return_value='path/to/level.py'):
            mock_file = mock.Mock(read=mock.Mock(return_value="description('foo')"))
            with mock.patch('__builtin__.open',
                            return_value=mock_file):
                self.level.load_level()
                self.assertEqual(self.level.description, 'foo')

    def test_should_have_a_player_path_from_profile(self):
        with mock.patch.object(self.profile, '_player_path', 'path/to/player'):
            self.assertEqual(self.level.player_path(), 'path/to/player')

    def test_should_have_a_load_path_from_profile_tower_with_level_number_in_it(self):
        with mock.patch.object(self.profile, 'tower_path', 'path/to/tower'):
            self.assertEqual(self.level.load_path(),
                             os.path.abspath('pythonwarrior/towers/tower/level_001.py'))

    @unittest.skip
    def test_should_exist_if_file_exists(self):
        self.assertTrue(False)

    @unittest.skip
    def test_should_load_player_and_player_path(self):
        self.level

    @unittest.skip
    def test_should_generate_player_files(self):
        self.level

    def test_should_setup_warrior_with_profile_abilities(self):
        self.profile.abilities = ['foo', 'bar']
        warrior = mock.Mock()
        self.level.setup_warrior(warrior)
        warrior.add_abilities.assert_called_once_with('foo', 'bar')

    def test_should_setup_warrior_with_profile_name(self):
        self.profile.warrior_name = "Joe"
        warrior = mock.Mock()
        self.level.setup_warrior(warrior)
        self.assertEqual(warrior.name, "Joe")

