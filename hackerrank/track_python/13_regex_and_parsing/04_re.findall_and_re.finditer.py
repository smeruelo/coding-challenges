#!/usr/bin/python2
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

if __name__ == '__main__':
    # regex = re.compile(r'([BCDFGHJKLMNPQRSTVWXYZ])([AEIOU]{2,})(?=[BCDFGHJKLMNPQRSTVWXYZ])', re.IGNORECASE)
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'AEIOU'
    regex = re.compile(r'([' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', re.I)
    matches = map(lambda x: x.group(2), re.finditer(regex, raw_input()))
    print '\n'.join(matches) if matches else '-1'
