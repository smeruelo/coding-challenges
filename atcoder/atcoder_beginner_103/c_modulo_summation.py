#!/usr/bin/python3
# https://abc103.contest.atcoder.jp/tasks/abc103_c

import sys

sys.setrecursionlimit(3100)


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(l):
    def aux(l, i):
        if i == len(l) - 1:
            return l[-1]
        rest = aux(l, i+1)
        return l[i] * rest // gcd(l[i], rest)
    return aux(l, 0)

def modsum(a):
    k = lcm(a) - 1
    return sum(map(lambda x: k % x, a))

if __name__ == '__main__':
    _ = input()
    a = list(map(int, input().split()))
    print(modsum(a))
