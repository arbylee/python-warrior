import re

from pythonwarrior.abilities.attack import Attack
from pythonwarrior.abilities.bind import Bind
from pythonwarrior.abilities.detonate import Detonate
from pythonwarrior.abilities.direction_of import DirectionOf
from pythonwarrior.abilities.direction_of_stairs import DirectionOfStairs
from pythonwarrior.abilities.distance_of import DistanceOf
from pythonwarrior.abilities.explode import Explode
from pythonwarrior.abilities.feel import Feel
from pythonwarrior.abilities.health import Health
from pythonwarrior.abilities.listen import Listen
from pythonwarrior.abilities.look import Look
from pythonwarrior.abilities.pivot import Pivot
from pythonwarrior.abilities.rescue import Rescue
from pythonwarrior.abilities.rest import Rest
from pythonwarrior.abilities.shoot import Shoot
from pythonwarrior.abilities.walk import Walk
from pythonwarrior.turn import Turn
from pythonwarrior.ui import UI


class UnitBase(object):
    def __init__(self):
        self.position = None
        self._health = None
        self.abilities_attr = None
        self.bound = False
        self.max_health = 0

    @property
    def abilities(self):
        if not self.abilities_attr:
            self.abilities_attr = {}
        return self.abilities_attr

    def __repr__(self):
        return self.name()

    @property
    def attack_power(self):
        return 0

    def is_alive(self):
        return self.position is not None

    def earn_points(self, points):
        pass

    @property
    def health(self):
        if self._health is None:
            self._health = self.max_health
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

    def take_damage(self, amount):
        if self.is_bound():
            self.unbind()
        if self.health:
            self._health -= amount
            self.say("takes %(amount)d damage, "
                     "%(health)d health power left" %
                     {'amount': amount, 'health': self.health})
            if self.health <= 0:
                self.position = None
                self.say("dies")

    def name(self):
        return self.__class__.__name__

    def prepare_turn(self):
        self.current_turn = self.next_turn()
        self.play_turn(self.current_turn)

    def next_turn(self):
        return Turn(self.abilities)

    def play_turn(self, turn):
        return None

    def is_bound(self):
        return self.bound

    def add_abilities(self, *new_abilities):
        for ability in new_abilities:
            class_name = re.sub("_", "", ability.title())
            self.abilities[ability] = eval("%s(self)" % class_name)

    def say(self, msg):
        UI.puts_with_delay("%(name)s %(msg)s" % {'name': self.name(),
                                                 'msg': msg})

    @property
    def character(self):
        return "?"

    def bind(self):
        self.bound = True

    def unbind(self):
        self.say("released from bonds")
        self.bound = False

    def perform_turn(self):
        if self.position:
            for ability in self.abilities.values():
                ability.pass_turn()
            if self.current_turn.action and not self.is_bound():
                name = self.current_turn.action[0]
                args = self.current_turn.action[1:]
                self.abilities[name].perform(*args)
