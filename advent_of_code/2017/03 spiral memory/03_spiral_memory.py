#!/usr/bin/python3
# https://adventofcode.com/2017/day/3

from math import sqrt


def distance(n):
    def lap(n):
        fix = int(sqrt(n)) ** 2 == n and int(sqrt(n)) % 2 == 1 and int(sqrt(n)/2) % 2 == 1
        return round(sqrt(n)/2) - int(fix)

    def size(lap):
        return lap * 2 + 1

    def fst(lap):
        return (size(lap - 1) ** 2) + 1

    def lst(lap):
        return size(lap) ** 2

    def coordinates(n):
        if n == 1:
            return (0, 0)
        l = lap(n)
        left_top_corner = fst(l) + 2 * size(l) - 3
        right_top_corner = left_top_corner - size(l) + 1
        left_bottom_corner = left_top_corner + size(l) - 1
        right_bottom_corner = lst(l)
        if n >= right_top_corner and n <= left_top_corner:
            row = -l
            col = left_top_corner - n - ((size(l) - 1) // 2)
        elif n >= left_bottom_corner and n <= right_bottom_corner:
            row = l
            col = n - left_bottom_corner - ((size(l) - 1) // 2)
        elif n > left_top_corner and n < left_bottom_corner:
            row = n - left_top_corner - ((size(l) - 1) // 2)
            col = -l
        else:
            row = right_top_corner - n - ((size(l) - 1) // 2)
            col = l
        return row, col

    row, col = coordinates(n)
    return abs(row) + abs(col)


def fill(spiral, n):
    def calc_value(row, col):
        return spiral[row-1][col-1] + spiral[row-1][col] + spiral[row-1][col+1] + \
            spiral[row][col-1] + spiral[row][col+1] + \
            spiral[row+1][col-1] + spiral[row+1][col] + spiral[row+1][col+1]

    center = len(spiral) // 2
    row = col = center
    spiral[row][col] = 1
    lap = 1
    while True:
        lap_size = lap * 2 + 1
        col += 1
        while row >= center - (lap_size - 1) // 2:
            spiral[row][col] = calc_value(row, col)
            if spiral[row][col] > n:
                return spiral[row][col]
            row -= 1
        row += 1
        col -= 1
        while col >= center - (lap_size - 1) // 2:
            spiral[row][col] = calc_value(row, col)
            if spiral[row][col] > n:
                return spiral[row][col]
            col -= 1
        col += 1
        row += 1
        while row <= center + (lap_size - 1) // 2:
            spiral[row][col] = calc_value(row, col)
            if spiral[row][col] > n:
                return spiral[row][col]
            row += 1
        row -= 1
        col += 1
        while col <= center + (lap_size - 1) // 2:
            spiral[row][col] = calc_value(row, col)
            if spiral[row][col] > n:
                return spiral[row][col]
            col += 1
        col -= 1
        lap += 1


if __name__ == '__main__':
    with open('03_spiral_memory.input') as f:
        n = int(f.read())

    # part 1
    print(distance(n))

    # part 2
    size = 11
    spiral = [[0] * size for _ in range(size)]
    last = fill(spiral, n)
    print(last)
