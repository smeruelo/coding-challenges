# https://exercism.io/my/solutions/dbe51764f42547c0a56ea0fab90db5b0


class Node:
    def __init__(self, prev=None, value=None, next=None):
        self._prev = prev
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def prev(self):
        return self._prev

    def next(self):
        return self._next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def __iter__(self):
        current_node = self._tail
        while current_node:
            yield current_node.value()
            current_node = current_node.prev()

    def __len__(self):
        return sum(1 for _ in self)

    def _is_empty(self):
        return self._head is None

    def head(self):
        if self._is_empty():
            raise EmptyListException('List is empty')
        return self._head

    def push(self, value):
        new_node = Node(None, value, self._head)
        if self._is_empty():
            self._tail = new_node
        else:
            self._head._prev = new_node
        self._head = new_node

    def unshift(self, value):
        new_node = Node(self._tail, value, None)
        if self._is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node

    def pop(self):
        if self._is_empty():
            raise EmptyListException('List is empty')
        popped = self._head.value()
        self._head = self._head.next()
        if self._head:
            self._head._prev = None
        else:
            self._tail = None
        return popped

    def shift(self):
        if self._is_empty():
            raise Exception('List is empty')
        popped = self._tail.value()
        self._tail = self._tail.prev()
        if self._tail:
            self._tail._next = None
        else:
            self._head = None
        return popped

    def __repr__(self):
        return ' -> '.join(str(value) for value in self)


class EmptyListException(Exception):
    pass
