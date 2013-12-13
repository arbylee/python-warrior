from pythonwarrior.abilities.base import AbilityBase


class Explode(AbilityBase):
    def description(self):
        return("Kills you and all surrounding units."
               " You probably don't want to do this intentionally.")

    def perform(self):
        if self._unit.position:
            self._unit.say("explodes, collapsing the ceiling and "
                           "damaging every unit.")
            for unit in self._unit.position.floor.units:
                unit.take_damage(100)

    def pass_turn(self):
        if self.time and self._unit.position:
            self._unit.say("is ticking")
            self.time -= 1
            if self.time == 0:
                self.perform()
