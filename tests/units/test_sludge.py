import unittest

from pythonwarrior.units.sludge import Sludge


class TestSludge(unittest.TestCase):
    def setUp(self):
        self.sludge = Sludge()

    def test_should_have_attack_action(self):
        self.assertIn('attack_', self.sludge.abilities.keys())

    def test_should_have_feel_sense(self):
        self.assertIn('feel', self.sludge.abilities.keys())

    def test_should_have_attack_of_3(self):
        self.assertEqual(self.sludge.attack_power, 3)

    def test_should_have_12_max_health(self):
        self.assertEqual(self.sludge.max_health, 12)

    def test_should_appear_as_s_on_map(self):
        self.assertEqual(self.sludge.character, "s")
