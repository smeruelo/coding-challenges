# https://exercism.io/my/solutions/6f3b13fcecf64674acca3c47c621f5f2


def sum_of_multiples(limit, multiples):
    return sum({m for i in multiples if i != 0 for m in range(i, limit, i)})
