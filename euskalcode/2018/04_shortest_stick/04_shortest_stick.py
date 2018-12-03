#!/usr/bin/python3

import math
import os
import random
import re
import sys

def juegoPalitos(sticks):
    out = []
    while sticks:
        out.append(len(sticks))
        minimum = min(sticks)
        sticks = list(map(lambda x: x - minimum, filter(lambda x: x != minimum, sticks)))
    return out


if __name__ == '__main__':
    fptr = sys.stdout

    lengths_count = int(input())

    lengths = []

    for _ in range(lengths_count):
        lengths_item = int(input())
        lengths.append(lengths_item)

    res = juegoPalitos(lengths)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
