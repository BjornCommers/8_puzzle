import copy
import random
import math
import heapq


class Puzzle(object):

    def __init__(self, board):
        self.board = board
        self.size = len(board)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    self.blank = (i, j)

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

    def is_solvable(self):
        inversions = 0
        numbers = [self.board[i][j] for i in range(self.size) for j in range(self.size) if self.board[i][j] != 0]
        for i, number in enumerate(numbers):
            for j in range(i+1, len(numbers)):
                if number > numbers[j]:
                    inversions += 1
        if inversions % 2 == 0:
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

    def board_tuple(self):
        return tuple([tuple(i) for i in self.board])

    def find_solution(self):
        if self.is_solvable():
            frontier = []
            heapq.heappush(frontier, (self.heuristic_fn(), [], self))
            explored = {self.board_tuple(): 0}
            while frontier:
                f, path, game = heapq.heappop(frontier)
                if game.is_solved():
                    return path
                for next_move, next_game in game.successors():
                    fn = len(path) + next_game.heuristic_fn()
                    if next_game.board_tuple() not in explored:
                        next_path = update_path(next_move, path)
                        explored[next_game.board_tuple()] = fn
                        heapq.heappush(frontier, (fn, next_path, next_game))
        return None


def update_path(point, path):
    new_path = copy.deepcopy(path)
    new_path.append(point)
    return new_path


def create_puzzle(size):
    board = [[j + (size*i) for j in range(size)] for i in range(size)]
    return Puzzle(board)
