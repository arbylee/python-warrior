#  ------
# |>a S @|
#  ------

level.description("You feel a wall right in front of you and an opening behind you.")
level.tip("You are not as effective at attacking backward. Use warrior.feel().is_wall() and warrior.pivot_() to turn around.")

level.time_bonus(30)
level.ace_score(50)
level.size(6, 1)
level.stairs(0, 0)

def add_abilities(warrior):
    warrior.add_abilities('pivot_')
level.warrior(5, 0, 'east', func=add_abilities)

level.unit('archer', 1, 0, 'east')
level.unit('thick_sludge', 3, 0, 'east')
