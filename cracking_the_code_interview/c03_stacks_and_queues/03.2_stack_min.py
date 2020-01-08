# We store the current minimum.
# When it is popped, we need to calculate the new current one --> O(n)

from c03_stacks_and_queues.stack import Stack


class StackMin(Stack):
    def __init__(self):
        self._min = None
        Stack.__init__(self)

    # O(1)
    def min(self):
        if self.is_empty():
            raise EmptyStackError
        return self._min

    # O(n)
    def _search_min(self):
        if self.is_empty():
            raise EmptyStackError
        current = self._lst.head
        minimum = current.data
        while current is not None:
            minimum = min(minimum, current.data)
            current = current.nxt
        return minimum

    # O(1) *amortized*
    def pop(self):
        popped = Stack.pop(self)
        if popped == self._min:
            if self.is_empty():
                self._min = None
            else:
                self._min = self._search_min()
        return popped

    # O(1)
    def push(self, item):
        if self.is_empty():
            self._min = item
        else:
            self._min = min(self._min, item)
        Stack.push(self, item)
