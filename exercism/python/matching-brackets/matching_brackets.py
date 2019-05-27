# https://exercism.io/my/solutions/32d94fec7b944f99b060a9b6424042e5


OPENING = '[{('
CLOSING = ']})'
MATCH = dict(zip(CLOSING, OPENING))


def is_paired(string):
    opened = []
    for c in string:
        if c in OPENING:
            opened.append(c)
        if c in CLOSING:
            if not opened or MATCH[c] != opened[-1]:
                return False
            opened.pop()
    return not opened
