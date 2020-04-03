from itertools import chain

DISCOUNTS = [0, 0, 5, 10, 20, 25]
GROUP_PRICES = [8 * i * (100 - DISCOUNTS[i]) for i in range(len(DISCOUNTS))]


class Group():
    def __init__(self, book=None):
        self.books = [0, 0, 0, 0, 0]
        if book:
            self.add(book)

    @property
    def size(self):
        return self.books.count(1)

    @property
    def price(self):
        return GROUP_PRICES[self.size]

    def add(self, book):
        if self.books[book-1] == 1:
            raise Exception(f'Group already contains book {book}.')
        self.books[book-1] = 1

    def contains(self, book):
        return self.books[book-1] == 1

    def copy(self):
        new = Group()
        for i, b in enumerate(self.books):
            if b:
                new.add(i+1)
        return new

    def __lt__(self, other):
        return str(self) < str(other)

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        return ''.join(map(str, self.books))


class Grouping():
    def __init__(self):
        self.groups = []

    @property
    def price(self):
        return sum(map(lambda g: g.price, self.groups))

    def add(self, group):
        self.groups.append(group)

    def contains(self, group):
        for g in self.groups:
            if g == group:
                return True
        return False

    def sort(self):
        self.groups.sort()

    def copy(self):
        new = Grouping()
        for g in self.groups:
            new.add(g.copy())
        return new

    def possibilities(self, book):
        grouping = self.copy()
        grouping.add(Group(book))
        pos = [grouping]
        for i, g in enumerate(self.groups):
            if not g.contains(book):
                grouping = self.copy()
                grouping.groups[i].add(book)
                pos.append(grouping)
        return pos
        
    def __eq__(self, other):
        return self.groups == other.groups

    def __repr__(self):
        return '(' + ' '.join([str(g) for g in self.groups]) + ')'



def total(basket):
    def uniques(possible_groupings):
        groupings = []
        for g in possible_groupings:
            g.sort()
            if not g in groupings:
                groupings.append(g)
        return groupings

    groupings = [Grouping()]
    for book in sorted(basket):
        possible_groupings = list(chain.from_iterable([g.possibilities(book) for g in groupings]))
        groupings = uniques(possible_groupings)
    return min(map(lambda g: g.price, groupings))
