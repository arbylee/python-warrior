#  -------
# |@ CaaSC|
#  -------

level.description("You hear cries for help. Captives must need rescuing.")
level.tip("Use warrior.feel().is_captive() to see if there is a captive and warrior.rescue_() to rescue him. Don't attack captives.")
level.clue("Don't forget to constantly check if you're taking damage. Rest until your health is full if you aren't taking damage.")

level.time_bonus(45)
level.ace_score(123)
level.size(7, 1)
level.stairs(6, 0)

def add_abilities(warrior):
    warrior.add_abilities('rescue_')

level.warrior(0, 0, 'east', func=add_abilities)

level.unit('captive', 2, 0, 'west')
level.unit('archer', 3, 0, 'west')
level.unit('archer', 4, 0, 'west')
level.unit('thick_sludge', 5, 0, 'west')
level.unit('captive', 6, 0, 'west')
