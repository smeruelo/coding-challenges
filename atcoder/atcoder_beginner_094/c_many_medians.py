#!/usr/bin/python3
# https://abc094.contest.atcoder.jp/tasks/arc095_a

def medians(nums, n):
    median_left = nums[(n + 1)//2]
    median_right = nums[(n + 1)//2 - 1]
    return median_left, median_right


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    median_left, median_right = medians(sorted(nums), n)
    for i in nums:
        print(median_left) if i < median_left else print(median_right)
