# https://exercism.io/my/solutions/1edf06f8150c4020a5c75f3586c3ba44

import sys

sys.setrecursionlimit(4000)


def min_num_coins(coins, target, memo):
    if target in memo:
        return memo[target]

    pos = list(filter(lambda x: x[0] is not None,
                      map(lambda t: (None, None) if t[0] < 0 else (min_num_coins(coins, t[0], memo)[0], t[1]),
                          ((target - c, c) for c in coins))))
    if pos == []:
        memo[target] = (None, None)
    else:
        memo[target] = min(map(lambda x: (x[0] + 1, x[1]), pos))
    return memo[target]


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError('Negative value given.')
    memo = {0: (0, None)}
    used_coins = []
    t = target
    num, first = min_num_coins(coins, target, memo)
    if num is None:
        raise ValueError('Impossible combination.')
    while first is not None:
        used_coins.append(first)
        t -= first
        _, first = memo[t]
    return used_coins
