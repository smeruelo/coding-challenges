class ISinglyLinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # O(1)
    def is_nil(self):
        return self.head is None and self.tail is None

    # O(n)
    def length(self):
        def aux(count, rest):
            if rest.is_nil():
                return count
            return aux(count + 1, rest.tail)
        return aux(0, self)

    # O(1)
    def push(self, data):
        return ISinglyLinkedList(data, self)

    # O(1)
    def pop(self):
        if self.is_nil():
            raise Exception('List is empty')
        return (self.head, self.tail)

    # O(n)
    def remove(self, value):
        def aux(rest):
            if rest.is_nil():
                return ISinglyLinkedList()
            if rest.head == value:
                return rest.tail
            return aux(rest.tail).push(rest.head)
        return aux(self)

    # O(n)
    def reverse(self):
        def aux(rev, rest):
            if rest.is_nil():
                return rev
            return aux(rev.push(rest.head), rest.tail)
        return aux(ISinglyLinkedList(), self)

    # O(n1) + O(n1) --> O(n1)
    def concat(self, lst):
        def aux(new, rest):
            if rest.is_nil():
                return new
            return aux(new.push(rest.head), rest.tail)
        return aux(lst, self.reverse())

    # O(n)
    def __repr__(self):
        if self.is_nil():
            return '.'
        return f'-> {self.head} ' + str(self.tail)
