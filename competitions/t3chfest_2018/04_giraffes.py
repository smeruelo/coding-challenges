#!/usr/bin/python3

def solution(A):
    count = 0
    s = sorted([(index, elem) for index, elem in enumerate(A)], key = lambda x: x[1])
    group_begin = 0
    while group_begin < len(s):
        i = group_begin
        group_end = s[i][0]
        while i < group_end:
            i += 1
            group_end = max(group_end, s[i][0])
        count += 1
        group_begin = group_end + 1
    return count
