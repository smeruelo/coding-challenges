#!/usr/bin/python2
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

from string import ascii_lowercase

def print_rangoli(n):
    letters = ascii_lowercase[0:n][::-1]
    for i in range(1, n + 1) + range(n - 1, 0, -1):
        padding = '-' * (2 * n - 2 * i)
        print padding + '-'.join(letters[0:i]) + '-'.join(letters[i-1::-1])[1:] + padding

if __name__ == '__main__':
    print_rangoli(int(raw_input()))
