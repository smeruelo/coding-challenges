from itertools import product

H1, H2, H3, H4, H5 = range(1, 6)
ENG, SPA, UKR, JAP, NOR = 'eng', 'spa', 'ukr', 'jap', 'nor'
RED, GRE, IVO, YEL, BLU = 'red', 'gre', 'ivo', 'yel', 'blu'
DOG, SNA, FOX, HOR, ZEB = 'dog', 'sna', 'fox', 'hor', 'zeb'
COF, TEA, MIL, JUI, WAT = 'cof', 'tea', 'mil', 'jui', 'wat'
OLD, KOO, CHE, LUC, PAR = 'old', 'koo', 'che', 'luc', 'par'

houses = {H1, H2, H3, H4, H5}
origins = {ENG, SPA, UKR, JAP, NOR}
colors = {RED, GRE, IVO, YEL, BLU}
pets = {DOG, SNA, FOX, HOR, ZEB}
drinks ={COF, TEA, MIL, JUI, WAT}
tobaccos = {OLD, KOO, CHE, LUC, PAR}

COMBOS = set(product(houses, origins, colors, pets, drinks, tobaccos))

def house(combo):
    return combo[0]

def origin(combo):
    return combo[1]

def color(combo):
    return combo[2]

def pet(combo):
    return combo[3]

def drink(combo):
    return combo[4]

def tobacco(combo):
    return combo[5]

CATEGORIES = {house, origin, color, pet, drink, tobacco}

def items(category):
    if category == house:
        return houses
    elif category == origin:
        return origins
    elif category == color:
        return colors
    elif category == pet:
        return pets
    elif category == drink:
        return drinks
    elif category == tobacco:
        return tobaccos

def category(item):
    if item in houses:
        return house
    elif item in origins:
        return origin
    elif item in colors:
        return color
    elif item in pets:
        return pet
    elif item in drinks:
        return drink
    elif item in tobaccos:
        return tobacco

def opposite(house_set):
    return set(range(1, 6)).difference(house_set)

def p(combos=COMBOS):
    for c in sorted(combos):
        print(c)
    print(len(combos))

def rule_out(h, o, c, p, d, t):
    COMBOS.difference_update(set(product(h, o, c, p, d, t)))

SYNONYMS = dict()
for thing in houses | origins | colors | pets | drinks | tobaccos:
    SYNONYMS[thing] = {thing}

def _thing(thing, opposite=False, other=(houses, origins, colors, pets, drinks, tobaccos)):
    cat = category(thing)
    h, o, c, p, d, t = other
    if cat == house:
        h = houses - {thing} if opposite else {thing}
    elif cat == origin:
        o = origins - {thing} if opposite else {thing}
    elif cat == color:
        c = colors - {thing} if opposite else {thing}
    elif cat == pet:
        p = pets - {thing} if opposite else {thing}
    elif cat == drink:
        d = drinks - {thing} if opposite else {thing}
    elif cat == tobacco:
        t = tobaccos - {thing} if opposite else {thing}
    return (h, o, c, p, d, t)

def _add_synonym(thing1, type1, thing2, type2):
    thing1_not_thing2 = _thing(thing2, opposite=True, other=_thing(thing1))
    not_thing1_thing2 = _thing(thing2, other=_thing(thing1, opposite=True))
    rule_out(*thing1_not_thing2)
    rule_out(*not_thing1_thing2)
    SYNONYMS[thing1].add(thing2)
    SYNONYMS[thing2].add(thing1)

def synonyms(thing):
    cat1 = category(thing)
    rest_cats = CATEGORIES - {cat1}
    combos = set(filter(lambda c: cat1(c) == thing, COMBOS))
    out = []
    for cat2 in rest_cats:
        if len(value := set(map(cat2, combos))) == 1:
            out.append(value.pop())
    return out

    
def _find_synonyms():
    def find(thing, rest):
        for t1 in items(thing):
            combos = set(filter(lambda c: thing(c) == t1, COMBOS))
            for t2 in rest:
                if len(value := set(map(t2, combos))) == 1:
                    v = value.pop()
                    if v not in SYNONYMS[t1]:
                        print(f'Found synonym: {t1} = {v}')
                    SYNONYMS[t1].add(v)
                    SYNONYMS[v].add(t1)

    for cat in CATEGORIES:
        find(cat, CATEGORIES - {cat})


# 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
# 12. Kools are smoked in the house next to the house where the horse is kept.
# 15. The Norwegian lives next to the blue house.
def _rule_next(thing1, thing2):
    ht1 = set(map(house, filter(lambda c: category(thing1)(c) == thing1, COMBOS)))
    ht2 = set(map(house, filter(lambda c: category(thing2)(c) == thing2, COMBOS)))
    ht2.intersection_update(set(map(lambda x: x + 1, ht1)))
    ht1.intersection_update(set(map(lambda x: x - 1, ht2)))
    rule_out(*_thing(thing1, other=(opposite(ht1), origins, colors, pets, drinks, tobaccos)))
    rule_out(*_thing(thing2, other=(opposite(ht2), origins, colors, pets, drinks, tobaccos)))

# 6. The green house is immediately to the right of the ivory house.
def _rule_right(thing1, thing2):
    ht1 = set(map(house, filter(lambda c: category(thing1)(c) == thing1, COMBOS)))
    ht2 = set(map(house, filter(lambda c: category(thing2)(c) == thing2, COMBOS)))
    ht2.intersection_update(set(map(lambda x: x - 1, ht1)))
    ht1.intersection_update(set(map(lambda x: x + 1, ht2)))
    rule_out(*_thing(thing1, other=(opposite(ht1), origins, colors, pets, drinks, tobaccos)))
    rule_out(*_thing(thing2, other=(opposite(ht2), origins, colors, pets, drinks, tobaccos)))


def _add_constraints():

    print('before', len(COMBOS))

    _add_synonym(ENG, origin, RED, color)    #  2. The Englishman lives in the red house.
    _add_synonym(SPA, origin, DOG, pet)      #  3. The Spaniard owns the dog.
    _add_synonym(GRE, color, COF, drink)     #  4. Coffee is drunk in the green house.
    _add_synonym(UKR, origin, TEA, drink)    #  5. The Ukrainian drinks tea.
    _add_synonym(OLD, tobacco, SNA, pet)     #  7. The Old Gold smoker owns snails.
    _add_synonym(KOO, tobacco, YEL, color)   #  8. Kools are smoked in the yellow house.
    _add_synonym(MIL, drink, H3, house)      #  9. Milk is drunk in the middle house.
    _add_synonym(NOR, origin, H1, house)     # 10. The Norwegian lives in the first house.
    _add_synonym(LUC, tobacco, JUI, drink)   # 13. The Lucky Strike smoker drinks orange juice.
    _add_synonym(JAP, origin, PAR, tobacco)  # 14. The Japanese smokes Parliaments.
    print('after synonyms', len(COMBOS))

    # # 6. The green house is immediately to the right of the ivory house.
    rule_out({H5}, origins, {IVO}, pets, drinks, tobaccos)
    rule_out({H1}, origins, {GRE}, pets, drinks, tobaccos)
    print('b 6', len(COMBOS))
    _rule_right(GRE, IVO)
    # ivory = set(map(house, filter(lambda c: color(c) == IVO, COMBOS)))
    # green = set(map(house, filter(lambda c: color(c) == GRE, COMBOS)))
    # green.intersection_update(set(map(lambda x: x + 1, ivory)))
    # ivory.intersection_update(set(map(lambda x: x - 1, green)))
    # rule_out(opposite(green), origins, {GRE}, pets, drinks, tobaccos)
    # rule_out(opposite(ivory), origins, {IVO}, pets, drinks, tobaccos)
    print('a 6', len(COMBOS))

    # # 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
    rule_out(houses, origins, colors, {FOX}, drinks, {CHE})
    print('b 11', len(COMBOS))
    _rule_next(CHE, FOX)
    # fox = set(map(house, filter(lambda c: pet(c) == FOX, COMBOS)))
    # chester = set(map(house, filter(lambda c: tobacco(c) == CHE, COMBOS)))
    # chester.intersection_update(set(map(lambda x: x + 1, fox)) | set(map(lambda x: x - 1, fox)))
    # fox.intersection_update(set(map(lambda x: x + 1, chester)) | set(map(lambda x: x - 1, chester)))
    # rule_out(opposite(chester), origins, colors, pets, drinks, {CHE})
    # rule_out(opposite(fox), origins, colors, {FOX}, drinks, tobaccos)
    print('a 11', len(COMBOS))

    # # 12. Kools are smoked in the house next to the house where the horse is kept.
    rule_out(houses, origins, colors, {HOR}, drinks, {KOO})
    print('b 12', len(COMBOS))
    _rule_next(HOR, KOO)
    # horse = set(map(house, filter(lambda c: pet(c) == HOR, COMBOS)))
    # kool = set(map(house, filter(lambda c: tobacco(c) == KOO, COMBOS)))
    # kool.intersection_update(set(map(lambda x: x + 1, horse)) | set(map(lambda x: x - 1, horse)))
    # horse.intersection_update(set(map(lambda x: x + 1, kool)) | set(map(lambda x: x - 1, kool)))
    # rule_out(opposite(kool), origins, colors, pets, drinks, {KOO})
    # rule_out(opposite(horse), origins, colors, {HOR}, drinks, tobaccos)
    print('a 12', len(COMBOS))

    # # 15. The Norwegian lives next to the blue house.
    rule_out(houses, {NOR}, {BLU}, pets, drinks, tobaccos)
    print('b 15', len(COMBOS))
    _rule_next(NOR, BLU)
    # norwegian = set(map(house, filter(lambda c: origin(c) == NOR, COMBOS)))
    # blue = set(map(house, filter(lambda c: color(c) == BLU, COMBOS)))
    # blue.intersection_update(set(map(lambda x: x + 1, norwegian)) | set(map(lambda x: x - 1, norwegian)))
    # norwegian.intersection_update(set(map(lambda x: x + 1, blue)) | set(map(lambda x: x - 1, blue)))
    # rule_out(opposite(norwegian), {NOR}, colors, pets, drinks, tobaccos)
    # rule_out(opposite(blue), origins, {BLU}, pets, drinks, tobaccos)
    print('a 15', len(COMBOS))



    print('after', len(COMBOS))
    _find_synonyms()
    return COMBOS

def drinks_water():
    pass


def owns_zebra():
    pass

#   #  6. The green house is immediately to the right of the ivory house.
#   # 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
#   # 12. Kools are smoked in the house next to the house where the horse is kept.
#   # 15. The Norwegian lives next to the blue house.
