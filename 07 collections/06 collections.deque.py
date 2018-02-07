#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-collections-deque/problem

from collections import deque

if __name__ == '__main__':
    d = deque()
    for _ in range(int(raw_input())):
        command, _, arg = raw_input().partition(' ')
        if command == 'append':
            d.append(int(arg))
        elif command == 'appendleft':
            d.appendleft(int(arg))
        elif command == 'pop':
            d.pop()
        else:
            d.popleft()
    print ' '.join(map(str, d))
