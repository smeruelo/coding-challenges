#!/usr/bin/python2
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(s):
    stuart = kevin = 0
    for i, c in enumerate(s):
        if c in 'AEIOU':
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if stuart > kevin:
        print 'Stuart {}'.format(stuart)
    elif kevin > stuart:
        print 'Kevin {}'.format(kevin)
    else:
        print 'Draw'


if __name__ == '__main__':
    minion_game(raw_input())
