# https://exercism.io/my/solutions/ee3ebb7b0d9c4c11a945ff0c4ec4e72f

from string import digits


def decode(encoded):
    plain = ''
    count_str = ''
    for c in encoded:
        if c in digits:
            count_str += c
        else:
            count = 1 if count_str == '' else int(count_str)
            plain += c * count
            count_str = ''
    return plain


def encode(plain):
    if plain == '':
        return ''

    def count_to_str(count):
        return '' if count == 1 else str(count)

    encoded = ''
    prev = plain[0]
    count = 0
    for c in plain:
        current = c
        if current == prev:
            count += 1
        else:
            encoded += count_to_str(count) + prev
            count = 1
            prev = current
    encoded += count_to_str(count) + prev
    return encoded
