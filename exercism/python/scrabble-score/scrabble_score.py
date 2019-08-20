# https://exercism.io/my/solutions/892c952351e2435480417e9976c95ecd

KEYS = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T', 'D', 'G', 'B',
        'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
VALUES = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 8, 8, 10, 10]
POINTS = dict(zip(KEYS, VALUES))


def score(word):
    try:
        return sum(POINTS[c] for c in word.upper())
    except KeyError:
        raise Exception("Word includes non valid characters.")
