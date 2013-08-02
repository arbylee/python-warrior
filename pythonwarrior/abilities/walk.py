from pythonwarrior.abilities.base import AbilityBase
class Walk(AbilityBase):
    def perform(self, direction="forward"):
        self.verify_direction(direction)
        if self.unit_attr.position:
            self.unit_attr.say("walks %s" % direction)
            if self.space(direction).is_empty():
                self.unit_attr.position.move(*self.offset(direction))
            else:
                self.unit_attr.say("bumps into %s" % self.space(direction))


