from pythonwarrior.units.base import UnitBase


class Archer(UnitBase):
    def __init__(self):
        super(Archer, self).__init__()
        self.max_health = 7
        self.add_abilities('shoot_', 'look')

    @property
    def shoot_power(self):
        return 3

    @property
    def character(self):
        return 'a'

    def play_turn(self, turn):
        for direction in ['forward', 'left', 'right']:
            for space in turn.look(direction):
                if space.is_player():
                    turn.shoot_(direction)
                    return
                elif not space.is_empty():
                    break
