#!/usr/bin/python3
# https://abc078.contest.atcoder.jp/tasks/abc078_b

# 2z + ny + z(n - 1) <= x
x, y, z = map(int, input().split())
print((x - z) // (y + z))

