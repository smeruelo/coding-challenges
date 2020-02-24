
"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(a, b):

    def aux(a, b, ib_ini):
        """Checks if a is a sublist of b."""
        if a == []:
            return True
        if len(a) > len(b) - ib_ini:
            return False

        ia = 0
        try:
            ib = b.index(a[0], ib_ini)
        except ValueError:
            return False

        while ib < len(b) and ia < len(a) and a[ia] == b[ib]:
            ia += 1
            ib += 1
        if ia == len(a):
            return True
        if ib == len(b):
            return False
        return aux(a, b, ib_ini + ia)

    if len(a) < len(b) and aux(a, b, 0):
        return SUBLIST
    elif len(b) < len(a) and aux(b, a, 0):
        return SUPERLIST
    elif aux(a, b, 0):
        return EQUAL
    return UNEQUAL
