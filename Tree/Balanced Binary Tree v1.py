from Node import Node

def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))

def check_balance(root):
    if not root:
        return True
    left = get_height(root.left)
    right = get_height(root.right)
    return abs(left - right) <= 1 and check_balance(root.left) and check_balance(root.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(check_balance(root))