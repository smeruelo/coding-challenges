#!/usr/bin/python3
# https://abc073.contest.atcoder.jp/tasks/abc073_b

groups = [list(map(int, input().split())) for _ in range(int(input()))]
print(sum(map(lambda x: x[1] - x[0] + 1 , groups)))
