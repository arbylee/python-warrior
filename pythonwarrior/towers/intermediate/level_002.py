#  ----
# |@s  |
# | sS>|
#  ----

level.description("Another large room, but with several enemies "
                  "blocking your way to the stairs.")
level.tip("Just like walking, you can attack_ and feel in multiple "
          "directions ('forward', 'left', 'right', 'backward').")
level.clue("Call warrior.feel(direction).is_enemy() in each direction "
           "to make sure there isn't an enemy beside you "
           "(attack if there is). "
           "Call warrior.rest_ if you're low and health when there "
           "are no enemies around.")
level.time_bonus(40)
level.ace_score(84)
level.size(4, 2)
level.stairs(3, 1)

def add_abilities(warrior):
    warrior.add_abilities('attack_')
    warrior.add_abilities('health')
    warrior.add_abilities('rest_')

level.warrior(0, 0, 'east', func=add_abilities)

level.unit('sludge', 1, 0, 'west')
level.unit('thick_sludge', 2, 1, 'west')
level.unit('sludge', 1, 1, 'north')
