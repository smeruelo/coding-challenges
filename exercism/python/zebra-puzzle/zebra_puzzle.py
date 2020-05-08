from itertools import product

H1, H2, H3, H4, H5 = range(1, 6)
ENG, SPA, UKR, JAP, NOR = 'English', 'Spaniard', 'Ukrainian', 'Japanese', 'Norwegian'
RED, GRE, IVO, YEL, BLU = 'Red', 'Green', 'Ivory', 'Yellow', 'Blue'
DOG, SNA, FOX, HOR, ZEB = 'Dog', 'Snails', 'Fox', 'Horse', 'Zebra'
COF, TEA, MIL, JUI, WAT = 'Coffee', 'Tea', 'Milk', 'Orange Juice', 'Water'
OLD, KOO, CHE, LUC, PAR = 'Old Gold', 'Kools', 'Chesterfield', 'Lucky Strike', 'Parliaments'

houses = {H1, H2, H3, H4, H5}
origins = {ENG, SPA, UKR, JAP, NOR}
colors = {RED, GRE, IVO, YEL, BLU}
pets = {DOG, SNA, FOX, HOR, ZEB}
drinks ={COF, TEA, MIL, JUI, WAT}
tobaccos = {OLD, KOO, CHE, LUC, PAR}

def house(combo): return combo[0]
def origin(combo): return combo[1]
def color(combo): return combo[2]
def pet(combo): return combo[3]
def drink(combo): return combo[4]
def tobacco(combo): return combo[5]

COMBOS = set(product(houses, origins, colors, pets, drinks, tobaccos))
SYNONYMS = dict()
for thing in houses | origins | colors | pets | drinks | tobaccos:
    SYNONYMS[thing] = {thing}
CATEGORIES = {house, origin, color, pet, drink, tobacco}

def items(category):
    if category == house: return houses
    elif category == origin: return origins
    elif category == color: return colors
    elif category == pet: return pets
    elif category == drink: return drinks
    elif category == tobacco: return tobaccos

def category(item):
    if item in houses: return house
    elif item in origins: return origin
    elif item in colors: return color
    elif item in pets: return pet
    elif item in drinks: return drink
    elif item in tobaccos: return tobacco

def _rule_out(h, o, c, p, d, t):
    before = COMBOS.copy()
    COMBOS.difference_update(set(product(h, o, c, p, d, t)))
    return before - COMBOS

def _thing(thing, opposite=False, other=(houses, origins, colors, pets, drinks, tobaccos)):
    cat = category(thing)
    h, o, c, p, d, t = other
    if cat == house: h = houses - {thing} if opposite else {thing}
    elif cat == origin: o = origins - {thing} if opposite else {thing}
    elif cat == color: c = colors - {thing} if opposite else {thing}
    elif cat == pet: p = pets - {thing} if opposite else {thing}
    elif cat == drink: d = drinks - {thing} if opposite else {thing}
    elif cat == tobacco: t = tobaccos - {thing} if opposite else {thing}
    return (h, o, c, p, d, t)

def _add_synonym(thing1, thing2):
    thing1_not_thing2 = _thing(thing2, opposite=True, other=_thing(thing1))
    not_thing1_thing2 = _thing(thing2, other=_thing(thing1, opposite=True))
    _rule_out(*thing1_not_thing2)
    _rule_out(*not_thing1_thing2)
    SYNONYMS[thing1].add(thing2)
    SYNONYMS[thing2].add(thing1)

def _find_synonyms():
    for cat in CATEGORIES:
        for t1 in items(cat):
            combos = set(filter(lambda c: cat(c) == t1, COMBOS))
            for cat2 in CATEGORIES - {cat}:
                if len(value := set(map(cat2, combos))) == 1:
                    t2 = value.pop()
                    if t2 not in SYNONYMS[t1]:
                        _add_synonym(t1, t2)

def _opposite_houses(house_set):
    return set(range(1, 6)).difference(house_set)

def _rule_next(thing1, thing2):  # thing1 lives next to thing2
    if category(thing1) == house or category(thing2) == house:
        return
    ht1 = set(map(house, filter(lambda c: category(thing1)(c) == thing1, COMBOS)))
    ht2 = set(map(house, filter(lambda c: category(thing2)(c) == thing2, COMBOS)))
    ht2.intersection_update(set(map(lambda x: x + 1, ht1)) | set(map(lambda x: x - 1, ht1)))
    ht1.intersection_update(set(map(lambda x: x + 1, ht2)) | set(map(lambda x: x - 1, ht2)))
    _rule_out(*_thing(thing1, other=(_opposite_houses(ht1), origins, colors, pets, drinks, tobaccos)))
    _rule_out(*_thing(thing2, other=(_opposite_houses(ht2), origins, colors, pets, drinks, tobaccos)))

def _rule_right(thing1, thing2):  # thing1 lives immediately to the right of thing2
    if category(thing1) == house or category(thing2) == house:
        return
    ht1 = set(map(house, filter(lambda c: category(thing1)(c) == thing1, COMBOS)))
    ht2 = set(map(house, filter(lambda c: category(thing2)(c) == thing2, COMBOS)))
    ht2.intersection_update(set(map(lambda x: x - 1, ht1)))
    ht1.intersection_update(set(map(lambda x: x + 1, ht2)))
    _rule_out(*_thing(thing1, other=(_opposite_houses(ht1), origins, colors, pets, drinks, tobaccos)))
    _rule_out(*_thing(thing2, other=(_opposite_houses(ht2), origins, colors, pets, drinks, tobaccos)))

def resolve():
    _add_synonym(ENG, RED)     #  2. The Englishman lives in the red house.
    _add_synonym(SPA, DOG)     #  3. The Spaniard owns the dog.
    _add_synonym(GRE, COF)     #  4. Coffee is drunk in the green house.
    _add_synonym(UKR, TEA)     #  5. The Ukrainian drinks tea.
    _add_synonym(OLD, SNA)     #  7. The Old Gold smoker owns snails.
    _add_synonym(KOO, YEL)     #  8. Kools are smoked in the yellow house.
    _add_synonym(MIL, H3)      #  9. Milk is drunk in the middle house.
    _add_synonym(NOR, H1)      # 10. The Norwegian lives in the first house.
    _add_synonym(LUC, JUI)     # 13. The Lucky Strike smoker drinks orange juice.
    _add_synonym(JAP, PAR)     # 14. The Japanese smokes Parliaments.

    while len(COMBOS) > 5:
        _rule_right(GRE, IVO)  #  6. The green house is immediately to the right of the ivory house.
        _rule_next(CHE, FOX)   # 11. The man who smokes Chester lives next to the man with the fox.
        _rule_next(HOR, KOO)   # 12. Kools are smoked in the house next to the horse.
        _rule_next(NOR, BLU)   # 15. The Norwegian lives next to the blue house.
        _find_synonyms()

    return COMBOS

for combo in sorted(resolve(), key=house):
    print(combo)


def who(what):
    return origin(list(filter(lambda c: category(what)(c) == what, COMBOS))[0])

def drinks_water():
    return who(WAT)

def owns_zebra():
    return who(ZEB)
