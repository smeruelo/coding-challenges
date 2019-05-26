from secrets import choice
from string import ascii_lowercase


class Cipher(object):
    KEY_LEN = 100
    ALFABET_LEN = ord('z') - ord('a') + 1

    def __init__(self, key=None):
        if key:
            if not (key.isalpha() and key.islower()):
                raise ValueError('Invalid cipher key')
            self.key = key
        else:
            self.key = ''.join(choice(ascii_lowercase) for _ in range(self.KEY_LEN))

    def _rotate(self, char, steps):
        return chr(ord('a') + (ord(char) - ord('a') + steps) % self.ALFABET_LEN)

    def _steps(self, i):
        """Returns the shift distance determined by the key's i-th character."""
        return ord(self.key[i % len(self.key)]) - ord('a')

    def encode(self, text):
        return ''.join(self._rotate(c, self._steps(i))
                       for i, c in enumerate(text))

    def decode(self, text):
        return ''.join(self._rotate(c, self.ALFABET_LEN - self._steps(i))
                       for i, c in enumerate(text))
