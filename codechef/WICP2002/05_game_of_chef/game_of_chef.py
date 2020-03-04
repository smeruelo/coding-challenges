#!/usr/bin/env python
# https://www.codechef.com/WICP2002/problems/WICP005


# O(n^2) (it could be done in O(n), see Laaksonen)
def max_subarray(nums, n):
    best = 0
    for i in range(n):
        sum_subarray = 0
        for j in range(i, n):
            sum_subarray += nums[j]
            best = max(sum_subarray, best)
    return best


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    print(max_subarray(nums, n))
