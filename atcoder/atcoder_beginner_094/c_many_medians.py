#!/usr/bin/python3
# https://abc094.contest.atcoder.jp/tasks/arc095_a

def medians(nums):
    n = len(nums)
    num_orig_pos = list(zip(nums, range(n)))
    nums_sorted = sorted(num_orig_pos)
    medians = []
    med_left = nums_sorted[(n + 1)//2][0]
    med_right = nums_sorted[(n + 1)//2 - 1][0]
    for i in range((n + 1)//2):
        medians.append((med_left, nums_sorted[i][1]))
    for i in range((n + 1)//2, n):
        medians.append((med_right, nums_sorted[i][1]))
    return map(lambda x: x[0], sorted(medians, key=lambda x: x[1]))


if __name__ == '__main__':
    _ = input()
    nums = list(map(int, input().split()))
    for i in medians(nums):
        print(i)
