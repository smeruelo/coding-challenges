#!/usr/bin/python3
# https://abc081.contest.atcoder.jp/tasks/abc081_b

_ = input()
nums = list(map(int, input().split()))
count = 0
while all(map(lambda x: x % 2 == 0, nums)):
    count += 1
    nums = list(map(lambda x: x / 2, nums))
print(count)
