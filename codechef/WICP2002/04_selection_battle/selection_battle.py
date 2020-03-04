#!/usr/bin/env python
# https://www.codechef.com/WICP2002/problems/WICP003


from math import sqrt
from sys import stdin


def read():
    input_data = stdin.read().split()
    for token in input_data:
        yield token


def is_prime(n):
    for i in range(int(sqrt(n)), 1, -1):
        if n % i == 0:
            return False
    return True


reader = read()
for _ in range(int(next(reader))):
    if is_prime(int(next(reader))):
        print('Divesh')
    else:
        print('Tanya')
