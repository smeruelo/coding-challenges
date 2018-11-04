#!/usr/bin/python3
# https://www.codechef.com/NOV18B/problems/MAGICHF2

def log2(n):
    x = 1
    k = 0
    while x < n:
        x *= 2
        k += 1
    return k

def prob_coins(c, w):
    def aux(coins, weights, first):
        if weights == 0:
            return 1 / coins
        else:
            if first:
                return aux(2 * (coins // 4) + min(2, coins % 4), weights - 1, False)
            else:
                return aux((coins + 1) // 2, weights - 1, False)

    if c <= 2:
        return 1 / c
    else:
        return aux(c, w, True)


if __name__ == '__main__':
    for _ in range(int(input())):
        coins, weights = map(float, input().split())
        if weights >= log2(coins):
            if coins == 2:
                print("{0:.8f}".format(0.5))
            else:
                print("{0:.8f}".format(1))
        else:
            print("{0:.8f}".format(prob_coins(coins, weights)))
