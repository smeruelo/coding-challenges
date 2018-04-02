#!/usr/bin/python3
# https://abc074.contest.atcoder.jp/tasks/abc074_b

def distance(balls, k):
    total = 0
    for x in balls:
        total += 2 * min(x, abs(x - k))
    return total


if __name__ == '__main__':
    _ = input()
    k = int(input())
    balls = map(int, input().split())
    print(distance(balls, k))
