#!/usr/bin/pypy3
# https://www.codechef.com/WICP2001/problems/INF1912

from fractions import Fraction


def cells_unguarded(n, k, rows, cols):
    cols_unguarded = n - len(cols)
    rows_unguarded = n - len(rows)
    return cols_unguarded * rows_unguarded


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        rows = set()
        cols = set()
        for _ in range(k):
            r, c = map(lambda x: int(x) - 1, input().split())
            rows.add(r)
            cols.add(c)
        possibilities = cells_unguarded(n, k, rows, cols)
        if possibilities == 0:
            print('Impossible')
        else:
            prob = Fraction(possibilities, n * n)
            print(prob.numerator, prob.denominator)
