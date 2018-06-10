#!/usr/bin/pypy3
# https://beta.atcoder.jp/contests/abc099/tasks/abc099_c

from math import log

def exp(n, base):
    e = int(log(n, base))
    if base ** (e + 1) <= n:
        return e + 1
    else:
        return e

def min_withdraw(n):
    if n < 6:
        return n
    else:
        exp_nine = exp(n, 9)
        exp_six = exp(n, 6)
        return 1 + min(min_withdraw(n - (6 ** exp_six)), min_withdraw(n - (9 ** exp_nine)))


if __name__ == '__main__':
    n = int(input())
    print(min_withdraw(n))
