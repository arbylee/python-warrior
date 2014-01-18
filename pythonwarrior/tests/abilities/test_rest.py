import mock
import unittest

from pythonwarrior.abilities.rest import Rest
from pythonwarrior.units.warrior import Warrior


class TestRest(unittest.TestCase):
    def setUp(self):
        self.warrior = Warrior()
        self.rest = Rest(self.warrior)

    def test_should_give_10_percent_health_back(self):
        self.warrior.max_health = 20
        self.warrior._health = 10
        self.rest.perform()
        self.assertEqual(12, self.warrior.health)

    def test_should_not_add_health_when_at_max(self):
        self.warrior.max_health = 20
        self._health = 20
        self.rest.perform()
        self.assertEqual(20, self.warrior.health)

    def test_should_not_go_over_max_health(self):
        self.warrior.max_health = 20
        self._health = 19
        self.rest.perform()
        self.assertEqual(20, self.warrior.health)

    def test_should_say_something_if_at_full_health(self):
        self.warrior.max_health = 20
        self.warrior.say = mock.Mock()
        self._health = 20
        self.rest.perform()
        self.assertTrue(self.warrior.say.called)
