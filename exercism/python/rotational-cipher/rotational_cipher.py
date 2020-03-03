# https://exercism.io/my/solutions/adc46951a0c149f89bdb8b21382d140f

from string import ascii_lowercase, ascii_uppercase, ascii_letters

ALPHABET = ascii_letters

def rotate(text, key):
    rotated_lower = ascii_lowercase[key:] + ascii_lowercase[:key]
    rotated_upper = ascii_uppercase[key:] + ascii_uppercase[:key]
    rotated_alphabet = f'{rotated_lower}{rotated_upper}'
    trans = str.maketrans(ALPHABET, rotated_alphabet)
    return text.translate(trans)
