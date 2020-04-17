# https://exercism.io/my/solutions/3a6b9e2373e74456b1ae1e250c9a9e3c

from math import sqrt


def score(x, y):
    r = sqrt(x**2 + y**2)
    if r <= 1:
        return 10
    elif r <= 5:
        return 5
    elif r<=10:
        return 1
    return 0
