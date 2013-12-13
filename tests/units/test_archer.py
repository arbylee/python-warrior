import unittest

from pythonwarrior.units.archer import Archer


class TestArcher(unittest.TestCase):
    def setUp(self):
        self.archer = Archer()

    def test_should_have_look_and_shoot_abilities(self):
        self.assertEqual({'shoot_', 'look'}, set(self.archer.abilities.keys()))

    def test_should_have_shoot_power_of_3(self):
        self.assertEqual(3, self.archer.shoot_power)

    def test_should_have_7_max_health(self):
        self.assertEqual(7, self.archer.max_health)

    def test_should_appear_as_a_on_map(self):
        self.assertEqual('a', self.archer.character)
