class Node():
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt

    def is_last(self):
        return self.data is None and self.nxt is None


class MSinglyLinkedList():
    def __init__(self):
        self.head = Node()

    def length(self):
        count = 0
        current_node = self.head
        while not current_node.is_last():
            count += 1
            current_node = current_node.nxt
        return count

    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        return self

    def pop(self):
        if self.head.is_last():
            raise Exception('List is empty')
        popped = self.head.data
        self.head = self.head.nxt
        return (popped, self)

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

    def concat(self, lst):
        p1 = self.head
        p2 = None
        while not p1.is_last():
            p2 = p1
            p1 = p1.nxt

        if p2:
            p2.nxt = lst.head
        else:
            self.head = lst.head

        # Careful! Now lst points somewhere in the middle of our list.
        # Maybe do lst.head = Node() so it stops doing that?

        return self

    def __repr__(self):
        s = ''
        current_node = self.head
        while not current_node.is_last():
            s = f'{s}-> {current_node.data} '
            current_node = current_node.nxt
        return f'{s}.'