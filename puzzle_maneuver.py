import math

def play_moves(droids, maneuver):
    pass

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