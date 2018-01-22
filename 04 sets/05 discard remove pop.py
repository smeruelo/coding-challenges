#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

if __name__ == '__main__':
    _ = input()
    s = set(map(int, raw_input().split()))
    for _ in range(int(raw_input())):
        command = raw_input().split()
        if command[0] == 'pop':
            s.pop()
        elif command[0] == 'remove':
            s.remove(int(command[1]))
        else:
            s.discard(int(command[1]))
    print sum(s)
