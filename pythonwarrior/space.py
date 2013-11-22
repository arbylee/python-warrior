class Space(object):
    def __init__(self, floor, x, y):
        self.floor = floor
        self.x = x
        self.y = y

    def __repr__(self):
        if self.unit:
            return str(self.unit)
        elif self.is_wall():
            return 'wall'
        else:
            return 'nothing'

    def is_wall(self):
        return self.floor.out_of_bounds(self.x, self.y)

    def is_warrior(self):
        return self.unit.__class__.__name__ == "Warrior"

    def is_golem(self):
        return self.unit.__class__.__name__ == "Golem"

    def is_player(self):
        return self.is_warrior() or self.is_golem()

    def is_enemy(self):
        return self.unit and not self.is_player() and not self.is_captive()

    def is_captive(self):
        return self.unit and self.unit.is_bound()

    def is_empty(self):
        return self.unit is None and not self.is_wall()

    def is_stairs(self):
        return self.floor.stairs_location == self.location()

    def is_ticking(self):
        return self.unit and 'explode_' in self.unit.abilities

    @property
    def unit(self):
        return self.floor.get(self.x, self.y)

    def location(self):
        return [self.x, self.y]

    @property
    def character(self):
        if self.unit:
            return self.unit.character
        elif self.is_stairs():
            return ">"
        else:
            return " "
