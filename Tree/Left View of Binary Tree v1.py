from Node import Node

max_level = 0

def print_left(root, level):
    if not root:
        return
    global max_level
    if max_level < level:
        print(root.val)
        max_level = level
    print_left(root.left, level + 1)
    print_left(root.right, level + 1)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print_left(root, 1)