from pythonwarrior.units.base import UnitBase


class Sludge(UnitBase):
    def __init__(self):
        super(Sludge, self).__init__()
        self.add_abilities('attack_', 'feel')
        self.max_health = 12

    def __repr__(self):
        return self.name()

    @property
    def attack_power(self):
        return 3

    @property
    def character(self):
        return "s"

    def play_turn(self, turn):
        for direction in ['forward', 'left', 'right', 'backward']:
            if turn.feel(direction).is_player():
                turn.attack_(direction)
                return
