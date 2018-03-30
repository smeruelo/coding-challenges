#!/usr/bin/python3
# https://abc071.contest.atcoder.jp/tasks/abc071_b

from string import ascii_lowercase

def first_not_in(s):
    for c in ascii_lowercase:
        if c not in s:
            return c
    return None

if __name__ == '__main__':
    print(first_not_in(input()))
