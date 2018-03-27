#!/usr/bin/python3
# https://abc053.contest.atcoder.jp/tasks/arc068_a

x = int(input())
rest = x % 11
if rest == 0:
    print((x // 11) * 2)
elif rest >= 7:
    print((x // 11) * 2 + 2)
else:
    print((x // 11) * 2 + 1)
