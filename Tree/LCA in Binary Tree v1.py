def find_path(root, item, arr):
    if not root:
        return False
    arr.append(root.val)
    if root.val == item:
        return True
    if find_path(root.left, item, arr) or find_path(root.right, item, arr):
        return True
    arr.pop()
    return False

def find_lca(root, m, n):
    path1, path2 = [], []
    if not find_path(root, m, path1) or not find_path(root, n, path1):
        return None
    i = 0
    while i < len(path1) - 1 and i < len(path2) - 1:
        if path1[i+1] != path2[i+1]:
            return path1[i]
        i += 1
    if path1[i] == path2[i]:
        return path1[i]
    return None

