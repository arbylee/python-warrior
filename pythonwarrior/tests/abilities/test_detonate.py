import mock
import unittest

from pythonwarrior.abilities.detonate import Detonate
from pythonwarrior.floor import Floor
from pythonwarrior.units.base import UnitBase
from pythonwarrior.units.warrior import Warrior


class TestDetonate(unittest.TestCase):
    def setUp(self):
        self.floor = Floor()
        self.floor.width = 4
        self.floor.height = 3
        self.warrior = Warrior()
        self.warrior._health = 20
        self.detonate = Detonate(self.warrior)

        self.target = UnitBase()
        self.target._health = 10

        self.floor.add(self.warrior, 0, 1, 'east')

    def test_should_deal_8_damage_if_forward_1_space(self):
        self.floor.add(self.target, 1, 1)
        self.detonate.perform()
        self.assertEqual(2, self.target._health)

    def test_should_deal_4_damage_if_forward_2_spaces(self):
        self.floor.add(self.target, 2, 1)
        self.detonate.perform()
        self.assertEqual(6, self.target._health)

    def test_should_deal_4_damage_if_diagonal_1_space(self):
        self.floor.add(self.target, 1, 2)
        self.detonate.perform()
        self.assertEqual(6, self.target._health)

        self.floor.add(self.target, 1, 0)
        self.detonate.perform()
        self.assertEqual(2, self.target._health)

    def test_should_deal_4_damage_to_the_user(self):
        self.detonate.perform()
        self.assertEqual(16, self.warrior._health)

    def test_should_cause_ticking_captives_to_explode(self):
        mock_explode = mock.Mock()
        self.target.abilities['explode_'] = mock_explode
        self.floor.add(self.target, 1, 1)
        self.detonate.perform()
        self.assertTrue(mock_explode.perform.called)
