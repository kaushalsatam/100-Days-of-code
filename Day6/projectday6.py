# Escaping the maze

# My solution on Reeborg's World
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go():
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    turn_right()
    if front_is_clear():
        if at_goal():
            turn_left()
        else:
            move()
            

while not at_goal():
    go()

# Comeback to this problem after Day 15