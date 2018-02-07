#!/usr/bin/python2
# https://www.hackerrank.com/challenges/python-mod-divmod/problem

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print a // b
    print a % b
    print divmod(a, b)
