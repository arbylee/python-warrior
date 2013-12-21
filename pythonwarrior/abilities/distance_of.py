from pythonwarrior.abilities.base import AbilityBase


class DistanceOf(AbilityBase):
    def description(self):
        return ("Pass a Space as an argument, and it will return an integer "
                "representing the distance to that space.")

    def perform(self, space):
        return self._unit.position.distance_of(space)
