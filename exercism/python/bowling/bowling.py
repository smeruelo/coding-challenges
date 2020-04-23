class BowlingGame:
    def __init__(self):
        self._rolls = []
        self._current_frame = None

    def roll(self, pins):
        try:
            self.score()
            raise GameEndedException('Game is already ended')
        except GameInProgressException:
            if pins < 0 or pins > 10:
                raise InvalidValues('Invalid roll value.')
            if self._current_frame is None:
                if pins != 10:
                    self._current_frame = pins
            elif self._current_frame + pins > 10:
                raise InvalidValues('Invalid roll value.')
            else:
                self._current_frame = None
            self._rolls.append(pins)

    def score(self):
        try:
            i = 0
            frames = []
            for frame in range(10):
                first, second = self._rolls[i], self._rolls[i+1]
                if first == 10:
                    frames.append(10 + self._rolls[i+1] + self._rolls[i+2])
                    i += 1
                elif first + second == 10:
                    frames.append(10 + self._rolls[i+2])
                    i += 2
                else:
                    frames.append(first + second)
                    i += 2
            return sum(frames)
        except IndexError:
            raise GameInProgressException('Game has not ended yet.')


class GameInProgressException(Exception):
    pass


class GameEndedException(Exception):
    pass


class InvalidValues(Exception):
    pass
