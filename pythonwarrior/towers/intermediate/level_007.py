#  -----
# | sC >|
# |@ s C|
# | s   |
#  -----

level.description("Another ticking sound, but some sludge is blocking the way.")
level.tip("Quickly kill the sludge and rescue the captive before the "
          "bomb goes off. You can't simply go around them.")
level.clue("Determine the direction of the ticking captive and kill any "
           "enemies blocking that path. You may need to bind surrounding "
           "enemies first.")
level.time_bonus(70)
level.ace_score(134)
level.size(5, 3)
level.stairs(4, 0)

level.warrior(0, 1, 'east')

level.unit('sludge', 1, 0, 'south')
level.unit('sludge', 1, 2, 'north')
level.unit('sludge', 2, 1, 'west')
level.unit('captive', 2, 0, 'west')

def add_abilities(unit):
    unit.add_abilities('explode_')
    unit.abilities_attr['explode_'].time = 10

level.unit('captive', 4, 1, 'west', func=add_abilities)

