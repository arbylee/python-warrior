from pythonwarrior.abilities.base import AbilityBase


class Pivot(AbilityBase):
    ROTATION_DIRECTIONS = ['forward', 'right', 'backward', 'left']

    def description(self):
        return "Rotate 'left', 'right', or 'backward' (default)"

    def perform(self, direction='backward'):
        self.verify_direction(direction)
        self._unit.position.rotate(self.ROTATION_DIRECTIONS.index(direction))
        self._unit.say("pivots %s" % direction)
