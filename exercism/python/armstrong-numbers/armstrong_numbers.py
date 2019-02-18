#!/usr/bin/python3
# https://exercism.io/my/solutions/c0c3120a9b0e43abbb8505d8f8e29448


def is_armstrong(number):
    n = str(number)
    return sum([int(d) ** len(n) for d in n]) == number
