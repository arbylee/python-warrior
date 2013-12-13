from pythonwarrior.abilities.base import AbilityBase
from pythonwarrior import units


class Rescue(AbilityBase):
    def description(self):
        return("Rescue a captive from his chains (earning 20 points)"
               "in given direction (forward by default)")

    def perform(self, direction='forward'):
        self.verify_direction(direction)
        if self.space(direction).is_captive():
            recipient = self.unit(direction)
            self._unit.say("unbinds %(direction)s and rescues %(recipient)s" %
                           {'direction': direction, 'recipient': recipient})
            recipient.unbind()
            if isinstance(recipient, units.captive.Captive):
                recipient.position = None
                self._unit.earn_points(20)
        else:
            self._unit.say("unbinds %s and rescues nothing" % direction)
