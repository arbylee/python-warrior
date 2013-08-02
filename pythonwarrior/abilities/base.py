from pythonwarrior.position import Position
class AbilityBase(object):
    def __init__(self, unit_attr):
        self.unit_attr = unit_attr

    def offset(self, direction, forward=1, right=0):
        if direction == "forward":
            return [forward, -right]
        elif direction == "backward":
            return [-forward, right]
        elif direction == "right":
            return [right, forward]
        elif direction == "left":
            return [-right, -forward]

    def space(self, direction, forward=1, right=0):
        return self.unit_attr.position.relative_space(*self.offset(direction, forward, right))

    def unit(self, direction, forward=1, right=2):
        return self.space(direction, forward, right).unit

    def damage(self, receiver, amount):
        receiver.take_damage(amount)
        if not receiver.is_alive():
            self.unit_attr.earn_points(receiver.max_health())

    def description(self):
        return None

    def pass_turn(self):
        raise Exception('unimplemented')

    def verify_direction(self, direction):
        if direction not in Position.RELATIVE_DIRECTIONS:
            raise Exception("Unknown direction %s. Should be 'forward', 'backward', 'left' or 'right'")
