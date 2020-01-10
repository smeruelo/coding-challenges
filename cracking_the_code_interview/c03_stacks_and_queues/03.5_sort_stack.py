# Problem: Sort Stack
# Write a program to sort a stack such that the smallest items are on the
# top. You can use an additional temporary stack, but you may not copy the
# elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and isEmpty.

# Solution: We use an aux stack and keep that one sorted (but in reversed order)
# We move elements from the stack to the aux one, inserting them in order.
# When we're finished, we move them back to the original stack


from c03_stacks_and_queues.stack import Stack


# O(n * n)
def sort_stack(s):
    def insert_sorted(item):
        while not s_aux.is_empty() and s_aux.peek() > item:
            s.push(s_aux.pop())
        s_aux.push(item)

    s_aux = Stack()
    while not s.is_empty():
        insert_sorted(s.pop())
    while not s_aux.is_empty():
        s.push(s_aux.pop())

    return s
