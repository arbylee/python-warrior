#  ----
# |C s |
# | @ S|
# |C s>|
#  ----

level.description("Your ears become more in tune with the surroundings. "
                  "Listen to find enemies and captives!")
level.tip("Use warrior.listen to find spaces with other units, "
          "and warrior.direction_of to determine what direction they're in.")
level.clue("Walk towards an enemy or captive with "
           "warrior.walk_(warrior.direction_of(warrior.listen()[0])), "
           "once len(warrior.listen()) == 0 then head for the stairs.")
level.time_bonus(55)
level.ace_score(144)
level.size(4, 3)
level.stairs(3, 2)

def add_abilities(warrior):
    warrior.add_abilities('listen')
    warrior.add_abilities('direction_of')

level.warrior(1, 1, 'east', func=add_abilities)

level.unit('captive', 0, 0, 'east')
level.unit('captive', 0, 2, 'east')
level.unit('sludge', 2, 0, 'south')
level.unit('thick_sludge', 3, 1, 'west')
level.unit('sludge', 2, 2, 'north')
