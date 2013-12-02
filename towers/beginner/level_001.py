#  --------
# |@      >|
#  --------
level.description("You see before yourself a long hallway with stairs at "
                  "the end. There is nothing in the way.")
level.tip("Call warrior.walk_ to walk forward in the Player "
          "'play_turn' method.")
level.time_bonus(15)
level.ace_score(10)
level.size(8, 1)
level.stairs(7, 0)
def a_func(warrior):
    warrior.add_abilities('walk')
level.warrior(0, 0, func=a_func)
