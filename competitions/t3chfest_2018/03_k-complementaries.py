#!/usr/bin/python3

from collections import Counter

def solution(K, A):
    dict_a = Counter(A)
    count = 0
    for i in dict_a:
        if (K - i) in dict_a:
            count += dict_a[i] * dict_a[K - i]
    return count
