#!/usr/bin/python2
# https://www.hackerrank.com/challenges/any-or-all/problem

def palindrome(s):
    reverse = s[::-1]
    return s == reverse

if __name__ == '__main__':
    _ = raw_input()
    numbers = raw_input().split()
    print all(map(lambda x: int(x) >= 0, numbers)) and any(map(palindrome, numbers))
