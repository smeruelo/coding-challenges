# https://exercism.io/my/solutions/a105330ed1e0459980304c1b72e17c7b


class Node:
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        for v in values:
            self.push(v)

    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node.value()
            current_node = current_node.next()

    def __len__(self):
        return sum(1 for _ in self)

    def _is_empty(self):
        return self._head is None

    def head(self):
        if self._is_empty():
            raise EmptyListException('List is empty')
        return self._head

    def push(self, value):
        self._head = Node(value, self._head)

    def pop(self):
        if self._is_empty():
            raise EmptyListException('List is empty')
        popped = self._head.value()
        self._head = self._head.next()
        return popped

    def reversed(self):
        rev = LinkedList()
        for value in self:
            rev.push(value)
        return rev

    def __repr__(self):
        return ' -> '.join(str(value) for value in self)


class EmptyListException(Exception):
    pass
