#!/usr/bin/python3
# https://exercism.io/my/solutions/55d439aa234544dcb5a8cc75b776dd7b


def is_isogram(string):
    letters = [c for c in string.lower() if c.isalpha()]
    return len(letters) == len(set(letters))
