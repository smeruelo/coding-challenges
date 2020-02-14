# https://exercism.io/my/solutions/654ad29b7d5d43d69fd76a64bc7db1ee

from collections import namedtuple

Cell = namedtuple('Cell', 'r c')


class ConnectGame:
    def __init__(self, board):
        self.board = list(map(lambda s: s.replace(' ', ''), board.split('\n')))
        self.height = len(self.board)
        self.width = len(self.board[0])

    def _adjacents(self, cell):
        adj = set([Cell(cell.r - 1, cell.c),
                   Cell(cell.r - 1, cell.c + 1),
                   Cell(cell.r, cell.c - 1),
                   Cell(cell.r, cell.c + 1),
                   Cell(cell.r + 1, cell.c - 1),
                   Cell(cell.r + 1, cell.c)])
        return set(filter(lambda cell: cell.r >= 0 and cell.r < self.height and
                   cell.c >= 0 and cell.c < self.width, adj))

    def _exists_path(self, player, current, prev, board):
        if (player == "O" and current.r == self.height - 1) or \
           (player == "X" and current.c == self.width - 1):
            return True

        board[current.r][current.c] = 'v'
        adj = set(filter(lambda cell: board[cell.r][cell.c] == player, self._adjacents(current)))
        for nxt in adj:
            if self._exists_path(player, nxt, current, board):
                return True
        return False

    def get_winner(self):
        for c in range(self.width):
            b = [list(s) for s in self.board]
            if b[0][c] == 'O' and self._exists_path('O', Cell(0, c), None, b):
                return 'O'
        for r in range(self.height):
            b = [list(s) for s in self.board]
            if b[r][0] == 'X' and self._exists_path('X', Cell(r, 0), None, b):
                return 'X'
        return ''
