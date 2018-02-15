#!/usr/bin/python2
# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

import operator

def person_lister(f):
    def inner(people):
        return map(lambda p: f(p), sorted(people, key = lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [raw_input().split() for i in range(int(raw_input()))]
    print '\n'.join(name_format(people))
