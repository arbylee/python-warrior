import unittest
from pythonwarrior.units.base import UnitBase
from pythonwarrior.floor import Floor


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

    def test_should_rotate_clockwise(self):
        self.assertEqual('north', self.position.direction)
        for direction in ['east', 'south', 'west', 'north', 'east']:
            self.position.rotate(1)
            self.assertEqual(direction, self.position.direction)

    def test_should_rotate_counter_clockwise(self):
        self.assertEqual('north', self.position.direction)
        for direction in ['west', 'south', 'east', 'north', 'west']:
            self.position.rotate(-1)
            self.assertEqual(direction, self.position.direction)

    def test_should_get_relative_space_in_front(self):
        unit = UnitBase()
        self.floor.add(unit, 1, 1)
        self.assertFalse(self.position.relative_space(1).is_empty())

    def test_should_get_relative_object_in_front_when_rotated(self):
        unit = UnitBase()
        self.floor.add(unit, 2, 2)
        self.position.rotate(1)
        self.assertFalse(self.position.relative_space(1).is_empty())

    def test_should_get_relative_object_diagonally(self):
        unit = UnitBase()
        self.floor.add(unit, 0, 1)
        self.assertFalse(self.position.relative_space(1, -1).is_empty())

    def test_should_get_relative_object_diagonally_when_rotating(self):
        unit = UnitBase()
        self.floor.add(unit, 0, 1)
        self.position.rotate(2)
        self.assertFalse(self.position.relative_space(-1, 1).is_empty())

    def test_should_move_object_on_floor_relatively(self):
        self.assertEqual(self.unit, self.floor.get(1, 2))
        self.position.move(-1, 2)
        self.assertEqual(None, self.floor.get(1, 2))
        self.assertEqual(self.unit, self.floor.get(3, 3))
        self.position.rotate(1)
        self.position.move(-1)
        self.assertEqual(None, self.floor.get(3, 3))
        self.assertEqual(self.unit, self.floor.get(2, 3))

    def test_should_return_distance_from_stairs_as_0_when_on_stairs(self):
        self.floor.place_stairs(1, 2)
        self.assertEqual(0, self.position.distance_from_stairs())

    def test_should_return_distance_from_stairs_in_both_directions(self):
        self.floor.place_stairs(0, 3)
        self.assertEqual(2, self.position.distance_from_stairs())

    def test_should_return_relative_direction_of_stairs(self):
        self.floor.place_stairs(0, 0)
        self.assertEqual('forward',
                         self.position.relative_direction_of_stairs())

    def test_should_return_relative_direction_of_given_space(self):
        result = self.position.relative_direction_of(self.floor.space(5, 3))
        self.assertEqual('right', result)

    def test_should_be_able_to_determine_relative_direction(self):
        self.assertEqual('forward', self.position.relative_direction('north'))
        self.assertEqual('backward', self.position.relative_direction('south'))
        self.assertEqual('left', self.position.relative_direction('west'))
        self.assertEqual('right', self.position.relative_direction('east'))
        self.position.rotate(1)
        self.assertEqual('left', self.position.relative_direction('north'))
        self.position.rotate(1)
        self.assertEqual('backward', self.position.relative_direction('north'))
        self.position.rotate(1)
        self.assertEqual('right', self.position.relative_direction('north'))

    def test_should_return_a_space_at_the_same_location_as_position(self):
        self.assertEqual([1, 2], self.position.space().location())

    def test_should_return_distance_of_given_space(self):
        self.assertEqual(5, self.position.distance_of(self.floor.space(5, 3)))
        self.assertEqual(3, self.position.distance_of(self.floor.space(4, 2)))
