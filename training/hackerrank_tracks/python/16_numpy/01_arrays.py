#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

def arrays(arr):
    # return numpy.flipud(numpy.array(arr, float))
    return numpy.array(arr, float)[::-1]

if __name__ == '__main__':
    arr = raw_input().strip().split(' ')
    print arrays(arr)
