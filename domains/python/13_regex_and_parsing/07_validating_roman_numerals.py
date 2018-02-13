#!/usr/bin/python2
# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re

if __name__ == '__main__':
    regex_pattern = r"(M{0,3})(CM|CD|(D?C{0,3}))(XC|XL|(L?X{0,3}))(IX|IV|(V?I{0,3}))$"
    print(str(bool(re.match(regex_pattern, raw_input()))))
