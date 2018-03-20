#!/usr/bin/python3
# https://abc048.contest.atcoder.jp/tasks/arc064_a

def eat_candies(candies, x):
    eaten = max(0, candies[0] - x)
    candies[0] -= eaten
    for i in range(1, len(candies)):
        extra = max(0, candies[i-1] + candies[i] - x)
        candies[i] -= extra
        eaten += extra
    return


if __name__ == '__main__':
    n, x = list(map(int, input().split()))
    candies = list(map(int, input().split()))
    print(eat_candies(candies, x))
