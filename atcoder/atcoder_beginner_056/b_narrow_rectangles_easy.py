#!/usr/bin/python3
# https://abc056.contest.atcoder.jp/tasks/abc056_b

w, a, b = map(int, input().split())
if b >= a and b <= (a + w):
    print(0)
else:
    print(min(abs(b - a - w), abs(a - b - w)))
