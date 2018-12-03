#!/usr/bin/python3

import math
import os
import random
import re
import sys


def miSuperPila(operations):
    stack = []

    for op in operations:
        command = op.split()
        if command[0] == 'pop':
            stack.pop()
        elif command[0] == 'push':
            stack.append(int(command[1]))
        elif command[0] == 'inc':
            e = int(command[1])
            k = int(command[2])
            for i in range(0, min(e, len(stack))):
                stack[i] += k
        if stack:
            print(stack[-1])
        else:
            print('EMPTY')

if __name__ == '__main__':
    operations_count = int(input())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    miSuperPila(operations)
