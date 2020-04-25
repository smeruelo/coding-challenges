# https://exercism.io/my/solutions/89c10865e57143848f71e3497957ce2a

DELTAS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
    'UP_LEFT': (-1, -1),
    'UP_RIGHT': (1, -1),
    'DOWN_LEFT': (-1, 1),
    'DOWN_RIGHT': (1, 1)
}


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def next(self, direction):
        return Point(self.x + DELTAS[direction][0], self.y + DELTAS[direction][1])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self._puzzle = puzzle
        self._height = len(puzzle)
        self._width = len(puzzle[0])

    def _is_in_bounds(self, p):
        return p.x >= 0 and p.x < self._width and p.y >= 0 and p.y < self._height


    def search(self, word):
        def rec(pt, word, dir):
            if len(word) == 0:
                return pt
            nxt = pt.next(dir)
            if self._is_in_bounds(nxt) and self._puzzle[nxt.y][nxt.x] == word[0]:
                return rec(nxt, word[1:], dir)
            return None

        for y, row in enumerate(self._puzzle):
            for x, letter in enumerate(row):
                if letter == word[0]:
                    start_pt = Point(x, y)
                    for dir in DELTAS.keys():
                        if (end_pt := rec(start_pt, word[1:], dir)) is not None:
                            return start_pt, end_pt
        return None
