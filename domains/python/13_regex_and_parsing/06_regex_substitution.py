#!/usr/bin/python2
# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

def no_symbols(text):
    def symbol_to_text(match):
        if match.group(1) == '&&':
            return 'and'
        elif match.group(1) == '||':
            return 'or'

    regex = re.compile('(?<= )(&&|\|\|)(?= )')
    return re.sub(regex, symbol_to_text, text)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print no_symbols(raw_input())
