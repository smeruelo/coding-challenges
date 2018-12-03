#!/usr/bin/python3

import math
import os
import random
import re
import sys

def longitudSecuenciaMagica(s):
    vowels = {0:'a', 1:'e', 2:'i', 3:'o', 4:'u'}

    def aux(vowel, index, count):
        if vowel > 4:
            return count
        if index >= len(s):
            if vowel == 4:
                return count
            else:
                return 0
        if s[index] == vowels[vowel]:
            return aux(vowel, index+1, count+1)
        if vowel < 4 and s[index] == vowels[vowel+1]:
            return max(aux(vowel, index+1, count), aux(vowel+1, index+1, count+1))
        return aux(vowel, index + 1, count)

    return aux(0, 0, 0)


if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    res = longitudSecuenciaMagica(s)

    fptr.write(str(res) + '\n')

    fptr.close()
