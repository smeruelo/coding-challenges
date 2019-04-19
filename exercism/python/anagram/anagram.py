#!/usr/bin/python3
# https://exercism.io/my/solutions/610deb702acc45ed859259f2e737f45c

from collections import Counter


def find_anagrams(word, candidates):
    w = word.lower()
    c = Counter(w)
    return list(filter(lambda x: x.lower() != w and Counter(x.lower()) == c, candidates))
