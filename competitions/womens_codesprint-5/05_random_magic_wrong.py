#!/usr/bin/python2
# https://www.hackerrank.com/contests/womens-codesprint-5/challenges/random-magic

def magic(s, c):
    if s == 1:
        return 0
    else:
        n = s * c
        p = (s * (s - 1)) / (n * (n - 1))              # 2 kings
        q = (s * (s - 1)) / ((n - 2) * (n - 3))        # 2 queens
        k = ((n - 4) * (n - 1)) + 2
        p3k = (s * (s - 1) * (s - 2)) / (n * (n - 1))  # 3 kings
        return (k * p * q) - p3k

if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        s, c = map(float, raw_input().split())
        print magic(s, c)
