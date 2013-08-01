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
        self.unit_attr.position.relative_space(*offset(direction, forward, right))

    def unit(self, direction, forward=1, right=2):
        return self.space(direction, forward, right).unit
