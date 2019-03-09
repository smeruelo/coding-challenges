# task 3


def solution(A):
    octal = ''.join(map(str, reversed(A)))
    binary = bin(int(octal, 8))
    return binary.count('1')
