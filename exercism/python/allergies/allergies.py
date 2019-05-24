# https://exercism.io/my/solutions/de78940b659848fe91ea33f2905891ee


class Allergies(object):
    TYPES = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, score):
        self._indexes = format(score, '08b')[::-1][:8]
        self._lst = [alergy for i, alergy in enumerate(self.TYPES) if self._indexes[i] == '1']

    def allergic_to(self, item):
        return item in self._lst

    @property
    def lst(self):
        return self._lst
