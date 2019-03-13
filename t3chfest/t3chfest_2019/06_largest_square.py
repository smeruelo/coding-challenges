# task 6

# max_size(cell) is the size of the largest square that can be placed in this cell.
# It's calculated with binary search over prefix sums

# f(cell) is the largest square that can reach the cell. It's calculated with dynamic programming.
# f(cell) = min(max_size(cell),
#               max(f(cell.y - 1, cell.x), f(cell.y, cell.x - 1)))
# The base case: f(0, 0) = max_size(0, 0)

# https://stackoverflow.com/questions/28664305/find-largest-square-in-matrix-that-can-move-from-one-corner-to-the-other
import random


def calc_prefix_sums(canvas):
    pf_row = []
    s = 0
    for col in range(len(canvas[0])):
        s += canvas[0][col]
        pf_row.append(s)
    pf = [pf_row]

    for row in range(1, len(canvas)):
        pf_row = []
        s = 0
        for col in range(len(canvas[0])):
            s += canvas[row][col]
            pf_row.append(s + pf[row - 1][col])
        pf.append(pf_row)

    return pf


def square_sum(top_corner_y, top_corner_x, size, pf):
    a_y, a_x = top_corner_y + size - 1, top_corner_x + size - 1
    b_y, b_x = top_corner_y + size - 1, top_corner_x - 1
    c_y, c_x = top_corner_y - 1, top_corner_x + size - 1
    d_y, d_x = top_corner_y - 1, top_corner_x - 1
    pf_a = 0 if (a_y < 0 or a_x < 0) else pf[a_y][a_x]
    pf_b = 0 if (b_y < 0 or b_x < 0) else pf[b_y][b_x]
    pf_c = 0 if (c_y < 0 or c_x < 0) else pf[c_y][c_x]
    pf_d = 0 if (d_y < 0 or d_x < 0) else pf[d_y][d_x]
    return pf_a - pf_b - pf_c + pf_d


def max_size(top_corner_y, top_corner_x, pf):
    rows = len(pf)
    columns = len(pf[0])

    def bin_search(max_s):
        s = 0
        b = max_s
        while b >= 1:
            while (top_corner_y + s + b <= rows
                   and top_corner_x + s + b <= columns
                   and square_sum(top_corner_y, top_corner_x, s + b, pf) == (s + b) ** 2):
                s += b
            b //= 2
        return s

    return bin_search(min(rows, columns))


def solution(canvas):
    rows = len(canvas)
    columns = len(canvas[0])
    pf = calc_prefix_sums(canvas)

    F = [[0] * columns for _ in range(rows)]
    F[0][0] = max_size(0, 0, pf)
    for col in range(1, columns):
        F[0][col] = min(max_size(0, col, pf), F[0][col - 1])
    for row in range(1, rows):
        for col in range(columns):
            F[row][col] = min(max_size(row, col, pf),
                              max(F[row - 1][col], F[row][col - 1]))

    size = 1
    while size <= min(rows, columns) and size == F[rows - size][columns - size]:
        size += 1
    return size - 1


if __name__ == '__main__':
    r = [[bool(random.randint(0, 1)) for _ in range(300)] for _ in range(300)]
    print(solution(r))
