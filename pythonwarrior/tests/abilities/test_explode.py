import unittest
from pythonwarrior.abilities.explode import Explode
from pythonwarrior.floor import Floor
from pythonwarrior.units.captive import Captive
from pythonwarrior.units.base import UnitBase


class TestExplode(unittest.TestCase):
    def setUp(self):
        self.floor = Floor()
        self.floor.width = 2
        self.floor.height = 3
        self.captive = Captive()
        self.floor.add(self.captive, 0, 0)
        self.explode = Explode(self.captive)

    def test_should_subtract_100_health_from_each_unit_on_the_floor(self):
        unit = UnitBase()
        unit._health = 20
        self.floor.add(unit, 0, 1)
        self.captive._health = 10
        self.explode.perform()
        self.assertEqual(self.captive.health, -90)
        self.assertEqual(unit.health, -80)

    def test_should_explode_when_bomb_time_reaches_zero(self):
        self.captive._health = 10
        self.explode.time = 3
        self.explode.pass_turn()
        self.explode.pass_turn()
        self.assertEqual(self.captive.health, 10)
        self.explode.pass_turn()
        self.assertEqual(self.captive.health, -90)
