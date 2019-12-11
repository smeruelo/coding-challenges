from c02_linked_lists.mutable_singly_linked_list import MSinglyLinkedList


class Stack():
    def __init__(self):
        self._lst = MSinglyLinkedList()

    def pop(self):
        try:
            item, _ = self._lst.pop()
            return item
        except Exception:
            raise EmptyStackError

    def push(self, item):
        self._lst.push(item)
        return self

    def peek(self):
        try:
            return self._lst.peek()
        except Exception:
            raise EmptyStackError

    def is_empty(self):
        return self._lst.is_empty()

    def __repr__(self):
        return self._lst.__repr__()


class EmptyStackError(Exception):
    pass
