#!/usr/bin/python3
# https://abc086.contest.atcoder.jp/tasks/abc086_a

a, b = map(int, input().split())
print('Even') if (a * b) % 2 == 0 else print('Odd')
