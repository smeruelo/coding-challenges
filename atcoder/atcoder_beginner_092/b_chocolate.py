#!/usr/bin/python3
# https://abc092.contest.atcoder.jp/tasks/abc092_b

n = int(input())
d, pieces = map(int, input().split())
a = [int(input()) for _ in range(n)]
for ai in a:
    pieces += 1
    j = 1
    while (j * ai) + 1 <= d:
        pieces += 1
        j += 1
print(pieces)
