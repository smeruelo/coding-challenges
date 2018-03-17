#!/usr/bin/python2
# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

def locate(k, s):
    regex = re.compile('(?=(' + k + '))')
    return [(m.start(1), m.end(1) - 1) for m in re.finditer(regex, s)]

if __name__ == '__main__':
    s = raw_input()
    k = raw_input()
    positions = locate(k, s)
    print '\n'.join(map(str, positions)) if positions else (-1, -1)
