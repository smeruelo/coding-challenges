#!/usr/bin/python3
# https://beta.atcoder.jp/contests/abc099/tasks/abc099_b

a, b = map(int, input().split())
h = (b - a) * (b - a + 1) // 2
print(h - b)
