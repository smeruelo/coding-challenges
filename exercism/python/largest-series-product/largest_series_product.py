# https://exercism.io/my/solutions/191eb72342b040439fb0eda6bc4b027d

from functools import reduce
from operator import mul


def slices(series, size):
    if len(series) < size or size < 0:
        raise ValueError('Invalid size.')

    return [series[i:i+size] for i in range(len(series) - size + 1)]


def largest_product(series, size):
    def product(s):
        return reduce(mul, map(int, s), 1)

    return max(map(product, slices(series, size)))
