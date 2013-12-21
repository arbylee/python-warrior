#  ------
# |Cs   >|
# |@  sC |
#  ------

level.description("What's that ticking? Some captives have a timed bomb "
                  "at their feet!")
level.tip("Hurry and rescue captives first that have space.is_ticking(), "
          "they'll soon go!")
level.clue("Avoid fighting enemies at first. Use warrior.listen() and "
           "space.is_ticking() and quickly rescue those captives.")
level.time_bonus(50)
level.ace_score(108)
level.size(6, 2)
level.stairs(5, 0)

level.warrior(0, 1, 'east')

level.unit('sludge', 1, 0, 'west')
level.unit('sludge', 3, 1, 'west')
level.unit('captive', 0, 0, 'west')

def add_abilities(unit):
    unit.add_abilities('explode_')
    unit.abilities_attr['explode_'].time = 7

level.unit('captive', 4, 1, 'west', func=add_abilities)
