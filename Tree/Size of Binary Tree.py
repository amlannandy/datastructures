from Node import Node

def get_size(root):
    if not root:
        return 0
    return 1 + get_size(root.left) + get_size(root.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(f'Size of binary tree is {get_size(root)}')