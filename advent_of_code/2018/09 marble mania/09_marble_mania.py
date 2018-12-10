#!/usr/bin/pypy3
# https://adventofcode.com/2018/day/9

def play1(n, v):
    marbles = [0]
    points = [0] * (n + 1)
    current = 0
    for value in range(1, v + 1):
        if value % 23 == 0:
            i = (current - 7) % len(marbles)
            points[value % n] += marbles.pop(i)
            points[value % n] += value
        else:
            i = (current + 2) % len(marbles)
            marbles.insert(i, value)
        current = i
    return (max(points))

class Node():
    def __init__(self, value, prev=None, nxt=None):
        self.prev = prev
        self.nxt = nxt
        self.marble = value

def play2(n, v):
    current = Node(0)
    current.prev = current
    current.nxt = current
    points = [0] * (n + 1)
    for value in range(1, v + 1):
        if value % 23 == 0:
            removed = current.prev.prev.prev.prev.prev.prev.prev
            removed.prev.nxt = removed.nxt
            current = removed.nxt
            points[value % n] += removed.marble
            points[value % n] += value
        else:
            new = Node(value, current.nxt, current.nxt.nxt)
            current.nxt.nxt.prev = new
            current.nxt.nxt = new
            current = new
    return (max(points))


if __name__ == '__main__':
    print(play1(458, 71307))
    print(play2(458, 7130700))

