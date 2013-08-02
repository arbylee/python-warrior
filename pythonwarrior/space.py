class Space(object):
    def __init__(self, floor, x, y):
        self.floor = floor
        self.x = x
        self.y = y

    def __repr__(self):
        if self.is_wall():
            return 'wall'
        else:
            return 'nothing'

    def is_enemy(self):
        return self.unit() and not self.is_player() and not self.is_captive()

    def is_player(self):
        return self.is_warrior() or self.is_golem()

    def is_captive(self):
        return self.unit() and self.unit.is_bound()

    def is_warrior(self):
        return self.unit().__class__.__name__ == "Warrior"

    def is_golem(self):
        return self.unit().__class__.__name__ == "Golem"

    def is_empty(self):
        return self.unit() == None and not self.is_wall()

    def is_wall(self):
        return self.floor.out_of_bounds(self.x, self.y)

    def is_stairs(self):
        return self.floor.stairs_location == self.location()

    def location(self):
        return [self.x, self.y]

    def unit(self):
        return self.floor.get(self.x, self.y)
