# https://exercism.io/my/solutions/191eb72342b040439fb0eda6bc4b027d

from functools import reduce
from operator import mul


def largest_product(series, size):
    if len(series) < size or size < 0:
        raise ValueError('Invalid size.')

    digits = [int(c) for c in series]
    max_product = 0
    for j in range(size, len(digits) + 1):
        product = reduce(mul, digits[j-size:j], 1)
        max_product = max(product, max_product)
    return max_product
