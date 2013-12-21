#  --------
# |@   s  >|
#  --------

level.description("It is too dark to see anything, but you smell sludge nearby.")
level.tip("Use warrior.feel().is_empty() to see if there is anything in front of you, and warrior.attack() to fight it. Remember, you can only do one action (ending in _) per turn.")
level.time_bonus(20)
level.ace_score(26)
level.size(8, 1)
level.stairs(7, 0)
def add_abilities(warrior):
    warrior.add_abilities('feel', 'attack_')
level.warrior(0, 0, 'east', func=add_abilities)
level.unit('sludge', 4, 0, 'west')
