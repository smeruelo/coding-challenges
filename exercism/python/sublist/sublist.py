
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
