#  ------
# |      |
# |@     |
# |      |
# |  >   |
#  ------

level.description("Silence. The room feels large, but empty. "
                  "Luckily you have a map of this tower to help "
                  "find the stairs.")
level.tip("Use warrior.direction_of_stairs to determine which "
          "direction stairs are located. Pass this to warrior.walk_ "
          "to walk in that direction."
          "'play_turn' method.")
level.time_bonus(20)
level.ace_score(19)
level.size(6, 4)
level.stairs(2, 3)

def add_abilities(warrior):
    warrior.add_abilities('walk_')
    warrior.add_abilities('feel')
    warrior.add_abilities('direction_of_stairs')

level.warrior(0, 1, 'east', func=add_abilities)
