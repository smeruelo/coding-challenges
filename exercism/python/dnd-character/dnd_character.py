# https://exercism.io/my/solutions/c42d216f6eac496aba790d8c9ec230b8

from random import randint


def modifier(constitution):
    return (constitution - 10) // 2


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)


    def ability(self):
        results = [randint(1, 6) for _ in range(4)]
        return sum(results) - min(results)
