class Position(object):
    DIRECTIONS = ["north", "east", "south", "west"]
    RELATIVE_DIRECTIONS = ["forward", "right", "backward", "left"]
    def __init__(self, floor, x, y, direction=None):
        self.floor = floor
        self.x = x
        self.y = y
        self.direction_index = Position.DIRECTIONS.index(direction or "north")

    def at(self, x, y):
        print self.x
        print self.y
        return self.x == x and self.y == y
