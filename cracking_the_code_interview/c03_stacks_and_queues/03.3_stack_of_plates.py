# Problem: Stack of Plates
# Imagine a (literal) stack of plates. If the stack gets too high,
# it might topple. Therefore, in real life, we would likely start a new stack
# when the previous stack exceeds some threshold. Implement a data structure
# SetOfStacks that mimics this. SetOfStacks should be composed of several
# stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to
# a single stack (that is, pop() should return the same values as it would if
#  there were just a single stack).

from c03_stacks_and_queues.stack import Stack


class SetOfStacks():
    def __init__(self, size):
        self._stacks = []
        self._size = size

    def pop(self):
        if self.is_empty():
            raise EmptyStackError
        popped = self._stacks[-1].pop()
        if self._stacks[-1].is_empty():
            self._stacks.pop()
        return popped

    def push(self, item):
        if self.is_empty() or self._stacks[-1].length() == self._size:
            self._stacks.append(Stack())
        self._stacks[-1].push(item)
        return self

    def peek(self):
        if self.is_empty():
            raise EmptyStackError
        return self._stacks[-1].peek()

    def is_empty(self):
        return self._stacks == []

    def __repr__(self):
        return ' '.join(map(repr, reversed(self._stacks)))


class EmptyStackError(Exception):
    pass
