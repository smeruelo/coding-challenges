#!/usr/bin/python2
# https://www.hackerrank.com/contests/womenscup/challenges/project-earth

def reaction_time(N, T):
    # N:    1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
    #      -1  -1  +2  +2  -3  -3  +4  +4  -5  -5  +6  +6  -7  -7  +8  +8
    # t:   -1  -2   0   2  -1  -4   0   4  -1  -6   0   6  -1  -8   0   8  (+ initial T)
    if N % 4 == 1:
        t = -1
    elif N % 4 == 2:
        t = - (N + 2) / 2
    elif N % 4 == 3:
        t = 0
    else:
        t = N / 2
    return T + t


if __name__ == '__main__':
    N, T = map(int, raw_input().split())
    print reaction_time(N, T)
