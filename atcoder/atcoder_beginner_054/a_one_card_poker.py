#!/usr/bin/python3
# https://abc054.contest.atcoder.jp/tasks/abc054_a

a, b = list(map(lambda x: 21 if int(x) == 1 else int(x), input().split()))
if a > b:
    print('Alice')
elif b > a:
    print('Bob')
else:
    print('Draw')
