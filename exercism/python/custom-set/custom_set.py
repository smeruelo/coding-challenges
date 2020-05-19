# https://exercism.io/my/solutions/c7b96f359d98401a8346025800d91b1d

from itertools import chain


class CustomSet:
    """Simple implementation of a set, using dictionaries to store the elements."""

    # O(n)
    def __init__(self, elements=[]):
        self._elements = {e: None for e in elements}

    @property
    def elements(self):
        return self._elements

    # O(1)
    def isempty(self):
        return len(self.elements) == 0

    # O(1)
    def __contains__(self, element):
        return element in self.elements

    # O(n)
    def issubset(self, other):
        return all(map(lambda e: e in other, self.elements))

    # O(n)
    def isdisjoint(self, other):
        return self.intersection(other).isempty()

    # O(n log n + m log m)
    def __eq__(self, other):
        return sorted(self.elements) == sorted(other.elements)

    # O(1)
    def add(self, element):
        self.elements[element] = None

    # O(n)
    def intersection(self, other):
        return CustomSet([e for e in self.elements if e in other])

    # O(n)
    def __sub__(self, other):
        return CustomSet([e for e in self.elements if e not in other])

    # O(n + m)
    def __add__(self, other):
        return CustomSet(chain(self.elements, other.elements))

    def __repr__(self):
        return '{' + list(self.elements.keys()).__repr__()[1:-1] + '}'
