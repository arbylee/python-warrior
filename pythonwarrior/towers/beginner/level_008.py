#  -------
# |@  Cww>|
#  -------

level.description("You hear the mumbling of wizards. Beware of their deadly wands! Good thing you found a bow.")
level.tip("Use warrior.look() to determine your surroundings, and warrior.shoot_() to fire an arrow.")
level.clue("Wizards are deadly but low in health. Kill them before they have time to attack.")

level.time_bonus(20)
level.ace_score(46)
level.size(6, 1)
level.stairs(5, 0)

def add_abilities(warrior):
    warrior.add_abilities('look', 'shoot_')
level.warrior(0, 0, 'east', func=add_abilities)

level.unit('captive', 2, 0, 'west')
level.unit('wizard', 3, 0, 'west')
level.unit('wizard', 4, 0, 'west')
