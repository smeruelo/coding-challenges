#!/usr/bin/python3
# https://abc071.contest.atcoder.jp/tasks/arc081_a

from collections import Counter

def max_rectangle(sticks):
    # sticks ordered by length, only if there's at least two of a kind
    valid_lengths = list(filter(lambda x: sticks[x] >= 2, sorted(sticks, reverse=True)))
    if valid_lengths and sticks[valid_lengths[0]] >= 4:
        return valid_lengths[0] ** 2
    if len(valid_lengths) >= 2:
        return valid_lengths[0] * valid_lengths[1]
    return 0


if __name__ == '__main__':
    _ = input()
    sticks = Counter(map(int, input().split()))
    print(max_rectangle(sticks))
