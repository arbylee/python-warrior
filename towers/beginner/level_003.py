#  ---------
# |@ s ss s>|
#  ---------

level.description("The air feels thicker than before. There must be a horde of sludge.")
level.tip("Be careful not to die! Use warrior.health to keep an eye on your health, and warrior.rest! to earn 10% of max health back.")
level.clue("When there is no enemy ahead of you call warrior.rest_() until health is full before walking forward.")
level.time_bonus(35)
level.ace_score(71)
level.size(9, 1)
level.stairs(8, 0)
def add_abilities(warrior):
    warrior.add_abilities('health')
    warrior.add_abilities('rest_')
level.warrior(0, 0, 'east', func=add_abilities)

level.unit('sludge', 2, 0, 'west')
level.unit('sludge', 4, 0, 'west')
level.unit('sludge', 5, 0, 'west')
level.unit('sludge', 7, 0, 'west')
