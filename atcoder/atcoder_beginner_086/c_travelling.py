#!/usr/bin/python3
# https://abc086.contest.atcoder.jp/tasks/arc089_a

n = int(input())
t1, x1, y1 = 0, 0, 0
feasible = True
for _ in range(n):
    t2, x2, y2 = map(int, input().split())
    movements = abs(x2 - x1) + abs(y2 - y1)
    if movements > (t2 - t1) or movements % 2 != (t2 - t1) % 2:
        feasible = False
    t1, x1, y1 = t2, x2, y2
print('Yes') if feasible else print('No')
