import copy
import random
import math
import heapq


class Puzzle(object):

    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.blank = (0, 0)

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        if self.is_legal_move(row, col):
            self.board[self.blank[0]][self.blank[1]] = self.board[row][col]
            self.board[row][col] = 0
            self.blank = (row, col)

    def is_legal_move(self, x, y):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
        if abs(self.blank[0] - x) + abs(self.blank[1] - y) != 1:
            return False
        return True

    def legal_moves(self):
        x, y = self.blank
        if self.is_legal_move(x - 1, y):
            yield (x-1, y)
        if self.is_legal_move(x + 1, y):
            yield (x+1, y)
        if self.is_legal_move(x, y - 1):
            yield (x, y-1)
        if self.is_legal_move(x, y + 1):
            yield (x, y+1)

    def scramble(self, num):
        for _ in range(num):
            x, y = random.choice(list(self.legal_moves()))
            self.perform_move(x, y)

    def is_solved(self):
        if self.board == [[j + (self.size*i) for j in range(self.size)] for i in range(self.size)]:
            return True
        return False

    def copy(self):
        return Puzzle(copy.deepcopy(self.board))

    def successors(self):
        for x, y in self.legal_moves():
            game = self.copy()
            game.perform_move(x, y)
            yield (x, y), game

    def heuristic_fn(self):
        total = 0
        for i in range(self.size):
            for j in range(self.size):
                total += self.manhattan_dist(i, j)
        return total

    def manhattan_dist(self, x, y):
        value = self.board[x][y]
        row = math.floor(value/self.size)
        col = value % self.size
        return abs(row - x) + abs(col - y)

    def update_path(self, point, path):
        new_path = copy.deepcopy(path)
        new_path.append(point)
        return new_path

    def find_solution(self):
        frontier = []
        heapq.heappush(frontier, (heuristic(start, goal), 0, start, [start]))
        explored = {start: 0}
        while frontier:
            f_dist, g_dist, point, path = heapq.heappop(frontier)
            if point == goal:
                return path
            for next_point in get_successors(point, scene):
                gd = g_dist + heuristic(point, next_point)
                if next_point not in explored or explored[next_point] > gd:
                    next_path = update_path(next_point, path)
                    explored[next_point] = gd
                    heapq.heappush(frontier, (gd + heuristic(next_point, goal), gd, next_point, next_path))
        return None


def create_puzzle(size):
    board = [[j + (size*i) for j in range(size)] for i in range(size)]
    return Puzzle(board)

