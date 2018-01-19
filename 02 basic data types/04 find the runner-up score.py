#!/usr/bin/python2
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    _ = raw_input()
    scores = map(int, raw_input().split())
    scores.sort(reverse = True)
    try:
        print filter(lambda x: x != scores[0], scores)[0]
    except IndexError:
        print "There's no runner-up."
