#!/usr/bin/python3
# https://exercism.io/my/solutions/55d439aa234544dcb5a8cc75b776dd7b

from string import ascii_lowercase


def is_isogram(string):
    letters = [c for c in str.lower(string) if c in ascii_lowercase]
    return len(letters) == len(set(letters))
