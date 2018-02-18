#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy

if __name__ == '__main__':
    rows, cols = tuple(map(int, raw_input().split()))
    print numpy.eye(rows, cols, 0)
