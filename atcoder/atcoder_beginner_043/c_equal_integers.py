#!/usr/bin/python3
# https://abc043.contest.atcoder.jp/tasks/arc059_a

def equalize_cost(numbers):
    average = round(sum(numbers) / len(numbers))
    return sum(map(lambda x: (x - average) ** 2, numbers))


if __name__ == '__main__':
    _ = input()
    numbers = list(map(int, input().split()))
    print(equalize_cost(numbers))
