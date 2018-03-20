#!/usr/bin/python3
# https://abc048.contest.atcoder.jp/tasks/abc048_b

a, b, x = list(map(int, input().split()))
biggest = b // x
lowest = (a + x - 1) // x
print(biggest - lowest + 1)
