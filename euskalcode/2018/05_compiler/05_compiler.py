#!/usr/bin/python3

import math
import os
import random
import re
import sys

def compila(values):
    def check(line):
        begin = '({['
        end = ')}]'
        match = {')':'(', '}':'{', ']':'['}

        stack = []
        for c in line:
            if c in begin:
                stack.append(c)
            if c in end:
                if stack and stack[-1] == match[c]:
                    stack.pop()
                else:
                    return 'NO'
        return 'NO' if stack else 'YES'

    return [check(line) for line in values]


if __name__ == '__main__':
    fptr = sys.stdout

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)

    res = compila(values)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()
