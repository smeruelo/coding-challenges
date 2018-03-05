#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy

if __name__ == '__main__':
    p = numpy.array(map(float, raw_input().split()))
    x = float(raw_input())
    print numpy.polyval(p, x)
