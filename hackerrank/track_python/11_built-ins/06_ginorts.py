#!/usr/bin/python2
# https://www.hackerrank.com/challenges/ginorts/problem

import string

def my_cmp(c1, c2):
    if c1 in string.ascii_lowercase and c2 in string.ascii_lowercase:
        return cmp(c1, c2)
    if c1 in string.ascii_uppercase and c2 in string.ascii_uppercase:
        return cmp(c1, c2)
    if c1 in string.digits and c2 in string.digits:
        if int(c2) % 2 == int(c1) % 2:
            return cmp(c1, c2)
        else:
            return int(c2) % 2 - int(c1) % 2
    return -1 * cmp(c1, c2)

if __name__ == '__main__':
    print reduce(lambda x, y: x + y, sorted(raw_input(), my_cmp))
