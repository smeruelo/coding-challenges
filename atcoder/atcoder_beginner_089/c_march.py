#!/usr/bin/python3
# https://abc089.contest.atcoder.jp/tasks/abc089_c

from itertools import combinations

names = [input() for _ in range(int(input()))]
march = [list(filter(lambda x: x[0] == c, names)) for c in 'MARCH']
ways = 0
for combo in combinations(march, 3):
    ways += len(combo[0]) * len(combo[1]) * len(combo[2])
print(ways)
