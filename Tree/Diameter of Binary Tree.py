from Node import Node

def get_height(root):
    if not root:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def get_diameter(root):
    if not root:
        return 0
    d1 = get_height(root.left) + get_height(root.right) + 1
    d2 = get_diameter(root.left)
    d3 = get_diameter(root.right)
    return max(d1, d2, d3)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(get_diameter(root))