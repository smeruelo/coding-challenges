#!/usr/bin/python3
# https://abc086.contest.atcoder.jp/tasks/abc086_b

from math import sqrt, floor

a, b = input().split()
n = int(a + b)
print('Yes') if floor(sqrt(n)) ** 2 == n else print('No')
