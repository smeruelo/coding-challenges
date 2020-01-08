from c02_linked_lists.mutable_singly_linked_list import MSinglyLinkedList


class Stack():
    def __init__(self):
        self._lst = MSinglyLinkedList()

    # O(1)
    def pop(self):
        try:
            return self._lst.pop()
        except Exception:
            raise EmptyStackError

    # O(1)
    def push(self, item):
        self._lst.push(item)
        return self

    # O(1)
    def peek(self):
        try:
            return self._lst.peek()
        except Exception:
            raise EmptyStackError

    # O(1)
    def is_empty(self):
        return self._lst.is_empty()

    # O(n)
    def length(self):
        return self._lst.length()

    def __repr__(self):
        return self._lst.__repr__()


class EmptyStackError(Exception):
    pass
