# https://exercism.io/my/solutions/3b111fdc1fa74d309221a4fb59ed546d

import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                             self.imaginary * other.real + self.real * other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) /
                             (pow(other.real, 2) + pow(other.imaginary, 2)),
                             (self.imaginary * other.real - self.real * other.imaginary) /
                             (pow(other.real, 2) + pow(other.imaginary, 2)))

    def __abs__(self):
        return pow(pow(self.real, 2) + pow(self.imaginary, 2), 0.5)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def conjugate(self):
        return ComplexNumber(self.real, -1 * self.imaginary)

    def exp(self):
        return ComplexNumber(pow(math.e, self.real) * math.cos(self.imaginary),
                             pow(math.e, self.real) * math.sin(self.imaginary))

    def __repr__(self):
        return f'{self.real} + {self.imaginary} i'
