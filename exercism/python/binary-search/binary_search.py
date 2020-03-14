# https://exercism.io/my/solutions/fb55f8af8f1243edb395db4fd187c79d


def find(search_list, value):
    def aux(l, r):
        if l > r:
            raise ValueError("value not found")
        n = (l + r) // 2
        if value > search_list[n]:
            return aux(n+1, r)
        elif value < search_list[n]:
            return aux(l, n-1)
        return n
    return aux(0, len(search_list)-1)
