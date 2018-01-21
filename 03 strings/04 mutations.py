#!/usr/bin/python2
# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    print mutate_string(s, int(i), c)
