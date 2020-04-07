# https://exercism.io/my/solutions/02552bfac69a40ebb745c2212197dcd4

from itertools import permutations
from collections import Counter
from operator import add

DISCOUNTS = [0, 0, 5, 10, 20, 25]
GROUP_PRICES = [8 * i * (100 - DISCOUNTS[i]) for i in range(len(DISCOUNTS))]


def total(books):
    """Calculates the minimum price for a series of books, by checking all the possibilities."""

    def price(basket):
        """Returns the price of a basket of books. A basket is a tuple where each element:
        - represents a group of books
        - its value is the number of different books that form the group."""
        return sum(GROUP_PRICES[g] for g in basket)

    if len(books) == 0:
        return 0

    # Let's calculate all the possible baskets
    # Baskets will have as many groups as books of the most repeated kind
    quantities = sorted(Counter(books).values(), reverse=True)
    num_groups = quantities[0]

    # For each book kind, calculate how can we distribute them among the groups of a basket (combos)
    # Since discounts are not based on the specific book types but only on their amounts,
    # we can sort these amounts to be able to rule out same-price baskets.
    baskets = set([tuple([1]*num_groups)])
    for q in quantities[1:]:
        combos = set(permutations([1]*q + [0]*(num_groups - q), num_groups))
        baskets = set(tuple(sorted(map(add, b, c))) for c in combos for b in baskets)

    return min(map(price, baskets))
