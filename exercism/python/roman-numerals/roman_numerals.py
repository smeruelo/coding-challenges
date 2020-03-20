# https://exercism.io/my/solutions/4ea9a49002414c2a90d902e3ceabcb1e

def roman(number):
    letters = ['IV', 'XL', 'CD', 'MV']

    def one_digit(n, power):
        ch1, ch5 = letters[power]
        if n <= 3:
            return ch1 * n
        if n >= 4 and n <= 8:
            return (ch1 * (5 - n)) + ch5 + (ch1 * (n - 5))
        if n == 9:
            if power > 2:
                raise Exception('Number too large')
            ch5 = letters[power+1][0]
            return ch1 + ch5

    s = ''
    for i, digit in enumerate(str(number)):
        power = len(str(number)) - 1 - i
        s += one_digit(int(digit), power)
    return s
