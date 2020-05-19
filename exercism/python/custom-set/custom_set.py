class CustomSet:
    def __init__(self, elements=[]):
        self._elements = set(elements)

    def isempty(self):
        return len(self._elements) == 0

    def __contains__(self, element):
        return element in self._elements

    def issubset(self, other):
        return self._elements <= other._elements

    def isdisjoint(self, other):
        return self._elements.isdisjoint(other._elements)

    def __eq__(self, other):
        return self._elements == other._elements

    def add(self, element):
        self._elements.add(element)

    def intersection(self, other):
        return CustomSet(list(self._elements & other._elements))

    def __sub__(self, other):
        return CustomSet(list(self._elements - other._elements))

    def __add__(self, other):
        return CustomSet(list(self._elements | other._elements))

    def __repr__(self):
        return self._elements.__repr__()
