#!/usr/bin/python3
# https://exercism.io/my/solutions/34f68f29449346e59df4e6d94d2f217f

from itertools import product
from random import shuffle
from string import ascii_uppercase, digits


letters = [''.join(p) for p in product(ascii_uppercase, ascii_uppercase)]
numbers = [''.join(p) for p in product(digits, digits, digits)]
names = [l + n for l, n in product(letters, numbers)]
shuffle(names)
NAMES = iter(names)


class Robot(object):
    def __init__(self):
        self.reset()

    def reset(self):
        try:
            self.name = next(NAMES)
        except StopIteration:
            raise Exception("No unique names available.")
