# https://exercism.io/my/solutions/9ecfc3f0ba0642ec9b73bb375b2d9c29

import re
from string import digits


class Phone(object):
    def __init__(self, phone_number):
        no_punct = ''.join(list(filter(lambda c: c in digits, phone_number)))
        parsed = re.match(r'(1)?([2-9][0-9]{2})([2-9][0-9]{2})([0-9]{4}$)', no_punct)
        if parsed is None:
            raise ValueError('Invalid phone_number')
        self._number = parsed.group(2) + parsed.group(3) + parsed.group(4)
        self._country_code = parsed.group(1)
        self._area_code = parsed.group(2)
        self._exchange_code = parsed.group(3)
        self._subscriber_number = parsed.group(4)

    @property
    def number(self):
        return self._number

    @property
    def area_code(self):
        return self._area_code

    def pretty(self):
        return f'({self.area_code}) {self._exchange_code}-{self._subscriber_number}'
