import mock
import unittest

from pythonwarrior.units.golem import Golem


class TestGolem(unittest.TestCase):
    def setUp(self):
        self.golem = Golem()

    def test_should_execute_turn_proc_when_playing_turn(self):
        proc = mock.Mock()
        self.golem.turn = proc
        self.golem.play_turn('turn')
        proc.assert_called_once_with('turn')

    def test_should_set_max_health_and_update_current_health(self):
        self.golem.max_health = 10
        self.assertEqual(self.golem.max_health, 10)
        self.assertEqual(self.golem.health, 10)

    def test_should_have_attack_power_of_3(self):
        self.assertEqual(self.golem.attack_power, 3)

    def test_should_appear_as_G_on_map(self):
        self.assertEqual(self.golem.character, 'G')
