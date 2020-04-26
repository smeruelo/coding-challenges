# https://exercism.io/my/solutions/20a7c2954e6a41169511e7c43c6db132

from itertools import cycle


def _rail_index(rows):
    values = list(range(rows)) + list(range(rows-2, 0, -1))
    return cycle(values)


def encode(plain, rows):
    rails = [[] for _ in range(rows)]
    index_gen = _rail_index(rows)
    for char in plain:
        rails[next(index_gen)].append(char)
    return ''.join(''.join(rail) for rail in rails)


def decode(encoded, rows):
    def lengths():
        index_gen = _rail_index(rows)
        rail_indexes = [next(index_gen) for _ in range(len(encoded))]
        return (rail_indexes.count(r) for r in range(rows))

    def split(lengths):
        rails = []
        begin = 0
        for l in lengths:
            rails.append(list(reversed(encoded[begin:begin+l])))
            begin += l
        return rails

    rails = split(lengths())
    decoded = []
    index_gen = _rail_index(rows)
    for _ in range(len(encoded)):
        decoded.append(rails[next(index_gen)].pop())
    return ''.join(decoded)
