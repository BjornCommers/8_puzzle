from puzzle import Puzzle
from client import DroidClient
import puzzle_maneuver

# start droids
droid_names = {1: 'D2-579a', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}
droids = {}

for num, droid_name in droid_names:
    droid = DroidClient()
    droid.connect_to_droid(droid_name)
    droid.animate(5)
    droids[num] = droid

# create puzzle and find solution to puzzle
start_board = []
puzzle = Puzzle(start_board)
solution = puzzle.find_solution()

# droids play out puzzle
puzzle_maneuver.play_moves(droids, solution)