from itertools import combinations


def is_triplet(triplet):
    a, b, c = triplet
    return a * a + b * b == c * c


def triplets_with_sum(sum_of_triplet):
    combos = combinations(range(sum_of_triplet), 3)
    return {c for c in combos if sum(c) == sum_of_triplet and is_triplet(c)}
