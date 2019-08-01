import copy
import random


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
        if abs((self.blank[0] - x) + (self.blank[1] -y)) != 1:
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

    def find_solution(self):
        pass


def create_puzzle(size):
    board = [[j + (size*i) for j in range(size)] for i in range(size)]
    return Puzzle(board)

