# https://exercism.io/my/solutions/32d94fec7b944f99b060a9b6424042e5


OPENING = '[{('
CLOSING = ']})'
MATCH = dict(zip(CLOSING, OPENING))


def is_paired(string):
    def aux(index, opened):
        if index == len(string):
            return not opened
        if string[index] in OPENING:
            return aux(index + 1, opened + string[index])
        if string[index] in CLOSING:
            if opened and opened[-1] == MATCH[string[index]]:
                return aux(index + 1, opened[:-1])
            return False
        return aux(index + 1, opened)

    return aux(0, '')
