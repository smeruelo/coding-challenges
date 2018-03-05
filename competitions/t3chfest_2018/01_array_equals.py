#!/usr/bin/python3

def solution(A):
    if A:
        even = list(map(lambda x: x % 2 == 0, A))
        if all(even) or not any(even):
            return (max(A) - min(A)) // 2
        else:
            return -1
    else:
        return 0
