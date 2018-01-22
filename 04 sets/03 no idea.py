#!/usr/bin/python2
# https://www.hackerrank.com/challenges/no-idea/problem

def happiness(array, a, b):
    return sum([(i in a) - (i in b) for i in array])
    # happiness = 0
    # for i in array:
    #     if i in a:
    #         happiness += 1
    #     elif i in b:
    #         happiness -= 1
    # return happiness

if __name__ == '__main__':
    _ = raw_input()
    array = map(int, raw_input().split())
    a = set(map(int, raw_input().split()))
    b = set(map(int, raw_input().split()))
    print happiness(array, a, b)
