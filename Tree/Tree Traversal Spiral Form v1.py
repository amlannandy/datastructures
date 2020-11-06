from Node import Node

def spiral_traversal(root):
    arr = []
    if not root:
        return arr
    queue = [root, None]
    curr = []
    reverse = False
    while len(queue) > 1:
        el = queue.pop(0)
        if el:
            curr.append(el.val)
            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
        else:
            if reverse:
                arr.extend(curr[::-1])
            else:
                arr.extend(curr)
            curr = []
            reverse = not reverse
            queue.append(None)
    else:
        if reverse:
            arr.extend(curr[::-1])
        else:
            arr.extend(curr)
    return arr