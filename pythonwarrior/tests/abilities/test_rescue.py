import mock
import unittest

from pythonwarrior.abilities.rescue import Rescue
from pythonwarrior.units.captive import Captive
from pythonwarrior.units.warrior import Warrior


class TestRescue(unittest.TestCase):
    def setUp(self):
        self.warrior = Warrior()
        self.rescue = Rescue(self.warrior)

    def test_should_rescue_captive(self):
        captive = Captive()
        captive.position = mock.Mock()
        mock_space = mock.Mock()
        mock_space.is_captive.return_value = True
        self.rescue.space = mock.Mock(return_value=mock_space)
        self.rescue.unit = mock.Mock(return_value=captive)
        self.warrior.earn_points = mock.Mock()

        self.rescue.perform()

        self.assertEqual(None, captive.position)
        self.warrior.earn_points.assert_called_once_with(20)
