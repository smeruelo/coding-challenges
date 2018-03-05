#!/usr/bin/python2
# https://www.hackerrank.com/challenges/re-split/problem

regex_pattern = r"[.,]"

if __name__ == '__main__':
    import re
    print("\n".join(re.split(regex_pattern, raw_input())))
