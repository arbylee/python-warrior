import functools


class Turn(object):
    def __init__(self, abilities):
        self.action = None
        self.senses = {}

        for name, sense in abilities.iteritems():
            if name.endswith("_"):
                self.add_action(name)
            else:
                self.add_sense(name, sense)

    def add_action(self, action):
        self.__dict__[action] = functools.partial(self._generic_action, action)

    def add_sense(self, name, sense):
        self.senses[name] = sense
        self.__dict__[name] = functools.partial(self._generic_sense, name)

    def _generic_action(self, action_name, *args):
        if self.action:
            raise Exception("Only one action can be performed per turn")
        self.action = [action_name]
        for arg in args:
            self.action.append(arg)

    def _generic_sense(self, sense_name, *args):
        return self.senses[sense_name].perform(*args)
