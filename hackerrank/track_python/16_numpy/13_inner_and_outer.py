#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy

if __name__ == '__main__':
    a = numpy.array(map(int, raw_input().split()))
    b = numpy.array(map(int, raw_input().split()))
    print numpy.inner(a, b)
    print numpy.outer(a, b)
