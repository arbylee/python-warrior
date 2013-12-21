#  ----
# |ssC>|
# |@sss|
# |ssC |
#  ----

level.description("Never before have you seen a room so full of sludge. "
                  "Start the fireworks!")
level.tip("Be careful not to let the ticking captive get caught in "
          "the flames. Use warrior.distance_of to avoid the captives.")
level.clue("Be sure to bind the surrounding enemies before fighting. "
           "Check your health before detonating explosives.")
level.time_bonus(70)
level.size(4, 3)
level.stairs(3, 0)

def add_war_abilities(warrior):
    warrior.add_abilities('distance_of')

level.warrior(0, 1, 'east', func=add_war_abilities)

def add_captive_abilities(unit):
    unit.add_abilities('explode_')
    unit.abilities_attr['explode_'].time = 20

level.unit('captive', 2, 0, 'south', func=add_captive_abilities)
level.unit('captive', 2, 2, 'north')

level.unit('sludge', 0, 0, 'south')
level.unit('sludge', 1, 0, 'south')
level.unit('sludge', 1, 1, 'east')
level.unit('sludge', 2, 1, 'east')
level.unit('sludge', 3, 1, 'east')
level.unit('sludge', 0, 2, 'north')
level.unit('sludge', 1, 2, 'north')
