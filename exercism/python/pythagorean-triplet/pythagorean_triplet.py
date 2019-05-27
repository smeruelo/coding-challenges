# https://exercism.io/my/solutions/c9fc1c47d12c46f189a86ae583ae861a


def is_pythagorean(triplet):
    a, b, c = triplet
    return a * a + b * b == c * c


def triplets_with_sum(sum_of_triplet):
    return {(a, b, sum_of_triplet - a - b)
            for a in range(1, sum_of_triplet)
            for b in range(a + 1, sum_of_triplet - a - 1)
            if is_pythagorean((a, b, sum_of_triplet - a - b))}
