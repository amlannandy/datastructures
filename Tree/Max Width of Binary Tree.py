from Node import Node

def max_width(root):
    if not root:
        return 0
    queue = [root]
    res = 0
    while len(queue) > 0:
        size = len(queue)
        res = max(size, res)
        for i in range(size):
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return res


root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(max_width(root))