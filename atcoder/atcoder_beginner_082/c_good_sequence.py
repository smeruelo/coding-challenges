#!/usr/bin/python3
# https://abc082.contest.atcoder.jp/tasks/arc087_a

from collections import Counter

def goodify(a):
    nums = Counter(a)
    bads = 0
    for k, v in nums.items():
        if v >= k:
            bads += v - k
        else:
            bads += v
    return bads


if __name__ == '__main__':
    _ = input()
    a = Counter(map(int, input().split()))
    print(goodify(a))
