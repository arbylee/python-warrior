import unittest
from pythonwarrior.tower import Tower


class TestTower(unittest.TestCase):
    def setUp(self):
        self.tower = Tower('path/to/tower')

    def test_should_consider_last_part_of_path_as_name(self):
        self.assertEqual(self.tower.name(), 'tower')

    def test_should_use_name_when_converting_to_string(self):
        self.assertEqual(str(self.tower), self.tower.name())
