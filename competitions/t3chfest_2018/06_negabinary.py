#!/usr/bin/python3

import random

def solution(A):
    A.append(0)
    for i in range(1, len(A), 2):
        A[i] = 0 if A[i] == 1 else 1  # f(a)
    carry = 1
    for i in range(len(A)):
        result = A[i] + (i % 2) + carry  # + f(0) + 1
        A[i] = result % 2
        carry = result // 2
    if carry:
        A.append(1)
    for i in range(0, len(A), 2):
        A[i] = 0 if A[i] == 1 else 1  # g
    for i in range(len(A)-1, -1, -1): # remove zeros at the right
        if A[i] == 0:
            A.pop()
        else:
            break
    return A


if __name__ == '__main__':
    # Some tests
    print(solution([1, 0, 0, 1, 1]), [1, 1, 0, 1])
    print(solution([1, 1, 0, 1]), [1, 0, 0, 1, 1])
    print(solution([1, 0, 0, 1, 1, 0, 0, 0]))
    print(solution([]))
    for i in range(1000):
        print(i)
        a = [random.randint(0, 1) for i in range(100000)]
        b = solution(solution(a[:]))
        for i in range(len(a)-1, -1, -1): # remove zeros at the right
            if a[i] == 0:
                a.pop()
            else:
                break
        if a != b:
            print(a)
            print(b)
            print()
