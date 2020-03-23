from functools import reduce


DISCOUNTS = [0, 0, 5, 10, 20, 25]
GROUP_PRICES = [8 * i * (100 - DISCOUNTS[i]) for i in range(len(DISCOUNTS))]


def price(grouping):
    return sum([GROUP_PRICES[len(g)] for g in grouping])


def add_book(grouping, book):
    new_groupings = [grouping + [{book}]]
    for i, group in enumerate(grouping):
        if book not in group:
            new_groupings.append(grouping[:i] + [group | {book}] + grouping[i+1:])
    return new_groupings


def flatten(lst):
    return reduce(lambda x, y: x + y, lst, [])


def total(basket):

    basket.sort()
    groupings = [[]]
    for i, book in enumerate(basket):
        groupings = flatten(map(lambda x: add_book(x, book), groupings))

    print(len(groupings))
    return min(map(price, groupings))
