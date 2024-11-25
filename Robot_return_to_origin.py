"""
Determine if a robot, starting at the origin (0, 0) on a 2D grid, returns
to the origin after following a sequence of movements.

The robot can move up ('U'), down ('D'), left ('L'), and right ('R').

Movements:
'U' increases the y-coordinate by 1.
'D' decreases the y-coordinate by 1.
'L' decreases the x-coordinate by 1.
'R' increases the x-coordinate by 1.

Start with x = 0 and y = 0.

Args:
    moves (str): A string containing the sequence of moves.

Returns:
    bool: True if the robot returns to the origin, False otherwise.
"""


def return_to_origin(moves):

    # Initial position
    x = 0
    y = 0

    # loop to check the position
    for i in moves:

        if i == "U":
            y += 1
        elif i == "D":
            y -= 1
        elif i == "L":
            x += 1
        elif i == "R":
            x -= 1

    return True if x == 0 and y == 0 else False

# output
moves = input("Enter the moves(U, D, L, R):").upper()
result = return_to_origin(moves)
print("Does robot return to origin? ", result)
