# https://exercism.io/my/solutions/0ff3ff5db5e04b0f81633c306a1e2131


class Luhn:
    def __init__(self, card_num):
        self._card_num = card_num

    def valid(self):
        trimmed = self._card_num.replace(' ', '')
        if len(trimmed) <= 1:
            return False
        else:
            total = 0
            for index, char in enumerate(reversed(trimmed)):
                try:
                    digit = int(char)
                except ValueError:
                    return False
                addend = digit + digit * (index % 2)
                total += addend if addend <= 9 else addend - 9
            return total % 10 == 0
