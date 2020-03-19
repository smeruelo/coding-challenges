# https://exercism.io/my/solutions/8d8f2c7494514351862390ebf6b23271

from math import sqrt, floor
from textwrap import wrap


def dimensions(n):
    rows = round(sqrt(n))
    columns = rows if n == rows ** 2 else floor(sqrt(n)) + 1
    return rows, columns


def cipher_text(plain_text):
    normalized = ''.join([c for c in plain_text if c.isalnum()]).lower()
    if normalized == '':
        return ''

    rows, columns = dimensions(len(normalized))
    rectangle = wrap(normalized, columns)
    rectangle[-1] = rectangle[-1].ljust(columns, ' ')

    encoded = []
    for c in range(columns):
        encoded.append(''.join([rectangle[r][c] for r in range(rows)]))
    return ' '.join(encoded)
