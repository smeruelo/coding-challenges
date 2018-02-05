#!/usr/bin/python2
# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

def compress(s):
    pairs = []
    for key, group in groupby(s):
        pairs.append((len(list(group)), int(key)))
    return pairs

if __name__ == '__main__':
    s = raw_input()
    print ' '.join(map(str, compress(s)))

