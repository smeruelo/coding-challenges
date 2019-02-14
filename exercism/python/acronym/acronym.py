#!/usr/bin/python3
# https://exercism.io/my/solutions/be2c49180e7d4869a5c0a4c61a008153

from string import ascii_letters


def abbreviate(words):
    no_hyphens = words.replace('-', ' ')
    letters_only = ''.join([c for c in no_hyphens if c in ascii_letters + ' '])
    return ''.join([str.upper(w[0]) for w in letters_only.split()])
