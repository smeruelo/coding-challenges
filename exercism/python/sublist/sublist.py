# https://exercism.io/my/solutions/1f98af6e854d474880ce66253d26d782


SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(a, b):

    def sub(l1, l2):
        """Checks if l1 is a sublist of l2."""

        for i in range(0, len(l2)-len(l1)+1):
            if l1 == l2[i:i+len(l1)]:
                return True
        return False

    if len(a) < len(b) and sub(a, b):
        return SUBLIST
    if len(a) > len(b) and sub(b, a):
        return SUPERLIST
    if sub(a, b):
        return EQUAL
    return UNEQUAL
