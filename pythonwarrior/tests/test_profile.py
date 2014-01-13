import base64
import mock
import pickle
import unittest
from pythonwarrior.profile import Profile


class TestProfile(unittest.TestCase):
    def setUp(self):
        self.profile = Profile()

    def test_should_have_warrior_name(self):
        self.profile.warrior_name = "Joe"
        self.assertEqual(self.profile.warrior_name, "Joe")

    def test_should_start_level_number_at_0(self):
        self.assertEqual(self.profile.level_number, 0)

    def test_should_start_score_at_0_and_allow_it_to_increment(self):
        self.assertEqual(self.profile.score, 0)
        self.profile.score += 5
        self.assertEqual(self.profile.score, 5)

    def test_should_have_no_abilities_and_allow_adding(self):
        self.assertEqual(self.profile.abilities, [])
        self.profile.abilities += ['foo', 'bar']
        self.assertEqual(self.profile.abilities, ['foo', 'bar'])

    def test_should_encode_with_pickle_and_base64(self):
        self.assertEqual(self.profile.encode(),
                         base64.b64encode(pickle.dumps(self.profile)))

    def test_should_decode_with_pickle_and_base64(self):
        self.assertEqual(Profile.decode(self.profile.encode()).warrior_name,
                         self.profile.warrior_name)

    @mock.patch('__builtin__.open')
    def test_load_should_read_file_decode_and_set_player_path(self, mock_open):
        profile = mock.Mock()
        mock_open.read.return_value = "encoded_profile"
        with mock.patch('pythonwarrior.profile.Profile.decode',
                        return_value=profile):
            self.assertEqual(Profile.load('path/to/.profile'), profile)
            mock_open.assert_called_once_with("path/to/.profile")

    def test_should_add_abilities_and_remove_duplicates(self):
        self.profile.add_abilities('foo', 'bar', 'blah', 'bar')
        self.assertItemsEqual(self.profile.abilities, ['foo', 'bar', 'blah'])

    def test_should_fetch_new_level_with_current_number(self):
        self.profile.level_number = 1
        self.assertEqual(self.profile.current_level().number, 1)

    def test_should_fetch_next_level(self):
        self.profile.level_number = 1
        self.assertEqual(self.profile.next_level().number, 2)

    def test_should_enable_epic_mode_and_reset_scores_if_none(self):
        self.profile.enable_epic_mode()
        self.assertTrue(self.profile.epic)
        self.assertEqual(0, self.profile.epic_score)
        self.assertEqual(0, self.profile.current_epic_score)

    def test_should_override_epic_score_with_current_one_if_it_is_higher(self):
        self.profile.enable_epic_mode()
        self.assertEqual(0, self.profile.epic_score)
        self.assertEqual(None, self.profile.average_grade)
        self.profile.current_epic_score = 123
        self.profile.current_epic_grades = {1: 0.7, 2: 0.9}
        self.profile.update_epic_score()
        self.assertEqual(123, self.profile.epic_score)
        self.assertEqual(0.8, self.profile.average_grade)

    def test_should_not_override_epic_score_with_current_one_if_lower(self):
        self.profile.enable_epic_mode()
        self.profile.epic_score = 124
        self.profile.average_grade = 0.9
        self.profile.current_epic_score = 123
        self.profile.current_epic_grades = {1: 0.7, 2: 0.9}
        self.profile.update_epic_score()
        self.assertEqual(124, self.profile.epic_score)
        self.assertEqual(0.9, self.profile.average_grade)

    def test_should_not_calculate_average_grade_if_no_grades_are_present(self):
        self.profile.enable_epic_mode()
        self.profile.current_epic_grades = {}
        self.assertIsNone(self.profile.calculate_average_grade())


class TestProfileWithTowerPath(unittest.TestCase):
    def setUp(self):
        self.profile = Profile()
        self.profile.warrior_name = "John Smith"
        self.profile.tower_path = "path/to/tower"

    def test_save_should_write_file_with_encoded_profile(self):
        with mock.patch('__builtin__.open') as mock_open:
            with mock.patch.object(self.profile, 'encode',
                                   return_value='encoded_profile'):
                f = mock.Mock()
                mock_open.return_value = f
                self.profile.save()
                f.write.assert_called_once_with('encoded_profile')
                mock_open.assert_called_once_with(self.profile._player_path +
                                                  '/.profile', 'w')

    def test_should_have_a_nice_string_representation(self):
        self.profile.warrior_name = "Joe"
        self.assertEqual(str(self.profile), "Joe - tower - level 0 - score 0")

    def test_should_guess_at_the_player_path(self):
        self.assertEqual(self.profile.player_path,
                         './pythonwarrior/john-smith-tower')

    def test_should_use_specified_player_path(self):
        self.profile._player_path = "path/to/player"
        self.assertEqual(self.profile.player_path, "path/to/player")

    def test_should_load_tower_from_path(self):
        with mock.patch('pythonwarrior.profile.Tower') as mock_tower:
            tower = mock.Mock()
            mock_tower.return_value = tower
            self.assertEqual(self.profile.tower(), tower)
