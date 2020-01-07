from c02_linked_lists.mutable_doubly_linked_list import MDoublyLinkedList


class Queue():
    def __init__(self):
        self._lst = MDoublyLinkedList()

    def add(self, item):
        self._lst.push_hd(item)
        return self

    def remove(self):
        try:
            return self._lst.pop_tl()
        except Exception:
            raise EmptyQueueError

    def peek(self):
        try:
            return self._lst.peek_tl()
        except Exception:
            raise EmptyQueueError

    def is_empty(self):
        return self._lst.is_empty()

    def __repr__(self):
        return self._lst.__repr__()


class EmptyQueueError(Exception):
    pass
