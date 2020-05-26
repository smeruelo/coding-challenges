# https://exercism.io/my/solutions/7f830a8092344275abdb9aa20eeaf314

COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
CODES = dict(zip(COLORS, range(len(COLORS))))


def value(colors):
    return CODES[colors[0]] * 10 + CODES[colors[1]]
