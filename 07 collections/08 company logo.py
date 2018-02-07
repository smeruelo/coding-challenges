#!/usr/bin/python2
# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

def frecuencies(s):
    def value_then_key((k1, v1), (k2, v2)):
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        elif k1 > k2:
            return -1
        elif k1 < k2:
            return 1
        else:
            return 0

    letters = Counter(s).items()
    return sorted(letters, cmp = value_then_key, reverse = True)


if __name__ == '__main__':
    s = raw_input()
    print '\n'.join(['{} {}'.format(k, str(v)) for (k, v) in frecuencies(s)[0:3]])
