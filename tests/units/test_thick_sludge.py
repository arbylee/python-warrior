import unittest

from pythonwarrior.units.thick_sludge import ThickSludge


class TestThickSludge(unittest.TestCase):
    def setUp(self):
        self.sludge = ThickSludge()

    def test_should_have_24_max_health(self):
        self.assertEqual(24, self.sludge.max_health)

    def test_should_appear_as_S_on_map(self):
        self.assertEqual("S", self.sludge.character)

    def test_should_have_the_name_Thick_Sludge(self):
        self.assertEqual("ThickSludge", self.sludge.name())
