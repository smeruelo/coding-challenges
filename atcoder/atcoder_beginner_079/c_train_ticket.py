#!/usr/bin/python3
# https://abc079.contest.atcoder.jp/tasks/abc079_c

from itertools import product

def solve(a, b, c, d):
    for ops in product('+-', repeat=3):
        op = a + ops[0] + b + ops[1] + c + ops[2] + d
        if eval(op) == 7:
            return op + '=7'


if __name__ == '__main__':
    a, b, c, d = input()
    print(solve(a, b, c, d))
