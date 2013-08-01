class UnitBase(object):
    def __init__(self):
        self.position = None
        self.health_attr = None

    def __repr__(self):
        return self.__class__.__name__

    def attack_power(self):
        return 0

    def is_alive(self):
        return self.position != None

    def max_health(self):
        return 0

    def health(self):
        if not self.health_attr:
            self.health_attr = self.max_health()
        return self.health_attr

    def take_damage(self, amount):
        if self.health():
            self.health_attr -= amount
            if self.health() <= 0:
                self.position = None
                print "dies"

    def name(self):
        return self.__class__.__name__

    def prepare_turn(self):
        self.current_turn = self.next_turn()
        self.play_turn(self.current_turn)

    def next_turn(self):
        return None

    def play_turn(self, turn):
        return None
