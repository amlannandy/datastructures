from Node import Node

def searchBST(root, item):
  if not root:
    return False
  if root.val == item:
    return True
  elif root.val < item:
    return searchBST(root.right, item)
  else:
    return searchBST(root.left, item)

root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(8)

item = int(input('Enter search item: '))
print(searchBST(root, item))