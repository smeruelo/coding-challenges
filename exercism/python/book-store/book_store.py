from functools import reduce


DISCOUNTS = [0, 0, 5, 10, 20, 25]
GROUP_PRICES = [8 * i * (100 - DISCOUNTS[i]) for i in range(len(DISCOUNTS))]


def price(grouping):
    return sum([GROUP_PRICES[len(g)] for g in grouping])


def group_hash(group):
    size = len(group)
    value = sum(group)
    return 100 * size + value

def grouping_hash(grouping):
    return sorted(map(group_hash, grouping))

def not_in(hashed_grouping, hashed_groupings):
    for g in hashed_groupings:
        if hashed_grouping == :
            return False
    return True

def uniques(groupings):
    """Given a list of groupings, it returns a list of those groupings that are not duplicated.
    It uses a hash function to represent groupings, so they can easily be ordered and compared."""
    nd = []
    hnd = []
    for g in groupings:
        hg = grouping_hash(g)
        if not_in(hg, hnd):
            hnd.append(hg)
            nd.append(g)
    return nd

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
    for book in basket:
        new_groupings = flatten(map(lambda g: add_book(g, book), groupings))
        groupings = uniques(new_groupings)

    # print(len(groupings))
    return min(map(price, groupings))
