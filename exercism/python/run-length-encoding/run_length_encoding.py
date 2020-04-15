from string import digits


def decode(encoded):
    plain = ''
    if encoded == '':
        return ''

    def add_char(char, count):
        nonlocal plain
        plain += char * count

    count_str = ''
    for c in encoded:
        if c in digits:
            count_str += c
        else:
            count = 1 if count_str == '' else int(count_str)
            add_char(c, count)
            count_str = ''
    return plain


def encode(plain):
    encoded = ''
    if plain == '':
        return ''

    def add_char(char, count):
        nonlocal encoded
        encoded += (str(count) if count > 1 else '') + char

    prev = plain[0]
    count = 0
    for c in plain:
        current = c
        if current == prev:
            count += 1
        else:
            add_char(prev, count)
            count = 1
            prev = current
    add_char(prev, count)
    return encoded
