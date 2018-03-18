#!/usr/bin/python3
# https://abc045.contest.atcoder.jp/tasks/abc045_b

def game(a, b, c):
    decks = {'a': list(a), 'b': list(b), 'c': list(c)}
    player = 'a'
    while decks[player]:
        player = decks[player].pop(0)
    return player.upper()


if __name__ == '__main__':
    deck_a = input()
    deck_b = input()
    deck_c = input()
    print(game(deck_a, deck_b, deck_c))
