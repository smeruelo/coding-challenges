#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == '__main__':
    _ = raw_input(); a = set(map(int, raw_input().split()))
    for _ in range(int(raw_input())):
        command, _ = raw_input().split()
        arg = set(map(int, raw_input().split()))
        if command == 'update':
            a.update(arg)
        elif command == 'intersection_update':
            a.intersection_update(arg)
        elif command == 'difference_update':
            a.difference_update(arg)
        else:
            a.symmetric_difference_update(arg)
    print sum(a)
