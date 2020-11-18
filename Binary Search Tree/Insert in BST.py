from Node import Node

def insertBST(root, item):
  if not root:
    return Node(item)
  elif item < root.val:
    root.left = insertBST(root.left, item)
  elif item > root.val:
    root.right = insertBST(root.right, item)
  return root

root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(8)

item = int(input('Enter item: '))
root = insertBST(root, item)