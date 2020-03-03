# https://exercism.io/my/solutions/adc46951a0c149f89bdb8b21382d140f

from string import ascii_lowercase, ascii_letters


CHAR = dict(enumerate(ascii_lowercase))
INDEX = {c: i for i, c in enumerate(ascii_lowercase)}

def rotate(text, key):
    def cipher_char(char, key):
        if char not in ascii_letters:
            return char
        i = (INDEX[char.lower()] + key) % len(ascii_lowercase)
        return CHAR[i] if char.islower() else CHAR[i].upper()

    return ''.join(map(lambda c: cipher_char(c, key), text))
