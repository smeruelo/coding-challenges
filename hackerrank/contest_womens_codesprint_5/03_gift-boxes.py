#!/usr/bin/python2
# https://www.hackerrank.com/contests/womens-codesprint-5/challenges/gift-boxes

# Score: 39.58 out of 45 (20 cases ok; 3 give timeout)

import re

def giftBoxes(g, c):
    boxes = 0
    conveyor, match = re.subn(g, '', c, count=1)
    while match:
        boxes += 1
        conveyor, match = re.subn(g, '', conveyor, count=1)
    return boxes

if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        g = raw_input()
        c = raw_input()
        print giftBoxes(g, c)
