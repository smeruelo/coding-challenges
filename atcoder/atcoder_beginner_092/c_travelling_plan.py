#!/usr/bin/python3
# https://abc092.contest.atcoder.jp/tasks/arc093_a

def cost(a):
    total = 0
    for i in range(1, len(a)):
        total += abs(a[i] - a[i-1])
    return total

def cancel(a, i, total):
    prev = a[i-1]
    spot = a[i]
    nxt = a[i+1]
    if (nxt >= prev and spot < prev) or (nxt <= prev and spot > prev):
        return total - 2 * abs(prev - spot)
    if (nxt >= prev and spot > nxt) or (nxt <= prev and spot < nxt):
        return total - 2 * abs(nxt - spot)
    return total


if __name__ == '__main__':
    _ = int(input())
    a = [0] + list(map(int, input().split()))
    a.append(0)
    total = cost(a)
    for i in range(1, len(a)-1):
        print(cancel(a, i, total))
