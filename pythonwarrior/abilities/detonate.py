from pythonwarrior.abilities.base import AbilityBase


class Detonate(AbilityBase):
    def description(self):
        return ("Detonate a bomb in a given direction (forward by default) "
                "which damages that space and surrounding 4 spaces "
                "(including yourself).")

    def perform(self, direction='forward'):
        self.verify_direction(direction)
        if self._unit.position:
            self._unit.say("detonates a bomb %s launching "
                           "a deadly explosion" % direction)
            self.bomb(direction, 1, 0, 8)
            for x, y in [(1, 1), (1, -1), (2, 0), (0, 0)]:
                self.bomb(direction, x, y, 4)

    def bomb(self, direction, x, y, damage_amount):
        if self._unit.position:
            receiver = self.space(direction, x, y).unit
            if receiver:
                if receiver.abilities.get('explode_'):
                    receiver.say("caught in bomb's flames which "
                                 "detonates ticking explosive")
                    receiver.abilities['explode_'].perform()
                else:
                    self.damage(receiver, damage_amount)
