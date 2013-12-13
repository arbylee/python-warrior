import mock
import unittest

from pythonwarrior.abilities.attack import Attack
from pythonwarrior.units.base import UnitBase


class TestAttack(unittest.TestCase):
    def setUp(self):
        self.attacker = mock.Mock(position=mock.Mock(),
                                  attack_power=3,
                                  say=lambda x: x)
        self.attack = Attack(self.attacker)

    @mock.patch('pythonwarrior.abilities.attack.Attack.unit')
    def test_should_subtract_attack_power_amount_from_health(self, mock_unit):
        receiver = UnitBase()
        receiver.position = mock.Mock()
        receiver._health = 5
        mock_unit.return_value = receiver
        self.attack.perform()
        self.assertEqual(receiver.health, 2)

    def test_should_do_nothing_if_recipient_is_None(self):
        return None
