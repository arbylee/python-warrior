from pythonwarrior.abilities.base import AbilityBase


class Listen(AbilityBase):
    def description(self):
        return "Returns an array of all spaces which have units in them."

    def perform(self):
        def _filter_out_main(item):
            return (item and item != self._unit)

        units = filter(_filter_out_main, self._unit.position.floor.units)

        units = filter(lambda x: x, units)
        return units
