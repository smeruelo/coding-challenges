#!/usr/bin/python3
# https://abc093.contest.atcoder.jp/tasks/arc094_a

smallest, medium, biggest = sorted(map(int, input().split()))
ops_1 = biggest - medium
ops_2 = (biggest - (smallest + ops_1)) // 2
rest = 2 * ((biggest - (smallest + ops_1)) % 2)
print(ops_1 + ops_2 + rest)
