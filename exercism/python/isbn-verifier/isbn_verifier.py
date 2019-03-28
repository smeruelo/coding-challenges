# https://exercism.io/my/solutions/6196ab96bd4e419fa6396ca79f1f1329

from string import digits


def verify(isbn):
    FORMULA_MULTIPLIERS = list(range(10, 0, -1))
    CHECK_DIGIT = 'xX'

    no_hyphens = list(filter(lambda c: c != '-', isbn))
    if len(no_hyphens) != 10:
        return False
    if no_hyphens[9] not in digits + CHECK_DIGIT:
        return False
    if any(map(lambda c: c not in digits, no_hyphens[:-1])):
        return False

    digits_only = map(lambda c: 10 if c in CHECK_DIGIT else int(c), no_hyphens)
    return sum(map(lambda x, y: x * y, digits_only, FORMULA_MULTIPLIERS)) % 11 == 0
