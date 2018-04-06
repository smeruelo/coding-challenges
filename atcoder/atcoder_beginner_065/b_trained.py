#!/usr/bin/python3
# https://abc065.contest.atcoder.jp/tasks/abc065_b

def buttons(n, paths):
    cont = 0
    button = 0
    for _ in range(n):
        if button == 1:
            return cont
        cont += 1
        button = paths[button]
    return -1


if __name__ == '__main__':
    n = int(input())
    print(buttons(n, [int(input()) - 1 for _ in range(n)]))
