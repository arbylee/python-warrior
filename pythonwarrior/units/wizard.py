from pythonwarrior.units.base import UnitBase


class Wizard(UnitBase):
    def __init__(self):
        super(Wizard, self).__init__()
        self.max_health = 3
        self.add_abilities('shoot_', 'look')

    def play_turn(self, turn):
        for direction in ['forward', 'left', 'right']:
            for space in turn.look(direction):
                if space.is_player():
                    turn.shoot_(direction)
                    return
                elif not space.is_empty():
                    break

    @property
    def shoot_power(self):
        return 11

    @property
    def character(self):
        return "w"
