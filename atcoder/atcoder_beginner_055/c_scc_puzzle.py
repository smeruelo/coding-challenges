#!/usr/bin/python3
# https://abc055.contest.atcoder.jp/tasks/arc069_a

s, c = map(int, input().split())
print(c // 2) if s >= c // 2 else print(s + (c - 2 * s) // 4)
