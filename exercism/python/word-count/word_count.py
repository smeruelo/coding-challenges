# https://exercism.io/my/solutions/47314adde6f04a67a6fd3f8082d61d52

from collections import Counter
from re import sub


def count_words(sentence):
    words = sub('[^0-9a-z\']+', ' ', sentence.lower()).split()
    no_quotes = map(lambda w: w.strip("'"), words)
    return Counter(no_quotes)
