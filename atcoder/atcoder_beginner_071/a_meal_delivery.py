#!/usr/bin/python3
# https://abc071.contest.atcoder.jp/tasks/abc071_a

x, a, b = map(int, input().split())
print('A') if abs(x - a) < abs(x - b) else print('B')
