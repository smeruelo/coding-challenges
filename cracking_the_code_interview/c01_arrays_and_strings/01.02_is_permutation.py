# Problem: Check Permutation
# Given two strings, write a method to decide if one is
# a permutation of the other.

from collections import Counter


# O(n)
def is_permutation_1(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    return c1 == c2

# O(n log n)
def is_permutation_2(s1, s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))
