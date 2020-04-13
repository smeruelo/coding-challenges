# https://exercism.io/my/solutions/0141222eca73472a9a2e2bcc0f31f6d9

from itertools import count


def spiral_matrix(size):
    m = [[None] * size for _ in range(size)]
    i = count(1)

    def perimeter(row, col, length):
        for c in range(col, col+length):
            m[row][c] = next(i)
        for r in range(row+1, row+length):
            m[r][col+length-1] = next(i)
        for c in range(col+length-2, col-1, -1):
            m[row+length-1][c] = next(i)
        for r in range(row+length-2, row, -1):
            m[r][col] = next(i)

    for length in range(size, 0, -2):
        start = (size - length) // 2
        perimeter(start, start, length)
    return m
