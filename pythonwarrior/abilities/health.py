from pythonwarrior.abilities.base import AbilityBase


class Health(AbilityBase):
    def description(self):
        return "Returns an integer representing your health."

    def perform(self):
        return self._unit.health
