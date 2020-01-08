# Problem: Queue via Stacks
# Implement a MyQueue class which implements a queue using two stacks.

# Solution:
# One stack, SIn, in which we push in the values
# One stack, SOut, from which we pop out the values
# When SOut empties, we fill it with reversed(SIn)
#      SIn    SOut
#      _ _ _|_ _
# --> |_|_|_|_|_| -->
#           |


from c03_stacks_and_queues.stack import Stack


class MyQueue():
    def __init__(self):
        self.SIn = Stack()
        self.SOut = Stack()

    # O(1)
    def add(self, item):
        self.SIn.push(item)
        return self

    # O(n)
    def _move(self):
        while not self.SIn.is_empty():
            self.SOut.push(self.SIn.pop())
        return self

    # O(1) amortized
    def peek(self):
        if self.is_empty():
            raise EmptyMyQueueError
        if self.SOut.is_empty():
            self._move()
        return self.SOut.peek()

    # O(1) amortized
    def remove(self):
        if self.is_empty():
            raise EmptyMyQueueError
        if self.SOut.is_empty():
            self._move()
        return self.SOut.pop()

    # O(1)
    def is_empty(self):
        return self.SIn.is_empty() and self.SOut.is_empty()

    def __repr__(self):
        return f'{repr(self.SIn)} | {repr(self.SOut)[::-1]}'


class EmptyMyQueueError(Exception):
    pass
