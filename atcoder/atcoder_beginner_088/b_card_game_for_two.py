#!/usr/bin/python3
# https://abc088.contest.atcoder.jp/tasks/abc088_b

def game(a, n):
    cards = sorted(a, reverse=True)
    alice = [cards[i] for i in range(n) if i % 2 == 0]
    bob = [cards[i] for i in range(n) if i % 2 != 0]
    return sum(alice) - sum(bob)


if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    print(game(a, n))
