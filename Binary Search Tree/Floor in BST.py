from Node import Node

def floorInBST(root, val):
  res = Node(-1)
  while root is not None:
    if val == root.val:
      return root
    elif val > root.val:
      res = root
      root = root.right
    else:
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
print(floorInBST(root, item).val)