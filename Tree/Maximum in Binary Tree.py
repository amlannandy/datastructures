from Node import Node

def find_max(root):
    if not root:
        return 0
    return max(root.val, find_max(root.left), find_max(root.right))

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(find_max(root))