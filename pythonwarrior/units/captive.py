from pythonwarrior.units.base import UnitBase


class Captive(UnitBase):
    def __init__(self):
        super(Captive, self).__init__()
        self.bind()
        self.max_health = 1

    @property
    def character(self):
        return "C"
