# https://exercism.io/my/solutions/5a6b231b50ac4f6ab8f3391f87a62638

from math import sqrt


def is_palindrome(n):
    return int(str(n)[::-1]) == n


def palindrome_and_factors(max_factor, min_factor, largest=True):
    if max_factor < min_factor:
        raise ValueError('Invalid range')

    if largest:
        range_values = (max_factor**2, min_factor**2 - 1, -1)
    else:
        range_values = (min_factor**2, max_factor**2 + 1)

    for value in range(*range_values):
        if is_palindrome(value):
            factors = set()
            for f1 in range(min_factor, int(sqrt(value)) + 1):
                f2 = value // f1
                if value % f1 == 0 and f2 <= max_factor:
                    factors.add((f1, f2))
            if factors:
                return value, factors
    return None, []


def largest_palindrome(max_factor, min_factor):
    return palindrome_and_factors(max_factor, min_factor, largest=True)


def smallest_palindrome(max_factor, min_factor):
    return palindrome_and_factors(max_factor, min_factor, largest=False)
