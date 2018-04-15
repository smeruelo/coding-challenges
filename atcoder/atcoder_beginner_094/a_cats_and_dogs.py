#!/usr/bin/python3
# https://abc094.contest.atcoder.jp/tasks/abc094_a

a, b, x = map(int, input().split())
print('YES') if x >= a and x <= a + b else print('NO')
