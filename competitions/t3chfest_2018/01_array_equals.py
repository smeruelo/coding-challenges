#!/usr/bin/python3

import random

def solution(A):
    if A:
        even = list(map(lambda x: x % 2 == 0, A))
        if all(even) or not any(even):
            return (max(A) - min(A)) // 2
        else:
            return -1
    else:
        return 0


if __name__ == '__main__':
    # Some tests
    print(solution([11,3,7,1]), 5)
    print(solution([0,1]), -1)
    print(solution([]), 0)
    print(solution([-8, -6, -2]), 3)
    print(solution([-11,-3,-7,-1]), 5)
    print(solution([-4, 0, 6]), 5)
    print(solution([7, 7, 7]), 0)
    for _ in range(10):
        print(solution([random.randint(-200000000, 200000000) for _ in range(20000)]))
