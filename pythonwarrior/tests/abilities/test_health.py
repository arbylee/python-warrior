import unittest

from pythonwarrior.units.warrior import Warrior
from pythonwarrior.abilities.health import Health


class TestHealth(unittest.TestCase):
    def setUp(self):
        self.warrior = Warrior()
        self.health = Health(self.warrior)

    def test_should_return_the_amount_of_health(self):
        self.warrior.health = 10
        self.assertEqual(10, self.health.perform())
