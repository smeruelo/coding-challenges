#!/usr/bin/python3
# https://abc098.contest.atcoder.jp/tasks/abc098_b

def max_common(n, s):
    maximum = 0
    for i in range(1, n):
        set_left = set(s[:i])
        set_right = set(s[i:])
        maximum = max(maximum, len(set_left.intersection(set_right)))
    return maximum


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(max_common(n, s))
