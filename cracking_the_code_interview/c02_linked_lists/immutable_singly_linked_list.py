class ISinglyLinkedList():
    def __init__(self, car=None, cdr=None):
        self.car = car
        self.cdr = cdr

    # O(1)
    def is_nil(self):
        return self.car is None and self.cdr is None

    # O(n)
    def length(self):
        def aux(count, rest):
            if rest.is_nil():
                return count
            return aux(count + 1, rest.cdr)
        return aux(0, self)

    # O(1)
    def push(self, data):
        return ISinglyLinkedList(data, self)

    # O(1)
    def pop(self):
        if self.is_nil():
            raise EmptyListError
        return (self.car, self.cdr)

    # O(n)
    def remove(self, value):
        def aux(rest):
            if rest.is_nil():
                return ISinglyLinkedList()
            if rest.car == value:
                return rest.cdr
            return aux(rest.cdr).push(rest.car)
        return aux(self)

    # O(n)
    def reverse(self):
        def aux(rev, rest):
            if rest.is_nil():
                return rev
            return aux(rev.push(rest.car), rest.cdr)
        return aux(ISinglyLinkedList(), self)

    # O(n1) + O(n1) --> O(n1)
    def concat(self, lst):
        def aux(new, rest):
            if rest.is_nil():
                return new
            return aux(new.push(rest.car), rest.cdr)
        return aux(lst, self.reverse())

    # O(n)
    def __repr__(self):
        if self.is_nil():
            return '.'
        return f'-> {self.car}{self.cdr}'

    # O(n), where n is the length of the shortest list
    def __eq__(self, other):
        def eq_contents(lst_1, lst_2):
            if lst_1.is_nil() and lst_2.is_nil():
                return True
            if lst_1.is_nil() or lst_2.is_nil():
                return False
            if lst_1.car != lst_2.car:
                return False
            return eq_contents(lst_1.cdr, lst_2.cdr)

        return isinstance(other, self.__class__) and eq_contents(self, other)

    # O(n), where n is the length of the shortest list
    def __ne__(self, other):
        return not self.__eq__(other)


class EmptyListError(Exception):
    pass
