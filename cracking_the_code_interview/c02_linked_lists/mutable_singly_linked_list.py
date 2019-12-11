class Node():
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    def __repr__(self):
        end = ' ' if self.nxt else ''
        return f'-> {self.data}{end}'


class MSinglyLinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    # O(n)
    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.nxt
        return count

    # O(1)
    def push(self, item):
        new_node = Node(item, self.head)
        self.head = new_node
        return self

    # O(1)
    def pop(self):
        if self.is_empty():
            raise Exception('List is empty')
        popped = self.head.data
        self.head = self.head.nxt
        return popped

    # O(1)
    def peek(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self.head.data

    # O(n)
    def remove(self, item):
        p1 = self.head
        p2 = None
        while p1 and p1.data != item:
            p2 = p1
            p1 = p1.nxt

        if p1:
            if not p2:
                self.head = p1.nxt
            else:
                p2.nxt = p1.nxt
        return self

    # O(n)
    def reverse(self):
        rev = MSinglyLinkedList()
        current_node = self.head
        while current_node:
            rev.push(current_node.data)
            current_node = current_node.nxt
        return rev

    # O(n1)
    def concat(self, lst):
        if self.is_empty():
            self.head = lst.head
        else:
            current_node = self.head
            while current_node.nxt:
                current_node = current_node.nxt
            current_node.nxt = lst.head

        # Careful! Now lst points somewhere in the middle of our list.
        # Maybe do lst.head = Node() so it stops doing that?

        return self

    # O(n)
    def __repr__(self):
        s = ''
        current_node = self.head
        while current_node:
            s += current_node.__repr__()
            current_node = current_node.nxt
        return s + '.'
