# https://exercism.io/my/solutions/09770b6fe3e04b8bb2070008e26f194d

# Iterative approach.
# In a recursive approach, we used memoization to reduce the number of recursive calls
# from 2^n, to (n+1)(max_weight+1)
# memo[i][x] = max total value adding the first i items, considering a max capacity of x
# Knowing this, we can directly build this matrix, in a bottom-up way


def maximum_value(maximum_weight, items):
    n = len(items)
    memo = [[0] * (maximum_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = items[i - 1]["weight"]
        value = items[i - 1]["value"]
        for x in range(maximum_weight + 1):
            omiting_item = memo[i - 1][x]
            including_item = value + memo[i - 1][x - weight] if x - weight >= 0 else 0
            memo[i][x] = max(omiting_item, including_item)

    return memo[n][maximum_weight]
