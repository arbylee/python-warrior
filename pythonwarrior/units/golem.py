from pythonwarrior.units.base import UnitBase

class Golem(UnitBase):
    def __init__(self):
        super(Golem, self).__init__()
        self.turn = None
        self.max_health_attr = None

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, value):
        self._max_health = value


    def play_turn(self, turn):
        if self.turn:
            self.turn(turn)

