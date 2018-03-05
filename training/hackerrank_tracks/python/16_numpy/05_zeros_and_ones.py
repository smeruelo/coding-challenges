#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy

if __name__ == '__main__':
    dimensions = tuple(map(int, raw_input().split()))
    print numpy.zeros(dimensions, dtype = numpy.int)
    print numpy.ones(dimensions, dtype = numpy.int)
