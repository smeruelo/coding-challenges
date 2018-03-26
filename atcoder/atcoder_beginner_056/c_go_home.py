#!/usr/bin/python3
# https://abc056.contest.atcoder.jp/tasks/arc070_a

def sum_naturals(n):
    return (n * (1 + n)) / 2

def jump(x):
    i = 0
    while x > sum_naturals(i):
        i += 1
    return i


if __name__ == '__main__':
    x = int(input())
    print(jump(x))
