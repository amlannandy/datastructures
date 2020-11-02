from Node import Node

def check_balance(root):
    if not root:
        return 0
    lh = check_balance(root.left)
    if lh == -1:
        return -1
    rh = check_balance(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    else:
        return max(lh, rh) + 1

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print('Balanced' if check_balance(root) != -1 else 'Not Balanced')