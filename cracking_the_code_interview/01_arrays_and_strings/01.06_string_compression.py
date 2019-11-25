# O(n * n)
def compress_1(s):
    compressed = ''
    if s:
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                compressed += s[i-1] + str(count)
                count = 1
        compressed += s[i-1] + str(count)
        if len(compressed) < len(s):
            return compressed
    return s


# O(n)
def compress_2(s):
    compressed = []
    if s:
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                compressed.extend([s[i-1], str(count)])
                count = 1
        compressed.extend([s[-1], str(count)])
        if len(compressed) < len(s):
            return ''.join(compressed)
    return s
