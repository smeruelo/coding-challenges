#!/usr/bin/python3
# https://abc058.contest.atcoder.jp/tasks/arc071_a

from collections import Counter
from string import ascii_lowercase

def biggest(s):
    common = ''
    for c in ascii_lowercase:
        if all(map(lambda d: c in d, s)):
            occurrences = min(map(lambda d: d[c], s))
            common += c * occurrences
    return common


if __name__ == '__main__':
    s = [Counter(input()) for _ in range(int(input()))]
    print(biggest(s))
