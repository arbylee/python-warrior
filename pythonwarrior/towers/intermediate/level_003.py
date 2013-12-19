#  ---
# |>s |
# |s@s|
# | C |
#  ---

level.description("You feel slime on all sides, you're surrounded!")
level.tip("Call warrior.bind_(direction) to bind an enemy to keep him "
          "from attacking. Bound enemies look like captives.")
level.clue("Count the number of enemies around you. Bind an enemy if "
           "there are two or more.")
level.time_bonus(50)
level.ace_score(101)
level.size(3, 3)
level.stairs(0, 0)

def add_abilities(warrior):
    warrior.add_abilities('bind_')
    warrior.add_abilities('rescue_')

level.warrior(1, 1, 'east', func=add_abilities)

level.unit('sludge', 1, 0, 'west')
level.unit('captive', 1, 2, 'west')
level.unit('sludge', 0, 1, 'west')
level.unit('sludge', 2, 1, 'west')
