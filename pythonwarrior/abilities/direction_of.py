from pythonwarrior.abilities.base import AbilityBase


class DirectionOf(AbilityBase):
    def description(self):
        return ("Pass a Space as an argument, and the direction "
                "(:left, :right, :forward, :backward) "
                "to that space will be returned.")

    def perform(self, space):
        return self._unit.position.relative_direction_of(space)
