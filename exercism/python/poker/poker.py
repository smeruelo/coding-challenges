# https://exercism.io/my/solutions/f898410ffa35441e904e37370d940345


class Card():
    def __init__(self, s):
        self.suit = s[-1]
        if s[:-1] == 'J':
            self.rank = 11
        elif s[:-1] == 'Q':
            self.rank = 12
        elif s[:-1] == 'K':
            self.rank = 13
        elif s[:-1] == 'A':
            self.rank = 14
        else:
            self.rank = int(s[:-1])
        self.color = 'RED' if (self.suit == 'H' or self.suit == 'D') else 'BLACK'

    def __lt__(self, other):
        return self.rank < other.rank

    def __repr__(self):
        s = ''
        if self.rank == 11:
            s += 'J'
        elif self.rank == 12:
            s += 'Q'
        elif self.rank == 13:
            s += 'K'
        elif self.rank == 14:
            s += 'A'
        else:
            s += str(self.rank)
        return s + self.suit


class Hand():
    def __init__(self, cards):
        self.cards = cards
        self.scards = sorted(cards, reverse=True)
        self.value, self.rank, self.untie = self.evaluate()

    def _straight(self):
        # If a straight starts with an ace, scards will be [14, 5, 4, 3, 2]
        if self.scards[0].rank == 14 and self.scards[1].rank == 5 and self.scards[2].rank == 4 and \
           self.scards[3].rank == 3 and self.scards[4].rank == 2:
            return (5, 5, [])
        else:
            i = 1
            while i < 5 and self.scards[i].rank == self.scards[i-1].rank - 1:
                i += 1
            if i == 5:
                return (5, self.scards[0].rank, [])
            return None

    def _flush(self):
        if self.scards[0].color == self.scards[1].color == self.scards[2].color == \
           self.scards[3].color == self.scards[4].color:
            return (6,
                    self.scards[0].rank,
                    [self.scards[1].rank, self.scards[2].rank, self.scards[3].rank, self.scards[4].rank])
        return None

    def _four_of_a_kind(self):
        if self.scards[1].rank == self.scards[2].rank == self.scards[3].rank:
            if self.scards[0].rank == self.scards[1].rank:
                return (8, self.scards[1].rank, [self.scards[4].rank])
            elif self.scards[4].rank == self.scards[1].rank:
                return (8, self.scards[1].rank, [self.scards[0].rank])
        return None

    def _full_house(self):
        if self.scards[0].rank == self.scards[1].rank and \
           self.scards[3].rank == self.scards[4].rank:
            if self.scards[2].rank == self.scards[0].rank:
                return (7, self.scards[2].rank, self.scards[4].rank)
            elif self.scards[2].rank == self.scards[4].rank:
                return (7, self.scards[2].rank, self.scards[0].rank)
        return None

    def _three_of_a_kind(self):
        if self.scards[0].rank == self.scards[1].rank == self.scards[2].rank:
            return (4, self.scards[2].rank, [self.scards[3].rank, self.scards[4].rank])
        elif self.scards[1].rank == self.scards[2].rank == self.scards[3].rank:
            return (4, self.scards[2].rank, [self.scards[0].rank, self.scards[4].rank])
        elif self.scards[2].rank == self.scards[3].rank == self.scards[4].rank:
            return (4, self.scards[2].rank, [self.scards[0].rank, self.scards[1].rank])
        return None

    def _two_pair(self):
        if self.scards[0].rank == self.scards[1].rank:
            if self.scards[2].rank == self.scards[3].rank:
                return (3,
                        max(self.scards[1].rank, self.scards[3].rank),
                        [min(self.scards[1].rank, self.scards[2].rank), self.scards[4].rank])
            elif self.scards[3].rank == self.scards[4].rank:
                return (3,
                        max(self.scards[1].rank, self.scards[3].rank),
                        [min(self.scards[1].rank, self.scards[3].rank), self.scards[2].rank])
        elif (self.scards[1].rank == self.scards[2].rank and \
              self.scards[3].rank == self.scards[4].rank):
            return (3,
                    max(self.scards[1].rank, self.scards[3].rank),
                    [min(self.scards[1].rank, self.scards[3].rank), self.scards[0].rank])
        return None

    def _pair(self):
        if self.scards[0].rank == self.scards[1].rank:
            return (2, self.scards[0].rank, [self.scards[2].rank, self.scards[3].rank, self.scards[4].rank])
        elif self.scards[1].rank == self.scards[2].rank:
            return (2, self.scards[1].rank, [self.scards[0].rank, self.scards[3].rank, self.scards[4].rank])
        elif self.scards[2].rank == self.scards[3].rank:
            return (2, self.scards[2].rank, [self.scards[0].rank, self.scards[1].rank, self.scards[4].rank])
        elif self.scards[3].rank == self.scards[4].rank:
            return (2, self.scards[3].rank, [self.scards[0].rank, self.scards[1].rank, self.scards[2].rank])
        return None

    def _high(self):
        return (1,
                self.scards[0].rank,
                [self.scards[1].rank, self.scards[2].rank, self.scards[3].rank, self.scards[4].rank])

    def evaluate(self):
        res_straight = self._straight()
        res_flush = self._flush()
        if res_straight and res_flush:
            value, rank, untie = res_straight[0] + res_flush[0], res_straight[1], res_straight[2]
        elif res := self._four_of_a_kind():
            value, rank, untie = res
        elif res := self._full_house():
            value, rank, untie = res
        elif res_flush:
            value, rank, untie = res_flush
        elif res_straight:
            value, rank, untie = res_straight
        elif res := self._three_of_a_kind():
            value, rank, untie = res
        elif res := self._two_pair():
            value, rank, untie = res
        elif res := self._pair():
            value, rank, untie = res
        else:
            value, rank, untie = self._high()
        return value, rank, untie

    def __gt__(self, other):
        return (self.value > other.value or \
                (self.value == other.value and self.rank > other.rank) or \
                (self.value == other.value and self.rank == other.rank and self.untie > other.untie))

    def __eq__(self, other):
        return (self.value == other.value and self.rank == other.rank and self.untie == other.untie)

    def __repr__(self):
        return ' '.join(map(str, self.cards))


def best_hands(hands):
    h = list(map(lambda s: Hand(list(map(lambda ss: Card(ss) , s.split()))), hands))
    sh = sorted(h, reverse=True)

    best = [str(sh[0])]
    i = 1
    while i < len(sh) and sh[i] == sh[i-1]:
        best.append(str(sh[i]))
        i += 1
    return best
