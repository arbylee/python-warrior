from pythonwarrior.units.base import UnitBase
class Captive(UnitBase):
    def __init__(self):
        super(Captive, self).__init__()
        self.bind()

    @property
    def max_health(self):
        return 1

    @property
    def character(self):
        return "C"
