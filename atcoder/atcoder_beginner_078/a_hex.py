#!/usr/bin/python3
# https://abc078.contest.atcoder.jp/tasks/abc078_a

a, b = input().split()
if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('=')
