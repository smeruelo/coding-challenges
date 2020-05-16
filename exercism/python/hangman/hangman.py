STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guessed = ['_'] * len(word)

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError('Game is over.')
        if char not in self.word or char in self.guessed:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
        else:
            for i, c in enumerate(self.word):
                if c == char:
                    self.guessed[i] = char
            if self.get_masked_word() == self.word:
                self.status = STATUS_WIN

    def get_masked_word(self):
        return ''.join(self.guessed)

    def get_status(self):
        return self.status
