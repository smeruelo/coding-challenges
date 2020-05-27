# https://exercism.io/my/solutions/09770b6fe3e04b8bb2070008e26f194d

# Recursive approach
# Using memoization, we reduce the number of recursive calls from 2^n, to (n+1)(max_weight+1)
# memo[i][x] = max total value adding the first i items, considering a max capacity of x


def maximum_value(maximum_weight, items):

    def rec(i, x):
        if memo[i][x] is not None:
            return memo[i][x]

        if i == 0:
            memo[i][x] = 0
            return 0

        weight = items[i - 1]["weight"]
        value = items[i - 1]["value"]
        omiting_item = rec(i - 1, x)
        including_item = value + rec(i - 1, x - weight) if x - weight >= 0 else 0
        memo[i][x] = max(omiting_item, including_item)
        return memo[i][x]

    n = len(items)
    memo = [[None] * (maximum_weight + 1) for _ in range(n + 1)]
    return rec(n, maximum_weight)
