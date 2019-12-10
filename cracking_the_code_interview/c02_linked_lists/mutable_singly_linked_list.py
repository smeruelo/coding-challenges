class Node():
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    def is_last(self):
        return self.data is None and self.nxt is None


class MSinglyLinkedList():
    def __init__(self):
        self.head = Node()

    # O(n)
    def length(self):
        count = 0
        current_node = self.head
        while not current_node.is_last():
            count += 1
            current_node = current_node.nxt
        return count

    # O(1)
    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        return self

    # O(1)
    def pop(self):
        if self.head.is_last():
            raise Exception('List is empty')
        popped = self.head.data
        self.head = self.head.nxt
        return (popped, self)

    # O(n)
    def remove(self, value):
        p1 = self.head
        p2 = None
        while not p1.is_last() and p1.data != value:
            p2 = p1
            p1 = p1.nxt

        if not p1.is_last():
            if p2:
                p2.nxt = p1.nxt
            else:
                self.head = p1.nxt

        return self

    # O(n)
    def reverse(self):
        rev = MSinglyLinkedList()
        def aux(current_node):
            if current_node.is_last():
                self.head = rev.head
                return
            rev.push(current_node.data)
            aux(current_node.nxt)
            return

        aux(self.head)
        return self


    # O(n1)
    def concat(self, lst):
        if self.head.is_last():
            self.head = lst.head
        else:
            current_node = self.head
            while not current_node.nxt.is_last():
                current_node = current_node.nxt
            current_node.nxt = lst.head

        # Careful! Now lst points somewhere in the middle of our list.
        # Maybe do lst.head = Node() so it stops doing that?

        return self

    # O(n)
    def __repr__(self):
        s = ''
        current_node = self.head
        while not current_node.is_last():
            s = f'{s}-> {current_node.data} '
            current_node = current_node.nxt
        return f'{s}.'
