from pythonwarrior.abilities.base import AbilityBase


class Walk(AbilityBase):
    def perform(self, direction="forward"):
        self.verify_direction(direction)
        if self._unit.position:
            self._unit.say("walks %s" % direction)
            if self.space(direction).is_empty():
                self._unit.position.move(*self.offset(direction))
            else:
                self._unit.say("bumps into %s" % self.space(direction))

    def description(self):
        return "Move in the given direction (forward by default)."
