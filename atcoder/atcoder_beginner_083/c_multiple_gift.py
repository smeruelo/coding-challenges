#!/usr/bin/python3
# https://abc083.contest.atcoder.jp/tasks/arc088_a

from math import log, floor
from random import randint

def formula(x, y):
    # This fails because of precision issues: log((2 ** 59) - 1) = 59
    return 1 + floor(log(y / x, 2))

def naive(x, y):
    count = 0
    n = x
    while n <= y:
        count += 1
        n *= 2
    return count


if __name__ == '__main__':
    x, y = map(int, input().split())
    print(naive(x, y))
    # for _ in range(10 ** 8):
    #     x = randint(1, 10 ** 18)
    #     y = randint(x, 10 ** 18)
    #     f = formula(x, y)
    #     n = naive(x, y)
    #     if f != n:
    #         print(x, y, f, n)
