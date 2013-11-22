class Position(object):
    DIRECTIONS = ["north", "east", "south", "west"]
    RELATIVE_DIRECTIONS = ["forward", "right", "backward", "left"]

    def __init__(self, floor, x, y, direction=None):
        self.floor = floor
        self.x = x
        self.y = y
        self.direction_index = self.DIRECTIONS.index(direction or "north")

    def at(self, x, y):
        return self.x == x and self.y == y

    @property
    def direction(self):
        return self.DIRECTIONS[self.direction_index]

    def rotate(self, amount):
        self.direction_index = (self.direction_index + amount) % 4

    def relative_space(self, forward, right=None):
        if right is None:
            right = 0
        return self.floor.space(*(self.translate_offset(forward, right)))

    def space(self):
        return self.floor.space(self.x, self.y)

    def move(self, forward, right=None):
        if right is None:
            right = 0
        (x, y) = self.translate_offset(forward, right)
        self.x = x
        self.y = y

    def distance_from_stairs(self):
        return self.distance_of(self.floor.stairs_space())

    def distance_of(self, space):
        (x, y) = space.location()
        return abs(self.x - x) + abs(self.y - y)

    def relative_direction_of_stairs(self):
        return self.relative_direction_of(self.floor.stairs_space())

    def relative_direction_of(self, space):
        return self.relative_direction(self.direction_of(space))

    def direction_of(self, space):
        (space_x, space_y) = space.location()
        if abs(self.x - space_x) > abs(self.y - space_y):
            return 'east' if space_x > self.x else 'west'
        else:
            return 'south' if space_y > self.y else 'north'

    def relative_direction(self, direction):
        offset = (self.DIRECTIONS.index(direction) - self.direction_index) % 4
        return self.RELATIVE_DIRECTIONS[offset]

    def translate_offset(self, forward, right):
        if self.direction == 'north':
            return [self.x + right, self.y - forward]
        if self.direction == 'east':
            return [self.x + forward, self.y + right]
        if self.direction == 'south':
            return [self.x - right, self.y + forward]
        if self.direction == 'west':
            return [self.x - forward, self.y - right]
