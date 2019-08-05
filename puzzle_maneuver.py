import math
import time

# method to perform all the moves in the solution
def perform_moves(droid_board, moves, blank):
    for move in moves:

        # get droid in move
        droid = droid_board[move[0]][move[1]]

        # set path from current location to next square (where blank is)
        path = [move, blank]

        # set droid on path and wait one second
        follow_path(droid, path, 0x88, .9)
        time.sleep(1)

        # update board
        droid_board[move[0]][move[1]] = None
        droid_board[blank[0]][blank[1]] = droid
        blank = move  # update new blank space

# modified from joe's code
def follow_path(sphero, path, speed, scale_dist=1):

    cur_pos = path[0]
    for next_pos in path[1:]:

        # compute distance and angle to next position
        print('%s -> %s' % (cur_pos, next_pos))
        dist, ang = compute_roll_parameters(cur_pos, next_pos)
        if ang == -90:
            ang = 270
        # if sphero.angle - ang == 180 or sphero.angle - ang == -180:
        #     dist += .15
        # if sphero.angle == 180 and ang == 0:
        #     dist += .05
        rolled = roll(sphero, speed, ang, dist*scale_dist)
        if not rolled:
            print('Something went wrong.')
            return False

        cur_pos = next_pos
    print('Path complete.')
    return True

# joe's code
def roll(sphero, speed, ang, time):
    return sphero.roll(speed, ang, time)


# joe's code
def compute_roll_parameters(old_pos, new_pos):

    x_1, y_1 = old_pos
    x_2, y_2 = new_pos
    d_x, d_y = (x_2 - x_1), (y_2 - y_1)

    dist = math.sqrt(d_x**2 + d_y**2)
    ang = 90 - math.atan2(d_y, d_x) * (180/math.pi)

    return dist, ang

