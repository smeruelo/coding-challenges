# https://exercism.io/my/solutions/1f639b987b894b4a9cc846ca43485690

from collections import Counter


YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def yatch(dice_count):
    return 50 if sorted(dice_count.values()) == [5] else 0

def repetitions(number):
    def f(dice_count):
        return dice_count[number] * number
    return f

def full_house(dice_count):
    return choice(dice_count) if sorted(dice_count.values()) == [2, 3] else 0

def four_of_a_kind(dice_count):
    most_repeated_k, most_repeated_v = sorted(dice_count.items(), key=lambda x: x[1], reverse=True)[0]
    return 4 * most_repeated_k if most_repeated_v >= 4 else 0

def little_straight(dice_count):
    return 30 if sorted(dice_count.keys()) == [1, 2, 3, 4, 5] else 0

def big_straight(dice_count):
    return 30 if sorted(dice_count.keys()) == [2, 3, 4, 5, 6] else 0

def choice(dice_count):
    return sum(k * v for k, v in dice_count.items())

SCORE = { YACHT: yatch,
          ONES: repetitions(ONES),
          TWOS: repetitions(TWOS),
          THREES: repetitions(THREES),
          FOURS: repetitions(FOURS),
          FIVES: repetitions(FIVES),
          SIXES: repetitions(SIXES),
          FULL_HOUSE: full_house,
          FOUR_OF_A_KIND: four_of_a_kind,
          LITTLE_STRAIGHT: little_straight,
          BIG_STRAIGHT: big_straight,
          CHOICE: choice }

def score(dice, category):
    return SCORE[category](Counter(dice))
