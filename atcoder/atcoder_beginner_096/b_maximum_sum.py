#!/usr/bin/python3
# https://abc096.contest.atcoder.jp/tasks/abc096_b

nums = list(map(int, input().split()))
k = int(input())

m = (2 ** k) * max(nums)
r = sum(nums) - max(nums)
print(m + r)

