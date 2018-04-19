#!/usr/bin/python3
# https://abc087.contest.atcoder.jp/tasks/abc087_b

from itertools import product

def ways(a, b, c, amount):
    combinations = list(product(range(a+1), range(b+1), range(c+1)))
    results = list(map(lambda x: 500 * x[0] + 100 * x[1] + 50 * x[2] == amount, combinations))
    return results.count(True)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    print(ways(a, b, c, x))
