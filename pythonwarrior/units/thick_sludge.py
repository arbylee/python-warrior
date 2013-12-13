from pythonwarrior.units.sludge import Sludge


class ThickSludge(Sludge):
    def __init__(self):
        super(ThickSludge, self).__init__()
        self.max_health = 24

    @property
    def character(self):
        return "S"
