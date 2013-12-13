from pythonwarrior.floor import Floor

# These are used dynamically via unit_to_constant
from pythonwarrior.units.archer import Archer
from pythonwarrior.units.captive import Captive
from pythonwarrior.units.golem import Golem
from pythonwarrior.units.sludge import Sludge
from pythonwarrior.units.thick_sludge import ThickSludge
from pythonwarrior.units.wizard import Wizard

from pythonwarrior.units.base import UnitBase
from pythonwarrior.units.warrior import Warrior


class LevelLoader(object):
    def __init__(self, level):
        self.floor = Floor()
        self.level = level
        self.level.floor = self.floor

    def description(self, desc):
        self.level.description = desc

    def tip(self, level_tip):
        self.level.tip = level_tip

    def clue(self, level_clue):
        self.level.clue = level_clue

    def time_bonus(self, bonus):
        self.level.time_bonus = bonus

    def ace_score(self, score):
        self.level.ace_score = score

    def size(self, width, height):
        self.floor.width = width
        self.floor.height = height

    def stairs(self, x, y):
        self.floor.place_stairs(x, y)

    def unit(self, a_unit, x, y, facing="north", func=None):
        if not isinstance(a_unit, UnitBase):
            a_unit = self._unit_to_constant(a_unit)()

        self.floor.add(a_unit, x, y, facing)
        if func:
            func(a_unit)
        return a_unit

    def warrior(self, *args, **kwargs):
        a_func = kwargs.get('func', None)
        warrior = Warrior(self.level)
        return self.level.setup_warrior(self.unit(warrior, *args, func=a_func))

    @staticmethod
    def _unit_to_constant(name):
        camel = "".join(map(lambda x: x.capitalize(), str(name).split('_')))
        return eval(camel)
