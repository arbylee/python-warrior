import base64
import os
import pickle
import re

from pythonwarrior.config import Config
from pythonwarrior.level import Level
from pythonwarrior.tower import Tower


class Profile(object):
    def __init__(self):
        self.tower_path = None
        self.warrior_name = None
        self.score = 0
        self.average_grade = None
        self.abilities = []
        self.level_number = 0
        self.last_level_number = None
        self._player_path = None

    def encode(self):
        return base64.b64encode(pickle.dumps(self))

    def save(self):
        f = open(self.player_path + '/.profile', 'w')
        f.write(self.encode())

    @staticmethod
    def decode(encoded_profile):
        return pickle.loads(base64.b64decode(encoded_profile))

    @staticmethod
    def load(path):
        f = open(path)
        player = Profile.decode(f.read())
        player._player_path = os.path.dirname(path)
        return player

    @property
    def player_path(self):
        if self._player_path is None:
            self._player_path = Config.path_prefix + \
                "/pythonwarrior/%s" % self.directory_name()
        return self._player_path

    def directory_name(self):
        return "-".join([re.sub("[^a-z0-9]", "-", self.warrior_name.lower()),
                        self.tower().name()])

    def __repr__(self):
        return " - ".join([self.warrior_name, self.tower().name(),
                           "level %s" % self.level_number,
                           "score %s" % self.score])

    def tower(self):
        return Tower(os.path.basename(self.tower_path))

    def current_level(self):
        return Level(self, self.level_number)

    def next_level(self):
        return Level(self, self.level_number+1)

    def add_abilities(self, *abilities):
        self.abilities += list(set(abilities))

    def enable_normal_mode(self):
        self.average_grade = None
        self.level_number = self.last_level_number
        self.last_level_number = None
