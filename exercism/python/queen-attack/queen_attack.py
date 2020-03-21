# https://exercism.io/my/solutions/d3b251cfb684443ba6b6b37a49877672

# dlr = diagonal from left to right
# drl = diagonal from right to left
#       DLRs:                DRLs:
#     0  1  2 ..         .. 2  1  0
#    -1  0  1               1  0 -1
#    -2 -1  0               0 -1 -2
#    ..                          ..

class Queen:
    def __init__(self, row, column):
        if row < 0 or row > 7 or column < 0 or column > 7:
            raise ValueError("Invalid value")
        self.row = row
        self.column = column
        self.dlr = column - row
        self.drl = 7 - column - row

    def can_attack(self, other):
        if self.row == other.row and self.column == other.column:
            raise ValueError("Queens must be in different positions")
        return self.row == other.row or \
            self.column == other.column or \
            self.dlr == other.dlr or \
            self.drl == other.drl
