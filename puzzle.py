class Puzzle(object):

    def __init__(self, board):
        self.board = board
        self.size = len(board)

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        if self.board == [[j + (self.size*i) for j in range(self.size)] for i in range(self.size)]:
            return True
        return False

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass


def create_puzzle(size):
    board = [[j + (size*i) for j in range(size)] for i in range(size)]
    return Puzzle(board)

