#!/usr/bin/python3

import random

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


if __name__ == '__main__':
    # Some tests
    print(solution([1, 5, 4, 9, 8, 7, 12, 13, 14]), 6); print()
    print(solution([1, 5, 4, 11, 3, 9, 6, 7, 12, 13, 14]), 5); print()
    print(solution([3, 1, 2]), 1); print()
    print(solution([4, 3, 2, 6, 1]), 1); print()
    print(solution([]), 0); print()
    for _ in range(20):
        a = list(range(100000))
        aa = []
        for i in range(0, 100000, 4):
            chunk = a[i:i+4]
            random.shuffle(chunk)
            aa += chunk
        print(solution(aa))


