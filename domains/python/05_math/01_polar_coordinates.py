#!/usr/bin/python2
# https://www.hackerrank.com/domains/python/py-math

from cmath import phase

if __name__ == '__main__':
    n = complex(raw_input())
    print abs(n)
    print phase(n)
