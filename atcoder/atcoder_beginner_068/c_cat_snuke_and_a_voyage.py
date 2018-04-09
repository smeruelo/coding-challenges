#!/usr/bin/python3
# https://abc068.contest.atcoder.jp/tasks/arc079_a

def read_boats(n, m):
    boats = [[] for i in range(max(n, m) + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        boats[a].append(b)
    return boats

def trip(n, boats):
    for origin in boats[1]:
        if n in boats[origin]:
            return('POSSIBLE')
    return('IMPOSSIBLE')


if __name__ == '__main__':
    n, m = map(int, input().split())
    boats = read_boats(n, m)
    print(trip(n, boats))
