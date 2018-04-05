#!/usr/bin/python3
# https://abc061.contest.atcoder.jp/tasks/abc061_a

a, b, c = map(int, input().split())
print('Yes') if c >= a and c <= b else print('No')
