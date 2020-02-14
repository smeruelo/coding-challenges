# https://exercism.io/my/solutions/c6273c9dffba4341be29f25e42be270f

from textwrap import wrap


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
PLAIN_CHAR = dict(enumerate(ALPHABET))
CIPHER_CHAR = dict(enumerate(ALPHABET[::-1]))
PLAIN_INDEX = dict([(c, i) for (i, c) in enumerate(ALPHABET)])
CIPHER_INDEX = dict([(c, i) for (i, c) in enumerate(ALPHABET[::-1])])


def str_to_alphanum(s):
    return ''.join([c for c in s if c.isalnum()]).lower()


def encode(plain_text):
    def encode_char(c):
        return c if c.isdigit() else CIPHER_CHAR[PLAIN_INDEX[c]]

    plain = str_to_alphanum(plain_text)
    ciphered = ''.join(list(map(encode_char, plain)))
    return ' '.join(wrap(ciphered, 5))


def decode(ciphered_text):
    def decode_char(c):
        return c if c.isdigit() else PLAIN_CHAR[CIPHER_INDEX[c]]

    ciphered = str_to_alphanum(ciphered_text)
    plain = ''.join(list(map(decode_char, ciphered)))
    return plain
