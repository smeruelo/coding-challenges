#!/usr/bin/python3

from functools import reduce

def diff(s):
    def decimal(digits, base):
        return reduce(lambda x, y: x * base + y, digits)

    base = len(s)
    maximum = decimal([i for i in range(base - 1, -1, -1)], base)
    minimum = decimal([1, 0] + [i for i in range(2, base)], base)
    return maximum - minimum


if __name__ == '__main__':
    for i in range(int(input())):
        s = input()
        print('Case #{}: {}'.format(i + 1, diff(s)))
