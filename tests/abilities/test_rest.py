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
        self.assertEquals(12, self.warrior.health)

    def test_should_add_health_what_at_max(self):
        self.warrior.max_health = 20
        self._health = 20
        self.rest.perform()
        self.assertEquals(20, self.warrior.health)

    def test_should_not_go_over_max_health(self):
        self.warrior.max_health = 20
        self._health = 19
        self.rest.perform()
        self.assertEquals(20, self.warrior.health)
