#!/usr/bin/python3
# https://abc098.contest.atcoder.jp/tasks/arc098_a

def directions(n, s):
    left = []
    right = []

    change = 0
    for p in s:
        if p == 'W':
            change += 1
        left.append(change)

    change = 0
    for p in s[::-1]:
        if p == 'E':
            change += 1
        right.append(change)
    right.reverse()

    return min(map(lambda x, y: x + y - 1, left, right))



if __name__ == '__main__':
    n = int(input())
    s = input()
    print(directions(n, s))
