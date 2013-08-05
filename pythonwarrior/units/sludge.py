from pythonwarrior.units.base import UnitBase
class Sludge(UnitBase):
    def __init__(self):
        super(Sludge, self).__init__()
        self.add_abilities('attack_', 'feel')

    def __repr__(self):
        return self.name()

    @property
    def attack_power(self):
        return 3

    @property
    def max_health(self):
        return 12

    @property
    def character(self):
        return "s"
