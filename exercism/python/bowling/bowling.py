# https://exercism.io/my/solutions/bc03e21a029d4573a9a059638e7b2ad0

TOTAL_PINS = 10
TOTAL_FRAMES = 10


class Frame():
    def __init__(self, is_last=False):
        self._rolls = [None, None, None]
        self._is_last = is_last

    def _num_rolls(self):
        return 3 - self._rolls.count(None)

    @property
    def first(self):
        return self._rolls[0]

    @property
    def second(self):
        return self._rolls[1]

    @property
    def third(self):
        return self._rolls[2]

    @property
    def is_last(self):
        return self._is_last

    @property
    def is_strike(self):
        return self.first == TOTAL_PINS

    @property
    def is_spare(self):
        return not self.is_strike and self._num_rolls() >= 2 and self.first + self.second == TOTAL_PINS

    @property
    def is_complete(self):
        if self.is_last and (self.is_strike or self.is_spare):
            return self._num_rolls() == 3
        elif self.is_strike:
            return self._num_rolls() == 1
        return self._num_rolls() == 2

    def roll(self, pins):
        if self.is_complete:
            raise Exception('No more rolls are possible for this frame.')
        if pins < 0 or pins > TOTAL_PINS:
            raise Exception('Invalid number of pins.')
        if not self.is_last and self._num_rolls() == 1 and self.first + pins > TOTAL_PINS:
            raise Exception("There ain't that many pins left.")
        if self.is_last and self._num_rolls() == 1:
            if not self.is_strike and self.first + pins > TOTAL_PINS:
                raise Exception("There ain't that many pins left.")
        if self.is_last and self._num_rolls() == 2:
            if self.is_strike and self.second != TOTAL_PINS and self.second + pins > TOTAL_PINS:
                raise Exception("There ain't that many pins left.")
        self._rolls[self._num_rolls()] = pins

    @property
    def score(self):
        return sum(filter(bool, self._rolls))


class BowlingGame:
    def __init__(self):
        self._frames = [Frame()]

    def roll(self, pins):
        if self._frames[-1].is_complete:
            raise Exception('Game is already ended.')
        self._frames[-1].roll(pins)
        if self._frames[-1].is_complete:
            if not self._frames[-1].is_last:
                self._frames.append(Frame(is_last=(len(self._frames) == TOTAL_FRAMES - 1)))

    def score(self):
        if len(self._frames) < TOTAL_FRAMES or not self._frames[-1].is_complete:
            raise Exception('Game is in progress.')
        points = 0
        for i, frame in enumerate(self._frames):
            points += frame.score
            if not frame.is_last:
                if frame.is_spare or frame.is_strike:
                    points += self._frames[i+1].first
                if frame.is_strike:
                    if self._frames[i+1].second:
                        points += self._frames[i+1].second
                    else:
                        points += self._frames[i+2].first
        return points
