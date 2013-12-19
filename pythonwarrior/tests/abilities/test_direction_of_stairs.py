import mock
import unittest

from pythonwarrior.abilities.direction_of_stairs import DirectionOfStairs


class TestDirectionOfStairs(unittest.TestCase):
    def setUp(self):
        self.position = mock.Mock()
        self.direction = DirectionOfStairs(mock.Mock(position=self.position))

    def test_should_return_relative_direction_of_stairs(self):
        self.position.relative_direction_of_stairs.return_value = 'left'
        self.assertEqual('left', self.direction.perform())
