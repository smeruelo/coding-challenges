# https://exercism.io/my/solutions/b077c47bf74d47088d5cd53bde1d514e

from itertools import chain


def encode_num(n):
    if n == 0:
        return [0]
    encoded = []
    while n > 0:
        byte7 = n & 0x7f
        n >>= 7
        control = 0 if encoded == [] else 0x80
        encoded.append(byte7 + control)
    return reversed(encoded)


def encode(numbers):
    return list(chain.from_iterable(map(encode_num, numbers)))


def decode_num(bytes8):
    decoded = 0
    for i in range(len(bytes8) - 1):
        decoded += bytes8[i] - 0x80
        decoded <<= 7
    decoded += bytes8[-1]
    return decoded


def decode(bytes8):
    nums = []
    num = []
    for byte8 in bytes8:
        num.append(byte8)
        if byte8 < 0x80:
            nums.append(num)
            num = []
    if num != []:
        raise ValueError("Incomplete sentence")
    return list(map(decode_num, nums))
