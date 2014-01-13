import mock
import unittest
from pythonwarrior.abilities.walk import Walk


class TestWalk(unittest.TestCase):
    def setUp(self):
        self.space = mock.Mock()
        self.space.is_empty.return_value = True
        self.space.unit.return_value = None
        self.position = mock.Mock()
        self.position.relative_space.return_value = self.space
        self.position.move.return_Value = None
        unit = mock.Mock(position=self.position)
        unit.say.return_value = None
        self.walk = Walk(unit)

    def test_should_move_position_forward_when_calling_perform(self):
        self.walk.perform()
        self.position.move.assert_called_once_with(1, 0)

    def test_should_move_position_right_if_that_is_direction(self):
        self.walk.perform("right")
        self.position.move.assert_called_once_with(0, 1)

    def test_should_keep_position_if_something_is_in_the_way(self):
        self.position.move.side_effect = Exception("Boom!")
        self.space.is_empty.return_value = False
        self.walk.perform("right")
