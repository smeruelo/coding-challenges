#!/usr/bin/python3

import math
import os
import random
import re
import sys

def traducir(phrase):
    def remove_format(w):
        word = w.lower()
        if word[-1] == '.':
            word = word[0:-1]
        return word

    def add_format(p):
        p[0] = p[0].capitalize()
        p[-1] = p[-1] + '.'
        return p

    words = map(remove_format, phrase.split())
    sorted_words = sorted(words, key=len)
    return ' '.join(add_format(sorted_words))


if __name__ == '__main__':
    fptr = sys.stdout

    frase = input()

    res = traducir(frase)

    fptr.write(res + '\n')

    fptr.close()
