# task 2


def solution(H):
    blocks = 0
    stack = []
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
        if not stack or stack[-1] != h:
            blocks += 1
            stack.append(h)
    return blocks
