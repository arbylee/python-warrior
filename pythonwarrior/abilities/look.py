from pythonwarrior.abilities.base import AbilityBase


class Look(AbilityBase):
    def description(self):
        return("Returns an array of up to three Spaces in the given direction",
               "(forward by default)")

    def perform(self, direction='forward'):
        self.verify_direction(direction)
        return map(lambda amount: self.space(direction, amount), [1, 2, 3])
