import unittest
from pythonwarrior.units.base import UnitBase
from pythonwarrior.units.warrior import Warrior
from pythonwarrior.floor import Floor


class TestFloorTwoByThree(unittest.TestCase):
    def setUp(self):
        self.floor = Floor()
        self.floor.width = 2
        self.floor.height = 3

    def test_should_be_able_to_add_and_fetch_a_unit(self):
        unit = UnitBase()
        self.floor.add(unit, 0, 1, "north")
        self.assertEqual(self.floor.get(0, 1), unit)

    def test_should_not_consider_unit_on_floor_if_no_position(self):
        unit = UnitBase()
        self.floor.add(unit, 0, 1, "north")
        unit.position = None
        self.assertEqual(self.floor.units, [])

    def test_should_fetch_other_units_not_warrior(self):
        unit = UnitBase()
        warrior = Warrior()
        self.floor.add(unit, 0, 0, 'north')
        self.floor.add(warrior, 1, 0, 'north')
        self.assertNotIn(warrior, self.floor.other_units())
        self.assertIn(unit, self.floor.other_units())

    def test_should_not_consider_corner_out_of_bounds(self):
        self.assertFalse(self.floor.out_of_bounds(0, 0))
        self.assertFalse(self.floor.out_of_bounds(1, 0))
        self.assertFalse(self.floor.out_of_bounds(1, 2))
        self.assertFalse(self.floor.out_of_bounds(0, 2))

    def test_should_consider_corner_out_of_bounds_when_beyond_sides(self):
        self.assertTrue(self.floor.out_of_bounds(-1, 0))
        self.assertTrue(self.floor.out_of_bounds(0, -1))
        self.assertTrue(self.floor.out_of_bounds(0, 3))
        self.assertTrue(self.floor.out_of_bounds(2, 0))

    def test_should_return_space_at_specified_location(self):
        self.assertEqual(self.floor.space(0, 0).__class__.__name__, 'Space')

    def test_should_place_stairs_and_be_able_to_fetch_the_location(self):
        self.floor.place_stairs(1, 2)
        self.assertEqual(self.floor.stairs_location, [1, 2])


class TestFloorThreeByOne(unittest.TestCase):
    def setUp(self):
        self.floor = Floor()
        self.floor.width = 3
        self.floor.height = 1

    def test_should_print_map_with_stairs_and_unit(self):
        self.floor.add(Warrior(), 0, 0)
        self.floor.place_stairs(2, 0)
        self.assertEqual(self.floor.character, ''' ---
|@ >|
 ---
''')

    def test_should_return_unique_units(self):
        u1 = UnitBase()
        self.floor.add(u1, 0, 0)
        self.floor.add(UnitBase(), 1, 0)
        self.assertEqual(self.floor.unique_units, [u1])

if __name__ == '__main__':
    unittest.main()
