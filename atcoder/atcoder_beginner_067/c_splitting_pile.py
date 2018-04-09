#!/usr/bin/python3
# https://abc067.contest.atcoder.jp/tasks/arc078_a

def split(a):
    raccoon = sum(a) - a[0]
    snuke = a[0]
    min_diff = abs(raccoon - snuke)
    for i in range(1, len(a) - 1):
        snuke += a[i]
        raccoon -= a[i]
        min_diff = min(min_diff, abs(snuke - raccoon))
    return min_diff


if __name__ == '__main__':
    _ = input()
    a = list(map(int, input().split()))
    print(split(a))
