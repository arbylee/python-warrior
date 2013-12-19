from pythonwarrior.abilities.base import AbilityBase


class DirectionOfStairs(AbilityBase):
    def description(self):
        return ("Returns the direction ('left', 'right', 'forward',"
                "'backward') the stairs are from your location")

    def perform(self):
        return self._unit.position.relative_direction_of_stairs()
