#!/usr/bin/python3
# https://abc042.contest.atcoder.jp/tasks/arc058_a
# Unecessarily efficient! n < 10000, bruteforce would do

from functools import reduce

def obsession(n, disliked):
    def nearest(digit):
        for i in range(digit, digit + 10):
            mod10 = i % 10
            if mod10 not in disliked:
                return (mod10, i != mod10)

    will_pay = list(map(int, str(n)))
    index = 0
    while index < len(will_pay):
        digit = will_pay[index]
        if digit in disliked:
            substitute, carry = nearest(digit)
            will_pay[index] = substitute

            # Propagate zeroes (or nearest) to the right
            i = index + 1
            substitute, _ = nearest(0)
            while i < len(will_pay):
                will_pay[i] = substitute
                i += 1

            # Propagate carry to the left
            i = index - 1
            while carry and i >= 0:
                substitute, carry = nearest(will_pay[i] + 1)
                will_pay[i] = substitute
                i -= 1
            if carry:
                will_pay.insert(0, nearest(1)[0])
                index += 1
        index += 1
    return reduce(lambda x, y: x * 10 + y, will_pay, 0)


if __name__ == '__main__':
    n, _ = map(int, input().split())
    disliked = set(map(int, input().split()))
    print(obsession(n, disliked))
