class CustomSet:
    """Simple implementation of a set, using lists to store the elements.
    We could reduce the cost O(n * m) to O(max(n, m)) if we kept the elements ordered."""

    # O(n log n)
    def __init__(self, elements=[]):
        if len(elements) == 0:
            self._elements = []
            return
        sorted_elements = sorted(elements)
        self._elements = [sorted_elements[0]]
        prev = sorted_elements[0]
        for e in sorted_elements:
            if e != prev:
                self._elements.append(e)
            prev = e

    @property
    def elements(self):
        return self._elements

    # O(1)
    def isempty(self):
        return len(self.elements) == 0

    # O(n)
    def __contains__(self, element):
        return element in self.elements

    # O(n * m)
    def issubset(self, other):
        return all(map(lambda e: e in other, self.elements))

    # O(n * m)
    def isdisjoint(self, other):
        return self.intersection(other).isempty()

    # O(n log n + m log m)
    def __eq__(self, other):
        return sorted(self.elements) == sorted(other.elements)

    # O(n)
    def add(self, element):
        if not element in self:
            self.elements.append(element)

    # O(n * m)
    def intersection(self, other):
        return CustomSet([e for e in self.elements if e in other])

    # O(n * m)
    def __sub__(self, other):
        return CustomSet([e for e in self.elements if e not in other])

    # O(m)
    def __add__(self, other):
        return CustomSet(self.elements + other.elements)

    def __repr__(self):
        return '{' + self.elements.__repr__()[1:-1] + '}'
