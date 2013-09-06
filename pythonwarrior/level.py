import os
from pythonwarrior.level_loader import LevelLoader


class Level(object):
    @staticmethod
    def grade_letter(percent):
        if percent >= 1.0:
            return "S"
        elif percent >= 0.9:
            return "A"
        elif percent >= 0.8:
            return "B"
        elif percent >= 0.7:
            return "C"
        elif percent >= 0.6:
            return "D"
        else:
            return "F"

    def __init__(self, profile, number):
        self.profile = profile
        self.number = number
        self.time_bonus = 0
        self.ace_score = None
        self.clue = None

    def player_path(self):
        return self.profile.player_path

    def load_path(self):
        return os.path.join(
            os.path.normpath(os.path.abspath(__file__) + '../../towers'),
            os.path.basename(self.profile.tower_path) +
            "/level_" + str(self.number).rjust(3, '0') +
            '.py'
        )

    def load_level(self):
        level = LevelLoader(self)
        f = open(self.load_path())
        eval("level." + f.read())

    def is_passed(self):
        return self.floor.stairs_space().is_warrior()

    def grade_for(self, score):
        if self.ace_score:
            return Level.grade_letter(score/float(self.ace_score))

    def exists(self):
        return os.path.exists(self.load_path())

    def setup_warrior(self, warrior):
        self.warrior = warrior
        self.warrior.add_abilities(*self.profile.abilities)
        self.warrior.name = self.profile.warrior_name
