from pythonwarrior.abilities.base import AbilityBase
class Feel(AbilityBase):
    def description(self):
        "Returns a Space for the given direction (forward by default)"

    def perform(self, direction):
        if direction is None:
            direction = 'forward'
        self.verify_direction(direction)
        return self.space(direction)

