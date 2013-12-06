import re
from pythonwarrior.abilities.attack import Attack
from pythonwarrior.abilities.explode import Explode
from pythonwarrior.abilities.feel import Feel
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

    @property
    def health(self):
        if not self._health:
            self._health = self.max_health
        return self._health

    def take_damage(self, amount):
        if self.is_bound():
            self.unbind()
        if self.health:
            self._health -= amount
            if self.health <= 0:
                self.position = None
                print "dies"

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
            self.abilities[ability] = eval("%s(self)" % re.sub("_$", "", ability).capitalize())

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
