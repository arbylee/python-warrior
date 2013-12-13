#  -------
# |@ Sa S>|
#  -------

level.description("You can hear bow strings being stretched.")
level.tip("No new abilities this time, but you must be careful not to rest while taking damage. Save a self.health instance variable and compare it on each turn to see if you're taking damage.")
level.clue("Set self.health to your current health at the end of the turn. If this is greater than your current health next turn then you know you're taking damage and shouldn't rest.")

level.time_bonus(45)
level.ace_score(90)
level.size(7, 1)
level.stairs(6, 0)

level.warrior(0, 0, 'east')

level.unit('thick_sludge', 2, 0, 'west')
level.unit('archer', 3, 0, 'west')
level.unit('thick_sludge', 5, 0, 'west')
