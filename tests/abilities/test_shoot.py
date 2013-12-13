import mock
import unittest

from pythonwarrior.abilities.shoot import Shoot


class TestShoot(unittest.TestCase):
    def setUp(self):
        mock_shooter = mock.Mock(shoot_power=2)
        mock_shooter.say.return_value = None
        self.shooter = mock_shooter
        self.shoot = Shoot(self.shooter)

    def test_should_shoot_only_first_unit(self):
        receiver = mock.Mock()
        receiver.is_alive.return_value = True
        receiver.say.return_value = None
        other = mock.Mock()
        self.shoot.multi_unit = mock.Mock()
        self.shoot.multi_unit.return_value = [None, receiver, other, None]

        self.shoot.perform()

        self.shoot.multi_unit.assert_called_once_with('forward', mock.ANY)
        receiver.take_damage.assert_called_once_with(2)
        assert not other.take_damage.called

    def test_should_shoot_and_do_nothing_if_no_units_in_the_way(self):
        self.shoot.multi_unit = mock.Mock(return_value=[None, None])
        self.shoot.perform()

        self.shoot.multi_unit.assert_called_once_with('forward', mock.ANY)
