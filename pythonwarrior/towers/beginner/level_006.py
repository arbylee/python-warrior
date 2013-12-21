#  --------
# |C @ S aa|
#  --------

level.description("The wall behind you feels a bit further away in this room. And you hear more cries for help.")
level.tip("You can walk backward by passing 'backward' as an argument to warrior.walk_. Same goes for warrior.feel, warrior.rescue_ and warrior.attack_. Archers have a limited attack distance.")
level.clue("Walk backward if you are taking damage from afar and do not have enough health to attack. You may also want to consider walking backward until warrior.feel('backward').is_wall().")

level.time_bonus(55)
level.ace_score(105)
level.size(8, 1)
level.stairs(7, 0)

level.warrior(2, 0, 'east')

level.unit('captive', 0, 0, 'east')
level.unit('thick_sludge', 4, 0, 'west')
level.unit('archer', 6, 0, 'west')
level.unit('archer', 7, 0, 'west')
