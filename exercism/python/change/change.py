# https://exercism.io/my/solutions/1edf06f8150c4020a5c75f3586c3ba44


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError('Impossible.')

    # memo[X] = (n, c), where n is the min number of coins to sum X and c is the first of those coins
    memo = {0: (0, None)}
    for i in range(target):
        if i in memo:
            for c in coins:
                if i + c in memo:
                    memo[i + c] = min(memo[i + c], (memo[i][0] + 1, c))
                else:
                    memo[i + c] = (memo[i][0] + 1, c)

    if target not in memo:
        raise ValueError('Impossible.')

    used_coins = []
    t = target
    while t != 0:
        _, first = memo[t]
        used_coins.append(first)
        t -= first
    return used_coins
