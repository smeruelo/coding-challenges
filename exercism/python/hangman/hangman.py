# https://exercism.io/my/solutions/6a51d22a63fe43fba02ec23b622b206c

# This is a (probably lame) FRP approach.
# Instead of keeping the state of the game inside of the class at every time,
# I just store the guesses and everything gets calculated when needed

from functools import reduce

STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    MAX_GUESSES = 9

    def __init__(self, word):
        self._word = word
        self._guesses = []

    @property
    def remaining_guesses(self):
        return self.MAX_GUESSES - self.count_fails()

    def count_fails(self):
        def f(count, char):
            already_guessed, fails = count
            if char in already_guessed or char not in self._word:
                return (already_guessed, fails + 1)
            else:
                return (already_guessed | {char}, fails)

        _, fails = reduce(f, self._guesses, (set(), 0))
        return fails

    def guess(self, char):
        if self.get_status() != STATUS_ONGOING:
            raise ValueError('Game is over.')
        self._guesses.append(char)

    def get_masked_word(self):
        return ''.join(map(lambda c: c if c in self._guesses else '_' , self._word))

    def get_status(self):
        if self.get_masked_word() == self._word:
            return STATUS_WIN
        elif self.remaining_guesses >= 0:
            return STATUS_ONGOING
        else:
            return STATUS_LOSE
