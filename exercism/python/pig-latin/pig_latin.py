# https://exercism.io/my/solutions/d2bdcc6120c34689abfbdb61c6e9b136


def pig_latin(word):
    if word[0] in 'aeiou' or word[:2] in ('yt', 'xr')
        return word + 'ay'
    elif word[0] == 'y':
        return word[1:] + word[:1] + 'ay'
    else:
        i = min(filter(lambda x: x>=0, (word.find(c) for c in 'aeiouy')))
        if word[i] == 'u' and word[i-1] == 'q':
            i += 1
        return word[i:] + word[:i] + 'ay'


def translate(sentence):
    return " ".join(pig_latin(word) for word in sentence.split())
