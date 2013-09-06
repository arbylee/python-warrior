import os
import unittest
from pythonwarrior.player_generator import PlayerGenerator
from pythonwarrior.level import Level
from pythonwarrior.profile import Profile


class TestPlayerGenerator(unittest.TestCase):
    def setUp(self):
        self.level = Level(Profile(), 15)
        self.generator = PlayerGenerator(self.level)

    def test_should_know_templates_path(self):
        expected = os.path.normpath(os.path.dirname(__file__) + '/../pythonwarrior/templates'),
        self.assertEqual(self.generator.templates_path(), expected[0])
