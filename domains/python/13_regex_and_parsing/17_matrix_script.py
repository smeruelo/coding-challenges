#!/usr/bin/python2
# https://www.hackerrank.com/challenges/matrix-script/problem

import re

def decode(text_matrix):
    transposed = ''.join(map(lambda x: ''.join(x), zip(*text_matrix)))
    regex = re.compile(r'(?<=[a-zA-Z0-9])([ !@#$%&])+(?=[a-zA-Z0-9])')
    return re.sub(regex, ' ', transposed)

rows, columns = map(int, raw_input().split())
text_matrix = [raw_input() for _ in range(rows)]
print decode(text_matrix)
