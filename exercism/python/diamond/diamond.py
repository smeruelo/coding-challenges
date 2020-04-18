# https://exercism.io/my/solutions/cd7a831ed7004c4082623bc5bc842955

from string import ascii_uppercase


def rows(letter):
    index = ascii_uppercase.index(letter)
    size = index * 2 + 1
    canvas = [[' ']*size for _ in range(size)]

    def add_letter(letter, row, offset):
        canvas[row][offset] = canvas[row][size-offset-1] = letter

    add_letter(letter, index, 0)
    for offset in range(index+1):
        l = ascii_uppercase[index-offset]
        add_letter(l, index - offset, offset)
        add_letter(l, index + offset, offset)

    return [''.join(row) for row in canvas]
