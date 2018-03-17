#!/usr/bin/python2
# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

if __name__ == '__main__':
    d = OrderedDict()
    for _ in range(int(raw_input())):
        word = raw_input()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    print len(d)
    print ' '.join(map(str, d.values()))


