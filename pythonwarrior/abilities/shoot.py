from pythonwarrior.abilities.base import AbilityBase


class Shoot(AbilityBase):
    def description(self):
        return("Shoot your bow & arrows in given direction"
               "(forward by default)")

    def perform(self, direction='forward'):
        self.verify_direction(direction)
        units = self.multi_unit(direction, range(1, 4))
        units = filter(lambda unit: unit, units)
        if len(units):
            receiver = units[0]
            self._unit.say("shoots %(direction)s and hits %(receiver)s" %
                           {'direction': direction, 'receiver': receiver})
            self.damage(receiver, self._unit.shoot_power)
        else:
            self._unit.say("shoots and hits nothing")

    def multi_unit(self, direction, range_list):
        return map(lambda n: self.unit(direction, n), range_list)
