import os
class Tower(object):
    def __init__(self, path):
        self.path = os.path.join(os.path.abspath('towers'), path)

    @property
    def name(self):
        return os.path.basename(self.path)

    def __repr__(self):
        return self.name
