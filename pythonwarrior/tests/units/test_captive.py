import unittest
from pythonwarrior.units.captive import Captive


class TestCaptive(unittest.TestCase):
    def setUp(self):
        self.captive = Captive()

    def test_should_have_1_max_health(self):
        self.assertEqual(self.captive.max_health, 1)

    def test_should_appear_as_C_on_map(self):
        self.assertEqual(self.captive.character, "C")

    def test_should_be_bound_by_default(self):
        self.assertTrue(self.captive.is_bound())

    def test_should_not_have_explode_ability_by_default(self):
        self.assertNotIn('explode_', self.captive.abilities)
