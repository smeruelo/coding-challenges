#!/usr/bin/python3
# https://cses.fi/problemset/task/1072

import sys
sys.setrecursionlimit(12000)


def knights(k):
    border_cells = (k * 2) - 1

    def two_in_border():
        threatened = 0 if k < 3 else 2
        return ((border_cells - 1) * border_cells) // 2 - threatened

    def one_in_border_one_inside():
        threatened = 0 if k < 3 else 2 + 2 * (10 + 4 * (k - 5))
        return (k - 1) * (k - 1) * border_cells - threatened

    if k == 1:
        return 0
    else:
        two_inside = knights(k - 1)
        print(two_inside)
        return two_in_border() + one_in_border_one_inside() + two_inside


if __name__ == '__main__':
    print(knights(int(input())))
