import mock
import unittest

from pythonwarrior.abilities.pivot import Pivot


class TestPivot(unittest.TestCase):
    def setUp(self):
        self.position = mock.Mock()
        mock_unit = mock.Mock(position=self.position)
        self.pivot = Pivot(mock_unit)

    def test_should_flip_around_when_not_passing_arguments(self):
        self.pivot.perform()
        self.position.rotate.assert_called_once_with(2)

    def test_should_rotate_1_when_pivoting_right(self):
        self.pivot.perform('right')
        self.position.rotate.assert_called_once_with(1)
