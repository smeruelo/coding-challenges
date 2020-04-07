from itertools import chain, permutations
from collections import Counter
from operator import add

DISCOUNTS = [0, 0, 5, 10, 20, 25]
GROUP_PRICES = [8 * i * (100 - DISCOUNTS[i]) for i in range(len(DISCOUNTS))]


def price(groups):
    return sum(GROUP_PRICES[g] for g in groups)


def best(groupings):
    _, i = min((p, i) for (i, p) in enumerate(map(price, groupings)))
    return groupings[i]


def total(basket):
    if len(basket) == 0:
        return 0

    quantities = sorted(Counter(basket).values(), reverse=True)
    num_groups = quantities[0]

    def aux(i, groups):
        if i == len(quantities):
            return price(groups)

        q = quantities[i]
        combos = set(permutations([True]*q + [False]*(num_groups-q), num_groups))
        possibilities = list(map(lambda c: list(map(add, c, groups)), combos))
        return aux(i+1, best(possibilities))

    return aux(1, [1]*num_groups)
