from Node import Node

def ceilInBST(root, val):
  res = -1
  while root is not None:
    if root.val == val:
      res = root.val
    elif root.val < val:
      root = root.right
    else:
      res = root.val 
      root = root.left
  return res

root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)

item = int(input('Enter search item: '))
print(ceilInBST(root, item))