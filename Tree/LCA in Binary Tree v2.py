def lca(root, n1, n2):
    if not root:
        return None
    if root.val == n1 or root.val == n2:
        return root
    lca1 = lca(root.left, n1, n2)
    lca2 = lca(root.right, n1, n2)
    if lca1 and lca2:
        return root
    if lca1:
        return lca1
    if lca2:
        return lca2

