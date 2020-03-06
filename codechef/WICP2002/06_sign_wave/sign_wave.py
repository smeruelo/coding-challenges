#!/usr/bin/env python
# https://www.codechef.com/WICP2002/problems/WICP006


def count(S, C, K):
    # Zero points correspond to "whole" PIs, half PIs, PI quarters, PI eighths, ..
    zeros = [0] * (max(S, C) + 1)

    # In [0, 2*PI] there are 3 whole PIs, 2 half PIs, 4 PI quarters, ..
    def points(i):
        return 3 if i == 0 else 2 ** i

    for i in range(S):
        zeros[i] = S - i
    for c in range(C):
        zeros[c + 1] += 1
    return sum(map(lambda i, x: points(i) if x >= K else 0,  range(len(zeros)), zeros))


for _ in range(int(input())):
    s, c, k = map(int, input().split())
    print(count(s, c, k))
