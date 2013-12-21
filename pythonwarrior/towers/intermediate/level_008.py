#  -------
# |@ Ss C>|
#  -------

level.description("You discover a satchel of bombs which will help "
                  "when facing a mob of enemies.")
level.tip("Detonate a bomb when you see a couple enemies ahead of "
          "you (warrior.look()). Watch out for your health too.")
level.clue("Calling warrior.look() will return an array of Spaces. If the "
           "first two contain enemies, detonate a bomb with "
           "warrior.detonate_().")
level.time_bonus(30)
level.size(7, 1)
level.stairs(6, 0)

def add_war_abilities(warrior):
    warrior.add_abilities('look', 'detonate_')

level.warrior(0, 0, 'east', func=add_war_abilities)

def add_captive_abilities(unit):
    unit.add_abilities('explode_')
    unit.abilities_attr['explode_'].time = 9

level.unit('captive', 5, 0, 'west', func=add_captive_abilities)
level.unit('thick_sludge', 2, 0, 'west')
level.unit('sludge', 3, 0, 'west')
