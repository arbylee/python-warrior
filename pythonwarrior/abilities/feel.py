from pythonwarrior.abilities.base import AbilityBase


class Feel(AbilityBase):
    def description(self):
        return "Returns a Space for the given direction (forward by default)"

    def perform(self, direction='forward'):
        if direction is None:
            direction = 'forward'
        self.verify_direction(direction)
        return self.space(direction)
