#!/usr/bin/python3

# Given an integer array A find how many complementary pairs there are in A
# A pair (i, j) is K-complementary if A[i] + A[j] = K
# For example given the array [2, 5, -1, 6, 10, -2] and an integer K = 4 the result must be 5
# The 5 pairs are (0, 0), (1, 2), (2, 1), (3, 5), (5, 3)

from collections import Counter

def solution(K, A):
    dict_a = Counter(A)
    count = 0
    for i in dict_a:
        if (K - i) in dict_a:
            count += dict_a[i] * dict_a[K - i]
    return count
