from Node import Node

def height_of_tree(root):
    if not root:
        return 0
    return max(height_of_tree(root.left), height_of_tree(root.right)) + 1

head = Node(1)
head.left = Node(2)
head.left.left = Node(3)
head.left.right = Node(4)
head.right = Node(5)
head.right.left = Node(6)
head.right.right = Node(7)
head.right.right.right = Node(8)

print(f'Height of Tree is {height_of_tree(head)}')