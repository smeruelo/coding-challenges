# https://exercism.io/my/solutions/96ff5b3cd1a74c3eb920d7f523fa0912

from math import gcd, log


class Rational:
    def __init__(self, numer, denom):
        sign = -1 if numer * denom < 0 else 1
        g = gcd(numer, denom)
        self.numer = sign * abs(numer) // g
        self.denom = abs(denom) // g

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(pow(self.numer, abs(power)), pow(self.denom, abs(power)))

    def __rpow__(self, base):
        return pow(2, log(base ** self.numer, 2) / self.denom)
