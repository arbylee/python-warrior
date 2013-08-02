from pythonwarrior.position import Position
from pythonwarrior.space import Space
class Floor(object):
    def __init__(self):
        self.width = 0
        self.height = 0
        self.units_attr = []
        self.stairs_location = [-1, -1]

    def add(self, unit, x, y, direction=None):
        self.units_attr.append(unit)
        unit.position = Position(self, x, y, direction)

    def get(self, x, y):
        for unit in self.units_attr:
            if unit.position.at(x, y):
                return unit

    def units(self):
        return filter(lambda unit: unit.position != None, self.units_attr)

    def out_of_bounds(self, x, y):
        return x < 0 or y < 0 or x > self.width-1 or y > self.height-1

    def space(self, x, y):
        return Space(self, x, y)

    def place_stairs(self, x, y):
        self.stairs_location = [x, y]
