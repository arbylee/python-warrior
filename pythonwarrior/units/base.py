import re
from pythonwarrior.abilities.walk import Walk
from pythonwarrior.turn import Turn
class UnitBase(object):
    def __init__(self):
        self.position = None
        self.health_attr = None
        self.abilities_attr = None
        self.bound = False

    @property
    def abilities(self):
        if not self.abilities_attr:
            self.abilities_attr = {}
        return self.abilities_attr

    @property
    def max_health(self):
        return 0

    def __repr__(self):
        return self.__class__.__name__

    def attack_power(self):
        return 0

    def is_alive(self):
        return self.position != None

    def health(self):
        if not self.health_attr:
            self.health_attr = self.max_health
        return self.health_attr

    def take_damage(self, amount):
        if self.is_bound():
            self.unbind()
        if self.health():
            self.health_attr -= amount
            if self.health() <= 0:
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
        print msg

    def character(self):
        return "?"

    def bind(self):
        self.bound = True

    def is_bound(self):
        return self.bound

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
                print "PERFORMIING"
                print name
                print args
                print self.abilities[name]
                self.abilities[name].perform(*args)
