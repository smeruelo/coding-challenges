#!/usr/bin/python2
# https://www.hackerrank.com/challenges/python-print/problem

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    print(*range(1, n + 1), sep = '')
