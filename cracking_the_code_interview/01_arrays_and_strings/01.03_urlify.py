# O(n)
def urlify(s, n):
    url = list(s)

    spaces = 0
    for i in range(n):
        if url[i] == ' ':
            spaces += 1

    j = n - 1
    i = j + spaces * 2
    while i >= 0:
        if url[j] == ' ':
            url[i] = '0'
            url[i-1] = '2'
            url[i-2] = '%'
            i -= 3
        else:
            url[i] = url[j]
            i -= 1
        j -= 1
    return ''.join(url)
