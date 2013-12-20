import mock
import unittest

from pythonwarrior.abilities.direction_of import DirectionOf


class TestDirectionOf(unittest.TestCase):
    def setUp(self):
        self.position = mock.Mock()
        self.direction_of = DirectionOf(mock.Mock(position=self.position))

    def test_should_return_relative_direction_of_given_space(self):
        self.position.relative_direction_of.return_value = 'left'
        self.assertEqual('left', self.direction_of.perform('space'))
        self.position.relative_direction_of.assert_called_once_with('space')
