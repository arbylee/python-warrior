from pythonwarrior.position import Position
from pythonwarrior.space import Space


class Floor(object):
    def __init__(self):
        self.width = 0
        self.height = 0
        self._units = []
        self.stairs_location = [-1, -1]

    def add(self, unit, x, y, direction=None):
        self._units.append(unit)
        unit.position = Position(self, x, y, direction)

    def place_stairs(self, x, y):
        self.stairs_location = [x, y]

    def stairs_space(self):
        return self.space(*self.stairs_location)

    @property
    def units(self):
        return filter(lambda unit: unit.position is not None, self._units)

    def other_units(self):
        return filter(lambda unit: unit.__class__.__name__ != 'Warrior',
                      self.units)

    def get(self, x, y):
        for unit in self.units:
            if unit.position.at(x, y):
                return unit

    def space(self, x, y):
        return Space(self, x, y)

    def out_of_bounds(self, x, y):
        return x < 0 or y < 0 or x > self.width-1 or y > self.height-1

    @property
    def character(self):
        rows = []
        rows.append(" " + ("-" * self.width))
        for y in range(self.height):
            row = "|"
            for x in range(self.width):
                row += self.space(x, y).character
            row += "|"
            rows.append(row)
        rows.append(" " + ("-" * self.width))
        return "\n".join(rows) + "\n"

    @property
    def unique_units(self):
        uniq_units = []
        for unit in self.units:
            uniq_classes = map(lambda unit: unit.__class__.__name__,
                               uniq_units)
            uniq_classes = list(set(uniq_classes))
            if not unit.__class__.__name__ in uniq_classes:
                uniq_units.append(unit)

        return uniq_units
