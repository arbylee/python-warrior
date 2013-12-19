import unittest

from pythonwarrior.abilities.listen import Listen
from pythonwarrior.floor import Floor
from pythonwarrior.units.base import UnitBase
from pythonwarrior.units.warrior import Warrior


class TestListen(unittest.TestCase):
    def setUp(self):
        self.floor = Floor()
        self.floor.width = 2
        self.floor.height = 3
        self.warrior = Warrior()
        self.floor.add(self.warrior, 0, 0)
        self.listen = Listen(self.warrior)

    def test_should_return_space_with_units_but_not_main_unit(self):
        self.floor.add(UnitBase(), 0, 1)
        self.assertEqual(1, len(self.listen.perform()))
