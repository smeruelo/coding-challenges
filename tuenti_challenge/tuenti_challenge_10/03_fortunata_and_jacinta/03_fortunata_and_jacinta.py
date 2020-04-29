from collections import Counter

LETTERS = 'abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ'

def read_and_count_words():
    with open('pg17013.txt', 'r') as f:
        chars = f.read()
        words = ''.join(map(lambda c: c.lower() if c in LETTERS else ' ', chars)).split()
        return Counter(filter(lambda w: len(w) >= 3, words))

def sort_words(words):
    ordered = sorted(sorted(words.items()), key=lambda kv: kv[1], reverse=True)
    ranking = dict()
    ranking_rev = dict()
    for i, kv in enumerate(ordered):
        ranking[kv[0]] = i + 1
        ranking_rev[i+1] = kv[0]
    return ranking, ranking_rev


frequencies = read_and_count_words()
ranking, ranking_rev = sort_words(frequencies)
for i in range(int(input())):
    case = input()
    if case.isdigit():
        rank = int(case)
        word = ranking_rev[rank]
        freq = frequencies[word]
        print(f'Case #{i+1}: {word} {freq}')
    else:
        word = case
        rank = ranking[word]
        freq = frequencies[word]
        print(f'Case #{i+1}: {freq} #{rank}')
