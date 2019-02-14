#!/usr/bin/python3
# https://exercism.io/my/solutions/fb0fec300bdc4f5e81409cf243f96b12


from string import ascii_lowercase


ALPHABET_SET = set(ascii_lowercase)


def is_pangram(sentence):
    sentence_set = set(filter(lambda c: c in ascii_lowercase, str.lower(sentence)))
    return sentence_set == ALPHABET_SET
