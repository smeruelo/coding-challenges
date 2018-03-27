#!/usr/bin/python3
# https://abc057.contest.atcoder.jp/tasks/abc057_c

from math import floor, sqrt

def divisors(n):
    div = [1]
    for i in range(2, 1 + floor(sqrt(n))):
        if n % i == 0:
            div.append(i)
    return div

def f(a, b):
    return max(len(str(a)), len(str(b)))


if __name__ == '__main__':
    n = int(input())
    minimum = len(str(n))
    for a in divisors(n):
        b = n // a
        minimum = min(minimum, f(a, b))
    print(minimum)
