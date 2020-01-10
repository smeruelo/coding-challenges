# Problem: Sort Stack
# Write a program to sort a stack such that the smallest items are on the
# top. You can use an additional temporary stack, but you may not copy the
# elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and isEmpty.

# Solution: Ugly, code is hard to understand.
# We move elements from the stack to an aux one until we meet an element
# that is out of order. Then we move back the elements inserting that one
# in order. We start again until it's completely sorted.

from c03_stacks_and_queues.stack import Stack


# O(n * n)
def sort_stack(s):
    s_aux = Stack()
    if s.is_empty():
        return s

    end = False
    while not end and not s.is_empty():
        if s_aux.is_empty() or s.peek() >= s_aux.peek():
            s_aux.push(s.pop())
        else:
            tmp = s.pop()
            if s.is_empty():
                end = True
            while not s_aux.is_empty():
                if not tmp or s_aux.peek() > tmp:
                    s.push(s_aux.pop())
                else:
                    s.push(tmp)
                    tmp = None
            if tmp:
                s.push(tmp)
    while not s_aux.is_empty():
        s.push(s_aux.pop())

    return s
