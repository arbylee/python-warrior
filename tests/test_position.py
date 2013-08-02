import unittest
from pythonwarrior.units.base import UnitBase
from pythonwarrior.floor import Floor
from pythonwarrior.position import Position

class TestPosition(unittest.TestCase):
    def setUp(self):
        self.unit = UnitBase()
        self.floor = Floor()
        self.floor.width = 6
        self.floor.height = 5
        self.floor.add(self.unit, 1, 2, "north")
        self.position = self.unit.position

    def test_at_should_be_true_if_position_matches_x_and_y(self):
        self.assertTrue(self.position.at(1, 2))
