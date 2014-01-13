import glob
import os
import sys

from pythonwarrior.level_loader import LevelLoader
from pythonwarrior.player_generator import PlayerGenerator
from pythonwarrior.ui import UI


class Level(object):
    @staticmethod
    def grade_letter(percent):
        if percent >= 1.0:
            return 'S'
        elif percent >= 0.9:
            return 'A'
        elif percent >= 0.8:
            return 'B'
        elif percent >= 0.7:
            return 'C'
        elif percent >= 0.6:
            return 'D'
        else:
            return 'F'

    def __init__(self, profile, number):
        self.profile = profile
        self.number = number
        self.time_bonus = 0
        self.ace_score = None
        self.clue = None
        self.warrior = None
        self.description = None
        self.tip = None
        self.floor = None

    def player_path(self):
        return self.profile.player_path

    def load_path(self):
        return os.path.join(
            os.path.normpath(os.path.abspath(__file__) + '../../towers'),
            os.path.basename(self.profile.tower_path) +
            '/level_' + str(self.number).rjust(3, '0') +
            '.py'
        )

    def load_level(self):
        level = LevelLoader(self)
        f = open(self.load_path())
        exec(f.read())

    def generate_player_files(self):
        self.load_level()
        PlayerGenerator(self, Level(self.profile, self.number-1)).generate()

    def play(self, turns=1000, fxn=None):
        self.load_level()
        for turn in range(turns):
            if self.is_passed() or self.is_failed():
                return
            UI.puts('- turn %d -' % (turn+1))
            UI.write(self.floor.character)
            for unit in self.floor.units:
                unit.prepare_turn()
            for unit in self.floor.units:
                unit.perform_turn()
            if fxn:
                fxn()
            if self.time_bonus > 0:
                self.time_bonus -= 1

    def tally_points(self):
        score = 0

        UI.puts('Level Score: %d' % self.warrior.score)
        score += self.warrior.score

        UI.puts('Time Bonus: %d' % self.time_bonus)
        score += self.time_bonus

        if not self.floor.other_units():
            UI.puts('Clear Bonus: %d' % self.clear_bonus())
            score += self.clear_bonus()

        if self.profile.epic:
            if self.grade_for(score):
                UI.puts('Level Grade: %s' % self.grade_for(score))
            UI.puts('Total Score: %s' %
                    self.score_calculation(self.profile.current_epic_score,
                                           score))
            if self.ace_score:
                grade = (score / float(self.ace_score))
                self.profile.current_epic_grades[self.number] = grade
            self.profile.current_epic_score += score
        else:
            UI.puts('Total Score: %s' %
                    self.score_calculation(self.profile.score, score))
            self.profile.score += score
            self.profile.abilities = self.warrior.abilities.keys()

    def grade_for(self, score):
        if self.ace_score:
            return Level.grade_letter(score/float(self.ace_score))

    def clear_bonus(self):
        return round((self.warrior.score + self.time_bonus) * 0.2)

    def score_calculation(self, current_score, addition):
        if current_score == 0:
            return str(addition)
        else:
            return '%d + %d = %d' % (current_score, addition,
                                     (current_score + addition))

    def is_passed(self):
        return self.floor.stairs_space().is_warrior()

    def is_failed(self):
        return self.warrior not in self.floor.units

    def exists(self):
        return os.path.exists(self.load_path())

    def setup_warrior(self, warrior):
        self.warrior = warrior
        self.warrior.add_abilities(*self.profile.abilities)
        self.warrior.name_attr = self.profile.warrior_name
