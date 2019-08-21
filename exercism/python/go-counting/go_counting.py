BLACK = 'B'
WHITE = 'W'
NONE = ' '


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self._board = board
        self._width = len(board[0])
        self._height = len(board)

    def is_valid(self, cell):
        x, y = cell
        return x >= 0 and x < self._width and y >= 0 and y < self._height

    def neighbours(self, cell):
        x, y = cell
        return filter(lambda cell: self.is_valid(cell), [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)])

    def explore(self, cell):
        encircled = set()

        def aux(cell):
            x, y = cell
            if self._board[y][x] == NONE:
                encircled.add((x, y))
                nexts_to_explore = filter(lambda c: not (c in encircled), self.neighbours(cell))
                owners = [aux(c) for c in nexts_to_explore]
                if owners and all(map(lambda o: o == BLACK, owners)):
                    return BLACK
                if owners and all(map(lambda o: o == WHITE, owners)):
                    return WHITE
                return NONE
            return self._board[y][x]

        owner = aux(cell)
        if encircled:
            return (owner, encircled)
        return (NONE, set())

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """

        if self.is_valid((x, y)):
            return self.explore((x, y))
        raise ValueError('Invalid coordinate')

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """

        d = dict()
        d[WHITE] = set()
        d[BLACK] = set()
        d[NONE] = set()
        visited = set()

        for y in range(self._height):
            for x in range(self._width):
                if not (x, y) in visited and self._board[y][x] == NONE:
                    owner, encircled = self.territory(x, y)
                    d[owner].update(encircled)
                    visited.update(encircled)

        return d
