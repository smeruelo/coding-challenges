# https://exercism.io/my/solutions/c7af812c3e4f44e8bd9ac8ef3a77bcd5


def anything_else(s, i):
    return int(s[:i]) != 0


def say3(number):
    UNITS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    s = str(number)[::-1]
    d = list(map(int, s))

    def units():
        return UNITS[d[0]]

    def tens():
        out = ''
        if len(s) > 1 and d[1] != 0:
            if d[1] == 1:
                return TEENS[d[0]]
            else:
                out = TENS[d[1]]
                if anything_else(s, 1):
                    out += '-'
        return out + units()

    def hundreds():
        out = ''
        if len(s) > 2 and d[2] != 0:
            out += UNITS[d[2]] + ' hundred'
            if anything_else(s, 2):
                out += ' and '
        return out + tens()

    return hundreds()


def say(number):
    if number == 0:
        return 'zero'
    if number < 0 or number >= 10 ** 12:
        raise ValueError('Invalid input')

    s = str(number)[::-1]
    out = ''

    if len(s) > 9:
        block = number // 10 ** 9
        out += say3(block) + ' billion'
        if anything_else(s, 9):
            out += ' '

    if len(s) > 6:
        block = (number % 10 ** 9) // 10 ** 6
        if block != 0:
            out += say3(block) + ' million'
            if anything_else(s, 6):
                out += ' '

    if len(s) > 3:
        block = (number % 10 ** 6) // 10 ** 3
        if block != 0:
            out += say3(block) + ' thousand'
            if anything_else(s, 3):
                out += ' '

    return out + say3(number % 10 ** 3)
