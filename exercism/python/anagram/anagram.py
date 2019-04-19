#!/usr/bin/python3
# https://exercism.io/my/solutions/610deb702acc45ed859259f2e737f45c


def find_anagrams(word, candidates):
    w = word.lower()
    s = sorted(w)
    return list(filter(lambda c: c.lower() != w and sorted(c.lower()) == s, candidates))
