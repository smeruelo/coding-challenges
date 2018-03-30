#!/usr/bin/python3
# https://abc070.contest.atcoder.jp

from functools import reduce

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    t = [int(input()) for _ in range(int(input()))]
    print(reduce(lambda x, y: lcm(x, y), t))
