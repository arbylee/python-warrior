import unittest

from pythonwarrior.units.wizard import Wizard


class TestWizard(unittest.TestCase):
    def setUp(self):
        self.wizard = Wizard()

    def test_should_have_look_and_shoot_abilities(self):
        self.assertEqual({'shoot_', 'look'}, set(self.wizard.abilities.keys()))

    def test_should_have_shoot_power_of_11(self):
        self.assertEqual(11, self.wizard.shoot_power)

    def test_should_have_3_max_health(self):
        self.assertEqual(3, self.wizard.max_health)

    def test_should_appear_as_w_on_map(self):
        self.assertEqual('w', self.wizard.character)
