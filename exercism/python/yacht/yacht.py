# https://exercism.io/my/solutions/1f639b987b894b4a9cc846ca43485690

from collections import Counter


YACHT = lambda dice_count: 50 if sorted(dice_count.values()) == [5] else 0
ONES = lambda dice_count: dice_count[1] * 1
TWOS = lambda dice_count: dice_count[2] * 2
THREES = lambda dice_count: dice_count[3] * 3
FOURS = lambda dice_count: dice_count[4] * 4
FIVES = lambda dice_count: dice_count[5] * 5
SIXES = lambda dice_count: dice_count[6] * 6
FULL_HOUSE = lambda dice_count: CHOICE(dice_count) if sorted(dice_count.values()) == [2, 3] else 0
def FOUR_OF_A_KIND(dice_count):
    most_repeated_k, most_repeated_v = sorted(dice_count.items(), key=lambda x: x[1], reverse=True)[0]
    return 4 * most_repeated_k if most_repeated_v >= 4 else 0
LITTLE_STRAIGHT = lambda dice_count: 30 if sorted(dice_count.keys()) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda dice_count: 30 if sorted(dice_count.keys()) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda dice_count: sum(k * v for k, v in dice_count.items())

def score(dice, category):
    return category(Counter(dice))
