#!/usr/bin/python3
# https://abc060.contest.atcoder.jp/tasks/abc060_a

a, b, c = input().split()
print('YES') if a[-1] == b[0] and b[-1] == c[0] else print('NO')
