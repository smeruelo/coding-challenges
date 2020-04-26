# https://exercism.io/my/solutions/20a7c2954e6a41169511e7c43c6db132

from itertools import cycle


def _rail_index(rows):
    values = list(range(rows)) + list(range(rows-2, 0, -1))
    return cycle(values)


def encode(plain, rows):
    index_gen = _rail_index(rows)
    return ''.join(sorted(plain, key=lambda _: next(index_gen)))


def decode(encoded, rows):
    index_gen = _rail_index(rows)
    indexes = sorted(range(len(encoded)), key=lambda _: next(index_gen))
    decoded = [''] * len(encoded)
    for i, char in zip(indexes, encoded):
        decoded[i] = char
    return ''.join(decoded)
