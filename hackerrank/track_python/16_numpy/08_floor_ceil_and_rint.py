#!/usr/bin/python2
# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

import numpy

if __name__ == '__main__':
    arr = numpy.array(map(float, raw_input().split()))
    print numpy.floor(arr)
    print numpy.ceil(arr)
    print numpy.rint(arr)
