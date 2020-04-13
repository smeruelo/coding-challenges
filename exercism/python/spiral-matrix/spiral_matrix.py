# https://exercism.io/my/solutions/0141222eca73472a9a2e2bcc0f31f6d9


def spiral_matrix(size):
    m = [[None] * size for _ in range(size)]
    def perimeter(length, i):
        row = col = (size - length) // 2
        r = row
        for c in range(col, col+length):
            m[r][c] = i
            i += 1
        c = col + length - 1
        for r in range(row+1, row+length):
            m[r][c] = i
            i += 1
        r = row + length - 1
        for c in range(col+length-2, col-1, -1):
            m[r][c] = i
            i += 1
        c = col
        for r in range(row+length-2, row, -1):
            m[r][c] = i
            i += 1
        return i

    i = 1
    for length in range(size, 0, -2):
        i = perimeter(length, i)
    return m
