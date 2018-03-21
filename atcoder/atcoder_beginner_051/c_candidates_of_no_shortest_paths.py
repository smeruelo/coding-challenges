#!/usr/bin/python3
# https://abc051.contest.atcoder.jp/tasks/abc051_c

sx, sy, tx, ty = list(map(int, input().split()))
forth1 = 'U' * (ty - sy) + 'R' * (tx - sx)
back1 = 'D' * (ty - sy) + 'L' * (tx - sx)
forth2 = 'L' + 'U' * (ty - sy + 1) + 'R' * (tx - sx + 1) + 'D'
back2 = 'R' + 'D' * (ty - sy + 1) + 'L' * (tx - sx + 1) + 'U'
print(forth1 + back1 + forth2 + back2)
