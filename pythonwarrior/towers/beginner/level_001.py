#  --------
# |@      >|
#  --------
level.description("You see before yourself a long hallway with stairs at "
                  "the end. There is nothing in the way.")
level.tip("Call warrior.walk_() to walk forward in the Player "
          "'play_turn' method.")
level.time_bonus(15)
level.ace_score(10)
level.size(8, 1)
level.stairs(7, 0)
def add_abilities(warrior):
    warrior.add_abilities('walk_')
level.warrior(0, 0, 'east', func=add_abilities)
