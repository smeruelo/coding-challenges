# Problem: Stack Min
# How would you design a stack which, in addition to push and pop, has a
# function min which returns the minimum element? Push, pop and min should all
# operate in 0(1) time.

# Solution:
# We store all the history of minimums.
# We could store the minimum at the time of pushing an element for every
# element --> too much space
# Instead, we use a different stack and store the minimum only when it changes.

from c03_stacks_and_queues.stack import Stack


class StackMin(Stack):
    def __init__(self):
        self._mins = Stack()
        Stack.__init__(self)

    # O(1)
    def min(self):
        if self._mins.is_empty():
            raise EmptyStackError
        return self._mins.peek()

    # O(1)
    def pop(self):
        popped = Stack.pop(self)
        if popped == self.min():
            self._mins.pop()
        return popped

    # O(1)
    def push(self, item):
        if self.is_empty() or item <= self.min():
            self._mins.push(item)
        Stack.push(self, item)
