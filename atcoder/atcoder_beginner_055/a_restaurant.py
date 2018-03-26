#!/usr/bin/python3
# https://abc055.contest.atcoder.jp/tasks/abc055_a

from math import floor

n = int(input())
print(800 * n - 200 * floor(n/15))
