from Node import Node

def children_sum(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    curr_sum = 0
    if root.left:
        curr_sum += root.left.val
    if root.right:
        curr_sum += root.right.val
    return root.val == curr_sum and children_sum(root.left) and children_sum(root.right)

root = Node(5)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(1)
root.right.left = Node(2)
root.right.right = Node(1)
print(children_sum(root))