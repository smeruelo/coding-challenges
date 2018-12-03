#!/usr/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

def numeroDeParejas(a, k):
    count = Counter(a)
    keys = list(filter(lambda x: x <= k // 2, sorted(count.keys())))

    pairs = 0
    for i in keys:
        if k - i in count.keys():
            pairs += 1

    if (k // 2) * 2 == k and count[k // 2] < 2:
        pairs -= 1

    return pairs


if __name__ == '__main__':
    fptr = sys.stdout

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    k = int(input())

    res = numeroDeParejas(a, k)

    fptr.write(str(res) + '\n')

    fptr.close()
