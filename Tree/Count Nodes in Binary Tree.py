from Node import Node

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

print(count_nodes(root))