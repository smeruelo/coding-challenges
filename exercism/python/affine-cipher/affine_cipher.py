# https://exercism.io/my/solutions/fb36dfbd24194c6dbbeff5ba7f5114db

from string import ascii_lowercase, digits
from textwrap import wrap

CHAR = dict(enumerate(ascii_lowercase))
INDEX = {c: i for i, c in enumerate(ascii_lowercase)}
M = len(ascii_lowercase)


def coprime(x, y):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    return gcd(x, y) == 1


def eulers_totient(x):
    count = 0
    for i in range(1, x+1):
        if coprime(i, x):
            count += 1
    return count


ET_M = eulers_totient(M)


def mmi_m(x):
    return x ** (ET_M - 1)


def encode(plain_text, a, b):
    if not coprime(a, M):
        raise ValueError('Error: a and m must be coprime')

    def cipher_char(c):
        if c in ascii_lowercase:
            return CHAR[(a * INDEX[c] + b) % M]
        if c in digits:
            return c
        return ''

    ciphered_text = ''.join(map(cipher_char, plain_text.lower()))
    return ' '.join(wrap(ciphered_text, 5))


def decode(ciphered_text, a, b):
    if not coprime(a, M):
        raise ValueError('Error: a and m must be coprime')

    def decipher_char(c):
        if c in digits:
            return c
        if c in ascii_lowercase:
            return CHAR[(mmi_m(a) * (INDEX[c] - b)) % M]
        return ''

    plain_text = ''.join(map(decipher_char, ciphered_text))
    return plain_text
