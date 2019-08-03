import math


def perform_moves(droid_board, moves, blank, speed, scale_dist=1):
    for move in moves:

        # get droid in move
        droid = droid_board[move[0]][move[1]]

        # calculate dist/ang into blank space
        dist, ang = compute_roll_parameters(move, blank)

        # roll
        rolled = roll(droid, speed, ang, dist * scale_dist)
        if not rolled:
            print('Something went wrong.')
            return False

        # update board
        droid_board[move[0]][move[1]] = None
        droid_board[blank[0]][blank[1]] = droid
        blank = move  # update new blank space


# copied from joe's code
def roll(sphero, speed, ang, time):
    return sphero.roll(speed, ang, time)


# copied from joe's code
def compute_roll_parameters(old_pos, new_pos):

    x_1, y_1 = old_pos
    x_2, y_2 = new_pos
    d_x, d_y = (x_2 - x_1), (y_2 - y_1)

    dist = math.sqrt(d_x**2 + d_y**2)
    ang = 90 - math.atan2(d_y, d_x) * (180/math.pi)

    return dist, ang

