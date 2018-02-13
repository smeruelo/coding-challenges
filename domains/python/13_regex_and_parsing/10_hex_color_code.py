#!/usr/bin/python2
# https://www.hackerrank.com/challenges/hex-color-code

import re

def colors(css):
    result = []
    for selector in re.finditer(r'\{((.*\n)*?)\}', css):
        for color in re.finditer(r'(#([0-9a-fA-F]{3}){1,2})', selector.group(1)):
            result.append(color.group(1))
    return result

if __name__ == '__main__':
    css = '\n'.join([raw_input() for _ in range(int(raw_input()))])
    for c in colors(css):
        print c
