# https://exercism.io/my/solutions/32050b2012384ffab9d80e96517a2ff9


def has_repeated_values(lst):
    return len(lst) != len(set(lst))


def tree_from_traversals(preorder, inorder):
    def rec(preorder, inorder):
        if set(preorder) != set(inorder):
            raise ValueError("Traversals do not match.")
        if len(preorder) == 0:
            return {}

        root = preorder[0]
        k = inorder.index(root)
        return {
            "v": root,
            "l": tree_from_traversals(preorder[1:k+1], inorder[0:k]),
            "r": tree_from_traversals(preorder[k+1:], inorder[k+1:])
        }

    if has_repeated_values(preorder) or has_repeated_values(inorder):
        raise ValueError("Values must be unique..")
    return rec(preorder, inorder)
