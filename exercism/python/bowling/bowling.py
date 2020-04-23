class Frame():
    def __init__(self):
        self._first = None
        self._second = None

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second

    def roll(self, pins):
        raise Exception('Not implemented.')

    def is_completed(self):
        raise Exception('Not implemented.')

    def score(self):
        raise Exception('Not implemented.')

    def _validate_roll(self, pins):
        if pins < 0 or pins > 10 or self.is_completed():
            raise Exception('Invalid roll.')


class RegularFrame(Frame):
    def roll(self, pins):
        self._validate_roll(pins)
        if self._first is not None:
            if self._first + pins > 10:
                raise Exception('Invalid roll.')
            self._second = pins
        else:
            self._first = pins

    def is_completed(self):
        return self.is_strike() or (self._second is not None)

    def score(self):
        if not self.is_completed():
            raise Exception('Frame is not completed yet')
        return self._first + self._second if self._second else self._first

    def is_strike(self):
        return self._first == 10

    def is_spare(self):
        return self._second is not None and self.score() == 10


class FillBall(Frame):
    def __init__(self, balls=1):
        self._balls = balls
        super().__init__()

    def roll(self, pins):
        self._validate_roll(pins)
        if self._first is None:
            self._first = pins
        else:
            if self._first != 10 and (self._first + pins > 10):
                raise Exception('Invalid roll.')
            self._second = pins

    def is_completed(self):
        return (self._first is not None and self._balls == 1) or \
            (self._first is not None and self._second is not None and self._balls == 2)

    def score(self):
        if not self.is_completed():
            raise Exception('Frame is not completed yet')
        return self._first if self._balls == 1 else self._first + self._second


class BowlingGame:
    def __init__(self):
        self._frames = []
        self._current_frame = RegularFrame()

    def roll(self, pins):
        num_frame = len(self._frames) + 1
        if self._current_frame is None:
            raise Exception('Game is already ended.')
        self._current_frame.roll(pins)
        if self._current_frame.is_completed():
            self._frames.append(self._current_frame)
            if num_frame < 10:
                self._current_frame = RegularFrame()
            elif num_frame == 10 and self._frames[-1].is_spare():
                self._current_frame = FillBall()
            elif num_frame == 10 and self._frames[-1].is_strike():
                self._current_frame = FillBall(balls=2)
            else:
                self._current_frame = None

    def score(self):
        if self._current_frame is not None:
            raise Exception('Game is in progress.')
        points = 0
        for i in range(10):
            frame = self._frames[i]
            points += frame.score()
            if frame.is_spare():
                points += self._frames[i+1].first
            elif frame.is_strike():
                points += self._frames[i+1].score()
                if i < 9 and self._frames[i+1].is_strike():
                    points += self._frames[i+2].first
        return points
