def spiral_traversal(root):
    if not root:
        return []
    arr = []
    s1 = [root]
    s2 = []
    while len(s1) != 0 or len(s2) != 0:
        while len(s1) != 0:
            el = s1.pop()
            arr.append(el.val)
            if el.left:
                s2.append(el.left)
            if el.right:
                s2.append(el.right)
        while len(s2) != 0:
            el = s2.pop()
            arr.append(el.val)
            if el.right:
                s1.append(el.right)
            if el.left:
                s1.append(el.left)
    return arr

