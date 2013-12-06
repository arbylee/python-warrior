import math
from pythonwarrior.abilities.base import AbilityBase


class Attack(AbilityBase):
    def perform(self, direction="forward"):
        self.verify_direction(direction)
        receiver = self.unit(direction)
        if receiver:
            self._unit.say("attacks %s and hits %s" %
                           (direction, receiver.__class__.__name__))
            if direction == "backward":
                power = math.ceil(self._unit.attack_power/2.0)
            else:
                power = self._unit.attack_power
            self.damage(receiver, power)
        else:
            self._unit.say("attacks %s and hits nothing" % direction)

    def description(self):
        return "Attacks a unit in given direction (forward by default)."
