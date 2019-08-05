from client import DroidClient
import puzzle_maneuver
import time
# assign droids to a number and start all droids
#droid_names = {1: 'D2-579A', 2: 'Q5-E3D3', 3: 'D2-0969', 4: 'Q5-240E', 5: 'D2-1C62', 6: 'Q5-B30E', 7: 'D2-8117', 8: 'Q5-D8D3'}

# droid_names = {7: 'D2-579A'}
# droids = {} # num: droid client
#
# for num, droid_name in droid_names.items():
#     droid = DroidClient()
#     droid.connect_to_droid(droid_name)
#     droid.battery()

# droid = DroidClient()
# droid.connect_to_droid('D2-1C62')
# #droid.animate(5)
# # puzzle_maneuver.roll(droid, 0x40, 0, .40)
# # puzzle_maneuver.roll(droid, 0x40, 180, .40)
#

droid = DroidClient()
droid.connect_to_droid('Q5-B30E')

path = [(2, 2), (2, 1)]
# puzzle_maneuver.follow_path(droid, path, 0x88, .9)
# time.sleep(5)
# path = [(2, 1), (2, 2)]
# puzzle_maneuver.follow_path(droid, path, 0x88, .9)

# path1 = [(1, 0), (1, 1)]
# maneuver.follow_path(droid, path1, 0x88, .75)
#
# path1 = [(1, 1), (1, 0), (2, 0)]
# maneuver.follow_path(droid, path1, 0x88, .75)

# dist, ang = maneuver.compute_roll_parameters((1, 1), (1, 0))
# maneuver.roll(droid, 0x40, ang, dist*.4)

# from puzzle import Puzzle
# from client import DroidClient
# import puzzle_maneuver
#
# # assign droids to a number and start all droids
# droid_names = {1: 'D2-579A', 2: 'Q5-E3D3', 3: 'D2-0969'}
# droids = {} # num: droid client
#
# for num, droid_name in droid_names.items():
#     droid = DroidClient()
#     droid.connect_to_droid(droid_name)
#     droids[num] = droid
#
# # create puzzle and find solution to puzzle
# start_board = [[1, 3], [2, 0]]
# puzzle = Puzzle(start_board)
# blank = puzzle.blank
# moves = puzzle.find_solution()
#
# # set up droids in grid
# droid_board = []
# for row in start_board:
#     new_row = []
#     for num in row:
#         if num != 0:
#             new_row.append(droids[num])
#         else:
#             new_row.append(None)
#     droid_board.append(new_row)
#
# # droids play out puzzle
# speed = 0x88  # half speed?
# puzzle_maneuver.perform_moves(droid_board, moves, blank, speed, .75)
#


