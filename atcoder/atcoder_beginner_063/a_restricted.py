#!/usr/bin/python3
# https://abc063.contest.atcoder.jp/tasks/abc063_a

a, b = map(int, input().split())
print(a + b) if a + b < 10 else print('error')
