from pythonwarrior.abilities.base import AbilityBase


class Bind(AbilityBase):
    def description(self):
        return("Binds a unit in given direction to keep him "
               "from moving (forward by default).")

    def perform(self, direction='forward'):
        self.verify_direction(direction)
        receiver = self.unit(direction)
        if receiver:
            self._unit.say("binds %(direction)s and restricts "
                           "%(receiver)s" %
                           {'direction': direction, 'receiver': receiver})
            receiver.bind()
        else:
            self._unit.say("binds %s and restricts nothing" % direction)
