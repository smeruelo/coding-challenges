class ISinglyLinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def is_nil(self):
        return self.head is None and self.tail is None

    def length(self):
        def aux(count, rest):
            if rest.is_nil():
                return count
            return aux(count + 1, rest.tail)
        return aux(0, self)

    def push(self, data):
        return ISinglyLinkedList(data, self)

    def pop(self):
        if self.is_nil():
            raise Exception('List is empty')
        return (self.head, self.tail)

    def remove(self, value):
        def aux(rest):
            if rest.is_nil():
                return ISinglyLinkedList()
            if rest.head == value:
                return rest.tail
            return aux(rest.tail).push(rest.head)
        return aux(self)

    def reverse(self):
        def aux(rev, rest):
            if rest.is_nil():
                return rev
            return aux(rev.push(rest.head), rest.tail)
        return aux(ISinglyLinkedList(), self)

    def concat(self, lst):
        def aux(new, rest):
            if rest.is_nil():
                return new
            return aux(new.push(rest.head), rest.tail)
        return aux(lst, self.reverse())

    def __repr__(self):
        if self.is_nil():
            return '.'
        return f'-> {self.head} ' + str(self.tail)
