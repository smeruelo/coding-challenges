#!/usr/bin/python3
# https://abc072.contest.atcoder.jp/tasks/arc082_a

from collections import Counter

def max_count(nums):
    nums_decr = map(lambda x: x - 1, nums)
    nums_incr = map(lambda x: x + 1, nums)
    counter = Counter(nums)
    counter.update(nums_decr)
    counter.update(nums_incr)
    return counter.most_common(1)[0][1]


if __name__ == '__main__':
    _ = input()
    nums = list(map(int, input().split()))
    print(max_count(nums))
