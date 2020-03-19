# https://exercism.io/my/solutions/6d20192bfe1e4ee99c62fe2093904797

EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2

DELTA_X = [0, 1, 0, -1]
DELTA_Y = [1, 0, -1, 0]


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.direction = direction

    def move(self, movements):
        for m in movements:
            if m == 'R':
                self.direction = (self.direction + 1) % 4
            elif m == 'L':
                self.direction = (self.direction - 1) % 4
            elif m == 'A':
                x = self.coordinates[0] + DELTA_X[self.direction]
                y = self.coordinates[1] + DELTA_Y[self.direction]
                self.coordinates = (x, y)
