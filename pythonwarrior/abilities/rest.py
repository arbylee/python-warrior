from pythonwarrior.abilities.base import AbilityBase


class Rest(AbilityBase):
    def description(self):
        return "Gain 10% of max health back, but do nothing more."

    def perform(self):
        if self._unit.health < self._unit.max_health:
            amount = int(self._unit.max_health * 0.1)
            if (self._unit.health + amount) > self._unit.max_health:
                amount = self._unit.max_health - self._unit.health
            self._unit.health += amount
            self._unit.say("receives %(heal_amount)d health from resting, "
                           "up to %(current)d health" %
                           {'heal_amount': amount,
                               'current': self._unit.health})
        else:
            self._unit.say("is already fit as a fiddle")
