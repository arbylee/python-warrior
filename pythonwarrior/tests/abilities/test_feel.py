import mock
import unittest
from pythonwarrior.abilities.feel import Feel


class TestFeel(unittest.TestCase):
    def setUp(self):
        self.unit = mock.Mock()
        self.unit.say.return_value = None
        self.feel = Feel(self.unit)

    def test_should_get_object_at_position_from_offset(self):
        self.unit.position.relative_space.return_value = [1, 0]
        self.feel.perform('forward')
        self.unit.position.relative_space.assert_called_once_with(1, 0)
