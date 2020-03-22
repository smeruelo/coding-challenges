DISCOUNTS = [0, 0, 5, 10, 20, 25]
GROUP_PRICES = [8 * i * (100 - DISCOUNTS[i]) for i in range(len(DISCOUNTS))]

def total(basket):
    def price(groups):
        return sum([GROUP_PRICES[len(g)] for g in groups])

    def aux(j, groups):
        if j == len(basket):
            return price(groups)
        for b in range(j, len(basket)):
            book = basket[b]
            posib = []
            for i in range(len(groups)):
                g = groups[i]
                if book not in g:
                    new_groups = groups[:i] + groups[i+1:] + [groups[i] | {book}]
                    posib.append(new_groups)
            if not posib:
                posib = [groups + [{book}]]
            return min([aux(b+1, p) for p in posib])

    basket.sort()
    return aux(0, [])
