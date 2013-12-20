#  -----
# |    S|
# |@> SC|
#  -----

level.description("You can feel the stairs right next to you, "
                  "but are you sure you want to go up them right away?")
level.tip("You'll get more points for clearing the level first. "
          "Use warrior.feel().is_stairs() and warrior.feel().is_empty() "
          "to determine where to go.")
level.clue("If going towards a unit is the same direction as the stairs, "
           "try moving another empty direction until you can safely move "
           "toward the enemies.")
level.time_bonus(45)
level.ace_score(107)
level.size(5, 2)
level.stairs(1, 1)

level.warrior(0, 1, 'east')

level.unit('thick_sludge', 4, 0, 'west')
level.unit('thick_sludge', 3, 1, 'north')
level.unit('captive', 4, 1, 'west')
