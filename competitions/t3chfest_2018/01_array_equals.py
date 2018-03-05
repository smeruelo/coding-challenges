#!/usr/bin/python3

# On every step, the numbers in the array A can be independently incremented or decremented by 1
# For a given array, return the number of steps needed so that all numbers in the array are equal
# If not possible, return -1
# Example: [11, 3, 7, 1] becomes [6, 6, 6, 6] in 5 steps:
# [11, 3, 7, 1], [10, 4, 6, 2], [9, 5, 5, 3], [8, 6, 6, 4], [7, 5, 5, 5], [6, 6, 6, 6]

def solution(A):
    if A:
        even = list(map(lambda x: x % 2 == 0, A))
        if all(even) or not any(even):
            return (max(A) - min(A)) // 2
        else:
            return -1
    else:
        return 0
