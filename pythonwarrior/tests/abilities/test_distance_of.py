import mock
import unittest

from pythonwarrior.abilities.distance_of import DistanceOf


class TestDistanceOf(unittest.TestCase):
    def setUp(self):
        self.position = mock.Mock()
        self.distance = DistanceOf(mock.Mock(position=self.position))

    def test_should_return_distance_from_stairs(self):
        self.position.distance_of.return_value = 5
        self.assertEqual(5, self.distance.perform('space'))
        self.position.distance_of.assert_called_once_with('space')
