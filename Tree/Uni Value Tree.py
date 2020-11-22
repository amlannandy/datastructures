from Node import Node

def checkUni(root):
  if not root:
    return True
  if not root.left and not root.right:
    return True
  isValid = True
  if root.left:
    isValid = checkUni(root.left) and root.left.val == root.val and isValid
  if root.right:
    isValid = checkUni(root.right) and root.right.val == root.val and isValid
  return isValid

root = Node(1)
root.left = Node(1)
root.left.left = Node(1)
root.left.right = Node(1)
root.right = Node(1)
root.right.left = Node(1)
root.right.right = Node(3)

print(checkUni(root))