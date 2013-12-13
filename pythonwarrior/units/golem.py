from pythonwarrior.units.base import UnitBase


class Golem(UnitBase):
    def __init__(self):
        super(Golem, self).__init__()
        self.turn = None
        self.max_health = None

    def play_turn(self, turn):
        if self.turn:
            self.turn(turn)

    @property
    def character(self):
        return "G"

    @property
    def attack_power(self):
        return 3
