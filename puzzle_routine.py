from puzzle import Puzzle
from client import DroidClient
import puzzle_maneuver

# assign droids to a number and start all droids
droid_names = {1: 'D2-579A', 2: 'Q5-8C54', 3: 'Q5-EFBE', 4: 'Q5-240E', 5: 'D2-0969', 6: 'Q5-B30E', 7: 'D2-1C62', 8: 'Q5-D8D3'}
droids = {} # num: droid client

for num, droid_name in droid_names.items():
    droid = DroidClient()
    droid.connect_to_droid(droid_name)
    droids[num] = droid

# create puzzle and find solution to puzzle
start_board = [[3, 7, 1], [6, 4, 2], [0, 8, 5]]
# Other boards to use/test:
# start_board = [[3, 1, 0], [4, 6, 5], [7, 8, 2]]
# start_board = [[7, 6, 4], [3, 0, 8], [2, 1, 5]]
puzzle = Puzzle(start_board)
blank = puzzle.blank
moves = puzzle.find_solution()

# set up droids in grid
droid_board = []
for row in start_board:
    new_row = []
    for num in row:
        if num != 0:
            new_row.append(droids[num])
        else:
            new_row.append(None)
    droid_board.append(new_row)

# droids play out puzzle
puzzle_maneuver.perform_moves(droid_board, moves, blank)
