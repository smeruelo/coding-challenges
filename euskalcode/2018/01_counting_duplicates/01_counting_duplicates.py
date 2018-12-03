#!/usr/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

def cuentaDuplicados(numbers):
    times = Counter(numbers)
    return sum(map(lambda x: times[x] > 1, times))


if __name__ == '__main__':
    fptr = sys.stdout

    numbers_count = int(input())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input())
        numbers.append(numbers_item)

    res = cuentaDuplicados(numbers)

    fptr.write(str(res) + '\n')

    fptr.close()
