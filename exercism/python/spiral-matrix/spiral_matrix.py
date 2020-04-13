# https://exercism.io/my/solutions/0141222eca73472a9a2e2bcc0f31f6d9

from itertools import count


def spiral_matrix(size):
    m = [[None] * size for _ in range(size)]
    i = count(1)

    def perimeter(length):
        row = col = (size - length) // 2
        r = row
        for c in range(col, col+length):
            m[r][c] = next(i)
        c = col + length - 1
        for r in range(row+1, row+length):
            m[r][c] = next(i)
        r = row + length - 1
        for c in range(col+length-2, col-1, -1):
            m[r][c] = next(i)
        c = col
        for r in range(row+length-2, row, -1):
            m[r][c] = next(i)

    for length in range(size, 0, -2):
        perimeter(length)
    return m
