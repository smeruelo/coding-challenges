#!/usr/bin/python2
# https://www.hackerrank.com/contests/womenscup/challenges/possible-maximum

# # Brute force, use PyPy to avoid timeouts
# def possible_max(n, k):
#     maximum = -1
#     for a in xrange(n, 0, -1):
#         if a <= maximum:
#             break
#         for b in xrange(a - 1, 0, -1):
#             if a & b < k:
#                 maximum = max(maximum, a & b)
#     return maximum

def possible_max(n, k):
    def x():
        # given a bin number, finds the 1st 0 to the right and switch it to 1
        binary = bin(k - 1)
        first_zero = len(binary) - binary[:1:-1].find('0')
        return int(binary[0:first_zero-1] + '1' + binary[first_zero:], 2)

    if k % 2 == 1:
        # k - 1 is even -->  k - 1 & k = k - 1, the highest possible value
        return k - 1
    else:
        # k - 1 is odd --> x = find first 0 in k - 1 (right to left) and switch it to 1 (x will be > k)
        # k - 1 & x     = k - 1
        # k - 1 & k - 2 = k - 2
        if x() <= n:
            return k - 1
        else:
            return k - 2


if __name__ == '__main__':
    for _ in xrange(int(raw_input())):
        n, k = map(int, raw_input().split())
        print possible_max(n, k)
