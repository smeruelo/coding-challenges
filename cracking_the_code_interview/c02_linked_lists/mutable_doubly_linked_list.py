class DNode():
    def __init__(self, prv=None, data=None, nxt=None):
        self.prv = prv
        self.data = data
        self.nxt = nxt

    def __repr__(self):
        end = ' ' if self.nxt else ''
        return f'<-> {self.data}{end}'


class MDoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

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
    def push_hd(self, item):
        new_node = DNode(None, item, self.head)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.prv = new_node
        self.head = new_node
        return self

    # O(1)
    def push_tl(self, item):
        new_node = DNode(self.tail, item, None)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.nxt = new_node
        self.tail = new_node
        return self

    # O(1)
    def pop_hd(self):
        if self.is_empty():
            raise Exception('List is empty')
        popped = self.head.data
        self.head = self.head.nxt
        if self.head:
            self.head.prv = None
        else:
            self.tail = None
        return popped

    # O(1)
    def pop_tl(self):
        if self.is_empty():
            raise Exception('List is empty')
        popped = self.tail.data
        self.tail = self.tail.prv
        if self.tail:
            self.tail.nxt = None
        else:
            self.head = None
        return popped

    # O(1)
    def peek_hd(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self.head.data

    # O(1)
    def peek_tl(self):
        if self.is_empty():
            raise Exception('List is empty')
        return self.tail.data

    # O(n)
    def remove(self, item):
        p = self.head
        while p and p.data != item:
            p = p.nxt

        if p:
            if p.prv:
                p.prv.nxt = p.nxt
            else:
                self.head = p.nxt
            if p.nxt:
                p.nxt.prv = p.prv
            else:
                self.tail = p.prv
        return self

    # O(n1)
    def concat(self, lst):
        if self.is_empty():
            self.head = lst.head
        else:
            lst.head.prv = self.tail
            self.tail.nxt = lst.head
        self.tail = lst.tail

        # Careful! Now lst points somewhere in the middle of our list.
        # Maybe do lst.head = DNode() so it stops doing that?

        return self

    # O(n)
    def __repr__(self):
        s = ''
        current_node = self.head
        while current_node:
            s += current_node.__repr__()
            current_node = current_node.nxt
        return s + '.'
