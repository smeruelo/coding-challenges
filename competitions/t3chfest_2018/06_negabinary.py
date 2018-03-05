#!/usr/bin/python3

# We are given a really big string that represents a negabinary number A
# (https://en.wikipedia.org/wiki/Negative_base)
# We must return -A, also in negabinary format

# https://math.stackexchange.com/questions/2303280/proof-of-negative-negabinary-addition-formula
# -(a + b) = g(f(a) + f(b) + 1)  --------->  -a = g(f(a) + f(0) + 1)
#                                  b = 0
# f = negate odd bits
# g = negate even bits

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
