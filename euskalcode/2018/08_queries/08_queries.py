#!/usr/bin/python3

import math
import os
import random
import re
import sys


def calcula(nums, maxes):
    sorted_nums = sorted(nums)
    sorted_maxes = sorted(zip(maxes, range(len(maxes))))

    i = 0
    count = 0
    out = []
    for m, j in sorted_maxes:
        while i < len(sorted_nums) and sorted_nums[i] <= m:
            count += 1
            i += 1
        out.append((j, count))
    return list(map(lambda x: x[1], sorted(out)))


if __name__ == '__main__':
    fptr = sys.stdout

    nums_count = int(input())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input())
        nums.append(nums_item)

    maxes_count = int(input())

    maxes = []

    for _ in range(maxes_count):
        maxes_item = int(input())
        maxes.append(maxes_item)

    res = calcula(nums, maxes)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
