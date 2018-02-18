#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy

def matrix(l):
    return numpy.reshape(numpy.array(l), (3, 3))

if __name__ == '__main__':
    print matrix(map(int, raw_input().split()))
