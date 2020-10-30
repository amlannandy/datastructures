from Node import Node

def node_at_k(root, k):
    if not root:
        return
    if k == 0:
        print(root.val, end=' ')
    node_at_k(root.left, k - 1)
    node_at_k(root.right, k - 1)

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

k = int(input('Enter distance: '))
node_at_k(root, k)