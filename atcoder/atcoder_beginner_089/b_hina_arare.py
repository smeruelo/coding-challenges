#!/usr/bin/python3
# https://abc089.contest.atcoder.jp/tasks/abc089_b

_ = input()
print('Four') if len(set(input().split())) == 4 else print('Three')
