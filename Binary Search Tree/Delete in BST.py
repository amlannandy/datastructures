from Node import Node

def getSuccessor(root):
  curr = root.right
  while curr is not None and curr.left is not None:
    curr = curr.left
  return curr

def deleteBST(root, val):
  if not root:
    return None
  elif val < root.val:
    root.left = deleteBST(root.left, val)
  elif val > root.val:
    root.right = deleteBST(root.right, val)
  else:
    if not root.left:
      return root.right
    elif not root.right:
      return root.left
    else:
      succ = getSuccessor(root)
      root.val = succ.val 
      root.right = deleteBST(root.right, succ.val)
  return root