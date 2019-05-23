# https://exercism.io/my/solutions/805b23216fd94e838c12b96d2bcf3308

from math import sqrt


def factors(number):
    """Returns all factors of the given natural number."""

    if number <= 0:
        raise ValueError('Number is not a positive integer.')
    f = set()
    for i in range(1, 1 + int(sqrt(number))):
        if number % i == 0:
            f.add(i)
            f.add(number // i)
    return f


def classify(number):
    """Determines if a number is perfect/abundant/deficient."""

    s = sum(factors(number)) - number
    if s == number:
        return 'perfect'
    elif s > number:
        return 'abundant'
    else:
        return 'deficient'
