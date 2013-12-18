import mock
import os
import unittest

from pythonwarrior.game import Game
from pythonwarrior.profile import Profile


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    @mock.patch('os.mkdir')
    @mock.patch('pythonwarrior.game.UI.ask')
    def test_should_make_game_directory_if_player_says_so(self,
                                                          mock_ask,
                                                          mock_mkdir):
        mock_ask.return_value = True
        self.game.make_game_directory()
        mock_mkdir.assert_called_with('./pythonwarrior')

    @mock.patch('os.mkdir')
    @mock.patch('pythonwarrior.game.UI.ask')
    def test_should_not_make_game_and_exit_if_player_says_no(self,
                                                             mock_ask,
                                                             mock_mkdir):
        mock_ask.return_value = False
        self.assertRaises(Exception, self.game.make_game_directory)
        assert not mock_mkdir.called

    @mock.patch('pythonwarrior.game.Profile.load')
    def test_should_load_profiles_for_each_profile_path(self, mock_load):
        mock_load.side_effect = lambda x: {'foo/.profile': 1,
                                           'bar/.profile': 2}[x]
        self.game.profile_paths = mock.Mock(
            return_value=['foo/.profile', 'bar/.profile']
        )
        self.assertEqual(self.game.profiles(), [1, 2])

    @mock.patch('pythonwarrior.game.glob')
    def test_should_find_profile_paths_using_glob_search(self, mock_glob):
        self.game.profile_paths()
        mock_glob.glob.assert_called_with('./pythonwarrior/**/.profile')

    def test_should_try_to_create_profile_when_no_profile_paths(self):
        self.game.profiles = mock.Mock(return_value=[])
        self.game.new_profile = mock.Mock(return_value='profile')
        self.assertEqual(self.game.profile(), 'profile')

    @mock.patch('pythonwarrior.game.UI.choose')
    @mock.patch('pythonwarrior.game.Game.profiles')
    def test_multiple_profiles_available(self, mock_profiles, mock_choose):
        """Should prompt the user for a profile choice, but only once."""
        mock_choose.return_value = 'profile1'
        mock_profiles.return_value = ['profile1']
        self.game.profile()
        self.game.profile()
        mock_choose.assert_called_once_with('profile',
                                            ['profile1',
                                                ['new', 'New Profile']])

    @mock.patch('pythonwarrior.game.UI.choose')
    def test_ask_user_to_choose_a_tower_when_creating_new_profile(self,
                                                                  mock_choose):
        self.game.towers = mock.Mock(return_value=['tower1', 'tower2'])
        mock_choose.return_value = mock.Mock(path='/foo/bar')
        self.game.new_profile()
        mock_choose.assert_called_with('tower', ['tower1', 'tower2'])

    @mock.patch('pythonwarrior.game.UI.choose')
    @mock.patch('pythonwarrior.game.UI.request')
    @mock.patch('pythonwarrior.game.Profile')
    def test_should_pass_name_and_selected_tower_to_profile(self,
                                                            mock_profile_class,
                                                            mock_request,
                                                            mock_choose):
        mock_profile = mock.Mock()
        mock_choose.return_value = mock.Mock(path='tower_path')
        mock_request.return_value = 'name'
        mock_profile_class.return_value = mock_profile
        self.assertEqual(self.game.new_profile(), mock_profile)
        self.assertEqual(mock_profile.tower_path, 'tower_path')
        self.assertEqual(mock_profile.warrior_name, 'name')

    @mock.patch('pythonwarrior.game.Tower')
    def test_load_towers_for_each_tower_path(self, mock_tower_class):
        mock_tower_class.side_effect = lambda x: {'towers/foo': 1,
                                                  'towers/bar': 2}[x]
        self.game.tower_paths = mock.Mock(return_value=['towers/foo',
                                                        'towers/bar'])
        self.assertEqual(self.game.towers(), [1, 2])

    @mock.patch.object(os.path, 'abspath')
    @mock.patch('pythonwarrior.game.glob')
    def test_should_find_tower_paths(self, mock_glob, mock_abspath):
        mock_abspath.return_value = 'foo/foo.py'
        self.game.tower_paths()
        mock_glob.glob.assert_called_with(
            'foo/towers/*')

    def test_should_fetch_current_level_from_profile_and_cache_it(self):
        mock_level = mock.Mock(return_value='foo')
        mock_profile = mock.Mock(current_level=mock_level)
        self.game.profile = mock.Mock(return_value=mock_profile)
        self.game.current_level()
        self.game.current_level()
        mock_level.assert_called_once_with()

    def test_should_fetch_next_level_from_profile_and_cache_it(self):
        mock_level = mock.Mock(return_value='foo')
        mock_profile = mock.Mock(next_level=mock_level)
        self.game.profile = mock.Mock(return_value=mock_profile)
        self.game.next_level()
        self.game.next_level()
        mock_level.assert_called_once_with()
